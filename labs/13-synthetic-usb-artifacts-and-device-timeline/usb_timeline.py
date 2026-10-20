from datetime import datetime,timezone
events=[
("2026-10-20T08:00:00+03:00","usb-device","attached"),
("2026-10-20T05:01:00+00:00","filesystem","synthetic-file-created"),
("2026-10-20T05:05:00+00:00","usb-device","removed")]
for ts,source,event in sorted(events,key=lambda x:datetime.fromisoformat(x[0])):
    print(datetime.fromisoformat(ts).astimezone(timezone.utc).isoformat(),source,event)
