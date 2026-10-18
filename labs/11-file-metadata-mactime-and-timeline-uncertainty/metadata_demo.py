from pathlib import Path
from datetime import datetime,timezone
import hashlib
p=Path('harmless_evidence.txt')
p.write_text('synthetic forensic training\n',encoding='utf8')
st=p.stat()
print('sha256',hashlib.sha256(p.read_bytes()).hexdigest())
print('mtime_utc',datetime.fromtimestamp(st.st_mtime,timezone.utc).isoformat())
print('ctime_utc',datetime.fromtimestamp(st.st_ctime,timezone.utc).isoformat())
print('ctime may represent metadata change, not creation, on Unix-like systems')
