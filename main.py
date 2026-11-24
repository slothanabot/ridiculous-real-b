"""Ridiculous at First Glance, Real by the Second — account B entry.

Writes one sentence (at most 200 characters) pitching a bizarre startup
idea that sounds absurd until you realise it would actually sell: rental
goats that mow your lawn — real goatscaping, already a business in
several US suburbs. The line is fixed and deterministic; the program
just writes it to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

MAX_CHARS = 200

LINE = (
    "Our rental goats mow your lawn for $30 a visit: it sounds like a "
    "farm joke, but suburbs pay because the herd weeds, fertilizes, and "
    "never needs gas."
)


def check_line(line: str) -> str:
    """Enforce the kit gate: 1-200 chars, one sentence, not blank."""
    text = line.strip()
    if not text:
        raise ValueError("pitch must not be empty")
    if len(text) > MAX_CHARS:
        raise ValueError(f"pitch is {len(text)} chars, over the {MAX_CHARS} limit")
    if text.count(".") > 1 or "\n" in text:
        raise ValueError("pitch must be a single sentence on one line")
    return text


def write_entry(line: str, out_dir: str) -> str:
    """Validate the pitch and write it to entry.txt; returns the path."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(check_line(line) + "\n")
    return path


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(LINE, out_dir)


if __name__ == "__main__":
    main()
