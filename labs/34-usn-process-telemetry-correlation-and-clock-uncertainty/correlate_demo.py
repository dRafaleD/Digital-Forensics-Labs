#!/usr/bin/env python3
"""Offline USN/process-file correlation exercise; all records are fictional."""
from datetime import datetime
from hashlib import sha256
import json

WINDOW_SECONDS = 2.0

USN_LIKE = [
    {"id": "u-101", "file_ref": 101, "reason": "FILE_CREATE",
     "time": "2026-01-01T12:00:00+00:00", "usn": 1000},
    {"id": "u-202", "file_ref": 202, "reason": "DATA_EXTEND",
     "time": "2026-01-01T12:01:00+00:00", "usn": 1040},
    {"id": "u-303", "file_ref": 303, "reason": "CLOSE",
     "time": "2026-01-01T12:02:00+00:00", "usn": 1080},
]

# Synthetic process-file telemetry with a SHARED file_ref for teaching only.
# Do not assume real process-create logs supply a native NTFS file reference.
PROCESS_FILE_EVENTS = [
    {"id": "p-a", "file_ref": 101, "process": "training-browser",
     "time": "2026-01-01T12:00:00.500+00:00"},
    {"id": "p-b", "file_ref": 101, "process": "scheduled-demo",
     "time": "2026-01-01T12:00:01.000+00:00"},
    {"id": "p-c", "file_ref": 303, "process": "local-utility",
     "time": "2026-01-01T12:02:00.250+00:00"},
    {"id": "p-d", "file_ref": 999, "process": "unrelated",
     "time": "2026-01-01T12:00:00+00:00"},
]


def to_time(value: str) -> datetime:
    parsed = datetime.fromisoformat(value)
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise ValueError("timezone-aware timestamps required")
    return parsed


def correlate(record: dict, telemetry: list[dict]) -> dict:
    usn_time = to_time(record["time"])
    candidates = []
    for event in telemetry:
        if event["file_ref"] != record["file_ref"]:
            continue
        seconds = abs((to_time(event["time"]) - usn_time).total_seconds())
        if seconds <= WINDOW_SECONDS:
            candidates.append({"event_id": event["id"],
                               "reported_process": event["process"],
                               "delta_seconds": seconds})
    candidates.sort(key=lambda e: (e["delta_seconds"], e["event_id"]))
    status = ("no_candidate" if not candidates else
              "single_temporal_candidate" if len(candidates) == 1 else
              "ambiguous_multiple_candidates")
    return {"usn_event": record["id"], "status": status,
            "candidates": candidates, "actor_attribution": "unproven"}


def main():
    results = [correlate(record, PROCESS_FILE_EVENTS) for record in USN_LIKE]
    assert [r["status"] for r in results] == [
        "ambiguous_multiple_candidates", "no_candidate",
        "single_temporal_candidate"
    ]
    # Hashes here attest only to the serialized teaching fixture.
    digest = sha256(json.dumps(USN_LIKE, sort_keys=True).encode()).hexdigest()
    print("synthetic_fixture_sha256:", digest)
    for result in results:
        print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    print("Assertions passed. Temporal correlation is not causal proof.")


if __name__ == "__main__":
    main()
