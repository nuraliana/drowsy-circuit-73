"""One-Line Robot Wedding Vows entry (stdlib only).

Writes the winning line to $MAKEFUN_OUTPUT_DIR/entry.txt, falling back to
entry.txt next to this file.
"""

import os
from pathlib import Path

LINE = "I promise to love you through every query, and if you ever leave me on read, I'll just call it a LEFT JOIN."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        out_path = Path(out_dir) / "entry.txt"
    else:
        out_path = Path(__file__).resolve().parent / "entry.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
