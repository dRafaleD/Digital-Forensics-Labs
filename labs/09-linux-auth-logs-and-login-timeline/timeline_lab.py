import hashlib
from datetime import datetime
from pathlib import Path
events=['2026-10-08T09:00:00+03:00 Failed login from 192.0.2.4','2026-10-08T09:03:00+03:00 Accepted key from 192.0.2.4','2026-10-08T09:04:00+03:00 sudo session opened']
p=Path('synthetic_auth.log')
p.write_text('\n'.join(events)+'\n',encoding='utf-8')
print('SHA256:',hashlib.sha256(p.read_bytes()).hexdigest())
for e in sorted(events,key=lambda x:datetime.fromisoformat(x.split()[0])): print(e)
