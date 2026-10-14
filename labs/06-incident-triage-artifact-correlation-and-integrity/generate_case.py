#!/usr/bin/env python3
"""Generate entirely synthetic DFIR artifact snapshots; no live collection."""
from pathlib import Path
from hashlib import sha256
import json

BASE=Path(__file__).resolve().parent
EVIDENCE=BASE/"evidence"
EVIDENCE.mkdir(exist_ok=True)

sources={
"processes.jsonl":[
 {"timestamp":"2026-10-14T10:00:05+03:00","source":"process","event":"start","pid":4102,"ppid":1,"name":"python3","account":"training"},
 {"timestamp":"2026-10-14T10:00:11+03:00","source":"process","event":"start","pid":4103,"ppid":4102,"name":"curl","account":"training"},
 {"timestamp":"2026-10-14T10:00:18+03:00","source":"process","event":"exit","pid":4103,"exit_code":0},
],
"connections.jsonl":[
 {"timestamp":"2026-10-14T10:00:12+03:00","source":"network","event":"connect","pid":4103,"dst_ip":"192.0.2.55","dst_port":443,"protocol":"TCP"},
 {"timestamp":"2026-10-14T10:00:17+03:00","source":"network","event":"close","pid":4103,"dst_ip":"192.0.2.55","dst_port":443,"protocol":"TCP"},
],
"files.jsonl":[
 {"timestamp":"2026-10-14T10:00:13+03:00","source":"file","event":"created","pid":4103,"path":"synthetic_report.txt"},
 {"timestamp":"2026-10-14T10:00:14+03:00","source":"file","event":"read","pid":4102,"path":"synthetic_report.txt"},
],
}
for name,events in sources.items():
    p=EVIDENCE/name
    p.write_text("".join(json.dumps(e,sort_keys=True)+"\n" for e in events),encoding="utf-8")

manifest={name:sha256((EVIDENCE/name).read_bytes()).hexdigest()
          for name in sources}
(BASE/"manifest.sha256.json").write_text(
    json.dumps(manifest,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print("Generated synthetic artifacts and SHA-256 manifest.")
