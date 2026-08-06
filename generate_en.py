"""
Generate English (/en/) versions of all pages with language switcher.
Translates nav, footer, product specs, and common UI to English.
"""
import os
import re
import shutil

BASE_DIR = r"d:\VS KODI\ROzo github"
EN_DIR = os.path.join(BASE_DIR, "en")
PRODUCTS_DIR = os.path.join(BASE_DIR, "products")
EN_PRODUCTS_DIR = os.path.join(EN_DIR, "en", "products")

# ── TRANSLATION MAP: Latvian → English ──
T = {
    # Nav
    'Iekārtas': 'Machines',
    'Rezerves daļas': 'Spare Parts',
    'Par mums': 'About Us',
    'Kontakti': 'Contact',
    'Oficiālais pārstāvis ↗': 'Official Dealer ↗',
    'Pieteikt': 'Inquire',
    'Pāriet uz saturu': 'Skip to content',
    'Galvenā navigācija': 'Main navigation',
    'Atrašanās vieta': 'Breadcrumb',
    'Sākums': 'Home',

    # Hero
    'Industriāla': 'Industrial',
    'lāzertehnoloģija': 'laser technology',
    'jūsu ražošanai': 'for your production',
    'Pieteikt konsultāciju': 'Request Consultation',
    'Apmeklēt bratus.lv': 'Visit bratus.lv',
    'Gadi tirgū': 'Years in market',
    'Pārdotas iekārtas': 'Machines sold',
    'Valstis pasaulē': 'Countries worldwide',

    # Category tabs
    'Izvēlieties iekārtu kategoriju': 'Choose machine category',
    'CO2 lāzera iekārtas': 'CO2 Laser Machines',
    'Metāla griešanas iekārtas': 'Metal Cutting Machines',
    'Marķēšanas iekārtas': 'Marking Machines',
    'Koks, āda, akrils, gumija — universāls lāzeris kvalitatīvai ražošanai.': 'Wood, leather, acrylic, rubber — universal laser for quality production.',
    'Tērauds, alumīnijs, varš, misiņš — šķiedru lāzers precīzai rūpnieciskai griešanai.': 'Steel, aluminum, copper, brass — fiber laser for precise industrial cutting.',
    'Šķiedru, UV un CO2 marķieri — svītrkodi, QR, logotipi uz metāla, plastmasas un stikla.': 'Fiber, UV and CO2 markers — barcodes, QR, logos on metal, plastic and glass.',
    'modeļi': 'models',
    'Skatīt →': 'View →',
    'Pilns katalogs': 'Full Catalog',
    'Jauns': 'New',
    'Jauns 2025': 'New 2025',
    '2025': '2025',
    'Bestseller': 'Bestseller',

    # Spare parts
    'Izvēlieties rezerves daļu kategoriju': 'Choose spare part category',
    'CO2 lampas': 'CO2 Tubes',
    'Perifērijas iekārtas': 'Peripheral Equipment',
    'Oficiālās rezerves daļas': 'Official Spare Parts',
    'Reci, Lasea un citi augstas kvalitātes CO2 lāzera avoti un barošanas bloki.': 'Reci, Lasea and other high-quality CO2 laser sources and power supplies.',
    'Dzesētāji (Chillers), gaisa kompresori un izplūdes sistēmas stabilam darbam.': 'Chillers, air compressors and exhaust systems for stable operation.',
    'Fokusa lēcas, spoguļi, siksnas un sensori garantētai saderībai un ilgmūžībai.': 'Focus lenses, mirrors, belts and sensors for guaranteed compatibility and durability.',

    # CO2 section
    'Griešana &amp; gravēšana<br><em>kokam, ādai, akrilam</em>': 'Cutting &amp; Engraving<br><em>wood, leather, acrylic</em>',
    'Griešana <strong>&amp;</strong> gravēšana<br><em>kokam, ādai, akrilam</em>': 'Cutting <strong>&amp;</strong> Engraving<br><em>wood, leather, acrylic</em>',
    'Koks, āda, gumija, akrils — CO2 lāzera iekārtas materiālu apstrādei ar augstu precizitāti.': 'Wood, leather, rubber, acrylic — CO2 laser machines for high-precision material processing.',

    # Metal section
    'Šķiedru lāzers <em>metālam</em><br><strong>precīzi un ātri</strong>': 'Fiber Laser <em>for metal</em><br><strong>precise and fast</strong>',
    'Alumīnijs, nerūsējošai tērauds, misiņš, varš un oglekļa tērauds. Griešana līdz 25 mm biezumam.': 'Aluminum, stainless steel, brass, copper and carbon steel. Cutting up to 25 mm thickness.',

    # Marker section
    '<strong>Marķētāji</strong><br><em>metālam un ne tikai</em>': '<strong>Markers</strong><br><em>for metal and more</em>',
    'Svītrkodi, QR kodi, logotipi un teksts uz metāla, plastmasas, keramikas un stikla.': 'Barcodes, QR codes, logos and text on metal, plastic, ceramics and glass.',

    # Parts section headers
    'Oriģinālās <strong>CO2 lampas</strong><br><em>un komponentes</em>': 'Original <strong>CO2 Tubes</strong><br><em>and components</em>',
    'Mēs piedāvājam tikai oriģinālos Reci, Lasea avotus ar rūpnīcas garantiju un ilgu kalpošanas laiku.': 'We offer only original Reci, Lasea sources with factory warranty and long service life.',
    'Papildaprīkojums <em>jūsu</em><br><strong>ražošanas efektivitātei</strong>': 'Accessories <em>for your</em><br><strong>production efficiency</strong>',
    'Industriālie dzesētāji (Chiller), droši izplūdes ventilatori un kompresori, kas uztur optimālu iekārtas darbību.': 'Industrial chillers, safe exhaust fans and compressors that maintain optimal equipment performance.',
    'Augstas precizitātes<br><strong>komponentes</strong>': 'High precision<br><strong>components</strong>',
    'Lēcas ar augstu caurlaidību, tīri atstarojoši spoguļi un izturīgas siksnas jūsu lāzera aprīkojumam.': 'High-transmission lenses, clean reflective mirrors and durable belts for your laser equipment.',

    # About
    'Par Wattsan Latvijā': 'About Wattsan in Latvia',
    'Ražotājs ar <strong>21 gada</strong> pieredzi': 'Manufacturer with <strong>21 years</strong> of experience',
    'Inženieri': 'Engineers',

    # CTA
    'Gatavi sākt?<br><strong>Sazinieties</strong> <em>ar mums</em>': 'Ready to start?<br><strong>Contact</strong> <em>us</em>',
    'Mūsu speciālisti palīdzēs izvēlēties piemērotāko iekārtu jūsu ražošanas vajadzībām un aprēķinās izmaksas.': 'Our specialists will help you choose the most suitable machine for your production needs and calculate costs.',

    # Contact
    'Sazināties': 'Get in Touch',
    'Pieteikt iekārtu<br>vai <em>konsultāciju</em>': 'Request a machine<br>or <em>consultation</em>',
    'Aizpildiet formu — mūsu speciālisti sazināsies ar jums 24 stundu laikā ar iekārtu rekomendācijām un cenu aprēķinu.': 'Fill out the form — our specialists will contact you within 24 hours with machine recommendations and pricing.',
    'Wattsan pārstāvis Latvijā': 'Wattsan representative in Latvia',
    'E-pasts': 'Email',
    'Tālrunis': 'Phone',
    'Nosūtīt pieprasījumu': 'Send Inquiry',
    'Vārds, uzvārds *': 'Full Name *',
    'Interesē iekārta': 'Machine of Interest',
    'Izvēlieties tipu...': 'Select type...',
    'CO2 lāzera iekārta': 'CO2 Laser Machine',
    'Metāla griešanas iekārta': 'Metal Cutting Machine',
    'Marķēšanas iekārta (Fiber)': 'Marking Machine (Fiber)',
    'UV marķētājs': 'UV Marker',
    'CNC frēze': 'CNC Router',
    'Nav pārliecības — nepieciešama konsultācija': 'Not sure — need consultation',
    'Projekta apraksts *': 'Project Description *',
    'Aprakstiet savu ražošanas vajadzību — materiāls, izmēri, apjoms...': 'Describe your production needs — material, dimensions, volume...',
    'Pieprasījums nosūtīts ✓': 'Inquiry Sent ✓',

    # FAQ
    'Biežāk uzdotie jautājumi': 'Frequently Asked Questions',
    'BUJ <em>par lāzera</em><br><strong>iekārtām Latvijā</strong>': 'FAQ <em>about laser</em><br><strong>machines in Latvia</strong>',
    'Atbildes uz biežākajiem jautājumiem par Wattsan iekārtu izvēli, iegādi un apkalpošanu Latvijā.': 'Answers to the most common questions about choosing, purchasing and servicing Wattsan machines in Latvia.',

    # Comparison table
    'Tehnoloģiju salīdzinājums': 'Technology Comparison',
    'Kādu lāzeri <strong>izvēlēties?</strong><br><em>CO2 vs Šķiedru vs UV</em>': 'Which laser <strong>to choose?</strong><br><em>CO2 vs Fiber vs UV</em>',
    'Ātrs salīdzinājums, kas palīdzēs izvēlēties pareizo tehnoloģiju jūsu materiālam un ražošanas vajadzībām.': 'A quick comparison to help you choose the right technology for your material and production needs.',
    'Raksturojums': 'Feature',
    'CO2 Lāzeris': 'CO2 Laser',
    'Šķiedru Lāzeris': 'Fiber Laser',
    'UV Marķētājs': 'UV Marker',
    'Viļņa garums': 'Wavelength',
    'Materiāli': 'Materials',
    'Koks, āda, akrils, audums': 'Wood, leather, acrylic, fabric',
    'Tērauds, alumīnijs, varš': 'Steel, aluminum, copper',
    'Stikls, plastmasa, keramika': 'Glass, plastic, ceramics',
    'Maks. griešanas biezums': 'Max. cutting thickness',
    'Līdz 30 mm (akrils)': 'Up to 30 mm (acrylic)',
    'Līdz 25 mm (tērauds)': 'Up to 25 mm (steel)',
    'Marķēšana (negriež)': 'Marking (non-cutting)',
    'Jaudas diapazons': 'Power range',
    'Izmaksas (sākuma)': 'Cost (starting)',
    'CE Sertifikācija': 'CE Certification',
    '✓ Visiem modeļiem': '✓ All models',

    # Definition list
    'Tehniskie termini': 'Technical Terms',
    'Lāzertehnoloģijas <strong>pamatjēdzieni</strong>': 'Laser Technology <strong>Key Concepts</strong>',
    'Gāzes lāzers ar 10.6 µm viļņa garumu': 'Gas laser with 10.6 µm wavelength',
    'Cietvielu lāzers ar 1.06 µm viļņa garumu': 'Solid-state laser with 1.06 µm wavelength',
    'Mērījums vatos (W), kas nosaka lāzera griešanas spēju': 'Measurement in watts (W) determining laser cutting capability',
    'Datorizēta vadības sistēma': 'Computer numerical control system',

    # Footer
    'Wattsan — profesionālas CNC lāzera iekārtas ar 21 gadu pieredzi. Officiālais pārstāvis Latvijā: SIA Bratus.': 'Wattsan — professional CNC laser machines with 21 years of experience. Official dealer in Latvia: SIA Bratus.',
    'Metāla griešana': 'Metal Cutting',
    'Marķieri': 'Markers',
    'CNC Frēzes': 'CNC Routers',
    'Lāzermetināšana': 'Laser Welding',
    'Par uzņēmumu': 'About Company',
    'Atbalsts': 'Support',
    'Dīleris Latvijā': 'Dealer in Latvia',
    'Blogs': 'Blog',
    'Wattsan oficiālais pārstāvis Latvijā': 'Wattsan official dealer in Latvia',
    'Privātuma politika': 'Privacy Policy',
    'Lietošanas noteikumi': 'Terms of Service',
    'SEO optimizāciju un mājaslapas izstrādi veica': 'SEO optimization and website development by',

    # Product specs
    'Darba zona': 'Work Area',
    'Jauda': 'Power',
    'Ātrums': 'Speed',
    'Nominālā jauda': 'Rated Power',
    'Maksimālā jauda': 'Max Power',
    'Garantija': 'Warranty',
    'dienas': 'days',
    'Dzesēšanas jauda': 'Cooling Capacity',
    'Temp. precizitāte': 'Temp. Accuracy',
    'Tvertne': 'Tank',
    'Avots': 'Source',
    'Tips': 'Type',
    'Pielietojums': 'Application',
    'Cena': 'Price',
    'Materiāls': 'Material',
    'Komplekts': 'Set',
    'Diametrs': 'Diameter',
    'Fokusa attālums': 'Focal Length',
    'Elektromagnētiskais': 'Electromagnetic',
    'CO2 lāzera iekārtas': 'CO2 laser machines',
    'Silīcijs (Si) ar zelta pārklājumu': 'Silicon (Si) with gold coating',
    'Molibdēns (Mo) ar sudraba pārklājumu': 'Molybdenum (Mo) with silver coating',
    'gab.': 'pcs.',

    # Product categories in breadcrumbs
    'Lāzera iekārtas Latvijā': 'Laser Machines in Latvia',
    'CO2 lāzera lampas': 'CO2 Laser Tubes',
    'Industriālais Dzesētājs': 'Industrial Chiller',

    # Reci lamp descriptions
    'CO2 Lampa · Kompakta': 'CO2 Tube · Compact',
    'CO2 Lampa · Populārākā': 'CO2 Tube · Most Popular',
    'CO2 Lampa · Lieljaudas': 'CO2 Tube · High Power',
    'CO2 Lampa · Lieljaudas+': 'CO2 Tube · High Power+',
    'CO2 Lampa · Industriāla': 'CO2 Tube · Industrial',

    # Chiller descriptions
    'Dzesētājs · Aktīvā dzesēšana': 'Chiller · Active Cooling',
    'Dzesētājs · UL Sertificēts': 'Chiller · UL Certified',
    'Dzesētājs · Fiber Lāzeram 3kW': 'Chiller · For 3kW Fiber Laser',
    'Dzesētājs · Fiber Lāzeram 6kW': 'Chiller · For 6kW Fiber Laser',
    'Dzesētājs · Fiber Lāzeram 12-15kW': 'Chiller · For 12-15kW Fiber Laser',
    'Dzesētājs · Fiber Lāzeram 20kW': 'Chiller · For 20kW Fiber Laser',
    'Dzesētājs · Fiber Lāzeram 30kW': 'Chiller · For 30kW Fiber Laser',
    'Populārākais · CE/REACH/RoHS': 'Most Popular · CE/REACH/RoHS',
    'UL Sertificēts · 5030W': 'UL Certified · 5030W',
    '12-15kW Fiber · UL': '12-15kW Fiber · UL',
    '20kW Fiber · SGS': '20kW Fiber · SGS',
    '30kW Fiber · SGS': '30kW Fiber · SGS',
    '3kW Fiber · SGS': '3kW Fiber · SGS',
    '6kW Fiber · SGS': '6kW Fiber · SGS',

    # CO2 machine descriptions
    'CO2 lāzeris · Konveijera / Audumam': 'CO2 Laser · Conveyor / Fabric',
    'CO2 lāzeris · PRO Sērija': 'CO2 Laser · PRO Series',
    'CO2 lāzeris · Flat Bed PRO': 'CO2 Laser · Flat Bed PRO',
    'CO2 lāzeris · Galda / Desktop': 'CO2 Laser · Desktop',
    'CO2 lāzeris · ST Sērija': 'CO2 Laser · ST Series',
    'CO2 lāzeris · DUOS ST (Divas lampas)': 'CO2 Laser · DUOS ST (Dual Tube)',
    'CO2 lāzeris · DUOS LT (Divas lampas)': 'CO2 Laser · DUOS LT (Dual Tube)',
    'CO2 lāzeris · LT Sērija': 'CO2 Laser · LT Series',

    # Metal cutter descriptions
    'Šķiedru lāzeris · A Sērija ar kabīni': 'Fiber Laser · A Series with Cabin',
    'Šķiedru lāzeris · Lielformāta': 'Fiber Laser · Large Format',
    'Šķiedru lāzeris · Lielformāta (Lieljaudas)': 'Fiber Laser · Large Format (High Power)',
    'Šķiedru lāzeris · Hard Ultra': 'Fiber Laser · Hard Ultra',
    'Šķiedru lāzeris · Hard Sērija': 'Fiber Laser · Hard Series',
    'Šķiedru lāzeris · MINI': 'Fiber Laser · MINI',
    'Šķiedru lāzeris · A Sērija': 'Fiber Laser · A Series',
    'Šķiedru lāzeris · S Sērija': 'Fiber Laser · S Series',
    'Šķiedru lāzeris · E Sērija (Ekonomiskā)': 'Fiber Laser · E Series (Economy)',

    # Marker descriptions
    'Šķiedru marķētājs · Statīvs': 'Fiber Marker · Stand',
    'Šķiedru marķētājs · Lielformāta': 'Fiber Marker · Large Format',
    'Šķiedru marķētājs · Galda / Kompakts': 'Fiber Marker · Desktop / Compact',
    'Šķiedru marķētājs · Rokas / Portatīvs': 'Fiber Marker · Handheld / Portable',
    'Šķiedru marķētājs · Galda / Slēgts': 'Fiber Marker · Desktop / Enclosed',
    'Šķiedru marķētājs · 3D Dinamiskais': 'Fiber Marker · 3D Dynamic',
    'UV marķētājs · Galda': 'UV Marker · Desktop',
    'CO2 marķētājs · Galda': 'CO2 Marker · Desktop',

    # Specs
    'Elektronika · Relejs': 'Electronics · Relay',
    'Optika · Spogulis': 'Optics · Mirror',
    'Optika · Lēca': 'Optics · Lens',
    'Spogulis Si <span class=\"lbl\">Zelta · 3 gab.</span>': 'Si Mirror <span class=\"lbl\">Gold · 3 pcs.</span>',
    'Spogulis Mo <span class=\"lbl\">Sudraba · 3 gab.</span>': 'Mo Mirror <span class=\"lbl\">Silver · 3 pcs.</span>',
    'Relejs <span class=\"lbl\">CO2 Lāzeram</span>': 'Relay <span class=\"lbl\">for CO2 Laser</span>',
    'Lēca <span class=\"lbl\">63.5 mm</span>': 'Lens <span class=\"lbl\">63.5 mm</span>',
    'Lēca <span class=\"lbl\">50.8 mm</span>': 'Lens <span class=\"lbl\">50.8 mm</span>',
}

# Translations that need regex (context-dependent, longer phrases)
# We'll handle these with simple string replacement in context


def translate_text(text):
    """Translate Latvian text to English using the translation map."""
    # Sort by length (longest first) to avoid partial matches
    for lv, en in sorted(T.items(), key=lambda x: -len(x[0])):
        if lv in text:
            text = text.replace(lv, en)
    return text


def create_english_homepage():
    """Create the English homepage."""
    src = os.path.join(BASE_DIR, "index.html")
    os.makedirs(EN_DIR, exist_ok=True)
    dst = os.path.join(EN_DIR, "index.html")

    with open(src, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update html lang
    content = content.replace('<html lang="lv">', '<html lang="en">')

    # Update canonical
    content = re.sub(
        r'<link rel="canonical" href="https://lazergriezeji\.lv/">',
        '<link rel="canonical" href="https://lazergriezeji.lv/en/">',
        content
    )

    # Update hreflang
    content = content.replace(
        '<link rel="alternate" hreflang="lv" href="https://lazergriezeji.lv/">',
        '<link rel="alternate" hreflang="lv" href="https://lazergriezeji.lv/">'
    )
    # Add en hreflang
    if 'hreflang="en"' not in content:
        content = content.replace(
            '<link rel="alternate" hreflang="x-default"',
            '<link rel="alternate" hreflang="en" href="https://lazergriezeji.lv/en/">\n<link rel="alternate" hreflang="x-default"'
        )

    # Update OG tags
    content = content.replace(
        'property="og:title" content="Wattsan Latvija',
        'property="og:title" content="Wattsan Latvia'
    )
    content = content.replace(
        'property="og:description" content="Profesionālas lāzergriešanas, marķēšanas un CO2 lāzera iekārtas Latvijā. Wattsan oficiālais pārstāvis Latvijā — Bratus.lv."',
        'property="og:description" content="Professional laser cutting, marking and CO2 laser machines in Latvia. Wattsan official dealer in Latvia — Bratus.lv."'
    )
    content = content.replace(
        'property="og:url" content="https://lazergriezeji.lv/"',
        'property="og:url" content="https://lazergriezeji.lv/en/"'
    )
    content = content.replace(
        'property="og:locale" content="lv_LV"',
        'property="og:locale" content="en_US"'
    )
    content = content.replace(
        'property="og:site_name" content="Wattsan Latvija"',
        'property="og:site_name" content="Wattsan Latvia"'
    )

    # Twitter
    content = content.replace(
        'name="twitter:title" content="Wattsan Latvija',
        'name="twitter:title" content="Wattsan Latvia'
    )
    content = content.replace(
        'name="twitter:description" content="Profesionālas lāzergriešanas, marķēšanas un CO2 lāzera iekārtas Latvijā. Oficiālais Wattsan pārstāvis."',
        'name="twitter:description" content="Professional laser cutting, marking and CO2 laser machines in Latvia. Official Wattsan dealer."'
    )
    content = content.replace(
        'name="twitter:url" content="https://lazergriezeji.lv/"',
        'name="twitter:url" content="https://lazergriezeji.lv/en/"'
    )

    # Title
    content = re.sub(
        r'<title>CO2 Lāzergriezēji un Lāzergravētāji Wattsan \| Bratus </title>',
        '<title>CO2 Laser Cutters & Engravers Wattsan | Bratus</title>',
        content
    )

    # Meta description
    content = re.sub(
        r'<meta name="description" content="Profesionālas lāzergriešanas iekārtas un CO2 lāzergravēšanas iekārta. Wattsan pārstāvis Latvijā – Bratus.lv. 21\+ gadu pieredze, 20k\+ pārdotas iekārtas.">',
        '<meta name="description" content="Professional laser cutting machines and CO2 laser engraving equipment. Wattsan dealer in Latvia — Bratus.lv. 21+ years experience, 20k+ machines sold.">',
        content
    )

    # Language switcher in nav
    content = content.replace(
        '<a href="/" class="lang-switch active-lang" aria-label="Latviešu valoda" title="Latviešu">LV</a>',
        '<a href="/" class="lang-switch" aria-label="Latviešu valoda" title="Latviešu">LV</a>'
    )
    content = content.replace(
        '<a href="/en/" class="lang-switch" aria-label="English language" title="English">EN</a>',
        '<a href="/en/" class="lang-switch active-lang" aria-label="English language" title="English">EN</a>'
    )

    # Breadcrumb
    content = content.replace(
        '<li style="color:var(--ink);font-weight:500;">Lāzera iekārtas Latvijā</li>',
        '<li style="color:var(--ink);font-weight:500;">Laser Machines in Latvia</li>'
    )

    # Translate all UI text
    content = translate_text(content)

    # Fix about section link translations
    content = content.replace('Apmeklēt bratus.lv ↗', 'Visit bratus.lv ↗')
    content = content.replace('Wattsan Dealer Latvia ↗', 'Wattsan Dealer Latvia ↗')
    content = content.replace('Par Wattsan ↗', 'About Wattsan ↗')

    # Fix specific button texts
    content = content.replace('>Oficiālais pārstāvis ↗<', '>Official Dealer ↗<')
    content = content.replace('>Pieteikt konsultāciju<', '>Request Consultation<')
    content = content.replace('>Apmeklēt bratus.lv ↗<', '>Visit bratus.lv ↗<')

    # Fix marquee
    content = content.replace('Piegāde Latvijā', 'Delivery in Latvia')
    content = content.replace('CE Sertificēts', 'CE Certified')
    content = content.replace('Bratus.lv — Oficiālais pārstāvis', 'Bratus.lv — Official Dealer')
    content = content.replace('Metāla griešana', 'Metal Cutting')
    content = content.replace('Šķiedru lāzeris', 'Fiber Laser')
    content = content.replace('Lāzergravēšana', 'Laser Engraving')
    content = content.replace('Lāzermetināšana', 'Laser Welding')

    # Fix contact text
    content = content.replace(
        'Wattsan pārstāvis Latvijā',
        'Wattsan dealer in Latvia'
    )
    content = content.replace('>bratus.lv<', '>bratus.lv<')  # Keep as-is

    # Fix footer legal links
    content = content.replace('>Par mums<', '>About Us<')

    # Update JSON-LD
    content = content.replace(
        '"name": "Wattsan Latvija"',
        '"name": "Wattsan Latvia"'
    )
    content = content.replace(
        '"description": "Profesionālas lāzergriešanas, marķēšanas un CO2 lāzera iekārtas Latvijā. Wattsan oficiālais pārstāvis Latvijā — SIA Bratus (bratus.lv). 21+ gadu pieredze, 20k+ pārdotas iekārtas, 100+ valstīs."',
        '"description": "Professional laser cutting, marking and CO2 laser machines in Latvia. Wattsan official dealer in Latvia — SIA Bratus (bratus.lv). 21+ years experience, 20k+ machines sold, 100+ countries."'
    )

    # Fix address country code for English
    content = content.replace('"addressCountry": "LV"', '"addressCountry": "LV"')  # Keep LV

    # Fix the FAQ answers - manually translate key ones
    faq_replacements = [
        ('Wattsan ir CNC lāzera iekārtu ražotājs no Jinan, Ķīna, ar 21 gada pieredzi. Uzņēmums pats projektē, ražo un pārdod savas iekārtas tiešā ceļā klientiem visā pasaulē — vairāk nekā 100 valstīs.',
         'Wattsan is a CNC laser equipment manufacturer from Jinan, China, with 21 years of experience. The company designs, manufactures and sells its own machines directly to customers worldwide — in more than 100 countries.'),
        ('Latvijā caur oficiālo pārstāvi Bratus.lv pieejamas: CO2 lāzera iekārtas kokam, ādai un akrilam (17 modeļi), šķiedru lāzera metāla griešanas iekārtas (16 modeļi), marķēšanas iekārtas — Fiber, UV un CO2 (11 modeļi), CNC frēzes un lāzermetināšanas iekārtas.',
         'Available in Latvia through the official dealer Bratus.lv: CO2 laser machines for wood, leather and acrylic (17 models), fiber laser metal cutting machines (16 models), marking machines — Fiber, UV and CO2 (11 models), CNC routers and laser welding machines.'),
        ('Zvaniet pa tālruni +371 24 424 434, rakstiet uz e-pastu sales@bratus.lv, apmeklējiet vietni bratus.lv vai aizpildiet kontaktformu mūsu lapā. Adrese: Pliederu iela 22, Ķekava, Latvija.',
         'Call +371 24 424 434, email sales@bratus.lv, visit bratus.lv or fill out the contact form on our page. Address: Pliederu iela 22, Ķekava, Latvia.'),
        ('Jā, visas Wattsan iekārtas tiek piegādātas ar ražotāja garantiju un pilnu vietējo servisa atbalstu Latvijā — ieskaitot uzstādīšanu, apmācību un garantijas apkalpošanu caur SIA Bratus.',
         'Yes, all Wattsan machines are supplied with a manufacturer warranty and full local service support in Latvia — including installation, training and warranty service through SIA Bratus.'),
        ('CO2 lāzera lampu kalpošanas laiks ir 3000–10000 stundas atkarībā no modeļa un ekspluatācijas apstākļiem. Reci lampām tiek nodrošināta 360–540 dienu garantija.',
         'CO2 laser tube lifespan is 3000–10000 hours depending on the model and operating conditions. Reci tubes come with a 360–540 day warranty.'),
        ('CO2 lāzeri ir piemēroti kokam, saplāksnim, MDF, ādai, akrilam (plexiglass), gumijai, tekstilam, papīram, kartonam un stikla gravēšanai. Metāla griešanai nepieciešams šķiedru lāzers.',
         'CO2 lasers are suitable for wood, plywood, MDF, leather, acrylic (plexiglass), rubber, textiles, paper, cardboard and glass engraving. Metal cutting requires a fiber laser.'),
        ('Standarta piegādes laiks ir 2–6 nedēļas atkarībā no modeļa un konfigurācijas. Populārākie modeļi bieži ir pieejami no noliktavas Latvijā ar piegādi 3–5 darba dienu laikā.',
         'Standard delivery time is 2–6 weeks depending on the model and configuration. Popular models are often available from stock in Latvia with delivery within 3–5 working days.'),
    ]
    for lv_text, en_text in faq_replacements:
        content = content.replace(lv_text, en_text)

    with open(dst, 'w', encoding='utf-8') as f:
        f.write(content)

    print("  Created: /en/index.html")
    return True


def create_english_product_pages():
    """Create English versions of all product pages."""
    count = 0
    for root, dirs, files in os.walk(PRODUCTS_DIR):
        for f in files:
            if f == 'index.html':
                src = os.path.join(root, f)
                rel = os.path.relpath(root, PRODUCTS_DIR)
                dst_dir = os.path.join(EN_DIR, "products", rel)
                os.makedirs(dst_dir, exist_ok=True)
                dst = os.path.join(dst_dir, f)

                with open(src, 'r', encoding='utf-8') as fh:
                    content = fh.read()

                # Update lang
                content = content.replace('<html lang="lv">', '<html lang="en">')

                # Update canonical
                content = re.sub(
                    r'href="https://lazergriezeji\.lv/products/([^"]+)/"',
                    r'href="https://lazergriezeji.lv/en/products/\1/"',
                    content
                )

                # Update nav links to point to EN versions
                content = content.replace('href="/#', 'href="/en/#')
                content = content.replace('href="https://lazergriezeji.lv/"', 'href="https://lazergriezeji.lv/en/"')

                # Language switcher
                content = content.replace(
                    '<a href="/" class="lang-switch active-lang" aria-label="Latviešu valoda" title="Latviešu">LV</a>',
                    '<a href="/" class="lang-switch" aria-label="Latviešu valoda" title="Latviešu">LV</a>'
                )
                content = content.replace(
                    '<a href="/en/" class="lang-switch" aria-label="English language" title="English">EN</a>',
                    '<a href="/en/" class="lang-switch active-lang" aria-label="English language" title="English">EN</a>'
                )

                # Fix breadcrumb home link
                content = content.replace(
                    '<li><a href="/"',
                    '<li><a href="/en/"'
                )

                # Translate UI text
                content = translate_text(content)

                # Fix specific English constructs
                content = content.replace(
                    '>Oficiālais pārstāvis ↗<',
                    '>Official Dealer ↗<'
                )
                content = content.replace(
                    '>Pieteikt konsultāciju<',
                    '>Request Consultation<'
                )
                content = content.replace(
                    '>Apmeklēt bratus.lv ↗<',
                    '>Visit bratus.lv ↗<'
                )
                content = content.replace(
                    '>Pieteikt<',
                    '>Inquire<'
                )

                # Update JSON-LD names
                content = content.replace('"name": "Wattsan Latvija"', '"name": "Wattsan Latvia"')

                # Fix meter/min → keep as is
                # Fix the "mm" and "W" units - keep as is

                with open(dst, 'w', encoding='utf-8') as fh:
                    fh.write(content)

                count += 1
                if count % 10 == 0:
                    print(f"  ... {count} pages done")

    print(f"  Created {count} English product pages")
    return count


def add_lang_switcher_to_lv_product_pages():
    """Add language switcher to all Latvian product pages."""
    count = 0
    for root, dirs, files in os.walk(PRODUCTS_DIR):
        for f in files:
            if f == 'index.html':
                src = os.path.join(root, f)
                slug = os.path.basename(root)

                with open(src, 'r', encoding='utf-8') as fh:
                    content = fh.read()

                if 'lang-switch' in content:
                    continue  # Already has it

                # Replace "Latvija · LV" with language switcher
                old = '<div class="nav-logo-lv">Latvija <em>·</em> LV</div>'
                new = f'<a href="/products/{slug}/" class="lang-switch active-lang" aria-label="Latviešu valoda" title="Latviešu">LV</a>\n    <a href="/en/products/{slug}/" class="lang-switch" aria-label="English language" title="English">EN</a>'
                if old in content:
                    content = content.replace(old, new)
                    with open(src, 'w', encoding='utf-8') as fh:
                        fh.write(content)
                    count += 1
                else:
                    # Try alternative format (inline)
                    pattern = r'<div class="nav-logo-lv">Latvija <em>·</em> LV</div>'
                    if re.search(pattern, content):
                        content = re.sub(pattern, new, content)
                        with open(src, 'w', encoding='utf-8') as fh:
                            fh.write(content)
                        count += 1
                    else:
                        print(f"  WARNING: Could not find LV indicator in {slug}")

    print(f"  Updated {count} LV product pages with lang switcher")
    return count


def add_lang_switcher_css_to_product_pages():
    """Add the language switcher CSS to all product pages."""
    count = 0
    for root, dirs, files in os.walk(PRODUCTS_DIR):
        for f in files:
            if f == 'index.html':
                src = os.path.join(root, f)
                with open(src, 'r', encoding='utf-8') as fh:
                    content = fh.read()

                if '.lang-switch {' in content:
                    continue  # Already has it

                # Add lang switcher CSS after .nav-logo-lv block
                lang_css = """
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

                # Insert after the .nav-logo-lv em rule (handles both spaced and minified)
                insert_patterns = [
                    '.nav-logo-lv em { font-style: normal; color: var(--accent); }',
                    '.nav-logo-lv em{font-style:normal;color:var(--accent)}',
                ]
                inserted = False
                for pat in insert_patterns:
                    if pat in content:
                        content = content.replace(pat, pat + lang_css)
                        inserted = True
                        break
                if inserted:
                    with open(src, 'w', encoding='utf-8') as fh:
                        fh.write(content)
                    count += 1

    print(f"  Added lang-switcher CSS to {count} product pages")
    return count


def main():
    print("=" * 60)
    print("GENERATING ENGLISH VERSION OF ENTIRE WEBSITE")
    print("=" * 60)

    print("\n[1/5] Creating English homepage...")
    create_english_homepage()

    print("\n[2/5] Adding language switcher CSS to LV product pages...")
    add_lang_switcher_css_to_product_pages()

    print("\n[3/5] Adding language switcher HTML to LV product pages...")
    add_lang_switcher_to_lv_product_pages()

    print("\n[4/5] Creating English product pages...")
    create_english_product_pages()

    print("\n[5/5] Adding language switcher CSS to EN product pages...")
    add_lang_switcher_css_to_en_product_pages()

    print("\n" + "=" * 60)
    print("DONE! English version created at /en/")
    print("=" * 60)


if __name__ == '__main__':
    main()
