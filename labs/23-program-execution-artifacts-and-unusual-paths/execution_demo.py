"""Flag rarely-run executables in unusual locations from synthetic execution records."""
RECORDS = [
    {"exe": r"C:\Windows\System32\notepad.exe", "runs": 120, "last": "2026-10-01"},
    {"exe": r"C:\Users\u1\AppData\Local\Temp\a1b2.exe", "runs": 1, "last": "2026-10-20"},
    {"exe": r"C:\Users\u1\Downloads\setup.exe", "runs": 1, "last": "2026-10-18"},
    {"exe": r"C:\Program Files\App\app.exe", "runs": 40, "last": "2026-10-19"},
]
UNUSUAL = ("\\temp\\", "\\downloads\\", "\\appdata\\local\\temp\\")


def flags(record):
    path = record["exe"].lower()
    reasons = []
    if any(u in path for u in UNUSUAL):
        reasons.append("runs from a user-writable staging location")
        if record["runs"] <= 2:
            reasons.append("rarely run")
    return reasons


if __name__ == "__main__":
    for r in RECORDS:
        print(f"{r['exe']:48} {flags(r)}")
    assert flags(RECORDS[0]) == [] and flags(RECORDS[3]) == []
    assert len(flags(RECORDS[1])) == 2
    print("PASS: unusual location plus low run count creates a lead, not a verdict.")
    print("Review: installers legitimately run from temp; correlate with logs and file times.")
