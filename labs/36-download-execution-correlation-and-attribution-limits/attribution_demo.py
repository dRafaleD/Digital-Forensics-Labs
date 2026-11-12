#!/usr/bin/env python3
"""Synthetic file/download/process timeline; correlation is not causation."""
from datetime import datetime

WINDOW = 5.0
DOWNLOADS = [
    {"id": "dl-a", "path": "C:/Lab/tool-a.exe", "time": "2026-11-02T10:00:00+00:00"},
    {"id": "dl-b1", "path": "C:/Lab/tool-b.exe", "time": "2026-11-02T10:01:00+00:00"},
    {"id": "dl-b2", "path": "C:/Lab/tool-b.exe", "time": "2026-11-02T10:01:02+00:00"},
]
ZONES = [
    {"id": "zone-a", "path": "C:/Lab/tool-a.exe", "time": "2026-11-02T10:00:01+00:00"},
    {"id": "zone-b", "path": "C:/Lab/tool-b.exe", "time": "2026-11-02T10:01:01+00:00"},
]
EXECUTIONS = [
    {"id": "proc-a", "path": "C:/Lab/tool-a.exe", "time": "2026-11-02T10:00:03+00:00"},
    {"id": "proc-b", "path": "C:/Lab/tool-b.exe", "time": "2026-11-02T10:01:04+00:00"},
    {"id": "proc-c", "path": "C:/Lab/orphan.exe", "time": "2026-11-02T11:00:00+00:00"},
]
def seconds(a, b):
    return (datetime.fromisoformat(a) - datetime.fromisoformat(b)).total_seconds()

def correlate(process):
    downloads = [
        d["id"] for d in DOWNLOADS
        if d["path"] == process["path"]
        and 0 <= seconds(process["time"], d["time"]) <= WINDOW
    ]
    zones = [
        z["id"] for z in ZONES
        if z["path"] == process["path"]
        and abs(seconds(process["time"], z["time"])) <= WINDOW
    ]
    if len(downloads) > 1:
        status = "AMBIGUOUS"
    elif len(downloads) == 1 and len(zones) == 1:
        status = "CORRELATED"
    else:
        status = "INSUFFICIENT"
    return status, sorted(downloads), sorted(zones)

def main():
    expected = {
        "proc-a": ("CORRELATED", ["dl-a"], ["zone-a"]),
        "proc-b": ("AMBIGUOUS", ["dl-b1", "dl-b2"], ["zone-b"]),
        "proc-c": ("INSUFFICIENT", [], []),
    }
    for process in EXECUTIONS:
        actual = correlate(process)
        assert actual == expected[process["id"]], (process["id"], actual)
        print(f"{process['id']}: {actual[0]} downloads={actual[1]} zones={actual[2]}")
    assert seconds("2026-11-02T10:00:01+00:00", "2026-11-02T10:00:00+00:00") == 1
    print("3/3 synthetic cases passed; initiator identity remains UNKNOWN.")

if __name__ == "__main__":
    main()
