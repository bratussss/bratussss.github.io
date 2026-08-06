import os, re
lv = set('āēīūšģķļžčņ')
words = {}
for r, d, fs in os.walk(r'en\products'):
    for f in fs:
        if f == 'index.html':
            c = open(os.path.join(r, f), 'r', encoding='utf-8').read()
            for t in re.findall(r'>([^<]{3,60})<', c):
                t = t.strip()
                if any(ch in t for ch in lv):
                    if 'Dārznieku' in t or 'Ķekava' in t or 'iekārtas' in t or 'rezerves' in t:
                        continue
                    words[t] = words.get(t, 0) + 1
for w, c in sorted(words.items(), key=lambda x: -x[1])[:100]:
    print(f'[{c}x] {w[:120]}')
