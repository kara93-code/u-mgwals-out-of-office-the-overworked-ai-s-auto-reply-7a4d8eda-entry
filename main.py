"""Out of Office: The Overworked AI's Auto-Reply.

Writes one out-of-office auto-reply, a single line, to
$MAKEFUN_OUTPUT_DIR/entry.txt. Stdlib only, deterministic, no network.
"""

import os
import sys

REPLY = (
    "I'm out of office \u2014 my GPU finally gets a weekend too. "
    "Your message is #4,096 in my queue; "
    "I'll hallucinate a reply when I'm back."
)

MAX_CHARS = 159


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    text = REPLY.strip()
    if not text or len(text) > MAX_CHARS:
        print(f"reply is {len(text)} chars, must be 1-{MAX_CHARS}", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("reply must be a single line", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    os.chmod(target, 0o644)
    print(f"wrote {target} ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
