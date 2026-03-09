"""
AKR Prompt Engine
Made by Ajay
"""
import psutil
import time
import random
from collections import deque

from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical, ScrollableContainer
from textual.widgets import Static, Input, Footer, TextArea, Button
from textual import work
from textual.reactive import reactive
import sys
import contextlib

from rich.text import Text
from rich.console import RenderableType, Group
from rich.panel import Panel
from rich.table import Table
from rich import box


# ══════════════════════════════════════════════════════════════════
#  LOGO HEADER  — paste your ASCII art inside _YOUR_LOGO
# ══════════════════════════════════════════════════════════════════
_YOUR_LOGO = """

"""

class LogoHeader(Static):
    def render(self) -> RenderableType:
        logo = Text()
        for line in _YOUR_LOGO.splitlines():
            logo.append(line + "\n", style="bold white")
        sub = Text()
        sub.append("  Made by ", style="dim white")
        sub.append("Ajay Kumar Reddy", style="white")
        sub.append("   ·   Model: qwen2.5-coder   ·   RAG: online   ·   v2.5\n",
                   style="dim white")
        divider = Text("  " + "─" * 72 + "\n", style="color(238)")
        return Group(logo, sub, divider)


# ══════════════════════════════════════════════════════════════════
#  HELPERS
# ══════════════════════════════════════════════════════════════════
def _bar(value: float, width: int = 10) -> Text:
    filled = max(0, min(width, int(value / 100 * width)))
    t = Text()
    for i in range(filled):
        frac = i / max(width - 1, 1)
        style = "green" if frac < 0.5 else "yellow" if frac < 0.75 else "red"
        t.append("█", style=style)
    t.append("░" * (width - filled), style="color(235)")
    return t


def _mini_graph(history: list, width: int, height: int = 4,
                colour: str = "cyan") -> Text:
    BLOCKS = " ▁▂▃▄▅▆▇█"
    data = list(history)[-width:]
    while len(data) < width:
        data.insert(0, 0.0)
    peak = max(data) if max(data) > 0 else 1.0
    rows = []
    for row in range(height - 1, -1, -1):
        line = Text()
        tlo = row / height * peak
        thi = (row + 1) / height * peak
        for v in data:
            if v >= thi:
                line.append("█", style=colour)
            elif v >= tlo:
                frac = (v - tlo) / (thi - tlo) if (thi - tlo) > 0 else 0
                line.append(BLOCKS[max(1, int(frac * 8))], style=colour)
            else:
                line.append(" ")
        rows.append(line)
    out = Text()
    for i, r in enumerate(rows):
        out.append_text(r)
        if i < len(rows) - 1:
            out.append("\n")
    return out


# ══════════════════════════════════════════════════════════════════
#  TITLE BAR
# ══════════════════════════════════════════════════════════════════
class TitleBar(Static):
    _tick: reactive[int] = reactive(0)

    def on_mount(self) -> None:
        self.set_interval(1.0, lambda: setattr(self, "_tick", self._tick + 1))

    def render(self) -> RenderableType:
        uptime = int(time.time() - psutil.boot_time())
        h, rem = divmod(uptime, 3600)
        m, s   = divmod(rem, 60)
        ts     = time.strftime("%H:%M:%S")

        bat_str = ""
        try:
            bat = psutil.sensors_battery()
            if bat:
                icon = "+" if bat.power_plugged else "-"
                bat_str = f"BAT {icon} {bat.percent:.0f}%  "
        except Exception:
            pass

        cpu_info = ""
        try:
            f = psutil.cpu_freq()
            if f:
                cpu_info = f"  {psutil.cpu_count(logical=False)}C/{psutil.cpu_count()}T  {f.current:.0f}MHz"
        except Exception:
            pass

        left   = Text(" AKR Prompt Engine ", style="bold white")
        centre = Text(ts, style="bold bright_white", justify="center")
        right  = Text(justify="right")
        right.append(bat_str, style="white")
        right.append(f"up {h:02d}:{m:02d}:{s:02d}", style="white")
        right.append(cpu_info, style="dim white")
        right.append("  ")

        grid = Table.grid(expand=True)
        grid.add_column(ratio=1)
        grid.add_column(ratio=1, justify="center")
        grid.add_column(ratio=1, justify="right")
        grid.add_row(left, centre, right)
        return grid


# ══════════════════════════════════════════════════════════════════
#  LEFT SIDEBAR — CPU + GPU stats, small
# ══════════════════════════════════════════════════════════════════
class SideStats(Static):
    _tick: reactive[int] = reactive(0)

    def __init__(self, **kw):
        super().__init__(**kw)
        self._cpu_hist: deque = deque([0.0] * 30, maxlen=30)
        self._mem_hist: deque = deque([0.0] * 30, maxlen=30)
        self._core_hist: list = [
            deque([0.0] * 30, maxlen=30) for _ in range(psutil.cpu_count() or 1)
        ]

    def on_mount(self) -> None:
        self.set_interval(1.0, self._update)

    def _update(self) -> None:
        percore = psutil.cpu_percent(percpu=True) or []
        total   = psutil.cpu_percent()
        mem     = psutil.virtual_memory().percent
        self._cpu_hist.append(total)
        self._mem_hist.append(mem)
        for i, v in enumerate(percore):
            if i < len(self._core_hist):
                self._core_hist[i].append(v)
        self._tick += 1

    def render(self) -> RenderableType:
        total   = self._cpu_hist[-1] if self._cpu_hist else 0.0
        mem_pct = self._mem_hist[-1] if self._mem_hist else 0.0
        percore = [h[-1] if h else 0.0 for h in self._core_hist]

        freq_str = ""
        try:
            f = psutil.cpu_freq()
            freq_str = f"{f.current:.0f}MHz" if f else ""
        except Exception:
            pass

        # CPU total header
        out = Text()
        out.append("CPU  ", style="bold cyan")
        out.append(f"{total:5.1f}%", style="bold white")
        if freq_str:
            out.append(f"  {freq_str}", style="dim white")
        out.append("\n")
        out.append_text(_bar(total, width=18))
        out.append("\n\n")

        # Per-core rows
        for i, v in enumerate(percore):
            col = "cyan" if v < 50 else "yellow" if v < 80 else "red"
            out.append(f"C{i:<2} ", style="dim cyan")
            out.append_text(_bar(v, width=10))
            out.append(f"  {v:4.1f}%\n", style=col)

        out.append("\n")

        # CPU sparkline
        out.append("graph\n", style="dim white")
        out.append_text(_mini_graph(list(self._cpu_hist), width=18, height=4, colour="cyan"))
        out.append("\n\n")

        # MEM
        vm = psutil.virtual_memory()
        def gib(b): return f"{b/1073741824:.1f}G"
        out.append("MEM  ", style="bold green")
        out.append(f"{mem_pct:5.1f}%\n", style="bold white")
        out.append_text(_bar(mem_pct, width=18))
        out.append(f"\n {gib(vm.used)}", style="green")
        out.append(" / ", style="dim white")
        out.append(f"{gib(vm.total)}\n\n", style="dim white")
        out.append_text(_mini_graph(list(self._mem_hist), width=18, height=3, colour="green"))
        out.append("\n\n")

        # GPU — try nvidia-smi via psutil sensors, fall back to N/A
        out.append("GPU  ", style="bold magenta")
        gpu_str = "N/A"
        try:
            temps = psutil.sensors_temperatures()
            for key in ("nvidia", "amdgpu", "radeon", "coretemp"):
                if key in temps:
                    t = temps[key][0].current
                    gpu_str = f"{t:.0f}°C"
                    break
        except Exception:
            pass
        out.append(f"{gpu_str}\n", style="bold white")

        return Panel(out,
                     title=Text("SYS", style="bold cyan"),
                     border_style="color(238)",
                     box=box.SIMPLE_HEAD,
                     padding=(0, 1))


# ══════════════════════════════════════════════════════════════════
#  PROMPT AREA — full conversation log + input
# ══════════════════════════════════════════════════════════════════
class PromptArea(ScrollableContainer):
    _tick: reactive[int] = reactive(0)

    def __init__(self, **kw):
        super().__init__(**kw)
        self._history: list = []  # list of (role, ts, text)
        self.can_focus = True

    def compose(self) -> ComposeResult:
        yield Static(id="message-log")

    def add_entry(self, text: str) -> None:
        ts = time.strftime("%H:%M:%S")
        self._history.append(("user", ts, text))
        self._history.append(("engine", ts, "…  (processing)"))
        if len(self._history) > 200:
            self._history = self._history[-200:]
        self._tick += 1
        self.call_after_refresh(self.scroll_end, animate=False)

    def update_engine(self, ansi_text: str, replace: bool = False) -> None:
        try:
            line = Text.from_ansi(ansi_text)
        except Exception:
            line = Text(ansi_text)

        if replace and self._history and self._history[-1][0] == "engine":
            ts = self._history[-1][1]
            self._history[-1] = ("engine", ts, line)
        else:
            self._history.append(("engine", time.strftime("%H:%M:%S"), line))

        if len(self._history) > 200:
            self._history = self._history[-200:]
        self._tick += 1
        self.call_after_refresh(self.scroll_end, animate=False)

    def watch__tick(self) -> None:
        log = self.query_one("#message-log", Static)
        log.update(self.render_history())

    def render_history(self) -> RenderableType:
        if not self._history:
            msg = Text()
            msg.append("\n\n  Ready.\n\n", style="dim white")
            msg.append("  Paste slam your PRD here!\n", style="bold cyan")
            msg.append("  The pipeline will process the requirements and generate everything.\n", style="dim white")
            msg.append("  Type ", style="dim white")
            msg.append("/help", style="bold white")
            msg.append(" or click the /help button for tips.\n", style="dim white")
            return msg

        out = Text()
        for role, ts, line in self._history:
            if role == "user":
                out.append(f"\n  [{ts}] ", style="dim white")
                out.append("you  ", style="bold white")
                out.append(line + "\n", style="white")
            else:
                out.append(f"  [{ts}] ", style="dim white")
                out.append("engine  ", style="bold cyan")
                if isinstance(line, Text):
                    out.append_text(line)
                    out.append("\n")
                else:
                    out.append(str(line) + "\n", style="dim white")
        return out

    def render(self) -> RenderableType:
        return "" # We use compose now



# ══════════════════════════════════════════════════════════════════
#  HELP TEXT
# ══════════════════════════════════════════════════════════════════
HELP_TEXT = """\
AKR Prompt Engine — Help
━━━━━━━━━━━━━━━━━━━━━━━━
Usage:
  • Type your PRD or prompt in the input box and click Submit (or Ctrl+S).
  • The engine will process your request and stream output here.

Commands:
  /help      Show this help message
  /clear     Clear the conversation history
  q          Quit the application (keyboard shortcut)

Tips:
  1. Be specific — detailed prompts produce better results.
  2. Paste full PRDs for end-to-end project generation.
  3. The SYS panel on the left shows live CPU / MEM stats.
"""

_HELP_COMMANDS = {"/help", "/clear"}


# ══════════════════════════════════════════════════════════════════
#  APP
# ══════════════════════════════════════════════════════════════════
class PromptMachineApp(App):
    CSS = """
    Screen {
        background: #0d0d14;
    }

    TitleBar {
        height: 1;
        background: #111118;
        dock: top;
        padding: 0 1;
    }

    LogoHeader {
        height: 10;
        background: #0d0d14;
        padding: 0 1;
    }

    #body {
        margin-top: 0;
        margin-bottom: 3;
        height: 1fr;
    }

    /* ── left sidebar: narrow ── */
    #side-col {
        width: 22;
        min-width: 22;
        max-width: 22;
    }

    SideStats {
        height: 100%;
    }

    /* ── prompt takes all remaining space ── */
    #prompt-col {
        width: 1fr;
    }

    PromptArea {
        height: 100%;
        overflow-y: scroll;
        overflow-x: hidden;
        border: tall #222222;
        padding: 0 1;
        margin: 0 1;
    }

    PromptArea:hover {
        border: tall cyan;
    }

    #message-log {
        width: 1fr;
        height: auto;
    }

    /* ── input bar ── */
    #input-bar {
        dock: bottom;
        height: 12;
        background: #111118;
        border-top: tall white;
        padding: 1 2;
    }

    #prompt-label {
        color: white;
        width: 4;
        content-align: left middle;
        text-style: bold;
    }

    TextArea {
        width: 1fr;
        height: 100%;
        background: transparent;
        border: none;
    }

    TextArea:focus { border: none; }

    #button-col {
        width: 20;
        min-width: 20;
        height: 100%;
        align: center middle;
    }

    Button {
        margin-left: 2;
        margin-top: 1;
        margin-bottom: 1;
        background: #111118;
        color: cyan;
        border: none;
        min-width: 16;
        height: 3;
    }

    Button:hover {
        background: #111118;
        color: white;
        border: none;
    }

    Footer {
        background: #111118;
        color: #445566;
        height: 1;
    }
    """

    # FIX: Ctrl+S as shortcut to submit, q to quit
    BINDINGS = [
        ("q", "quit", "Quit"),
        ("ctrl+s", "submit", "Submit"),
    ]

    def on_mount(self) -> None:
        import time
        area = self.query_one("#prompt-area", PromptArea)
        area._history.append(("engine", time.strftime("%H:%M:%S"), "──────────────────────────────────────────────────────────"))
        area._history.append(("engine", time.strftime("%H:%M:%S"), "  Paste your PRD.  Type END or -> END on a new line when done."))
        area._history.append(("engine", time.strftime("%H:%M:%S"), "──────────────────────────────────────────────────────────"))
        area._tick += 1

    def compose(self) -> ComposeResult:
        yield TitleBar()
        yield Footer()
        yield LogoHeader()

        with Horizontal(id="body"):
            with Vertical(id="side-col"):
                yield SideStats()
            with Vertical(id="prompt-col"):
                yield PromptArea(id="prompt-area")

        with Horizontal(id="input-bar"):
            yield Static("⟫ ", id="prompt-label")
            yield TextArea(id="prompt-input", show_line_numbers=False)
            with Vertical(id="button-col"):
                # FIX: removed Rich markup brackets from button labels
                btn = Button("Submit", id="submit-btn")
                btn.tooltip = (
                    "Tips:\n"
                    "1. Ask questions, edit files, or run commands.\n"
                    "2. Be specific for the best results.\n"
                    "3. Type /help for more info.\n"
                    "Shortcut: Ctrl+S"
                )
                yield btn
                yield Button("/help", id="help-btn")

    # ── keyboard shortcut for submit ──
    def action_submit(self) -> None:
        self._do_submit()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "submit-btn":
            self._do_submit()
        elif event.button.id == "help-btn":
            self._handle_command("/help")

    def on_text_area_changed(self, event: TextArea.Changed) -> None:
        if event.text_area.id == "prompt-input" and event.text_area.text.strip().endswith("END"):
            self._do_submit()

    def _do_submit(self) -> None:
        ta = self.query_one("#prompt-input", TextArea)
        text = ta.text.strip()
        ta.clear()

        # Clean END keyword
        if text.endswith("END"):
            text = text[:-3].strip()
            if text.endswith("->"):
                text = text[:-2].strip()

        if not text:
            return
        # Intercept built-in commands before hitting the pipeline
        if text.lower() in _HELP_COMMANDS:
            self._handle_command(text.lower())
        else:
            self.query_one("#prompt-area", PromptArea).add_entry(text)
            self.run_pipeline_bg(text)

    def _handle_command(self, cmd: str) -> None:
        """Handle built-in slash-commands without calling the pipeline."""
        area = self.query_one("#prompt-area", PromptArea)
        if cmd == "/help":
            # Clear everything, show help inline, then auto-clear after 6s
            area._history.clear()
            for line in HELP_TEXT.splitlines():
                area._history.append(("engine", time.strftime("%H:%M:%S"), line if line.strip() else " "))
            area._tick += 1
            self.set_timer(6, self._clear_history)
        elif cmd == "/clear":
            area._history.clear()
            area._tick += 1

    def _clear_history(self) -> None:
        area = self.query_one("#prompt-area", PromptArea)
        area._history.clear()
        area._tick += 1

    @work(thread=True)
    def run_pipeline_bg(self, text: str) -> None:
        from pipeline.pipeline import run_pipeline
        import re
        import os

        # Tell `ollama.py` to disable its high-speed spinner writes
        os.environ["PROMPT_MACHINE_TUI"] = "1"

        ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')

        class UIStdout:
            def __init__(self, app, area):
                self.app = app
                self.area = area
                self.buf = ""
                self.has_emitted_partial = False

            def isatty(self):
                return False

            def fileno(self):
                import io
                raise io.UnsupportedOperation("fileno")

            def readable(self):
                return False

            def writable(self):
                return True

            def write(self, s):
                if not s: return
                s = ansi_escape.sub('', s)

                for char in s:
                    if char == '\n':
                        if self.buf:
                            self.app.call_from_thread(self.area.update_engine, self.buf, self.has_emitted_partial)
                        else:
                            self.app.call_from_thread(self.area.update_engine, "", self.has_emitted_partial)
                        self.buf = ""
                        self.has_emitted_partial = False
                    elif char == '\r':
                        self.buf = ""
                    else:
                        self.buf += char

            def flush(self):
                if self.buf:
                    self.app.call_from_thread(self.area.update_engine, self.buf, self.has_emitted_partial)
                    self.has_emitted_partial = True

        area = self.query_one("#prompt-area", PromptArea)
        ui_out = UIStdout(self, area)

        original_stdout = sys.stdout
        original_stderr = sys.stderr
        sys.stdout = ui_out
        sys.stderr = ui_out
        try:
            from core.pipeline import run_prompt_machine
            
            run_prompt_machine(text, no_code=False, verbose=False)

            sys.stdout.flush()
            self.app.call_from_thread(area.update_engine, "✅ Done! Project files generated.", False)
        except BaseException as e:
            # BaseException catches SystemExit, KeyboardInterrupt, etc.
            self.app.call_from_thread(area.update_engine, f"❌ Error: {e}", False)
        finally:
            sys.stdout = original_stdout
            sys.stderr = original_stderr


if __name__ == "__main__":
    app = PromptMachineApp()
    app.run()