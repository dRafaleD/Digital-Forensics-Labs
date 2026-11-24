"""Synthetic forensic coverage metadata; no real logs or host access."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Interval:
    start: int
    end: int

def covers(intervals: list[Interval], start: int, end: int) -> bool:
    if end < start:
        return False
    cursor = start
    for item in sorted(intervals, key=lambda item: item.start):
        if item.end <= item.start or item.end <= cursor:
            continue
        if item.start > cursor:
            break
        cursor = max(cursor, item.end)
        if cursor >= end:
            return True
    return start == end

def assess(intervals, start, end, observations):
    if end <= start:
        return "INVALID_WINDOW"
    if not covers(intervals, start, end):
        return "PARTIAL_COVERAGE"
    if not observations:
        return "NO_POSITIVE_EVIDENCE"
    if len(set(observations)) > 1:
        return "CONFLICT"
    return "CONSISTENT_CONTEXT"

def main():
    full = [Interval(0, 20), Interval(20, 40)]
    gap = [Interval(0, 19), Interval(20, 40)]
    cases = [
        (full, 10, 30, [], "NO_POSITIVE_EVIDENCE"),
        (gap, 10, 30, [], "PARTIAL_COVERAGE"),
        (full, 10, 30, ["parent-a"], "CONSISTENT_CONTEXT"),
        (full, 10, 30, ["parent-a", "parent-b"], "CONFLICT"),
        ([Interval(0, 50)], 10, 30, ["parent-a"], "CONSISTENT_CONTEXT"),
        ([Interval(20, 50)], 10, 30, [], "PARTIAL_COVERAGE"),
        ([], 10, 30, [], "PARTIAL_COVERAGE"),
        (full, 30, 10, [], "INVALID_WINDOW"),
        ([Interval(0, 25), Interval(10, 40)], 10, 30, [], "NO_POSITIVE_EVIDENCE"),
    ]
    for intervals, start, end, observations, expected in cases:
        actual = assess(intervals, start, end, observations)
        assert actual == expected, (actual, expected)
        print(actual)
    print(f"{len(cases)}/{len(cases)} interval checks passed")

if __name__ == "__main__":
    main()
