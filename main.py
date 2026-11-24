#!/usr/bin/env python3
"""One Emoji, One Smile — entry program.

Writes exactly one emoji to /output/entry.txt: nothing else, no words,
no explanation, no trailing newline.

Emoji choice, reconsidered against the judge's brief (in its order):
  1. Warm/friendly at first glance: a literal smiling face.
  2. Universality: sunshine reads the same to any stranger, any age.
  3. Chosen, not default: the brief rewards a pick that is NOT the first
     smiley that comes to mind (so not 🙂/😊/😄), while staying instantly
     readable. A smiling sun is exactly that — distinctive, yet nobody
     has to think about what it means.
  4. Right for a stranger: no hug, hearts or flirtation (so not 🤗/🥰/🫶),
     just warmth offered from a safe distance.
"""

import os

EMOJI = "\U0001F31E"  # 🌞 sun with face — a warm, smiling face

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
