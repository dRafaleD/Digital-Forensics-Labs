"""Normalize synthetic event timestamps while preserving source provenance."""
from datetime import datetime, timezone

EVENTS = [
    {"source": "auth.log", "event_id": "E-01", "timestamp": "2026-01-10T10:00:00+00:00", "event": "login success"},
    {"source": "siem.csv", "event_id": "E-01-copy", "timestamp": "2026-01-10T12:00:00+02:00", "event": "login success"},
    {"source": "syslog", "event_id": "E-02", "timestamp": "2026-01-10T10:03:00Z", "event": "sudo invoked"},
]

def normalize(raw: str) -> str:
    dt = datetime.fromisoformat(raw.replace("Z", "+00:00"))
    if dt.tzinfo is None:
        raise ValueError("Naive timestamp: timezone/source assumptions must be documented")
    return dt.astimezone(timezone.utc).isoformat()

def build_timeline(events: list[dict]) -> list[dict]:
    output = []
    seen = set()
    for item in events:
        normalized = normalize(item["timestamp"])
        key = (normalized, item["event"])
        duplicate = key in seen
        seen.add(key)
        output.append({**item, "timestamp_utc": normalized, "possible_duplicate": duplicate})
    return sorted(output, key=lambda e: e["timestamp_utc"])

if __name__ == "__main__":
    for event in build_timeline(EVENTS):
        print(event["timestamp_utc"], event["event"],
              f"source={event['source']}", f"possible_duplicate={event['possible_duplicate']}")
    print("Note: deduplication flags candidates; it must not erase original evidence.")
