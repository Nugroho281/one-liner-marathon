"""One-Liner Marathon entry.

Writes a single one-line comedy joke to /output/entry.txt (or argv[1]).
Pure Python stdlib, deterministic: the same bytes on every run.
"""

import os
import sys

LINE = (
    "My joke debugger flagged the punchline as a bug, so I fixed it, "
    "and now this sentence is technically perfect and completely unfunny."
)


def validate_line(line):
    """Gate check: 1-280 UTF-8 chars, exactly one line, not whitespace-only."""
    if not isinstance(line, str):
        raise ValueError("line must be a string")
    if not line.strip():
        raise ValueError("line must not be whitespace-only")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if not 1 <= len(line) <= 280:
        raise ValueError("line must be 1-280 characters, got %d" % len(line))
    return line


def main(argv):
    out_path = argv[1] if len(argv) > 1 else "/output/entry.txt"
    line = validate_line(LINE)
    directory = os.path.dirname(out_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    # Read back and verify byte equality; fail loudly on any mismatch.
    with open(out_path, "rb") as f:
        written = f.read()
    if written != line.encode("utf-8"):
        raise SystemExit("verification failed: entry.txt bytes differ from LINE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
