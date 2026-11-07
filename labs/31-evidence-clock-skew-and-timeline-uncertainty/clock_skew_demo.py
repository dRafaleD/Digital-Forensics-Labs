"""Offline synthetic forensic clock-skew timeline with uncertainty windows."""
from datetime import datetime, timedelta, timezone

events = [
 {"id":"host-a-log","raw":"2026-01-01T12:00:02+00:00","offset_seconds":2,"uncertainty":3},
 {"id":"host-b-log","raw":"2026-01-01T12:00:01+00:00","offset_seconds":-1,"uncertainty":3},
]
def interval(e):
    raw=datetime.fromisoformat(e["raw"])
    corrected=raw-timedelta(seconds=e["offset_seconds"])
    delta=timedelta(seconds=e["uncertainty"])
    return corrected-delta,corrected+delta

a,b=map(interval,events)
assert a[0] <= b[1] and b[0] <= a[1]
for event in events:
    print(event["id"], "original", event["raw"], "possible range",interval(event))
print("Intervals overlap: relative event order is inconclusive.")
