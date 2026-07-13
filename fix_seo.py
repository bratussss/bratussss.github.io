#!/usr/bin/env python3
"""Add canonical URLs, JSON-LD schema, and fix alt texts across all HTML pages."""
import os, re, glob

BASE_URL = "https://bratussss.github.io"

def get_canonical(filepath):
    """Get canonical URL from file path."""
    rel = os.path.relpath(filepath, "d:\\VS KODI\\ROzo github").replace("\\", "/")
    if rel == "index.html":
        return f"{BASE_URL}/"
    # products/xxx/index.html -> /products/xxx/
    rel = rel.replace("/index.html", "/")
    return f"{BASE_URL}/{rel}"

def get_page_type(content, filepath):
    """Determine page type for schema."""
    if "products/" in filepath.replace("\\", "/"):
        name = os.path.basename(os.path.dirname(filepath))
        if name.startswith("reci-"):
            return "reci", name
        elif name.startswith("chiller-"):
            return "chiller", name
        else:
            return "machine", name
    return "home", None

def extract_meta(content):
    """Extract title and description from HTML."""
    title_m = re.search(r'<title>(.*?)</title>', content)
    desc_m = re.search(r'<meta name="description" content="(.*?)"', content)
    title = title_m.group(1) if title_m else "Wattsan Latvija"
    desc = desc_m.group(1) if desc_m else ""
    return title, desc

def extract_product_info(content, page_type):
    """Extract product info from page content."""
    info = {}
    # Try to get main product image
    img_m = re.search(r'<img[^>]*class="gallery-main"[^>]*src="([^"]+)"', content)
    if not img_m:
        img_m = re.search(r'<img[^>]*id="mainImg"[^>]*src="([^"]+)"', content)
    if img_m:
        info['main_img'] = img_m.group(1)
    
    # Get h1
    h1_m = re.search(r'<h1[^>]*>(.*?)</h1>', content, re.DOTALL)
    if h1_m:
        info['h1'] = re.sub(r'<[^>]+>', ' ', h1_m.group(1)).strip()
    
    # Get product specs
    specs = {}
    for m in re.finditer(r'<div class="key-spec">.*?<div class="key-spec-l">(.*?)</div>.*?<div class="key-spec-v">(.*?)</div>.*?</div>', content, re.DOTALL):
        specs[m.group(1).strip()] = m.group(2).strip()
    info['specs'] = specs
    
    return info

def build_jsonld(page_type, name, content, filepath, canonical):
    """Build JSON-LD structured data."""
    title, desc = extract_meta(content)
    info = extract_product_info(content, page_type)
    
    if page_type == "home":
        return f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Wattsan Latvija",
  "url": "{canonical}",
  "logo": "{BASE_URL}/wattsan-logo.svg",
  "description": "{desc}",
  "contactPoint": {{
    "@type": "ContactPoint",
    "telephone": "+371-24-424-434",
    "contactType": "sales",
    "availableLanguage": ["Latvian", "Russian", "English"]
  }},
  "sameAs": ["https://bratus.lv"]
}}
</script>"""
    
    elif page_type in ("machine", "reci", "chiller"):
        product_name = info.get('h1', name.replace("-", " ").title())
        main_img = info.get('main_img', '')
        if main_img and not main_img.startswith("http"):
            main_img = f"{BASE_URL}/{main_img}"
        
        specs = info.get('specs', {})
        manufacturer = "Wattsan" if page_type == "machine" else ("Reci Laser" if page_type == "reci" else "TEYU Chiller")
        
        jsonld = f"""{{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "{product_name}",
  "description": "{desc}",
  "url": "{canonical}",
  "brand": {{
    "@type": "Brand",
    "name": "{manufacturer}"
  }},
  "manufacturer": {{
    "@type": "Organization",
    "name": "{manufacturer}"
  }},"""
        
        if main_img:
            jsonld += f'\n  "image": "{main_img}",'
        
        jsonld += f"""
  "offers": {{
    "@type": "Offer",
    "availability": "https://schema.org/InStock",
    "itemCondition": "https://schema.org/NewCondition",
    "priceCurrency": "EUR",
    "seller": {{
      "@type": "Organization",
      "name": "SIA Bratus"
    }}
  }}"""
        
        # Add specs as additionalProperty
        if specs:
            jsonld += ',\n  "additionalProperty": ['
            prop_items = []
            for key, val in specs.items():
                prop_items.append(f'''\n    {{
      "@type": "PropertyValue",
      "name": "{key}",
      "value": "{val}"
    }}''')
            jsonld += ",".join(prop_items)
            jsonld += "\n  ]"
        
        jsonld += "\n}"
        return f"""<script type="application/ld+json">
{jsonld}
</script>"""
    
    return ""

def fix_img_alts(content, page_type, name):
    """Add meaningful alt text to all images."""
    product_name = name.replace("-", " ").title() if name else ""
    
    def get_alt(img_tag):
        """Generate a meaningful alt for an image."""
        # Already has alt
        alt_m = re.search(r'alt="([^"]*)"', img_tag)
        if alt_m and alt_m.group(1).strip():
            return img_tag  # Keep existing
        
        # Get src to determine alt
        src_m = re.search(r'src="([^"]*)"', img_tag)
        src = src_m.group(1) if src_m else ""
        
        # Determine alt based on context and src
        if "wattsan_logo" in src:
            alt = "Wattsan logo"
        elif "reci" in src.lower():
            alt = f"Reci {product_name} CO2 lāzera lampa"
        elif "teyu" in src.lower() or "chiller" in src.lower():
            alt = f"TEYU {product_name} industriālais dzesētājs"
        elif "gallery" in src.lower() or "result" in src.lower() or "product" in src.lower():
            alt = f"{product_name} — profesionāla lāzera iekārta"
        elif "bratus" in src.lower():
            alt = "Bratus.lv — Wattsan oficiālais pārstāvis Latvijā"
        elif "placeholder" in src.lower():
            alt = product_name if product_name else "Attēls"
        else:
            # Generic descriptive alt
            if page_type == "machine":
                alt = f"{product_name} lāzera iekārta"
            elif page_type == "reci":
                alt = f"{product_name} CO2 lāzera caurule"
            elif page_type == "chiller":
                alt = f"{product_name} dzesētājs"
            else:
                alt = "Wattsan lāzera iekārta"
        
        # Insert alt attribute
        if 'alt=' not in img_tag:
            return img_tag.replace('<img', f'<img alt="{alt}"')
        else:
            return re.sub(r'alt="[^"]*"', f'alt="{alt}"', img_tag)
    
    # Find all img tags and fix them
    def replace_img(match):
        return get_alt(match.group(0))
    
    content = re.sub(r'<img[^>]*>', replace_img, content)
    return content

def process_file(filepath):
    """Process a single HTML file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    canonical = get_canonical(filepath)
    page_type, name = get_page_type(content, filepath)
    
    # Add canonical
    if '<link rel="canonical"' not in content:
        content = content.replace('</head>', f'\n<link rel="canonical" href="{canonical}">\n</head>')
    
    # Add JSON-LD schema
    if 'application/ld+json' not in content:
        jsonld = build_jsonld(page_type, name, content, filepath, canonical)
        if jsonld:
            content = content.replace('</head>', f'\n{jsonld}\n</head>')
    
    # Fix image alts
    content = fix_img_alts(content, page_type, name)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  ✓ {os.path.basename(os.path.dirname(filepath))}/{os.path.basename(filepath)}")

# Process all HTML files
print("Processing HTML files...")
for filepath in glob.glob("d:\\VS KODI\\ROzo github\\**\\*.html", recursive=True):
    process_file(filepath)

print("\n✅ All done!")
