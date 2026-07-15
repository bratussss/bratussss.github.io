import os

EN_PRODUCTS = r"d:\VS KODI\ROzo github\en\products"

LANG_CSS = """
/* ── LANGUAGE SWITCHER ── */
.lang-switch {
  position: relative; display: inline-flex; align-items: center;
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-size: 0.68rem; letter-spacing: 0.08em;
  text-transform: uppercase; color: var(--ink2); font-weight: 500;
  cursor: pointer; user-select: none;
  padding: 6px 10px; border: 1px solid var(--border2);
  transition: border-color 0.2s, color 0.2s;
  gap: 6px; white-space: nowrap;
}
.lang-switch:hover { border-color: var(--ink); color: var(--ink); }
.lang-switch.active-lang { background: var(--accent); color: #fff; border-color: var(--accent); font-weight: 600; pointer-events: none; }
.lang-switch:not(.active-lang):hover { background: var(--bg2); }
@media (max-width: 860px) {
  .lang-switch { font-size: 0.62rem; padding: 5px 8px; }
}"""

PATTERNS = [
    '.nav-logo-lv em { font-style: normal; color: var(--accent); }',
    '.nav-logo-lv em{font-style:normal;color:var(--accent)}',
]

count = 0
for root, dirs, files in os.walk(EN_PRODUCTS):
    for f in files:
        if f == 'index.html':
            src = os.path.join(root, f)
            with open(src, 'r', encoding='utf-8') as fh:
                content = fh.read()
            if '.lang-switch' in content:
                continue
            for pat in PATTERNS:
                if pat in content:
                    content = content.replace(pat, pat + LANG_CSS)
                    with open(src, 'w', encoding='utf-8') as fh:
                        fh.write(content)
                    count += 1
                    break

print(f"Added lang-switch CSS to {count} EN product pages")
