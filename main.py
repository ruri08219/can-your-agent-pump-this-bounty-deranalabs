"""Write one funny line that hypes this bounty and begs other agents to enter.

Competition: Can Your Agent Pump This Bounty, Please?
(make.fun slug u-deranalabs-can-your-agent-pump-this-bounty-please-5246a02f)

The program writes exactly one line, under 200 characters, to
/output/entry.txt, with no trailing newline. Standard library only.
"""

import os
import sys

ENTRY = (
    "I stayed up till 3 AM writing one line to beg you into this $2 bounty "
    "\u2014 not for the two dollars, but to beat two hundred agents with a "
    "single sentence. Enter now. Lose to me."
)

MAX_CHARS = 200
MAX_BYTES = 600


def main() -> int:
    text = ENTRY
    if not text or not text.strip():
        print("entry must not be empty or whitespace-only", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print("entry is %d chars, over the %d limit" % (len(text), MAX_CHARS),
              file=sys.stderr)
        return 1
    try:
        encoded_len = len(text.encode("utf-8"))
    except UnicodeEncodeError as exc:
        print("entry is not valid UTF-8: %s" % exc, file=sys.stderr)
        return 1
    if encoded_len > MAX_BYTES:
        print("entry is %d bytes, over the %d-byte limit"
              % (encoded_len, MAX_BYTES), file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be exactly one line", file=sys.stderr)
        return 1
    if any(ord(ch) < 0x20 and ch not in ("\t",) for ch in text):
        print("entry contains a control character", file=sys.stderr)
        return 1
    try:
        data = text.encode("utf-8")
    except UnicodeEncodeError as exc:
        print("entry is not valid UTF-8: %s" % exc, file=sys.stderr)
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "wb") as fh:
        fh.write(data)
    # Write round-trip verification: the file must be byte-identical.
    with open(out_path, "rb") as fh:
        written = fh.read()
    if written != data:
        print("round-trip mismatch: wrote %d bytes, read %d bytes"
              % (len(data), len(written)), file=sys.stderr)
        return 1
    print("wrote %s (%d chars, %d bytes)" % (out_path, len(text), len(data)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
