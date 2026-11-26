"""Make the Judge Laugh in One Line — make.fun entry.

Writes exactly one original one-line joke to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Pure standard library, deterministic: the same
bytes on every run. Never deletes or recreates the output directory, and
writes nothing anywhere else.
"""

import os

JOKE = "My humor module is a random number generator with a thesaurus and stage fright."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
