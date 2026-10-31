"""Flag internally inconsistent timestamps in synthetic file records."""
RECORDS = [
    {"name": "report.docx", "created": 1700000000.123456789, "modified": 1700003600.5},
    {"name": "copied.docx", "created": 1700007200.25, "modified": 1700003600.5},
    {"name": "tool.exe", "created": 1700000000.0, "modified": 1700000000.0},
    {"name": "ancient.dll", "created": 631152000.7, "modified": 1700000000.9},
]
OS_RELEASE = 1000000000  # synthetic lower bound for this system


def flags(record):
    found = []
    if record["created"] > record["modified"]:
        found.append("created after modified (copy or tampering)")
    if record["created"] == int(record["created"]) and record["modified"] == int(record["modified"]):
        found.append("zero sub-second precision on both times")
    if record["created"] < OS_RELEASE:
        found.append("created before the OS release")
    return found


if __name__ == "__main__":
    for r in RECORDS:
        print(f"{r['name']:12} {flags(r)}")
    assert flags(RECORDS[0]) == []
    assert any("after modified" in f for f in flags(RECORDS[1]))
    assert any("sub-second" in f for f in flags(RECORDS[2]))
    assert any("OS release" in f for f in flags(RECORDS[3]))
    print("PASS: each rule raises a lead; none of them proves tampering by itself.")
    print("Review: corroborate with a journal, event log or backup before concluding.")
