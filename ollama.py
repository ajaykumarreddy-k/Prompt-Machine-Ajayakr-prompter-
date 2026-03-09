"""
ollama.py — Qwen2.5 client via Ollama REST API
Supports both streaming (for code output) and non-streaming (for JSON stages).
"""

import json
import os
import sys
import threading
import time
import urllib.error
import urllib.request

OLLAMA_HOST = os.environ.get("OLLAMA_HOST", "localhost")
OLLAMA_PORT = os.environ.get("OLLAMA_PORT", "11434")
MODEL       = os.environ.get("OLLAMA_MODEL", "qwen2.5")
OLLAMA_URL  = f"http://{OLLAMA_HOST}:{OLLAMA_PORT}/api/generate"


# ── SPINNER ───────────────────────────────────────────────────────────────────
class Spinner:
    _FRAMES = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]

    def __init__(self, msg: str):
        self.msg    = msg
        self._stop  = threading.Event()
        self.is_tui = os.environ.get("PROMPT_MACHINE_TUI") == "1"
        self._thread = threading.Thread(target=self._run, daemon=True)

    def _run(self):
        i = 0
        while not self._stop.is_set():
            if not self.is_tui:
                sys.stdout.write(f"\r\033[36m{self._FRAMES[i % 10]} {self.msg}...\033[0m")
                sys.stdout.flush()
                time.sleep(0.08)
            else:
                # In TUI, print dots occasionally to keep standard out "alive" 
                # so the Textual app knows the worker is not completely frozen.
                if i == 0:
                    sys.stdout.write(f"\r{self.msg}...")
                elif i % 10 == 0:
                    sys.stdout.write(".")
                sys.stdout.flush()
                time.sleep(0.5)
            i += 1

    def __enter__(self):
        self._thread.start()
        return self
 
    def __exit__(self, *_):
        self._stop.set()
        if self._thread.is_alive():
            self._thread.join()
        
        if self.is_tui:
            sys.stdout.write(f"\r{self.msg}... Done.\n")
        else:
            sys.stdout.write("\r" + " " * (len(self.msg) + 6) + "\r")
        sys.stdout.flush()


# ── HELPERS ───────────────────────────────────────────────────────────────────
def _make_request(payload: dict, timeout: int = 360) -> urllib.request.Request:
    data = json.dumps(payload).encode()
    return urllib.request.Request(
        OLLAMA_URL,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )


def check_ollama():
    """Verify Ollama is reachable. Exit with a clear message if not."""
    try:
        urllib.request.urlopen(f"http://{OLLAMA_HOST}:{OLLAMA_PORT}", timeout=3)
    except urllib.error.URLError:
        print(f"\033[31m\033[1m[ERROR]\033[0m Ollama not running.")
        print(f"        Start it:  ollama serve")
        print(f"        Pull model: ollama pull {MODEL}")
        sys.exit(1)


# ── STREAMING (for code gen — shows tokens live) ──────────────────────────────
def ollama_stream(prompt: str, system: str = "") -> str:
    """Stream tokens to stdout and return full text. Used for code generation."""
    payload = {
        "model":  MODEL,
        "prompt": prompt,
        "system": system,
        "stream": True,
        "options": {"temperature": 0.3, "top_p": 0.9, "num_ctx": 8192},
    }
    req = _make_request(payload)
    result: list[str] = []

    try:
        with urllib.request.urlopen(req, timeout=360) as resp:
            for line in resp:
                line = line.strip()
                if not line:
                    continue
                try:
                    chunk = json.loads(line)
                    token = chunk.get("response", "")
                    sys.stdout.write(token)
                    sys.stdout.flush()
                    result.append(token)
                    if chunk.get("done"):
                        break
                except json.JSONDecodeError:
                    continue
    except urllib.error.URLError as e:
        raise ConnectionError(f"Ollama connection failed: {e}") from e

    print()  # newline after streaming
    return "".join(result)


# ── NON-STREAMING (for JSON stages — cleaner) ─────────────────────────────────
def ollama(prompt: str, system: str = "", label: str = "Thinking") -> str:
    """Send prompt and return full response. Shows spinner while waiting."""
    payload = {
        "model":  MODEL,
        "prompt": prompt,
        "system": system,
        "stream": False,
        "options": {"temperature": 0.3, "top_p": 0.9, "num_ctx": 8192},
    }
    req = _make_request(payload)

    with Spinner(label):
        try:
            with urllib.request.urlopen(req, timeout=360) as resp:
                raw = resp.read().decode()
        except urllib.error.URLError as e:
            raise ConnectionError(f"Ollama connection failed: {e}") from e

    try:
        data = json.loads(raw)
        return (data.get("response") or "").strip()
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse Ollama response: {raw[:200]}") from e


# ── JSON EXTRACTOR ────────────────────────────────────────────────────────────
def extract_json(text: str) -> dict | list | None:
    """Pull JSON from model output — handles markdown fences, leading text, etc."""
    import re

    # ```json ... ``` or ``` ... ```
    fence = re.search(r"```(?:json)?\s*([\s\S]*?)```", text)
    if fence:
        try:
            return json.loads(fence.group(1).strip())
        except json.JSONDecodeError:
            pass

    # bare { ... } or [ ... ]
    match = re.search(r"(\{[\s\S]*\}|\[[\s\S]*\])", text)
    if match:
        try:
            return json.loads(match.group(1))
        except json.JSONDecodeError:
            pass

    # whole string
    try:
        return json.loads(text.strip())
    except json.JSONDecodeError:
        return None
