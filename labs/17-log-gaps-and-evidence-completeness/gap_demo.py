"""Flag unusually large gaps between synthetic log entries."""
from datetime import datetime, timedelta

LOG = [
    "2026-01-10T10:00:00",
    "2026-01-10T10:01:00",
    "2026-01-10T10:02:00",
    "2026-01-10T10:45:00",
    "2026-01-10T10:46:00",
]

def find_gaps(stamps, threshold=timedelta(minutes=5)):
    times = [datetime.fromisoformat(s) for s in stamps]
    return [(a, b, b - a) for a, b in zip(times, times[1:]) if b - a > threshold]

if __name__ == "__main__":
    gaps = find_gaps(LOG)
    for start, end, size in gaps:
        print(f"gap candidate: {start} -> {end} ({size})")
    assert len(gaps) == 1
    print("Note: a gap is a question to investigate, not proof of deletion; it may be idle time, rotation or collection loss.")
