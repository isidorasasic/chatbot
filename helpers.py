from pathlib import Path


PROMPT_DIR = Path(__file__).resolve().parents[0] / "prompts"

def load_prompt(filename: str):
    filepath = PROMPT_DIR / filename
    if not filepath.exists():
        raise FileNotFoundError(f"Prompt file not found: {filepath}")
    
    return filepath.read_text(encoding="utf-8")

