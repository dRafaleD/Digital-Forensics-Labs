#!/usr/bin/env python3
"""Synthetic browser/Zone.Identifier correlation with uncertain attribution."""
from datetime import datetime

WINDOW_SECONDS = 2
DOWNLOADS = [
    {"id": "browser-01", "path": "C:/Lab/model-a.bin",
     "time": "2026-11-01T12:00:00+00:00", "url": "https://example.invalid/a"},
    {"id": "browser-02", "path": "C:/Lab/model-b.bin",
     "time": "2026-11-01T12:00:04+00:00", "url": "https://example.invalid/b"},
    {"id": "browser-03", "path": "C:/Lab/model-b.bin",
     "time": "2026-11-01T12:00:06+00:00", "url": "https://example.invalid/b2"},
]
ZONE_OBSERVATIONS = [
    {"id": "zone-01", "path": "C:/Lab/model-a.bin",
     "time": "2026-11-01T12:00:01+00:00", "zone_id": 3},
    {"id": "zone-02", "path": "C:/Lab/model-b.bin",
     "time": "2026-11-01T12:00:05+00:00", "zone_id": 3},
    {"id": "zone-03", "path": "C:/Lab/orphan.bin",
     "time": "2026-11-01T12:00:01+00:00", "zone_id": 3},
]


def candidates(observation, downloads):
    observed_time = datetime.fromisoformat(observation["time"])
    matches = []
    for event in downloads:
        if event["path"] != observation["path"]:
            continue
        elapsed = abs((datetime.fromisoformat(event["time"]) -
                       observed_time).total_seconds())
        if elapsed <= WINDOW_SECONDS:
            matches.append(event["id"])
    return sorted(matches)


def main():
    expected = {"zone-01": 1, "zone-02": 2, "zone-03": 0}
    for observation in ZONE_OBSERVATIONS:
        ids = candidates(observation, DOWNLOADS)
        status = ("none" if not ids else
                  "possible" if len(ids) == 1 else "ambiguous")
        print(f"{observation['id']}: {status}, candidate_ids={ids}; "
              "initiator=UNKNOWN")
        assert len(ids) == expected[observation["id"]]
    print("No download causation, execution or actor identity was established.")


if __name__ == "__main__":
    main()
