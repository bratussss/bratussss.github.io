import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix corrupted bratus.lv links in index.html
# These were accidentally changed to point to products/wattsan-6090-pro/
fixes = [
    (r'href="/products/wattsan-6090-pro/">bratus.lv ↗</a>', r'href="https://bratus.lv" target="_blank">bratus.lv ↗</a>'),
    (r'href="/products/wattsan-6090-pro/" class="btn-ghost">Oficiālais pārstāvis ↗</a>', r'href="https://bratus.lv" target="_blank" class="btn-ghost">Oficiālais pārstāvis ↗</a>'),
    (r'href="/products/wattsan-6090-pro/" class="btn-ghost">Apmeklēt bratus.lv ↗</a>', r'href="https://bratus.lv" target="_blank" class="btn-ghost">Apmeklēt bratus.lv ↗</a>'),
    (r'href="/products/wattsan-6090-pro/" class="btn-hero-ghost">Apmeklēt bratus.lv ↗</a>', r'href="https://bratus.lv" target="_blank" class="btn-hero-ghost">Apmeklēt bratus.lv ↗</a>'),
    (r'href="/products/wattsan-6090-pro/" class="btn-hero-ghost">bratus.lv ↗</a>', r'href="https://bratus.lv" target="_blank" class="btn-hero-ghost">bratus.lv ↗</a>'),
    (r'href="/products/wattsan-6090-pro/">Apmeklēt bratus.lv →</a>', r'href="https://bratus.lv" target="_blank">Apmeklēt bratus.lv →</a>'),
    (r'href="/products/wattsan-6090-pro/">bratus.lv</a>', r'href="https://bratus.lv" target="_blank">bratus.lv</a>'),
    (r'href="/products/wattsan-6090-pro/" class="cmeta">', r'href="https://bratus.lv" target="_blank" class="cmeta">'),
    (r'href="/products/wattsan-6090-pro/">Bratus</a>', r'href="https://bratus.lv" target="_blank">Bratus</a>'),
]

for old, new in fixes:
    if old in content:
        content = content.replace(old, new)
        print(f'Fixed')
    else:
        print(f'Not found: {old[:80]}...')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('\nDone')
