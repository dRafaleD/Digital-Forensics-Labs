#!/usr/bin/env python3
"""Verify original bytes, normalize times and correlate synthetic PID events."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json
import sys

BASE=Path(__file__).resolve().parent
EXPECTED={"processes.jsonl","connections.jsonl","files.jsonl"}
manifest=json.loads((BASE/"manifest.sha256.json").read_text(encoding="utf-8"))
if set(manifest)!=EXPECTED:
    sys.exit("Manifest has unexpected or missing evidence filenames.")

timeline=[]
for name in sorted(EXPECTED):
    path=BASE/"evidence"/name
    data=path.read_bytes()
    actual=sha256(data).hexdigest()
    if actual!=manifest[name]:
        sys.exit(f"INTEGRITY FAILED: {name}; do not analyze altered evidence.")
    print(f"OK SHA-256 {name}: {actual}")
    for line_no,line in enumerate(data.decode("utf-8").splitlines(),1):
        event=json.loads(line)
        timestamp=datetime.fromisoformat(event["timestamp"])
        if timestamp.utcoffset() is None:
            sys.exit(f"Missing timezone in {name}:{line_no}")
        timeline.append((timestamp.astimezone(timezone.utc),name,event))

known_processes={}
for _,_,e in timeline:
    if e["source"]=="process" and e["event"]=="start":
        known_processes[e["pid"]]=e["name"]

print("\nTimeline (normalized UTC):")
for timestamp,source,e in sorted(timeline,key=lambda row:row[0]):
    pid=e.get("pid")
    observed_name=known_processes.get(pid,"unknown process")
    detail={k:v for k,v in e.items() if k!="timestamp"}
    print(timestamp.isoformat(),source,f"pid={pid} process={observed_name}",detail)
print("\nInterpretation limit: matching PID and time support correlation, NOT causation or human attribution.")
