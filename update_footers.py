"""
Replace all product page footers with the homepage footer.
"""
import os
import re

BASE_DIR = r"d:\VS KODI\ROzo github\products"

# The full homepage footer HTML (exactly as from index.html)
HOMEPAGE_FOOTER = """<footer role="contentinfo">
  <div class="footer-grid">
    <div class="footer-brand">
      <div style="display:flex;align-items:center;gap:12px;margin-bottom:14px;">
        <img src="https://wattsan.com/wp-content/uploads/wattsan_logo-1.svg" alt="Wattsan" style="margin-bottom:0;">
        <span style="color:rgba(255,255,255,0.15);font-size:0.7rem;">×</span>
        <a href="https://bratus.lv" target="_blank"><img src="https://cdn.shopify.com/s/files/1/0720/6325/4803/files/BRATUS_BALTS_LOGO_PNG_31ca2710-d923-44ca-ab97-7d4706e0ce6d.png?v=1764954367" alt="Bratus.lv" style="height:26px;width:auto;opacity:0.8;margin-bottom:0;"></a>
      </div>
      <p>Wattsan — profesionālas CNC lāzera iekārtas ar 21 gadu pieredzi. Officiālais pārstāvis Latvijā: SIA Bratus.</p>
    </div>
    <div class="footer-col">
      <h5>Iekārtas</h5>
      <a href="https://wattsan.com/products/laser-machines/" target="_blank">CO2 Lāzeri</a>
      <a href="https://wattsan.com/products/fiber-metal-cutters/" target="_blank">Metāla griešana</a>
      <a href="https://wattsan.com/products/laser-markers/" target="_blank">Marķieri</a>
      <a href="https://wattsan.com/products/cnc-routers/" target="_blank">CNC Frēzes</a>
      <a href="https://wattsan.com/products/laser-welding/" target="_blank">Lāzermetināšana</a>
    </div>
    <div class="footer-col">
      <h5>Kontakti</h5>
      <a href="tel:+37124424434">+371 24 424 434</a>
      <a href="mailto:sales@bratus.lv">sales@bratus.lv</a>
      <a href="https://bratus.lv" target="_blank">bratus.lv</a>
      <p style="margin-top:6px;color:rgba(255,255,255,0.22)">Dārznieku iela 42,<br>Ķekava, Latvija</p>
    </div>
    <div class="footer-col">
      <h5>Wattsan</h5>
      <a href="https://wattsan.com/about-company-wattsan/" target="_blank">Par uzņēmumu</a>
      <a href="https://wattsan.com/support-wattsan/" target="_blank">Atbalsts</a>
      <a href="https://bratus.lv/en" target="_blank">Dīleris Latvijā</a>
      <a href="https://wattsan.com/blog/" target="_blank">Blogs</a>
    </div>
  </div>
  <div class="footer-bar">
    <p>© <span id="yr"></span> SIA <a href="https://bratus.lv" target="_blank" rel="noopener">Bratus</a> · Wattsan oficiālais pārstāvis Latvijā · Reģ. nr. 40203628316</p>
    <p style="display:flex;gap:12px;flex-wrap:wrap;">
      <a href="https://bratus.lv/policies/privacy-policy" target="_blank" rel="noopener">Privātuma politika</a>
      <span style="color:rgba(255,255,255,0.1);">|</span>
      <a href="https://bratus.lv/policies/terms-of-service" target="_blank" rel="noopener">Lietošanas noteikumi</a>
      <span style="color:rgba(255,255,255,0.1);">|</span>
      <a href="https://bratus.lv/pages/par-mums" target="_blank" rel="noopener">Par mums</a>
      <span style="color:rgba(255,255,255,0.1);">|</span>
      <span class="fa">lazergriezeji.lv</span>
    </p>
  </div>
  <p style="text-align:center;font-size:0.58rem;color:rgba(255,255,255,0.12);padding:0 0 8px;letter-spacing:0.04em;">SEO optimizāciju un mājaslapas izstrādi veica <a href="https://latseo.com" target="_blank" rel="noopener" style="color:rgba(255,255,255,0.18);transition:color 0.2s;">Latseo.com</a></p>
</footer>"""

# Regex to match any <footer...>...</footer> (handles multi-line and single-line)
FOOTER_PATTERN = re.compile(r'<footer[^>]*>.*?</footer>', re.DOTALL)


def update_footer(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if HOMEPAGE_FOOTER in content:
        return False  # Already updated

    if not FOOTER_PATTERN.search(content):
        print(f"  SKIP (no footer found): {filepath}")
        return False

    new_content = FOOTER_PATTERN.sub(HOMEPAGE_FOOTER, content, count=1)

    if new_content == content:
        return False

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    return True


def main():
    updated = 0
    skipped = 0

    for root, dirs, files in os.walk(BASE_DIR):
        for f in files:
            if f == 'index.html':
                filepath = os.path.join(root, f)
                slug = os.path.basename(root)
                if update_footer(filepath):
                    print(f"  OK: {slug}")
                    updated += 1
                else:
                    skipped += 1

    print(f"\nDONE: {updated} updated, {skipped} skipped")


if __name__ == '__main__':
    main()
