"""stage11_code_validator.py — Strict JSX token validator with Style Awareness."""

import os
import sys

# Base forbidden tokens (removed rounded-xl and bg-gradient as they are style-dependent)
FORBIDDEN_TOKENS = ["bg-custom-", "text-custom-"]

STYLE_ALLOWED_TOKENS = {
     "glassmorphism": ["rounded-xl", "backdrop-blur", "bg-white/", "bg-gradient"],
     "futuristic":    ["bg-gradient", "animate-", "rounded-xl"],
     "aurora":        ["bg-gradient", "animate-", "rounded-xl", "backdrop-blur"],
     "cyberpunk":     ["bg-gradient", "border-green"],
     "dark_mode":     ["bg-gray-950", "bg-zinc-950", "bg-slate-950"],
     "neobrutalism":  ["border-2", "border-black", "shadow-["],
     "neumorphism":   ["rounded-xl", "shadow-[", "bg-gray-200"],
     "retro_80s":     ["bg-gradient", "rounded-xl"],
     "y2k":           ["bg-gradient", "rounded-xl"],
     "claymorphism":  ["rounded-xl", "rounded-2xl", "rounded-3xl"],
     "gradient_mesh": ["bg-gradient"],
}

def validate_generated_code(output_dir: str, detected_styles: list[str] = None):
    """Scans all .jsx files in the output directory for forbidden tokens, respecting active styles."""
    print("\033[36m  Stage 11 — Strict Token Validation\033[0m")
    
    src_dir = os.path.join(output_dir, "src")
    if not os.path.exists(src_dir):
        # Fallback
        src_dir = os.path.join(output_dir, "code", "src")
        
    if not os.path.exists(src_dir):
        print(f"\033[33m    ⚠ Skipping validation: src directory not found at {src_dir}\033[0m")
        return True

    # Build allowed set from detected_styles (Fix 5)
    allowed_this_run = set()
    for style in (detected_styles or []):
        allowed_this_run.update(STYLE_ALLOWED_TOKENS.get(style, []))

    violations = []
    
    # Also define hard forbidden (if not specifically allowed)
    hard_forbidden = ["container", "bg-custom-", "text-custom-"]
    # bg-gradient and rounded-xl are forbidden UNLESS allowed by style
    maybe_forbidden = ["bg-gradient", "rounded-xl"]

    for root, _, files in os.walk(src_dir):
        for file in files:
            if file.endswith(".jsx") or file.endswith(".tsx"):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                        # 1. Check Hard Forbidden
                        for token in hard_forbidden:
                            if token in content:
                                line_num = content.count('\n', 0, content.find(token)) + 1
                                violations.append(f"{file}:{line_num} -> Contains forbidden token '{token}'")
                        
                        # 2. Check Style-Dependent Forbidden
                        for token in maybe_forbidden:
                            if token in content:
                                # Skip if directly allowed or contained in an allowed string
                                if any(token in a or a in token for a in allowed_this_run):
                                    continue
                                line_num = content.count('\n', 0, content.find(token)) + 1
                                violations.append(f"{file}:{line_num} -> Contains forbidden token '{token}' for detected styles")
                                
                        # 3. Check for any generic allowed violations (e.g. backdrop-blur if not glassmorphism)
                        # (Optional: implement stricter reverse checks)

                except Exception as e:
                    print(f"\033[31m    Error reading {file}: {e}\033[0m")

    if violations:
        print("\033[31m  ✖ CODE VALIDATION FAILED\033[0m")
        for v in violations:
            print(f"\033[31m    - {v}\033[0m")
        return False
    
    print("\033[32m    ✓ All components pass strict token validation.\033[0m")
    return True
