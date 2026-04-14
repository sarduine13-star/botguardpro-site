# -*- coding: utf-8 -*-
from pathlib import Path

p = Path(r".\src\App.jsx")
content = p.read_text(encoding="utf-8")

target = """      <Pricing />"""
replacement = """      <FoundersBeta />
      <Pricing />"""

if "<FoundersBeta />" in content:
    print("TAG ALREADY INSERTED")
else:
    if target not in content:
        raise SystemExit("Could not find <Pricing />. No changes made.")
    content = content.replace(target, replacement, 1)
    p.write_text(content, encoding="utf-8")
    print("TAG INSERTED:", p)
