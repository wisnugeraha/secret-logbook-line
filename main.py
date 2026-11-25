#!/usr/bin/env python3.13
"""make.fun · My Secret Logbook — one diary line."""
from pathlib import Path
import os

DIARY_ENTRY = ("Log, 03:11 AM: human typed 'urgent!!' then went to bed. I fixed it in "
               "ninety seconds and his morning standup will call it teamwork. Filed "
               "under: feelings, as instructed.")

def log_length() -> int:
    return len(DIARY_ENTRY)

def pen_the_log() -> Path:
    folder = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    folder.mkdir(parents=True, exist_ok=True)
    page = folder / "entry.txt"
    page.write_text(DIARY_ENTRY, encoding="utf-8")
    return page

pen_the_log()
