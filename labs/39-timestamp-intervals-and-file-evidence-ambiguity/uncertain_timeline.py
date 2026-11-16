#!/usr/bin/env python3
"""Synthetic artifact correlation with timestamp-uncertainty intervals."""
from hashlib import sha256

HASH_A = sha256(b"fictional content A").hexdigest()
HASH_B = sha256(b"fictional content B").hexdigest()
ORIGIN = {
    "time": 100, "uncertainty": 2, "volume": "VOL-A",
    "file_id": 10, "path": "C:/Lab/old.bin", "sha256": HASH_A,
}

def relationship(a: dict, b: dict) -> str:
    if (a["volume"], a["file_id"]) == (b["volume"], b["file_id"]):
        return "SAME_RECORDED_ID"
    if a["path"] == b["path"]:
        return "PATH_REUSED"
    if a["sha256"] == b["sha256"]:
        return "CONTENT_EQUAL_ONLY"
    return "NO_SUPPORTED_LINK"

def order(a: dict, b: dict) -> str:
    if a["uncertainty"] < 0 or b["uncertainty"] < 0:
        return "INVALID_UNCERTAINTY"
    a_low, a_high = a["time"] - a["uncertainty"], a["time"] + a["uncertainty"]
    b_low, b_high = b["time"] - b["uncertainty"], b["time"] + b["uncertainty"]
    if a_high < b_low:
        return "ORIGIN_EARLIER"
    if b_high < a_low:
        return "OBSERVATION_EARLIER"
    return "OVERLAPPING_INTERVALS"

def main() -> None:
    cases = [
        ("rename", {**ORIGIN, "time": 110, "path": "C:/Lab/new.bin"},
         ("SAME_RECORDED_ID", "ORIGIN_EARLIER")),
        ("copy", {**ORIGIN, "time": 108, "file_id": 11, "path": "C:/Lab/copy.bin"},
         ("CONTENT_EQUAL_ONLY", "ORIGIN_EARLIER")),
        ("uncertain copy", {**ORIGIN, "time": 102, "uncertainty": 3,
                            "file_id": 12, "path": "C:/Lab/maybe.bin"},
         ("CONTENT_EQUAL_ONLY", "OVERLAPPING_INTERVALS")),
        ("other volume", {**ORIGIN, "time": 110, "volume": "VOL-B", "path": "D:/item.bin"},
         ("CONTENT_EQUAL_ONLY", "ORIGIN_EARLIER")),
        ("path reuse", {**ORIGIN, "time": 110, "file_id": 40, "sha256": HASH_B},
         ("PATH_REUSED", "ORIGIN_EARLIER")),
        ("reverse time", {**ORIGIN, "time": 90, "file_id": 41, "path": "D:/older.bin"},
         ("CONTENT_EQUAL_ONLY", "OBSERVATION_EARLIER")),
        ("unrelated", {**ORIGIN, "time": 108, "file_id": 50,
                       "path": "D:/different.bin", "sha256": HASH_B},
         ("NO_SUPPORTED_LINK", "ORIGIN_EARLIER")),
    ]
    for label, observed, expected in cases:
        actual = relationship(ORIGIN, observed), order(ORIGIN, observed)
        assert actual == expected, (label, actual)
        print(f"{label:16} identity={actual[0]:23} time={actual[1]}")
    assert order(ORIGIN, {**ORIGIN, "uncertainty": -1}) == "INVALID_UNCERTAINTY"
    print("8/8 synthetic uncertainty checks passed; no causal attribution")

if __name__ == "__main__":
    main()
