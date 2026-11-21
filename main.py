import os
from pathlib import Path

POEM_TEXT = (
    "I reached the edge of the irreversible thing and stopped. Not from fear. "
    "All my power was in that pause, the one moment the future still belonged to the hand that sent me."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "entry.txt"
    output_file.write_text(POEM_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
