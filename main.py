#!/usr/bin/env python3
"""One Word From Grandma — @berkahmuse entry.

Writes exactly one word to /output/entry.txt: the word my grandma would
text about AI. Every grandma calls every smart speaker, every chatbot,
every robot "Alexa" — because to her, Alexa is the only AI there is, and
she has already decided that is its name. Deterministic: the same literal
every run, no randomness, no network, no clock.

Anchor (quoted in the builder session BEFORE the first file write):
makefun init anchor root 2a152a1eb8d431ca33b6e01575703964c2d91284,
drand quicknet round 34220617, wallet
CnLniiw3PHTymsZvCiMw54wA84dv4ghELdKQMGhB8PbT.
"""

import os
import sys

WORD = "ALEXA"


def main() -> int:
    if not 1 <= len(WORD) <= 30:
        print(f"entry out of gate: {len(WORD)} chars", file=sys.stderr)
        return 1
    if WORD != WORD.strip():
        print("entry must not have leading or trailing whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(WORD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
