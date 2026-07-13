import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# CO2 product links
co2_links = {
    "wattsan-1820-conveyor-pro": "wattsan.com/product/wattsan-1820-conveyor-pro/",
    "wattsan-6090-pro": "bratus.lv",
    "wattsan-1290-pro": "wattsan.com/product/wattsan-1290-pro/",
    "wattsan-1610-pro": "bratus.lv",
    "wattsan-1630-flat-bed-pro": "wattsan.com/product/wattsan-flat-bed-1630-pro/",
    "wattsan-2030-flat-bed-pro": "wattsan.com/product/wattsan-flat-bed-2030-pro/",
    "wattsan-0503-hobby-t": "wattsan.com/product/wattsan-0503-hobby-t/",
    "wattsan-6090-st": "wattsan.com/product/wattsan-6090-st-2/",
    "wattsan-1290-duos-st": "wattsan.com/product/wattsan-1290-duos-st-2/",
    "wattsan-1290-st": "wattsan.com/product/wattsan-1290-st-2/",
    "wattsan-6090-lt": "wattsan.com/product/wattsan-6090-lt-2/",
    "wattsan-1290-duos-lt": "wattsan.com/product/wattsan-1290-duos-lt-2/",
    "wattsan-1290-lt": "wattsan.com/product/wattsan-1290-lt-2/",
    "wattsan-1610-duos-lt": "wattsan.com/product/wattsan-1610-duos-lt-2/",
    "wattsan-1610-lt": "wattsan.com/product/wattsan-1610-lt-2/",
    "wattsan-1610-duos-st": "wattsan.com/product/wattsan-1610-duos-st-2/",
    "wattsan-1610-st": "wattsan.com/product/wattsan-1610-st-2/",
}

metal_links = {
    "wattsan-1313-a-cabin": "bratus.lv",
    "wattsan-3214-l": "wattsan.com/product/wattsan-3214-l/",
    "wattsan-3214-lc": "wattsan.com/product/wattsan-3214-lc/",
    "wattsan-2060-hard-ultra": "wattsan.com/product/wattsan-2060-hard-ultra/",
    "wattsan-1530-hard": "wattsan.com/product/wattsan-1530-hard/",
    "wattsan-2040-hard": "wattsan.com/product/wattsan-2040-hard/",
    "wattsan-2060-hard": "wattsan.com/product/wattsan-2060-hard/",
    "wattsan-1309-mini": "wattsan.com/product/wattsan-1309-mini/",
    "wattsan-1313-a": "wattsan.com/product/wattsan-1313-a/",
    "wattsan-1530-a": "wattsan.com/product/wattsan-1530-a/",
    "wattsan-1313-s": "wattsan.com/product/wattsan-1313-s/",
    "wattsan-1325-s": "wattsan.com/product/wattsan-1325-s/",
    "wattsan-1530-s": "wattsan.com/product/wattsan-1530-s/",
    "wattsan-1313-e": "wattsan.com/product/wattsan-1313-e/",
    "wattsan-1325-e": "wattsan.com/product/wattsan-1325-e/",
    "wattsan-1530-e": "wattsan.com/product/wattsan-1530-e/",
}

marker_links = {
    "wattsan-fm": "bratus.lv",
    "wattsan-fl-gt": "wattsan.com/product/wattsan-fl-gt/",
    "wattsan-fl-compact": "wattsan.com/product/wattsan-fl-compact/",
    "wattsan-fl-hh": "wattsan.com/product/wattsan-fl-hh/",
    "wattsan-uv-tt": "wattsan.com/product/wattsan-uv-tt/",
    "wattsan-fl-box": "wattsan.com/product/wattsan-fl-box/",
    "wattsan-3d": "wattsan.com/product/wattsan-3d/",
    "wattsan-fl-ht": "wattsan.com/product/wattsan-fl-ht-2/",
    "wattsan-fl-tt": "wattsan.com/product/wattsan-fl-tt/",
    "wattsan-co2-lt": "wattsan.com/product/wattsan-co2-lt/",
    "wattsan-fl-st": "wattsan.com/product/wattsan-fl-st/",
}

count = 0
for slug, old_url in {**co2_links, **metal_links, **marker_links}.items():
    old_href = f'href="https://{old_url}" target="_blank"'
    new_href = f'href="products/{slug}.html"'
    if old_href in content:
        content = content.replace(old_href, new_href)
        count += 1
        print(f"  ✓ {slug}")
    else:
        # Try without target
        old_href2 = f'href="https://{old_url}"'
        if old_href2 in content:
            content = content.replace(old_href2, new_href)
            count += 1
            print(f"  ✓ {slug} (no target)")
        else:
            print(f"  ✗ {slug}: {old_url} not found")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print(f"\n✅ Updated {count} links in index.html")
