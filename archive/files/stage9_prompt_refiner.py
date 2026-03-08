"""stage9_prompt_refiner.py — Final polish pass on the generated UI prompt."""

from ollama import ollama

SYSTEM = (
    "You are a prompt engineering expert for AI UI tools (v0.dev, Lovable, Bolt). "
    "Refine prompts to be maximally precise, layout-specific, and design-accurate. "
    "Preserve all details. Output only the improved prompt — no commentary."
)


def refine_prompt(raw_prompt: str, intent: dict) -> str:
    if not raw_prompt or not raw_prompt.strip():
        return raw_prompt

    user_prompt = f"""Improve this frontend generation prompt.

Original prompt:
{raw_prompt}

Improvement goals:
1. Make layout instructions more explicit — exact component order, column counts
2. Add specific Tailwind class hints for the AI to follow  
3. Strengthen the design language description (precise aesthetic)
4. Add responsive breakpoint notes (mobile → tablet → desktop)
5. Ensure tone matches: {intent.get('tone', 'professional')}
6. Keep it focused on {intent['product_name']} — no generic filler

Output ONLY the improved prompt. No preamble, no sign-off."""

    refined = ollama(user_prompt, system=SYSTEM, label="Refining prompt")

    # Fall back to original if refiner returns nothing
    return refined if refined and refined.strip() else raw_prompt
