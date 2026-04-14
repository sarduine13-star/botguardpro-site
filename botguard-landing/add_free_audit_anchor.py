# -*- coding: utf-8 -*-
from pathlib import Path

p = Path(r".\src\App.jsx")
content = p.read_text(encoding="utf-8")

# Add ID to the calculator section
if 'id="free-audit"' not in content:
    content = content.replace(
        "How Much Are You Losing?",
        '<span id="free-audit"></span>How Much Are You Losing?'
    )

p.write_text(content, encoding="utf-8")
print("Free audit anchor added.")
