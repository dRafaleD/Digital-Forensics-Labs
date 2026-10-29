"""Correlate bursts of failed logons followed by a success in synthetic events."""
from datetime import datetime, timedelta

EVENTS = [
    ("2026-01-10T10:00:00", "alice", "10.0.0.7", "fail"),
    ("2026-01-10T10:00:05", "alice", "10.0.0.7", "fail"),
    ("2026-01-10T10:00:09", "alice", "10.0.0.7", "fail"),
    ("2026-01-10T10:00:14", "alice", "10.0.0.7", "success"),
    ("2026-01-10T11:30:00", "bob", "10.0.0.8", "fail"),
    ("2026-01-10T11:30:40", "bob", "10.0.0.8", "success"),
]

def correlate(events, threshold=3, window=timedelta(minutes=2)):
    hits, recent = [], {}
    for stamp, user, source, result in events:
        when = datetime.fromisoformat(stamp)
        key = (user, source)
        recent[key] = [t for t in recent.get(key, []) if when - t <= window]
        if result == "fail":
            recent[key].append(when)
        elif len(recent[key]) >= threshold:
            hits.append((user, source, len(recent[key]), stamp))
    return hits

if __name__ == "__main__":
    for user, source, count, stamp in correlate(EVENTS):
        print(f"review: {count} failures then success for {user} from {source} at {stamp}")
    assert len(correlate(EVENTS)) == 1
    print("Note: a forgotten password looks the same; confirm with the source host, user contact and later activity.")
