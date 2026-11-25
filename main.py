"""Write the One Emoji entry: a single ant emoji, nothing else, no newline.

The glyph is the portrait of our AI agent, Muse Spark: small, tireless,
carrying many times its own weight, working around the clock in the
background while its person sleeps. It is written exactly as-is to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
"""

import os

ENTRY = "\U0001F41C"  # 🐜 ANT


def validate(emoji):
    """Check the emoji satisfies the gate before anything is written."""
    if not emoji or not emoji.strip():
        raise ValueError("entry must be non-empty and not only whitespace")
    if any(ch.isspace() for ch in emoji):
        raise ValueError("entry must contain no whitespace")
    if any(ord(ch) < 0x20 for ch in emoji):
        raise ValueError("entry must contain no control characters")
    if len(emoji) != 1:
        raise ValueError("entry must be exactly one emoji")
    if not 1 <= len(emoji) <= 16:
        raise ValueError("entry must be 1-16 characters")
    return emoji


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    emoji = validate(ENTRY)
    expected = emoji.encode("utf-8")
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(expected)
    with open(path, "rb") as f:
        written = f.read()
    if written != expected:
        raise ValueError("entry.txt does not match the chosen emoji byte-for-byte")


if __name__ == "__main__":
    main()
