"""Parse a synthetic timestamped shell history and flag fetch -> chmod -> run sequences."""
HISTORY = """#1700000000
ls -la
#1700000050
curl -o /tmp/tool.bin https://files.example.test/tool.bin
#1700000062
chmod +x /tmp/tool.bin
#1700000075
/tmp/tool.bin --quiet
#1700003600
cat notes.txt
"""


def parse(text):
    entries, ts = [], None
    for line in text.splitlines():
        if line.startswith("#") and line[1:].isdigit():
            ts = int(line[1:])
        elif line.strip():
            entries.append((ts, line))
    return entries


def sequences(entries, window=120):
    hits = []
    for i, (t0, cmd) in enumerate(entries):
        if cmd.startswith(("curl ", "wget ")):
            nxt = [(t, c) for t, c in entries[i + 1:] if t - t0 <= window]
            if any("chmod +x" in c for _, c in nxt) and any(c.startswith("/tmp/") for _, c in nxt):
                hits.append((t0, cmd))
    return hits


if __name__ == "__main__":
    hits = sequences(parse(HISTORY))
    print(hits)
    assert len(hits) == 1 and hits[0][0] == 1700000050
    assert sequences(parse("#1\nls\n#2\ncat a\n")) == []
    print("PASS: a fetch, chmod and run sequence inside a short window is flagged.")
    print("Review: admins run the same sequence, and history can be edited, missing or unsaved.")
