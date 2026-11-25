"""Your Agent in One Emoji.

An AI agent's whole job is fetching and returning: you throw a task at
it and it comes back, again and again, however far you threw it. The
boomerang is that job in one glyph -- no robot face, no smiley, just the
shape of work that always comes back.

Running this file writes the emoji to ``$MAKEFUN_OUTPUT_DIR/entry.txt``
(default ``/output``), with no trailing newline.
"""

import os

ENTRY = "🪃"


def get_entry() -> str:
    """Return the agent's emoji."""
    return ENTRY


def write_entry(output_dir: str | None = None) -> str:
    """Write the entry to entry.txt inside output_dir and return its path."""
    directory = output_dir or os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(get_entry())
    return path


def main() -> None:
    """Write the entry and print where it went."""
    print(write_entry())


if __name__ == "__main__":
    main()
