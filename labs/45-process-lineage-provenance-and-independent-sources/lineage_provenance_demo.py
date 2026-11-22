#!/usr/bin/env python3
"""Fictional process-lineage provenance: forwarded logs are not independent witnesses."""
from dataclasses import dataclass

# Controlled by the examiner, not copied from a log payload.
ORIGIN_BY_COLLECTOR = {
    "agent-a": "host-sensor-a",
    "relay-a": "host-sensor-a",
    "agent-b": "host-sensor-b",
    "agent-c": "host-sensor-c",
}

@dataclass(frozen=True)
class Observation:
    collector: str
    child_guid: str
    parent_guid: str
    child_started: int
    parent_started: int

def classify(child: str, records: list[Observation]) -> str:
    evidence: dict[str, set[str]] = {}
    for item in records:
        if item.child_guid != child:
            continue
        origin = ORIGIN_BY_COLLECTOR.get(item.collector)
        if not origin or not item.parent_guid:
            continue
        if item.parent_started >= item.child_started:
            return "TIME_CONFLICT"
        evidence.setdefault(origin, set()).add(item.parent_guid)
    if not evidence:
        return "UNKNOWN"
    if any(len(parents) != 1 for parents in evidence.values()):
        return "SOURCE_CONFLICT"
    candidates = {next(iter(parents)) for parents in evidence.values()}
    if len(candidates) > 1:
        return "CROSS_SOURCE_CONFLICT"
    return "CORROBORATED_CONTEXT" if len(evidence) >= 2 else "SINGLE_ORIGIN"

def main():
    a = Observation("agent-a", "child", "parent-1", 50, 10)
    forwarded = Observation("relay-a", "child", "parent-1", 50, 10)
    b = Observation("agent-b", "child", "parent-1", 50, 10)
    contradicts = Observation("agent-b", "child", "parent-2", 50, 15)
    cases = [
        ("single producer", [a], "SINGLE_ORIGIN"),
        ("forwarding is not corroboration", [a, forwarded], "SINGLE_ORIGIN"),
        ("two independent sources", [a, b], "CORROBORATED_CONTEXT"),
        ("same origin conflicting parents", [a, Observation("relay-a","child","parent-2",50,15)], "SOURCE_CONFLICT"),
        ("two sources disagree", [a, contradicts], "CROSS_SOURCE_CONFLICT"),
        ("invalid time order", [Observation("agent-a","child","parent-1",30,40)], "TIME_CONFLICT"),
        ("unknown collector", [Observation("untrusted","child","parent-1",50,10)], "UNKNOWN"),
        ("different child ignored", [Observation("agent-a","other","parent-1",50,10)], "UNKNOWN"),
        ("three independent sources", [a,b,Observation("agent-c","child","parent-1",50,10)], "CORROBORATED_CONTEXT"),
    ]
    for name, observations, expected in cases:
        actual = classify("child", observations)
        assert actual == expected, (name, actual)
        print(f"{name:39} {actual}")
    print(f"{len(cases)}/{len(cases)} fictional provenance checks passed")

if __name__ == "__main__":
    main()
