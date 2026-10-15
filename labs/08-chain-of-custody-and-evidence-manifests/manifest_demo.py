import hashlib,json
from pathlib import Path
base=Path(__file__).parent/"synthetic_evidence"
base.mkdir(exist_ok=True)
for name,data in {"note.txt":"Synthetic note\n","events.log":"2026-10-16T08:00:00+03:00 training event\n"}.items():(base/name).write_text(data,encoding="utf-8")
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
data={p.name:{"sha256":sha(p),"bytes":p.stat().st_size} for p in sorted(base.iterdir()) if p.is_file()}
(Path(__file__).parent/"manifest.json").write_text(json.dumps(data,indent=2)+"\n",encoding="utf-8")
assert all(sha(base/n)==info["sha256"] for n,info in data.items())
print("PASS",len(data),"synthetic evidence files")