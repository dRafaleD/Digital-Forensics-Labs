"""Build a synthetic SQLite history dataset; never touches real profiles."""
import sqlite3
from pathlib import Path
p=Path(__file__).with_name("training_history.sqlite")
if p.exists():p.unlink()
with sqlite3.connect(p) as db:
 db.execute("CREATE TABLE visits(url TEXT,visited_at TEXT)")
 db.execute("CREATE TABLE downloads(filename TEXT,source_url TEXT,downloaded_at TEXT)")
 db.executemany("INSERT INTO visits VALUES (?,?)",[
 ("https://example.org/guide","2026-10-15T09:10:00+03:00"),
 ("https://example.org/files","2026-10-15T09:14:00+03:00")])
 db.execute("INSERT INTO downloads VALUES (?,?,?)",("training.txt","https://example.org/files","2026-10-15T09:15:00+03:00"))
print("Generated synthetic training_history.sqlite.")
