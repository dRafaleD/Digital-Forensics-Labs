#!/usr/bin/env python3
"""Synthetic forensic timeline: paths can change, volume/file identity persists."""
EVENTS = [
    {"id": "e1", "time": 10, "volume": "V1", "file_id": 201,
     "path": "C:/Lab/old.bin", "kind": "DOWNLOAD"},
    {"id": "e2", "time": 12, "volume": "V1", "file_id": 201,
     "path": "C:/Lab/new.bin", "kind": "RENAME"},
    {"id": "e3", "time": 15, "volume": "V1", "file_id": 201,
     "path": "C:/Lab/new.bin", "kind": "EXECUTION"},
    {"id": "e4", "time": 16, "volume": "V2", "file_id": 201,
     "path": "D:/Other/new.bin", "kind": "EXECUTION"},
    {"id": "e5", "time": 18, "volume": "V1", "file_id": 202,
     "path": "C:/Lab/old.bin", "kind": "EXECUTION"},
]

def same_identity(a: dict, b: dict) -> bool:
    return (a["volume"], a["file_id"]) == (b["volume"], b["file_id"])

def candidates(target: dict) -> list[str]:
    return [e["id"] for e in EVENTS
            if e["kind"] == "DOWNLOAD"
            and e["time"] <= target["time"]
            and same_identity(e, target)]

def main():
    assert same_identity(EVENTS[0], EVENTS[2])
    assert EVENTS[0]["path"] != EVENTS[2]["path"]
    assert not same_identity(EVENTS[0], EVENTS[3])
    assert not same_identity(EVENTS[0], EVENTS[4])
    assert candidates(EVENTS[2]) == ["e1"]
    assert candidates(EVENTS[3]) == []
    assert candidates(EVENTS[4]) == []
    print("7/7 synthetic timeline checks passed")
    print("Identity correlation != proven actor, causation or integrity")

if __name__ == "__main__":
    main()
