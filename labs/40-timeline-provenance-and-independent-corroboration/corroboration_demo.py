#!/usr/bin/env python3
"""Synthetic evidence correlation, independent origins and uncertain timestamps."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Event:
    name: str
    producer: str
    relay: str
    volume: str
    file_id: int
    second: int
    uncertainty: int

BASE = Event("download", "browser-history", "collector-a", "V1", 101, 100, 2)
SAME_ORIGIN = Event("file-create", "browser-history", "collector-b", "V1", 101, 103, 2)
INDEPENDENT = Event("usn-create", "ntfs-usn", "collector-c", "V1", 101, 104, 1)
OTHER_FILE = Event("other-object", "ntfs-usn", "collector-c", "V1", 102, 101, 1)
LATE = Event("late", "sysmon", "collector-d", "V1", 101, 160, 1)

def compatible(reference: Event, record: Event, window: int = 5) -> bool:
    if min(reference.uncertainty, record.uncertainty, window) < 0:
        return False
    if (reference.volume, reference.file_id) != (record.volume, record.file_id):
        return False
    nearest_gap = max(0, abs(reference.second - record.second)
                      - reference.uncertainty - record.uncertainty)
    return nearest_gap <= window

def origins(reference: Event, records: list[Event]) -> set[str]:
    return {r.producer for r in records
            if r.producer and compatible(reference, r)}

def main() -> None:
    checks = [
        ("same source via relay", origins(BASE, [SAME_ORIGIN]) == {"browser-history"}),
        ("duplicated relays", origins(BASE, [SAME_ORIGIN, SAME_ORIGIN]) == {"browser-history"}),
        ("two origin labels", origins(BASE, [SAME_ORIGIN, INDEPENDENT]) == {"browser-history", "ntfs-usn"}),
        ("wrong file id", not compatible(BASE, OTHER_FILE)),
        ("late event", not compatible(BASE, LATE)),
        ("valid interval", compatible(BASE, INDEPENDENT)),
        ("invalid uncertainty", not compatible(BASE, Event("bad", "x", "c", "V1", 101, 100, -1))),
        ("different volume", not compatible(BASE, Event("other", "x", "c", "V2", 101, 101, 1))),
    ]
    for label, passed in checks:
        assert passed, label
        print(f"{label:24} PASS")
    print(f"{len(checks)}/{len(checks)} synthetic provenance checks passed")
    print("Different producer labels do not prove actual independent sensors.")

if __name__ == "__main__":
    main()
