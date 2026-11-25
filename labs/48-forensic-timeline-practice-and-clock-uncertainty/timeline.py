"""Fictional evidence timeline: distinguish order from temporal overlap."""
from dataclasses import dataclass
from datetime import datetime, timezone

@dataclass(frozen=True)
class Event:
    label: str
    timestamp: str
    uncertainty: int = 0

def interval(event):
    dt = datetime.fromisoformat(event.timestamp)
    if dt.tzinfo is None or event.uncertainty < 0:
        raise ValueError("timezone and nonnegative uncertainty required")
    t = dt.astimezone(timezone.utc).timestamp()
    return t-event.uncertainty, t+event.uncertainty

def compare(a,b):
    try:
        lo1,hi1 = interval(a)
        lo2,hi2 = interval(b)
    except ValueError:
        return "INVALID_TIME"
    if hi1 < lo2:
        return "BEFORE"
    if hi2 < lo1:
        return "AFTER"
    return "ORDER_UNCERTAIN"

def main():
    a = Event("download","2026-01-01T10:00:00+00:00",2)
    def e(t,u=0):
        return Event("other",t,u)
    cases = [
        (e("2026-01-01T10:00:10+00:00"),"BEFORE"),
        (e("2026-01-01T09:59:50+00:00"),"AFTER"),
        (e("2026-01-01T10:00:01+00:00"),"ORDER_UNCERTAIN"),
        (e("2026-01-01T13:00:00+03:00"),"ORDER_UNCERTAIN"),
        (e("2026-01-01T10:00:04+00:00",2),"ORDER_UNCERTAIN"),
        (e("2026-01-01T10:00:05+00:00",2),"BEFORE"),
        (e("2026-01-01T09:59:56+00:00",2),"ORDER_UNCERTAIN"),
        (e("2026-01-01T09:59:55+00:00",2),"AFTER"),
        (e("2026-01-01T10:00:00"),"INVALID_TIME"),
        (e("bad"),"INVALID_TIME"),
        (e("2026-01-01T10:00:00+00:00",-1),"INVALID_TIME"),
        (e("2026-01-01T05:00:30-05:00"),"BEFORE"),
    ]
    for other, expected in cases:
        got=compare(a,other)
        assert got==expected,(other,got)
        print(f"{other.timestamp:32} +/-{other.uncertainty:2} {got}")
    print(f"{len(cases)}/{len(cases)} timeline cases passed")

if __name__=="__main__":
    main()
