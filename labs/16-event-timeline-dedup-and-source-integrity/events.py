from datetime import datetime,timezone
records=[("a","2026-10-23T09:00:00+03:00","login"),("a","2026-10-23T06:00:00+00:00","login"),("b","2026-10-23T06:00:00+00:00","login")]
seen=set()
for source,ts,event in records:
    utc=datetime.fromisoformat(ts).astimezone(timezone.utc)
    key=(source,utc,event)
    print("duplicate" if key in seen else "evidence",source,utc.isoformat(),event)
    seen.add(key)
