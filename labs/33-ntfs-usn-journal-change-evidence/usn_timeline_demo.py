#!/usr/bin/env python3
"""Offline illustrative USN-like records; NOT an NTFS journal parser."""
from collections import defaultdict

# USNs here are illustrative positions, not real journal offsets.
EVENTS = [
    {"usn": 1000, "file_ref": 101, "name": "model.bin",
     "reason": "FILE_CREATE", "timestamp": "2026-01-01T12:00:00Z"},
    {"usn": 1040, "file_ref": 101, "name": "model.bin",
     "reason": "DATA_EXTEND", "timestamp": "2026-01-01T12:00:02Z"},
    {"usn": 1096, "file_ref": 101, "name": "model.bin",
     "reason": "CLOSE", "timestamp": "2026-01-01T12:00:03Z"},
    {"usn": 1120, "file_ref": 202, "name": "model.bin",
     "reason": "FILE_CREATE", "timestamp": "2026-01-01T12:00:05Z"},
]


def build_timeline(events: list[dict]) -> dict[int, list[dict]]:
    grouped = defaultdict(list)
    for event in events:
        if not isinstance(event["usn"], int) or event["usn"] < 0:
            raise ValueError("invalid synthetic USN")
        grouped[event["file_ref"]].append(dict(event))
    return {file_ref: sorted(records, key=lambda item: item["usn"])
            for file_ref, records in grouped.items()}


def main():
    timeline = build_timeline(EVENTS)
    assert len(timeline) == 2
    assert [e["reason"] for e in timeline[101]] == [
        "FILE_CREATE", "DATA_EXTEND", "CLOSE"
    ]
    assert timeline[101][0]["name"] == timeline[202][0]["name"]
    for file_ref, entries in sorted(timeline.items()):
        print(f"File reference: {file_ref} (initiator: UNKNOWN)")
        for event in entries:
            print(f"  USN={event['usn']:4}  {event['reason']:11} "
                  f"{event['name']}  reported_time={event['timestamp']}")
    print("No human/process/agent attribution can be drawn from these records.")
    print("USN gaps are not in themselves proof of missing or altered evidence.")


if __name__ == "__main__":
    main()
