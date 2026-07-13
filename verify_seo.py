import re, glob
no_alt = 0
total = 0
has_c = 0
has_s = 0
total_f = 0
for f in glob.glob('**/*.html', recursive=True):
    total_f += 1
    with open(f, 'r', encoding='utf-8') as fh:
        c = fh.read()
    if 'canonical' in c:
        has_c += 1
    if 'application/ld+json' in c:
        has_s += 1
    for img in re.findall(r'<img[^>]*>', c):
        total += 1
        if 'alt=' not in img:
            no_alt += 1
            print(f"MISSING ALT: {f}")
print(f"\nFiles:{total_f} | Canonical:{has_c}/{total_f} | Schema:{has_s}/{total_f} | Images:{total} | NoAlt:{no_alt}")
