"""Ridiculous at First Glance, Real by the Second — account B entry.

Writes one sentence (at most 200 characters) pitching a bizarre startup
idea that sounds absurd until you realise it would actually sell: a Wi-Fi
toaster that texts you when your bread is done. The line is fixed and
deterministic; the program just writes it to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

LINE = (
    "Our Wi-Fi toaster texts you when your bread is done: it sounds like "
    "a parody product, but it is real, and busy parents happily pay $49 "
    "to never burn breakfast again."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
