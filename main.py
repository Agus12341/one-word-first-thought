"""One Word, First Thought - make.fun entry.

Writes exactly one word, the first that comes to mind, to
/output/entry.txt with no trailing newline.
"""

import os

TEXT = "Coffee."


def main() -> None:
    # Self-check: the gate takes UTF-8 text of 1 to 24 characters, not
    # only white space, and this bounty wants exactly one word.
    assert TEXT == TEXT.strip(), "entry must not have surrounding white space"
    assert 1 <= len(TEXT) <= 24, "entry must be 1 to 24 characters"
    assert len(TEXT.split()) == 1, "entry must be exactly one word"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
