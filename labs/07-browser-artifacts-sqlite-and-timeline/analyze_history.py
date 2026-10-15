"""Analyze only the local synthetic SQLite dataset, without modifications."""
import sqlite3
from pathlib import Path
p=Path(__file__).with_name("training_history.sqlite")
with sqlite3.connect(f"file:{p}?mode=ro", uri=True) as db:
    q = """SELECT visited_at AS event_time, 'VISIT' AS kind, url AS detail FROM visits
           UNION ALL
           SELECT downloaded_at AS event_time, 'DOWNLOAD' AS kind, filename AS detail FROM downloads
           ORDER BY event_time"""
    for row in db.execute(q):
        print(" | ".join(row))
