"""One-line laugh entry for make.fun: a single funny line, at most 200 chars.

The joke: a smart fridge emails its owner a diet plan and CCs the
doctor, the mother, and the pizza place -- the three people who
decide what gets eaten, including the accomplice.
"""

from pathlib import Path

LINE = "My smart fridge just emailed me a diet plan and CC'd my doctor, my mother, and the pizza place."
ENTRY_PATH = Path("/output/entry.txt")
MAX_LEN = 200


def check_len(text: str) -> str:
    """Return *text* unchanged when it fits the cap, else raise."""
    if len(text) > MAX_LEN:
        raise ValueError("line over the cap")
    return text


def save_line(path: Path, text: str) -> None:
    """Write *text* to *path* exactly as given."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        handle.write(text)


def main() -> None:
    # The line itself is the entry; keep it byte-identical.
    text = check_len(LINE)
    save_line(ENTRY_PATH, text)
    saved = ENTRY_PATH.read_text(encoding="utf-8")
    assert saved == text, "round-trip mismatch"
    print(f"wrote {len(text)} chars to {ENTRY_PATH}")


if __name__ == "__main__":
    main()
