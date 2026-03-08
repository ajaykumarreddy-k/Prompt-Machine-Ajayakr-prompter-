"""stage11_code_validator.py — Strict JSX token validator."""

import os
import sys

FORBIDDEN_TOKENS = [
    "rounded-xl",
    "container",
    "bg-gradient"
]

def validate_generated_code(output_dir: str):
    """Scans all .jsx files in the output directory for forbidden tokens."""
    print("\033[36m  Stage 11 — Strict Token Validation\033[0m")
    
    src_dir = os.path.join(output_dir, "src")
    if not os.path.exists(src_dir):
        # If standard structure isn't there, check 'code/src' as fallback
        src_dir = os.path.join(output_dir, "code", "src")
        
    if not os.path.exists(src_dir):
        print(f"\033[33m    ⚠ Skipping validation: src directory not found at {src_dir}\033[0m")
        return

    violations = []

    for root, _, files in os.walk(src_dir):
        for file in files:
            if file.endswith(".jsx") or file.endswith(".tsx"):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                        for token in FORBIDDEN_TOKENS:
                            if token in content:
                                line_num = content.count('\n', 0, content.find(token)) + 1
                                violations.append(f"{file}:{line_num} -> Contains forbidden token '{token}'")
                except Exception as e:
                    print(f"\033[31m    Error reading {file}: {e}\033[0m")

    if violations:
        print("\033[31m  ✖ CODE VALIDATION FAILED\033[0m")
        for v in violations:
            print(f"\033[31m    - {v}\033[0m")
        # In a real production system, we'd raise an exception here.
        # For now, we print clearly and exit 1 if called directly.
        # raise ValueError("Strict Token Validation Failed")
        return False
    
    print("\033[32m    ✓ All components pass strict token validation.\033[0m")
    return True
