# -*- coding: utf-8 -*-
from pathlib import Path
import re

p = Path(r".\src\App.jsx")
content = p.read_text(encoding="utf-8")

# make sure the target exists
if 'id="free-audit"' not in content:
    content = content.replace(
        "How Much Are You Losing?",
        '<span id="free-audit"></span>How Much Are You Losing?',
        1
    )

# replace Claim Free Beta anchor with real scroll button
content = re.sub(
    r'<a\s+href="#free-audit"\s+style=\{\{(.*?)\}\}\s*>\s*Claim Free Beta\s*</a>',
    r'''<button
            onClick={() => document.getElementById("free-audit")?.scrollIntoView({ behavior: "smooth", block: "start" })}
            style={{\1, border: "none", cursor: "pointer" }}
          >
            Claim Free Beta
          </button>''',
    content,
    count=1,
    flags=re.S
)

# replace Run Free Audit anchor with real scroll button
content = re.sub(
    r'<a\s+href="#free-audit"\s+style=\{\{(.*?)\}\}\s*>\s*Run Free Audit\s*</a>',
    r'''<button
            onClick={() => document.getElementById("free-audit")?.scrollIntoView({ behavior: "smooth", block: "start" })}
            style={{\1, cursor: "pointer" }}
          >
            Run Free Audit
          </button>''',
    content,
    count=1,
    flags=re.S
)

p.write_text(content, encoding="utf-8")
print("BUTTONS FIXED:", p)
