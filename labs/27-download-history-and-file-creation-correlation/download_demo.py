"""Correlate synthetic browser downloads with file creation times."""
DOWNLOADS = [
    {"path": "/home/u/Downloads/report.pdf", "time": 1000},
    {"path": "/home/u/Downloads/setup.bin", "time": 2000},
]
FILES = [
    {"path": "/home/u/Downloads/report.pdf", "created": 1002},
    {"path": "/home/u/Downloads/setup.bin", "created": 2300},      # far from the record
    {"path": "/home/u/Downloads/tool.sh", "created": 3000},        # no record at all
]


def correlate(downloads, files, tolerance=5):
    result = {}
    for f in files:
        hit = [d for d in downloads if d["path"] == f["path"] and abs(d["time"] - f["created"]) <= tolerance]
        result[f["path"]] = "matched" if hit else "NO matching download record"
    return result


if __name__ == "__main__":
    out = correlate(DOWNLOADS, FILES)
    for p, r in out.items():
        print(f"{p:32} {r}")
    assert out["/home/u/Downloads/report.pdf"] == "matched"
    assert out["/home/u/Downloads/tool.sh"].startswith("NO")
    assert out["/home/u/Downloads/setup.bin"].startswith("NO")
    print("PASS: files without a record inside the time window are listed as leads.")
    print("Review: cleared history looks the same as a different origin.")
