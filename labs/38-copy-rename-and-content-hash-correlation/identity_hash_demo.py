#!/usr/bin/env python3
"""Synthetic copy vs rename evidence: identity, path and digest answer different questions."""
from hashlib import sha256

def digest(content: bytes) -> str:
    return sha256(content).hexdigest()

CONTENT_A = digest(b"fictional training artifact A")
CONTENT_B = digest(b"fictional training artifact B")
SOURCE = {"time": 10, "volume": "VOL-1", "id": 100, "path": "C:/Lab/a.bin", "sha": CONTENT_A}

def classify(origin: dict, observed: dict) -> str:
    if observed["time"] < origin["time"]:
        return "TIME_REVERSED"
    same_object = (origin["volume"], origin["id"]) == (observed["volume"], observed["id"])
    if same_object:
        return "SAME_IDENTITY"
    if origin["path"] == observed["path"]:
        return "PATH_REUSED"
    if origin["sha"] == observed["sha"]:
        return "CONTENT_MATCH_ONLY"
    return "NO_MATCH"

def main() -> None:
    cases = [
        ("rename", {**SOURCE, "time": 12, "path": "C:/Lab/renamed.bin"}, "SAME_IDENTITY"),
        ("same object", {**SOURCE, "time": 15}, "SAME_IDENTITY"),
        ("copy", {"time": 20, "volume": "VOL-1", "id": 200, "path": "C:/Lab/copy.bin", "sha": CONTENT_A}, "CONTENT_MATCH_ONLY"),
        ("other volume", {"time": 25, "volume": "VOL-2", "id": 100, "path": "D:/copy.bin", "sha": CONTENT_A}, "CONTENT_MATCH_ONLY"),
        ("path reused", {**SOURCE, "time": 30, "id": 300, "sha": CONTENT_B}, "PATH_REUSED"),
        ("unrelated", {"time": 35, "volume": "VOL-2", "id": 999, "path": "D:/other.bin", "sha": CONTENT_B}, "NO_MATCH"),
        ("clock order", {**SOURCE, "time": 8}, "TIME_REVERSED"),
    ]
    for label, target, expected in cases:
        result = classify(SOURCE, target)
        assert result == expected, (label, result)
        print(f"{label:15} {result}")
    assert CONTENT_A != CONTENT_B
    print("8/8 synthetic evidence checks passed; copy/rename causation unproven")

if __name__ == "__main__":
    main()
