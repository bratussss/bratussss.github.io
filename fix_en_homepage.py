"""Fix the broken English homepage - replace ALL pseudo-translated text with proper English."""
import re

with open(r"d:\VS KODI\ROzo github\en\index.html", "r", encoding="utf-8") as f:
    c = f.read()

# ── TITLE & META ──
c = c.replace(
    '<title>CO2 Lazergriezeji un Lazergravetaji Wattsan | Bratus </title>',
    '<title>CO2 Laser Cutters & Engravers Wattsan | Bratus</title>'
)
c = c.replace(
    '<meta name="description" content="Professional laser cutting machines un CO2 laser engraving machine. Wattsan dealer in Latvia – Bratus.lv. 21+ year experience, 20k+ sold machines.">',
    '<meta name="description" content="Professional CO2 laser cutting and engraving machines. Official Wattsan dealer in Latvia — Bratus.lv. 21+ years experience, 20k+ machines sold worldwide.">'
)
c = c.replace(
    '<meta name="author" content="SIA Bratus — Wattsan Oficialais Parstavis in Latvia">',
    '<meta name="author" content="SIA Bratus — Official Wattsan Dealer in Latvia">'
)
c = c.replace(
    'property="og:title" content="Wattsan Latvia — Lazera machines | Bratus.lv"',
    'property="og:title" content="Wattsan Latvia — Laser Machines | Bratus.lv"'
)
c = c.replace(
    'property="og:description" content="Professional laser cutting, marking un CO2 Laser Machines in Latvia. Wattsan official dealer in Latvia — Bratus.lv."',
    'property="og:description" content="Professional laser cutting, marking and CO2 laser machines in Latvia. Official Wattsan dealer — Bratus.lv."'
)
c = c.replace(
    'name="twitter:title" content="Wattsan Latvia — Lazera machines | Bratus.lv"',
    'name="twitter:title" content="Wattsan Latvia — Laser Machines | Bratus.lv"'
)
c = c.replace(
    'name="twitter:description" content="Professional laser cutting, marking un CO2 Laser Machines in Latvia. Oficialais Wattsan dealer."',
    'name="twitter:description" content="Professional laser cutting, marking and CO2 laser machines in Latvia. Official Wattsan dealer."'
)

# ── JSON-LD ──
c = c.replace(
    '"description": "Professional laser cutting machines un CO2 laser engraving machine. Wattsan dealer in Latvia – Bratus.lv. 21+ year experience, 20k+ sold machines."',
    '"description": "Professional CO2 laser cutting and engraving machines. Official Wattsan dealer in Latvia — Bratus.lv. 21+ years experience, 20k+ machines sold worldwide."'
)
c = c.replace(
    '"streetAddress": "Darznieku iela 42"',
    '"streetAddress": "Pliederu iela 22"'
)
c = c.replace(
    '"addressLocality": "Kekava"',
    '"addressLocality": "Ķekava"'
)
c = c.replace(
    '"name": "Wattsan Latvia — Lazera machines"',
    '"name": "Wattsan Latvia — Laser Machines"'
)
c = c.replace(
    '"description": "Professional laser cutting, marking un CO2 Laser Machines in Latvia."',
    '"description": "Professional laser cutting, marking and CO2 laser machines in Latvia."'
)
# Fix JSON-LD FAQ entries
c = c.replace(
    '"name": "Kadas laser machines available in Latvia?"',
    '"name": "What laser machines are available in Latvia?"'
)
c = c.replace(
    '"text": "in Latvia through the official dealer Bratus.lv available: CO2 Laser Machines wood, leather un acrylic (17 models), skiedru laser metala cutting machines (16 models), marking machines — Fiber, UV un CO2 (11 models), CNC frezes un laser welding machines."',
    '"text": "Available in Latvia through the official dealer Bratus.lv: CO2 laser machines for wood, leather and acrylic (17 models), fiber laser metal cutting machines (16 models), marking machines — Fiber, UV and CO2 (11 models), CNC routers and laser welding machines."'
)
c = c.replace(
    '"name": "Ka sazinaties ar Wattsan dealer in Latvia?"',
    '"name": "How to contact the Wattsan dealer in Latvia?"'
)
c = c.replace(
    '"name": "Vai are provided warranty un local serviss?"',
    '"name": "Is warranty and local service provided?"'
)
c = c.replace(
    '"name": "Cik long laika are piegadata machine in Latvia?"',
    '"name": "How long does delivery take in Latvia?"'
)

# ── NAV ──
c = c.replace('aria-label="Izvelne"', 'aria-label="Menu"')

# ── BREADCRUMB ──
c = c.replace(
    '<li style="color:var(--ink);font-weight:500;">Lazera machines in Latvia</li>',
    '<li style="color:var(--ink);font-weight:500;">Laser Machines in Latvia</li>'
)

# ── HERO ──
c = c.replace(
    '<h1 class="hero-h1" id="hero-heading">\n      Professional<br>\n      <strong>laser cutting machines</strong><br>\n      <em>jusu productioni</em>\n    </h1>',
    '<h1 class="hero-h1" id="hero-heading">\n      Industrial-Grade<br>\n      <strong>Laser Technology</strong><br>\n      <em>for your production</em>\n    </h1>'
)
c = c.replace(
    '<p class="hero-sub">CO2 lasers, metala cutting machines un markers — Eiropas qualitys CNC aprikoyou ar delivery un support in Latvia through <strong style="color:rgba(255,255,255,0.75)">Bratus.lv</strong>.</p>',
    '<p class="hero-sub">CO2 lasers, metal cutting machines, and laser markers — European-quality CNC equipment with delivery and support across Latvia through <strong style="color:rgba(255,255,255,0.75)">Bratus.lv</strong>.</p>'
)
c = c.replace(
    '<div class="hero-stat-label">Pardotas machines</div>',
    '<div class="hero-stat-label">Machines Sold</div>'
)

# ── MARQUEE ──
c = c.replace('Metala cutting', 'Metal Cutting')
c = c.replace('Skiedru laserss', 'Fiber Laser')
c = c.replace('Lazerengraving', 'Laser Engraving')

# ── BANNER ──
c = c.replace(
    '<p>🇱🇻 <strong>Bratus.lv</strong> — Wattsan official dealer in Latvia. Delivery, installation un warrantys service.</p>',
    '<p>🇱🇻 <strong>Bratus.lv</strong> — Official Wattsan dealer in Latvia. Delivery, installation, and warranty service.</p>'
)

# ── CO2 PANEL ──
c = c.replace(
    '<h2 class="section-title">Griesana <strong>&amp;</strong> engraving<br><em>wood, leather, acrylic</em></h2>',
    '<h2 class="section-title">Cutting <strong>&amp;</strong> Engraving<br><em>for wood, leather, acrylic</em></h2>'
)
c = c.replace(
    '<p class="section-sub">Wood, ada, gumija, akrils — CO2 Laser Machines materialu processingi ar high precision.</p>',
    '<p class="section-sub">Wood, leather, rubber, acrylic — CO2 laser machines for high-precision material processing.</p>'
)
# Machine cats: CO2
c = c.replace('<div class="machine-cat">CO2 laserss · Conveyor / Fabric</div>', '<div class="machine-cat">CO2 Laser · Conveyor / Fabric</div>')
c = c.replace('<div class="machine-cat">CO2 laserss · PRO Series</div>', '<div class="machine-cat">CO2 Laser · PRO Series</div>')
c = c.replace('<div class="machine-cat">CO2 laserss · Flat Bed PRO</div>', '<div class="machine-cat">CO2 Laser · Flat Bed PRO</div>')
c = c.replace('<div class="machine-cat">CO2 laserss · Desktop / Compact</div>', '<div class="machine-cat">CO2 Laser · Desktop</div>')
c = c.replace('<div class="machine-cat">CO2 laserss · ST Series</div>', '<div class="machine-cat">CO2 Laser · ST Series</div>')
c = c.replace('<div class="machine-cat">CO2 laserss · DUOS ST (Divas lampas)</div>', '<div class="machine-cat">CO2 Laser · DUOS ST (Dual Tube)</div>')
c = c.replace('<div class="machine-cat">CO2 laserss · DUOS LT (Divas lampas)</div>', '<div class="machine-cat">CO2 Laser · DUOS LT (Dual Tube)</div>')
c = c.replace('<div class="machine-cat">CO2 laserss · LT Series</div>', '<div class="machine-cat">CO2 Laser · LT Series</div>')

# ── METAL PANEL ──
c = c.replace(
    '<h2 class="section-title">Skiedru lazers <em>metalam</em><br><strong>precisely un quickly</strong></h2>',
    '<h2 class="section-title">Fiber Laser <em>for metal</em><br><strong>precise and fast</strong></h2>'
)
c = c.replace(
    '<p class="section-sub">Aluminum, nerusejosai terauds, misins, vars un oglekla terauds. Griesana up to 25 mm biezumam.</p>',
    '<p class="section-sub">Aluminum, stainless steel, brass, copper, and carbon steel. Cutting up to 25 mm thickness.</p>'
)
# Machine cats: Metal
c = c.replace('<div class="machine-cat">Skiedru laserss · A Series ar kabini</div>', '<div class="machine-cat">Fiber Laser · A Series with Cabin</div>')
c = c.replace('<div class="machine-cat">Skiedru laserss · Large Format</div>', '<div class="machine-cat">Fiber Laser · Large Format</div>')
c = c.replace('<div class="machine-cat">Skiedru laserss · Large Format (High Power)</div>', '<div class="machine-cat">Fiber Laser · Large Format (High Power)</div>')
c = c.replace('<div class="machine-cat">Skiedru laserss · Hard Ultra</div>', '<div class="machine-cat">Fiber Laser · Hard Ultra</div>')
c = c.replace('<div class="machine-cat">Skiedru laserss · Hard Series</div>', '<div class="machine-cat">Fiber Laser · Hard Series</div>')
c = c.replace('<div class="machine-cat">Skiedru laserss · MINI</div>', '<div class="machine-cat">Fiber Laser · MINI</div>')
c = c.replace('<div class="machine-cat">Skiedru laserss · A Series</div>', '<div class="machine-cat">Fiber Laser · A Series</div>')
c = c.replace('<div class="machine-cat">Skiedru laserss · S Series</div>', '<div class="machine-cat">Fiber Laser · S Series</div>')
c = c.replace('<div class="machine-cat">Skiedru laserss · E Series (Ekonomiska)</div>', '<div class="machine-cat">Fiber Laser · E Series (Economy)</div>')

# ── MARKER PANEL ──
c = c.replace(
    '<p class="section-sub">Svitrkodi, QR kodi, logotipi un teksts uz metala, plastmasas, keramikas un glass.</p>',
    '<p class="section-sub">Barcodes, QR codes, logos, and text on metal, plastic, ceramics, and glass.</p>'
)
c = c.replace('<div class="machine-cat">Skiedru marker · Stativs</div>', '<div class="machine-cat">Fiber Marker · Floor Stand</div>')
c = c.replace('<div class="machine-cat">Skiedru marker · Large Format</div>', '<div class="machine-cat">Fiber Marker · Large Format</div>')
c = c.replace('<div class="machine-cat">Skiedru marker · Desktop / Compact</div>', '<div class="machine-cat">Fiber Marker · Desktop / Compact</div>')
c = c.replace('<div class="machine-cat">Skiedru marker · Handheld / Portable</div>', '<div class="machine-cat">Fiber Marker · Handheld / Portable</div>')
c = c.replace('<div class="machine-cat">UV marker · Galda</div>', '<div class="machine-cat">UV Marker · Desktop</div>')
c = c.replace('<div class="machine-cat">Skiedru marker · Desktop / Enclosed</div>', '<div class="machine-cat">Fiber Marker · Desktop / Enclosed</div>')
c = c.replace('<div class="machine-cat">Skiedru marker · 3D Dynamic</div>', '<div class="machine-cat">Fiber Marker · 3D Dynamic</div>')
c = c.replace('<div class="machine-cat">CO2 marker · Galda</div>', '<div class="machine-cat">CO2 Marker · Desktop</div>')
c = c.replace('<div class="machine-cat">Skiedru marker · Galda</div>', '<div class="machine-cat">Fiber Marker · Desktop</div>')

# ── SPARE PARTS PANEL HEADERS ──
c = c.replace(
    '<h2 class="section-title">Originalas <strong>CO2 Laser Tubes</strong><br><em>un components</em></h2>',
    '<h2 class="section-title">Genuine <strong>CO2 Tubes</strong><br><em>and components</em></h2>'
)
c = c.replace(
    '<p class="section-sub">Mes offer tikai the genuines Reci, Lasea avotus ar factorys warranty un ilgu service laiku.</p>',
    '<p class="section-sub">We supply only original Reci and Lasea sources with full factory warranty and extended service life.</p>'
)
c = c.replace('<div class="machine-cat">CO2 Tube · Kompakta</div>', '<div class="machine-cat">CO2 Tube · Compact</div>')
c = c.replace('<div class="machine-cat">CO2 Tube · Popularaka</div>', '<div class="machine-cat">CO2 Tube · Most Popular</div>')
c = c.replace('<div class="machine-cat">CO2 Tube · Lieljaudas</div>', '<div class="machine-cat">CO2 Tube · High Power</div>')
c = c.replace('<div class="machine-cat">CO2 Tube · Lieljaudas+</div>', '<div class="machine-cat">CO2 Tube · High Power+</div>')
c = c.replace('<div class="machine-cat">CO2 Tube · Industriala</div>', '<div class="machine-cat">CO2 Tube · Industrial</div>')

# Peripherals panel
c = c.replace(
    '<h2 class="section-title">Papildaprikoyou <em>jusu</em><br><strong>production efficiencyi</strong></h2>',
    '<h2 class="section-title">Accessories <em>for your</em><br><strong>production efficiency</strong></h2>'
)
c = c.replace(
    '<p class="section-sub">Industrialie chillers (Chiller), drosi izpludes ventilatori un kompresori, kas uztur optimalu machines darbibu.</p>',
    '<p class="section-sub">Industrial chillers, safe exhaust fans, and compressors that keep your equipment running at peak performance.</p>'
)
c = c.replace('<div class="machine-cat">Chiller · Aktiva cooling</div>', '<div class="machine-cat">Chiller · Active Cooling</div>')
c = c.replace('<div class="machine-cat">Chiller · UL Sertificets</div>', '<div class="machine-cat">Chiller · UL Certified</div>')
c = c.replace('<div class="machine-cat">Chiller · Fiber Lazeram 3kW</div>', '<div class="machine-cat">Chiller · For 3kW Fiber Laser</div>')
c = c.replace('<div class="machine-cat">Chiller · Fiber Lazeram 6kW</div>', '<div class="machine-cat">Chiller · For 6kW Fiber Laser</div>')
c = c.replace('<div class="machine-cat">Chiller · Fiber Lazeram 12-15kW</div>', '<div class="machine-cat">Chiller · For 12–15kW Fiber Laser</div>')
c = c.replace('<div class="machine-cat">Chiller · Fiber Lazeram 20kW</div>', '<div class="machine-cat">Chiller · For 20kW Fiber Laser</div>')
c = c.replace('<div class="machine-cat">Chiller · Fiber Lazeram 30kW</div>', '<div class="machine-cat">Chiller · For 30kW Fiber Laser</div>')

# Spare parts panel
c = c.replace(
    '<h2 class="section-title">Augstas accuracys<br><strong>components</strong></h2>',
    '<h2 class="section-title">High-Precision<br><strong>Components</strong></h2>'
)
c = c.replace(
    '<p class="section-sub">Lenss ar augstu caurlaidibu, tiri atstarojosi spoguli un durables siksnas jusu laser aprikojumam.</p>',
    '<p class="section-sub">High-transmission lenses, clean reflective mirrors, and durable belts for your laser equipment.</p>'
)

# ── ABOUT SECTION ──
c = c.replace('<div class="eyebrow">Par Wattsan in Latvia</div>', '<div class="eyebrow">About Wattsan in Latvia</div>')
c = c.replace(
    '<h2 id="about-heading">Razotajs ar <strong>21 years</strong> experience</h2>',
    '<h2 id="about-heading">A Manufacturer with <strong>21 Years</strong> of Experience</h2>'
)
c = c.replace(
    '<p>Wattsan ir CNC iekartu manufacturer no Jinan, China. Mes are not reseller — mes design, manufacture un sell savas machines directly uz jusu production. Musu rupnica work <strong>185 engineers</strong>, un mes have pardevusi more than <strong>20,000 iekartu</strong> customers <strong>100+ countries</strong> worldwide.</p>',
    '<p>Wattsan is a CNC equipment manufacturer based in Jinan, China. We are not a reseller — we design, manufacture, and sell our own machines directly to your production floor. Our factory employs <strong>185 engineers</strong>, and we have delivered over <strong>20,000 machines</strong> to customers in <strong>100+ countries</strong> worldwide.</p>'
)
c = c.replace(
    '<p>in Latvia have Wattsan bazes dileris ar <strong>more than 5 year experience</strong> lazertehnologija. Mes offer full support — no machines selection up to installationi, trainingi un warrantys servicei. <strong>Musu klientu vidu ir gan mazie uznemumi, gan lielas factorys</strong> visa in Latvia.</p>',
    '<p>In Latvia, we are the official Wattsan base dealer with <strong>over 5 years of hands-on experience</strong> in laser technology. We provide full support — from machine selection through installation, training, and warranty service. <strong>Our customers range from small workshops to large-scale factories</strong> across Latvia.</p>'
)
c = c.replace(
    '<time datetime="2026-07-15">Pedejo reizi atjaunots: 2026. years 15. julija</time>',
    '<time datetime="2026-07-15">Last updated: July 15, 2026</time>'
)
c = c.replace('>Par Wattsan ↗<', '>About Wattsan ↗<')
c = c.replace('<div class="a-lbl">Pardotas machines</div>', '<div class="a-lbl">Machines Sold</div>')

# ── CTA ──
c = c.replace(
    '<p>Musu specialists paup toes select most suitable iekartu jusu production needs un calculate costs.</p>',
    '<p>Our specialists will help you select the most suitable machine for your production needs and provide a detailed cost estimate.</p>'
)

# ── CONTACT ──
c = c.replace('<div class="eyebrow">Sazinaties</div>', '<div class="eyebrow">Get in Touch</div>')
c = c.replace(
    '<label class="form-lbl" for="cf-machine">Interese machine</label>',
    '<label class="form-lbl" for="cf-machine">Machine of Interest</label>'
)
c = c.replace('<option>Metala cutting machine</option>', '<option>Metal Cutting Machine</option>')
c = c.replace('<option>Markesanas machine (Fiber)</option>', '<option>Marking Machine (Fiber)</option>')
c = c.replace('<option>CNC freze</option>', '<option>CNC Router</option>')
c = c.replace(
    '<option>Nav parliecibas — required konsultacija</option>',
    '<option>Not Sure — I Need a Consultation</option>'
)
c = c.replace(
    'placeholder="Aprakstiet savu production vajadzibu — materials, izmeri, apjoms..."',
    'placeholder="Describe your production requirements — material, dimensions, volume..."'
)

# ── FAQ SECTION ──
c = c.replace(
    '<h2 id="faq-heading" class="section-title">BUJ <em>par laser</em><br><strong>machines in Latvia</strong></h2>',
    '<h2 id="faq-heading" class="section-title">FAQ <em>About Laser</em><br><strong>Machines in Latvia</strong></h2>'
)
c = c.replace(
    '<p class="section-sub">Atbildes uz most common questions par Wattsan iekartu selection, purchasing un service in Latvia.</p>',
    '<p class="section-sub">Answers to the most common questions about choosing, purchasing, and servicing Wattsan machines in Latvia.</p>'
)

# ── DEFINITION LIST ──
c = c.replace(
    '<dt style="font-weight:600;font-size:0.82rem;color:var(--ink);margin-bottom:3px;">CO2 laserss</dt>',
    '<dt style="font-weight:600;font-size:0.82rem;color:var(--ink);margin-bottom:3px;">CO2 Laser</dt>'
)
c = c.replace(
    '<dd style="font-size:0.76rem;color:var(--ink2);line-height:1.6;font-weight:300;">Gazes lazers ar 10.6 µm vilna garumu, kas uses CO2 gazes maisijumu. Piemerots nemetalisku materialu cuttingi un engravingi: koks, ada, akrils, audums.</dd>',
    '<dd style="font-size:0.76rem;color:var(--ink2);line-height:1.6;font-weight:300;">A gas laser with a 10.6 µm wavelength that uses a CO2 gas mixture. Ideal for cutting and engraving non-metal materials: wood, leather, acrylic, fabric.</dd>'
)
c = c.replace(
    '<dt style="font-weight:600;font-size:0.82rem;color:var(--ink);margin-bottom:3px;">Skiedru laserss (Fiber)</dt>',
    '<dt style="font-weight:600;font-size:0.82rem;color:var(--ink);margin-bottom:3px;">Fiber Laser</dt>'
)
c = c.replace(
    '<dd style="font-size:0.76rem;color:var(--ink2);line-height:1.6;font-weight:300;">Cietvielu lazers ar 1.06 µm vilna garumu. Izmanto optisko skiedru ka pastiprinasanas vidi. Paredzets metalu cuttingi ar high precision un speed.</dd>',
    '<dd style="font-size:0.76rem;color:var(--ink2);line-height:1.6;font-weight:300;">A solid-state laser with a 1.06 µm wavelength. Uses optical fiber as the gain medium. Designed for high-precision, high-speed metal cutting.</dd>'
)
c = c.replace(
    '<dd style="font-size:0.76rem;color:var(--ink2);line-height:1.6;font-weight:300;">Meriyou vatos (W), kas nosaka laser cutting speju. Lielaka jauda lauj griezt biezakus materialus un workt atrak. CO2: 55–700W, Fiber: 1–120kW.</dd>',
    '<dd style="font-size:0.76rem;color:var(--ink2);line-height:1.6;font-weight:300;">Measured in watts (W), this determines the laser\'s cutting capability. Higher power allows cutting thicker materials at higher speeds. CO2: 55–700W, Fiber: 1–120kW.</dd>'
)
c = c.replace(
    '<dd style="font-size:0.76rem;color:var(--ink2);line-height:1.6;font-weight:300;">Datorizeta controls sistema, kas automatiski kontrole machines kustibas. CNC provides atkartojamu precizitati un iespeju darbinat iekartu bez manuals iejauksanas.</dd>',
    '<dd style="font-size:0.76rem;color:var(--ink2);line-height:1.6;font-weight:300;">A computerized control system that automatically manages machine movements. CNC delivers repeatable precision and enables unattended operation.</dd>'
)

# ── COMPARISON TABLE ──
c = c.replace(
    '<h2 id="compare-heading" class="section-title">Kadu lasers <strong>select?</strong><br><em>CO2 vs Skiedru vs UV</em></h2>',
    '<h2 id="compare-heading" class="section-title">Which Laser <strong>Should You Choose?</strong><br><em>CO2 vs Fiber vs UV</em></h2>'
)
c = c.replace(
    '<p class="section-sub">Atrs saup toinayou, kas paup toes select pareizo tehnologiju jusu materialam un production needs.</p>',
    '<p class="section-sub">A quick comparison to help you pick the right technology for your material and production needs.</p>'
)
# Table cells
c = c.replace('<td style="padding:12px 16px;color:var(--ink2);">Wood, ada, akrils, audums</td>', '<td style="padding:12px 16px;color:var(--ink2);">Wood, leather, acrylic, fabric</td>')
c = c.replace('<td style="padding:12px 16px;color:var(--ink2);">Glass, plastmasa, keramika</td>', '<td style="padding:12px 16px;color:var(--ink2);">Glass, plastic, ceramics</td>')
c = c.replace(
    '<th scope="row" style="padding:12px 16px;text-align:left;font-weight:500;color:var(--ink);">Maks. cutting biezums</th>',
    '<th scope="row" style="padding:12px 16px;text-align:left;font-weight:500;color:var(--ink);">Max. Cutting Thickness</th>'
)
c = c.replace('<td style="padding:12px 16px;color:var(--ink2);">Up to 30 mm (akrils)</td>', '<td style="padding:12px 16px;color:var(--ink2);">Up to 30 mm (acrylic)</td>')
c = c.replace('<td style="padding:12px 16px;color:var(--ink2);">Up to 25 mm (terauds)</td>', '<td style="padding:12px 16px;color:var(--ink2);">Up to 25 mm (steel)</td>')
c = c.replace(
    '<th scope="row" style="padding:12px 16px;text-align:left;font-weight:500;color:var(--ink);">Powers diapazons</th>',
    '<th scope="row" style="padding:12px 16px;text-align:left;font-weight:500;color:var(--ink);">Power Range</th>'
)
c = c.replace('<td style="padding:12px 16px;color:var(--ink2);">No €2,500</td>', '<td style="padding:12px 16px;color:var(--ink2);">From €2,500</td>')
c = c.replace('<td style="padding:12px 16px;color:var(--ink2);">No €12,000</td>', '<td style="padding:12px 16px;color:var(--ink2);">From €12,000</td>')
c = c.replace('<td style="padding:12px 16px;color:var(--ink2);">No €4,500</td>', '<td style="padding:12px 16px;color:var(--ink2);">From €4,500</td>')
c = c.replace('<td style="padding:12px 16px;color:var(--ink2);">✓ Visiem models</td>', '<td style="padding:12px 16px;color:var(--ink2);">✓ All Models</td>')
# Fix the 3 occurrences of "✓ Visiem models" 
c = c.replace('✓ Visiem models', '✓ All Models')

# ── FOOTER ──
c = c.replace(
    '<p>Wattsan — professionals CNC laser machines ar 21 year experience. Officialais dealer in Latvia: SIA Bratus.</p>',
    '<p>Wattsan — professional CNC laser equipment backed by 21 years of experience. Official dealer in Latvia: SIA Bratus.</p>'
)
c = c.replace(
    '<a href="https://wattsan.com/products/fiber-metal-cutters/" target="_blank">Metala cutting</a>',
    '<a href="https://wattsan.com/products/fiber-metal-cutters/" target="_blank">Metal Cutting</a>'
)
c = c.replace('>Par company<', '>About Company<')
c = c.replace('>Dileris in Latvia<', '>Dealer in Latvia<')

# ── Any remaining "CO2 laserss" ──
c = c.replace('CO2 laserss', 'CO2 Laser')
c = c.replace('alt="CO2 laserss"', 'alt="CO2 Laser"')

# ── Fix image alt texts ──
c = c.replace('alt="Metala cutting"', 'alt="Metal Cutting"')

# Save
with open(r"d:\VS KODI\ROzo github\en\index.html", "w", encoding="utf-8") as f:
    f.write(c)

print("Done — English homepage fully translated!")
