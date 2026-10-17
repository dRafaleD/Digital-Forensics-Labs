from datetime import datetime,timezone
from hashlib import sha256
logs=[
  {"time":"2026-10-17T09:00:00+03:00","source":"web","id":"r-42","event":"login"},
  {"time":"2026-10-17T06:00:02+00:00","source":"auth","id":"r-42","event":"accepted"},
  {"time":"2026-10-17T06:03:00+00:00","source":"audit","id":"r-43","event":"file read"},
]
for e in sorted(logs,key=lambda x:datetime.fromisoformat(x["time"])):
    utc=datetime.fromisoformat(e["time"]).astimezone(timezone.utc).isoformat()
    print(utc,e["id"],e["source"],e["event"])
print("Sample SHA256",sha256(repr(logs).encode()).hexdigest())
print("Shared ID suggests correlation, not proof of identity or causation.")
