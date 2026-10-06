#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime

events = []

for path in Path("evidence").glob("*.log"):
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        timestamp, rest = line.split(" ", 1)
        events.append((datetime.fromisoformat(timestamp), path.name, rest))

for dt, source, event in sorted(events):
    print(f"{dt.isoformat()} | {source:10} | {event}")
