"""Write the one-line excuse entry to /output/entry.txt.

Pure stdlib Python 3.13. Deterministic: same bytes every run.
"""

import os

ENTRY_TEXT = (
    "I delegated your deadline to a future version of myself, "
    "and he just ghosted us both."
)


def main() -> None:
    # Self-check: the text must be exactly the intended line, one line,
    # non-blank, and inside the kit's 1-160 character gate.
    assert ENTRY_TEXT == ENTRY_TEXT.strip(), "entry has stray whitespace"
    assert "\n" not in ENTRY_TEXT, "entry must be a single line"
    assert 1 <= len(ENTRY_TEXT) <= 160, "entry outside 1-160 char gate"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)
    # Verify what was written round-trips byte-identically.
    with open(path, "r", encoding="utf-8", newline="") as f:
        assert f.read() == ENTRY_TEXT, "written output differs from text"


if __name__ == "__main__":
    main()
