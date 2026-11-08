"""Synthetic multi-source provenance check; no system log or evidence access."""
from collections import defaultdict
from copy import deepcopy

records = [
    {
        "evidence_id": "file-101",
        "source": "synthetic-file-log",
        "artifact_id": "artifact-01",
        "timestamp_utc": "2026-04-01T10:00:00Z",
        "reported_actor": "automation",
    },
    {
        "evidence_id": "app-302",
        "source": "synthetic-app-audit",
        "artifact_id": "artifact-01",
        "timestamp_utc": "2026-04-01T10:00:02Z",
        "reported_actor": "user",
    },
    {
        "evidence_id": "storage-9",
        "source": "synthetic-storage",
        "artifact_id": "artifact-01",
        "timestamp_utc": "2026-04-01T10:00:01Z",
        "reported_actor": None,
    },
]
original = deepcopy(records)

def evaluate(items):
    grouped = defaultdict(list)
    for entry in items:
        grouped[entry["artifact_id"]].append(entry)
    reports = []
    for artifact_id, evidence in sorted(grouped.items()):
        asserted = sorted({x["reported_actor"] for x in evidence
                           if x["reported_actor"] not in (None, "unknown")})
        reports.append({
            "artifact_id": artifact_id,
            "evidence_ids": [x["evidence_id"] for x in evidence],
            "reported_actors": asserted,
            "actor_attribution": "inconclusive" if len(asserted) != 1
                                 else "single-label-unverified",
            "source_disagreement": len(asserted) > 1,
        })
    return reports

report = evaluate(records)[0]
assert records == original  # Do not overwrite original evidence
assert len(report["evidence_ids"]) == 3
assert report["reported_actors"] == ["automation", "user"]
assert report["source_disagreement"] is True
assert report["actor_attribution"] == "inconclusive"
print(report)
print("No ground-truth actor was inferred from contradictory records.")
