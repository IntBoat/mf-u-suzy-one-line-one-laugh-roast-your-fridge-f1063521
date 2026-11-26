"""One Line, One Laugh: Roast Your Fridge — make.fun entry.

The entry is one line of at most 200 characters, written exactly
as-is with no trailing newline.
"""

import os

ENTRY = "My fridge hums all night like it's plotting something, yet the only thing it's ever preserved is my disappointment and a jar from 2019."


def write_entry():
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY == ENTRY.strip(), "entry must not have leading/trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


def main():
    write_entry()


if __name__ == "__main__":
    main()
