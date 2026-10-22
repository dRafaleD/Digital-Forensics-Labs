from datetime import datetime,timezone
records=[("2026-10-22T10:00:00+03:00","system","login"),("2026-10-22T07:00:03+00:00","application","session opened")]
for timestamp,source,event in sorted(records,key=lambda r:datetime.fromisoformat(r[0])):
    print(datetime.fromisoformat(timestamp).astimezone(timezone.utc).isoformat(),source,event)
print("Temporal proximity does not establish causality.")
