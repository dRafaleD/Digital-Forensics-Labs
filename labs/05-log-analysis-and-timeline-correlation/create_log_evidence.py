#!/usr/bin/env python3
from pathlib import Path

base = Path("evidence")
base.mkdir(exist_ok=True)

(base / "auth.log").write_text("""2026-10-06T08:15:12+03:00 LOGIN user=eren source=127.0.0.1 status=success
2026-10-06T08:18:41+03:00 LOGIN user=eren source=127.0.0.1 status=failure
2026-10-06T08:19:03+03:00 LOGIN user=eren source=127.0.0.1 status=success
""", encoding="utf-8")

(base / "web.log").write_text("""2026-10-06T08:20:10+03:00 GET /report status=200 user=eren request_id=req-17
2026-10-06T08:21:32+03:00 GET /download?id=17 status=200 user=eren request_id=req-18
2026-10-06T08:23:55+03:00 POST /logout status=204 user=eren request_id=req-19
""", encoding="utf-8")

(base / "system.log").write_text("""2026-10-06T08:14:50+03:00 service=demo state=started
2026-10-06T08:22:04+03:00 file=report17.txt action=created request_id=req-18
2026-10-06T08:24:01+03:00 service=demo state=stopped
""", encoding="utf-8")

print("Created harmless timeline training evidence in ./evidence/")
