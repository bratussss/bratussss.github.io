"""
Clean English version generator. Translates ALL text safely without breaking HTML.
"""
import os, re

BASE = r"d:\VS KODI\ROzo github"
EN = os.path.join(BASE, "en")

# Safe LV→EN dictionary using multi-word phrases with diacritics
# Sorted by priority - longest phrases first
TR = [
    # ── CONTACT FORM (must be FIRST — longest phrases before words) ──
    ('Aizpildiet formu — mūsu speciālisti sazināsies ar jums 24 stundu laikā ar iekārtu rekomendācijām un cenu aprēķinu.',
     'Fill out the form — our specialists will get back to you within 24 hours with machine recommendations and a detailed price quote.'),
    ('Aizpildiet formu — mūsu speciālisti sazināsies ar jums 24 hours ar iekārtu rekomendācijām un cenu aprēķinu.',
     'Fill out the form — our specialists will get back to you within 24 hours with machine recommendations and a detailed price quote.'),
    ('Aizpildiet formu, lai saņemtu konsultāciju par lāzera iekārtām',
     'Fill out the form to receive a consultation about laser machines'),
    ('Aizpildiet formu, lai saņemtu konsultāciju par laser machines',
     'Fill out the form to receive a consultation about laser machines'),
    # ── FAQ items (JSON-LD + HTML) ──
    # HTML FAQ answers (long form with HTML tags)
    ('<p style="font-size:0.82rem;color:var(--ink2);line-height:1.7;font-weight:300;">Wattsan ir CNC lāzera iekārtu ražotājs no Jinan, Ķīna, ar <strong>21 gada pieredzi</strong>. Atšķirībā no tālākpārdevējiem, Wattsan pats projektē un ražo savas iekārtas — vairāk nekā <strong>20,000 iekārtu</strong> pārdotas <strong>100+ valstīs</strong>. Latvijā oficiālais pārstāvis ir SIA Bratus (bratus.lv), kas nodrošina pilnu atbalstu — no izvēles līdz servisam.</p>',
     '<p style="font-size:0.82rem;color:var(--ink2);line-height:1.7;font-weight:300;">Wattsan is a CNC laser equipment manufacturer from Jinan, China, with <strong>21 years of experience</strong>. Unlike resellers, Wattsan designs and builds its own machines — over <strong>20,000 units</strong> sold across <strong>100+ countries</strong>. In Latvia, the official dealer is SIA Bratus (bratus.lv), providing end-to-end support — from selection through after-sales service.</p>'),
    ('<p style="font-size:0.82rem;color:var(--ink2);line-height:1.7;font-weight:300;">CO2 lāzeri (10.6 µm viļņa garums) ir piemēroti <strong>kokam, ādai, akrilam, gumijai, tekstilam</strong>. Šķiedru lāzeri (1.06 µm) ir paredzēti <strong>metāla griešanai</strong> — tēraudam, alumīnijam, varšam, misiņam. CO2 lāzeri ir universālāki nemetāliskiem materiāliem, bet šķiedru lāzeri nodrošina lielāku ātrumu un precizitāti metāla apstrādē.</p>',
     '<p style="font-size:0.82rem;color:var(--ink2);line-height:1.7;font-weight:300;">CO2 lasers (10.6 µm wavelength) are ideal for <strong>wood, leather, acrylic, rubber, and textiles</strong>. Fiber lasers (1.06 µm) are designed for <strong>metal cutting</strong> — steel, aluminum, copper, and brass. CO2 lasers are more versatile for non-metal materials, while fiber lasers deliver higher speed and precision in metal processing.</p>'),
    ('<p style="font-size:0.82rem;color:var(--ink2);line-height:1.7;font-weight:300;"><strong>1.</strong> Konsultācija — mūsu speciālisti izvērtē jūsu vajadzības. <strong>2.</strong> Piedāvājums — saņemat detalizētu cenu un konfigurāciju. <strong>3.</strong> Pasūtījums — apstiprinātā iekārta tiek pasūtīta no ražotāja. <strong>4.</strong> Piegāde — 2–6 nedēļas līdz Latvijai. <strong>5.</strong> Uzstādīšana un apmācība — mūsu tehniķi visu uzstāda un apmāca jūsu darbiniekus.</p>',
     '<p style="font-size:0.82rem;color:var(--ink2);line-height:1.7;font-weight:300;"><strong>1.</strong> Consultation — our specialists assess your requirements. <strong>2.</strong> Proposal — you receive a detailed quote with specifications. <strong>3.</strong> Order — the confirmed machine is ordered from the factory. <strong>4.</strong> Delivery — 2–6 weeks to Latvia. <strong>5.</strong> Installation & Training — our technicians set everything up and train your team.</p>'),
    ('<p style="font-size:0.82rem;color:var(--ink2);line-height:1.7;font-weight:300;">Visas Wattsan iekārtas tiek piegādātas ar <strong>ražotāja garantiju</strong>. CO2 lampām — <strong>360–540 dienu garantija</strong> atkarībā no modeļa. SIA Bratus nodrošina <strong>vietējo servisu Latvijā</strong>: garantijas un pēcgarantijas remonts, rezerves daļu piegāde, tehniskās konsultācijas latviešu, krievu un angļu valodā.</p>',
     '<p style="font-size:0.82rem;color:var(--ink2);line-height:1.7;font-weight:300;">All Wattsan machines come with a <strong>manufacturer warranty</strong>. CO2 tubes carry a <strong>360–540 day warranty</strong> depending on the model. SIA Bratus provides <strong>local service across Latvia</strong>: warranty and post-warranty repairs, spare parts supply, and technical support in Latvian, Russian, and English.</p>'),
    ('<p style="font-size:0.82rem;color:var(--ink2);line-height:1.7;font-weight:300;">CO2 lāzeri efektīvi apstrādā: <strong>koku, saplāksni, MDF</strong> (griešana līdz 25 mm), <strong>akrilu</strong> (līdz 30 mm), <strong>ādu</strong> (līdz 6 mm), gumiju, tekstilu, papīru, kartonu, kā arī veic stikla gravēšanu. Metālu CO2 lāzers tieši negriež — tam nepieciešams šķiedru lāzers.</p>',
     '<p style="font-size:0.82rem;color:var(--ink2);line-height:1.7;font-weight:300;">CO2 lasers efficiently process: <strong>wood, plywood, MDF</strong> (cutting up to 25 mm), <strong>acrylic</strong> (up to 30 mm), <strong>leather</strong> (up to 6 mm), rubber, textiles, paper, cardboard, and also perform glass engraving. CO2 lasers cannot directly cut metal — that requires a fiber laser.</p>'),
    ('<p style="font-size:0.82rem;color:var(--ink2);line-height:1.7;font-weight:300;">Wattsan izmanto <strong>Raycus, IPG, HIWIN</strong> komponentes — nozares līderus. Iekārtām ir <strong>CE sertifikācija</strong>, atbilstība Eiropas drošības standartiem. 21 gada pieredze un 185 inženieru komanda nodrošina nepārtrauktu produktu uzlabošanu. Vietējais serviss Latvijā nozīmē, ka jums nav jāgaida rezerves daļas no Ķīnas.</p>',
     '<p style="font-size:0.82rem;color:var(--ink2);line-height:1.7;font-weight:300;">Wattsan uses <strong>Raycus, IPG, HIWIN</strong> components — industry-leading brands. All machines carry <strong>CE certification</strong>, compliant with European safety standards. 21 years of experience and a team of 185 engineers drive continuous product improvement. Local service in Latvia means you never have to wait for spare parts from China.</p>'),
    ('Kas ir Wattsan un kāpēc izvēlēties šo ražotāju?', 'What is Wattsan and why choose this manufacturer?'),
    ('Kāda ir atšķirība starp CO2 un šķiedru lāzeru?', 'What is the difference between CO2 and fiber lasers?'),
    ('Kā notiek iekārtas iegādes process Latvijā?', 'How does the machine purchasing process work in Latvia?'),
    ('Kādas garantijas un servisa iespējas tiek nodrošinātas?', 'What warranty and service options are available?'),
    ('Kādi materiāli ir piemēroti CO2 lāzera griešanai un gravēšanai?', 'What materials are suitable for CO2 laser cutting and engraving?'),
    ('Kāpēc izvēlēties Wattsan, nevis lētāku alternatīvu?', 'Why choose Wattsan over a cheaper alternative?'),
    ('Biežāk uzdotie jautājumi', 'Frequently Asked Questions'),

    # ── Complex FAQ answers (JSON-LD versions) ──
    ('Wattsan ir CNC lāzera iekārtu ražotājs no Jinan, Ķīna, ar 21 gada pieredzi. Uzņēmums pats projektē, ražo un pārdod savas iekārtas tiešā ceļā klientiem visā pasaulē — vairāk nekā 100 valstīs.',
     'Wattsan is a CNC laser equipment manufacturer from Jinan, China, with 21 years of experience. The company designs, manufactures, and sells its own machines directly to customers worldwide — in more than 100 countries.'),
    ('Zvaniet pa tālruni +371 24 424 434, rakstiet uz e-pastu sales@bratus.lv, apmeklējiet vietni bratus.lv vai aizpildiet kontaktformu mūsu lapā. Adrese: Pliederu iela 22, Ķekava, Latvija.',
     'Call +371 24 424 434, email sales@bratus.lv, visit bratus.lv or fill out our contact form. Address: Pliederu iela 22, Ķekava, Latvia.'),
    ('Jā, visas Wattsan iekārtas tiek piegādātas ar ražotāja garantiju un pilnu vietējo servisa atbalstu Latvijā — ieskaitot uzstādīšanu, apmācību un garantijas apkalpošanu caur SIA Bratus.',
     'Yes, all Wattsan machines are supplied with a manufacturer warranty and full local service support in Latvia — including installation, training, and warranty service through SIA Bratus.'),
    ('CO2 lāzera lampu kalpošanas laiks ir 3000–10000 stundas atkarībā no modeļa un ekspluatācijas apstākļiem. Reci lampām tiek nodrošināta 360–540 dienu garantija.',
     'CO2 laser tube lifespan is 3000–10000 hours depending on the model and operating conditions. Reci tubes come with a 360–540 day warranty.'),
    ('CO2 lāzeri ir piemēroti kokam, saplāksnim, MDF, ādai, akrilam (plexiglass), gumijai, tekstilam, papīram, kartonam un stikla gravēšanai. Metāla griešanai nepieciešams šķiedru lāzers.',
     'CO2 lasers are suitable for wood, plywood, MDF, leather, acrylic (plexiglass), rubber, textiles, paper, cardboard and glass engraving. Metal cutting requires a fiber laser.'),
    ('Standarta piegādes laiks ir 2–6 nedēļas atkarībā no modeļa un konfigurācijas. Populārākie modeļi bieži ir pieejami no noliktavas Latvijā ar piegādi 3–5 darba dienu laikā.',
     'Standard delivery time is 2–6 weeks depending on the model and configuration. Popular models are often available from stock in Latvia with delivery within 3–5 business days.'),

    # ── Long product descriptions ──
    ('Reci W sērijas CO2 stikla lāzera caurule — 3.0 paaudzes tehnoloģija ar metāla-stikla saķepināšanu, >95% TEM00 staru kūļa kvalitāti un līdz pat 12 000 stundu kalpošanas laiku.',
     'Reci W-series CO2 glass laser tube — 3rd generation technology with metal-glass frit sealing, >95% TEM00 beam quality, and up to 12,000 hours of service life.'),
    ('Vispārdotākais TEYU industriālais dzesētājs — kompakts, portatīvs ar 1430W dzesēšanas jaudu un ±0.3℃ temperatūras precizitāti. Piemērots CO2 lāzera iekārtām līdz 150W.',
     'TEYU\'s best-selling industrial chiller — compact and portable with 1430W cooling capacity and ±0.3℃ temperature accuracy. Suitable for CO2 laser machines up to 150W.'),

    # ── Product titles/names ──
    ('Industriālais Dzesētājs Lāzeriekārtām', 'Industrial Chiller for Laser Machines'),
    ('Metāla Griešanas Iekārta', 'Metal Cutting Machine'),
    ('Lāzergravēšanas Iekārta', 'Laser Engraving Machine'),
    ('Lāzergriešanas Iekārta', 'Laser Cutting Machine'),
    ('Lāzermarķēšanas Iekārta', 'Laser Marking Machine'),
    ('Marķēšanas Iekārta', 'Marking Machine'),
    ('CO2 Lāzera Iekārta', 'CO2 Laser Machine'),
    ('CO2 Lāzera Lampa', 'CO2 Laser Tube'),

    # ── Section headings ──
    ('Kāpēc <strong>', 'Why <strong>'),
    ('Nepieciešams <strong>', 'Need a <strong>'),
    ('</strong>?<br><em>Pasūtiet tūlīt</em>', '</strong>?<br><em>Order Today</em>'),
    ('</strong>?<br><em>Pieprasiet cenu tūlīt</em>', '</strong>?<br><em>Request a Quote Today</em>'),
    ('Interesē <strong>', 'Interested in the <strong>'),
    ('Galvenās īpašības', 'Key Features'),
    ('Tehniskie parametri', 'Technical Specifications'),
    ('Detalizēta <strong>specifikācija</strong>', 'Detailed <strong>Specifications</strong>'),
    ('Apstrādājamie <strong>materiāli</strong>', 'Compatible <strong>Materials</strong>'),
    ('Produkta <strong>attēli</strong>', 'Product <strong>Images</strong>'),
    ('Tehnoloģiju salīdzinājums', 'Technology Comparison'),
    ('Tehniskie termini', 'Technical Glossary'),
    ('Lāzertehnoloģijas <strong>pamatjēdzieni</strong>', 'Laser Technology <strong>Key Concepts</strong>'),

    # ── Nav / common UI ──
    ('Pāriet uz saturu', 'Skip to main content'),
    ('Galvenā navigācija', 'Main navigation'),
    ('Atrašanās vieta', 'You are here'),
    ('Izvēlieties iekārtu kategoriju', 'Select a Machine Category'),
    ('Izvēlieties rezerves daļu kategoriju', 'Select a Spare Part Category'),
    ('Oficiālais pārstāvis', 'Official Dealer'),
    ('oficiālais pārstāvis', 'official dealer'),
    ('oficiālo pārstāvi', 'the official dealer'),
    ('Pieteikt konsultāciju', 'Request a Consultation'),
    ('Apmeklēt bratus.lv', 'Visit bratus.lv'),
    ('Pieprasīt cenu', 'Request Pricing'),
    ('Skatīt wattsan.com', 'View on wattsan.com'),
    ('Pilns katalogs', 'Full Catalog'),
    ('Jaunais Modelis', 'New Model'),
    ('Jauns 2025', 'New 2025'),
    ('Pieprasījums nosūtīts', 'Inquiry Sent'),
    ('Nosūtīt pieprasījumu', 'Send Inquiry'),
    ('Velc, lai redzētu vairāk', 'Scroll to see more'),
    ('Iepriekšējais', 'Previous'),
    ('Nākamais', 'Next'),

    # ── Product categories ──
    ('CO2 lāzera iekārtas', 'CO2 Laser Machines'),
    ('Metāla griešanas iekārtas', 'Metal Cutting Machines'),
    ('Marķēšanas iekārtas', 'Marking Machines'),
    ('Perifērijas iekārtas', 'Peripheral Equipment'),
    ('Oficiālās rezerves daļas', 'Genuine Spare Parts'),
    ('CO2 lampas', 'CO2 Laser Tubes'),
    ('CO2 lāzera lampas', 'CO2 Laser Tubes'),
    ('Rezerves daļas', 'Spare Parts'),

    # ── Product category descriptions ──
    ('Koks, āda, akrils, gumija &mdash; universāls lāzeris kvalitatīvai ražošanai.', 'Wood, leather, acrylic, rubber — a versatile laser for quality production.'),
    ('Tērauds, alumīnijs, varš, misiņš &mdash; šķiedru lāzers precīzai rūpnieciskai griešanai.', 'Steel, aluminum, copper, brass — fiber laser for precision industrial cutting.'),
    ('Šķiedru, UV un CO2 marķieri &mdash; svītrkodi, QR, logotipi uz metāla, plastmasas un stikla.', 'Fiber, UV and CO2 markers — barcodes, QR codes, logos on metal, plastic and glass.'),
    ('Reci, Lasea un citi augstas kvalitātes CO2 lāzera avoti un barošanas bloki.', 'Reci, Lasea and other high-quality CO2 laser sources and power supplies.'),
    ('Dzesētāji (Chillers), gaisa kompresori un izplūdes sistēmas stabilam darbam.', 'Chillers, air compressors and exhaust systems for reliable operation.'),
    ('Fokusa lēcas, spoguļi, siksnas un sensori garantētai saderībai un ilgmūžībai.', 'Focus lenses, mirrors, belts and sensors for guaranteed compatibility and long service life.'),

    # ── Feature cards ──
    ('Wattsan SAS Drošība', 'Wattsan SAS Safety System'),
    ('Safety Assurance System ar FOX ugunsgrēka detektoru un rūdīta stikla vāku.', 'Safety Assurance System with FOX fire detector and tempered glass lid.'),
    ('Precīza Jaudas Kontrole', 'Precision Power Control'),
    ('Digitālais potenciometrs ar precizitāti līdz 0.001 A smalkai gravēšanai.', 'Digital potentiometer with precision down to 0.001 A for fine engraving.'),
    ('Ātrgaitas Gravēšana', 'High-Speed Engraving'),
    ('Līdz pat 1000 mm/s gravēšanas ātrums — maksimāla produktivitāte.', 'Up to 1000 mm/s engraving speed — maximum productivity.'),
    ('Caurstaigājams Galds', 'Pass-Through Table'),
    ('Y-ass caurlaide ļauj apstrādāt garākus materiālus.', 'Y-axis pass-through allows processing longer materials.'),
    ('Leadshine Servo Motori', 'Leadshine Servo Motors'),
    ('Precīzi servo motori ar pozicionēšanas precizitāti 0.03 mm.', 'Precision servo motors with 0.03 mm positioning accuracy.'),
    ('Globāls Atbalsts', 'Global Support'),
    ('21 gada pieredze, 185 inženieri, 20 000+ iekārtu 100+ valstīs.', '21 years of experience, 185 engineers, 20,000+ machines in 100+ countries.'),
    ('Ruida Kontrolieris', 'Ruida Controller'),
    ('CE Sertificēta Iekārta', 'CE Certified Machine'),

    # ── JSON-LD product names ──
    ('Konveijera / Audumam', 'Conveyor / Fabric'),
    ('Ar kabīni', 'With Cabin'),
    ('Lielformāta HP', 'Large Format HP'),
    ('Lielformāta (Lieljaudas)', 'Large Format (High Power)'),
    ('Lielformāta', 'Large Format'),
    ('Rokas / Portatīvs', 'Handheld / Portable'),
    ('Galda / Kompakts', 'Desktop / Compact'),
    ('Galda / Slēgts', 'Desktop / Enclosed'),
    ('Galda / Desktop', 'Desktop / Compact'),
    ('3D Dinamiskais', '3D Dynamic'),
    ('UV · Galda', 'UV · Desktop'),
    ('CO2 · Galda', 'CO2 · Desktop'),
    ('CO2 Lāzeram', 'for CO2 Laser'),
]

# Safe word-level replacements (ONLY words with diacritics that can't appear in HTML/CSS/JS)
SAFE_WORDS = [
    # Product badges
    ('Jauns', 'New'), ('Bestseller', 'Bestseller'), ('Jaunais', 'New'),
    # Spec labels
    ('Darba zona', 'Work Area'), ('Jauda', 'Power'), ('Ātrums', 'Speed'),
    ('Nominālā jauda', 'Rated Power'), ('Maksimālā jauda', 'Max Power'),
    ('Garantija', 'Warranty'), ('dienas', 'days'), ('dienu', 'day'),
    ('Dzesēšanas jauda', 'Cooling Capacity'), ('Temp. precizitāte', 'Temp Accuracy'),
    ('Tvertne', 'Tank'), ('Avots', 'Source'), ('Tips', 'Type'),
    ('Pielietojums', 'Application'), ('Cena', 'Price'), ('Materiāls', 'Material'),
    ('Komplekts', 'Set'), ('Diametrs', 'Diameter'), ('Fokusa attālums', 'Focal Length'),
    ('Svars', 'Weight'), ('Izmēri', 'Dimensions'), ('Platums', 'Width'),
    ('Garums', 'Length'), ('Augstums', 'Height'), ('Biezums', 'Thickness'),
    # Material tags
    ('Koks', 'Wood'), ('Saplāksnis', 'Plywood'), ('MDF', 'MDF'), ('Akrils', 'Acrylic'),
    ('Āda', 'Leather'), ('Gumija', 'Rubber'), ('Audums', 'Fabric'), ('Akmens', 'Stone'),
    ('Granīts', 'Granite'), ('Plastmasa', 'Plastic'), ('Bambuss', 'Bamboo'),
    ('Keramika', 'Ceramics'), ('Stikls', 'Glass'), ('Papīrs', 'Paper'),
    ('Kartons', 'Cardboard'), ('Putuplasts', 'Foam'), ('Korķis', 'Cork'),
    ('Alumīnijs', 'Aluminum'), ('Nerūsējošais tērauds', 'Stainless Steel'),
    ('Oglekļa tērauds', 'Carbon Steel'), ('Varš', 'Copper'), ('Misiņš', 'Brass'),
    ('Cinks', 'Zinc'), ('Titāns', 'Titanium'),
    # Spec values / units
    ('līdz', 'up to'), ('Līdz', 'Up to'),
    # Image labels
    ('Pilns iekārtas skats', 'Full Machine View'),
    ('Lāzera detaļa', 'Laser Detail'),
    ('Vadības panelis', 'Control Panel'),
    ('Ražošanas kvalitāte', 'Build Quality'),
    ('Priekšskats', 'Front View'),
    # Spec sub-labels
    ('Lāzera jauda', 'Laser Power'), ('Lāzera caurule', 'Laser Tube'),
    ('Spoguļa diametrs', 'Mirror Diameter'), ('ZnSe lēca', 'ZnSe Lens'),
    ('Caurules darbmūžs', 'Tube Lifespan'), ('Min. gravēšanas izmērs', 'Min. Engraving Size'),
    ('Darba virsma', 'Work Surface'), ('Asmeņu galds', 'Blade Table'),
    ('Griešanas ātrums', 'Cutting Speed'), ('Gravēšanas ātrums', 'Engraving Speed'),
    ('Pozicionēšanas precizitāte', 'Positioning Accuracy'),
    ('Dzesēšana', 'Cooling'), ('Ūdens', 'Water'), ('Barošana', 'Power Supply'),
    ('Jaudas patēriņš', 'Power Consumption'), ('Caurstaigājams galds', 'Pass-Through Table'),
    ('Jā (Y-ass)', 'Yes (Y-axis)'), ('Kontrolieris', 'Controller'),
    ('Programmatūra', 'Software'), ('Savienojamība', 'Connectivity'),
    ('Atbalstītie formāti', 'Supported Formats'),
    # Section labels
    ('Galerija', 'Gallery'), ('Optika', 'Optics'),
    ('Mehānika & Elektronika', 'Mechanics & Electronics'),
    ('Materiāli', 'Materials'),
    # Nav sub labels
    ('CO2 lāzeri:', 'CO2 Lasers:'), ('TEYU Dzesētāji:', 'TEYU Chillers:'),
    ('Reci Lampas:', 'Reci Tubes:'), ('Metāla Lāzeri:', 'Metal Lasers:'),
    ('Marķieri:', 'Markers:'), ('Šķiedru lāzeri:', 'Fiber Lasers:'),
    # Product page series labels
    ('PRO Sērija', 'PRO Series'), ('ST Sērija', 'ST Series'),
    ('LT Sērija', 'LT Series'), ('A Sērija', 'A Series'),
    ('S Sērija', 'S Series'), ('E Sērija', 'E Series'),
    ('Hard Sērija', 'Hard Series'),
    # Spare parts
    ('Elektronika · Relejs', 'Electronics · Relay'), ('Optika · Spogulis', 'Optics · Mirror'),
    ('Optika · Lēca', 'Optics · Lens'), ('Relejs', 'Relay'), ('Lēca', 'Lens'),
    ('Spogulis', 'Mirror'), ('Zelta', 'Gold'), ('Sudraba', 'Silver'),
    ('gab.', 'pcs.'), ('Elektromagnētiskais', 'Electromagnetic'),
    ('CO2 lāzera iekārtas', 'CO2 laser machines'),
    ('Silīcijs (Si) ar zelta pārklājumu', 'Silicon (Si) with gold coating'),
    ('Molibdēns (Mo) ar sudraba pārklājumu', 'Molybdenum (Mo) with silver coating'),
    # Chiller badges
    ('Populārākais · CE/REACH/RoHS', 'Most Popular · CE/REACH/RoHS'),
    ('UL Sertificēts · 5030W', 'UL Certified · 5030W'),
    ('12-15kW Fiber · UL', '12–15kW Fiber · UL'),
    ('20kW Fiber · SGS', '20kW Fiber · SGS'),
    ('30kW Fiber · SGS', '30kW Fiber · SGS'),
    ('3kW Fiber · SGS', '3kW Fiber · SGS'),
    ('6kW Fiber · SGS', '6kW Fiber · SGS'),
    # Common compound words (safe - contain diacritics)
    ('lāzergravēšanas', 'laser engraving'), ('lāzergriešanas', 'laser cutting'),
    ('lāzermetināšanas', 'laser welding'), ('lāzermarķēšanas', 'laser marking'),
    ('gravēšanas', 'engraving'), ('griešanas', 'cutting'),
    ('marķēšanas', 'marking'), ('dzesēšanas', 'cooling'),
    ('apstrādes', 'processing'), ('ražošanas', 'production'),
    ('uzstādīšanas', 'installation'), ('apmācības', 'training'),
    ('kalpošanas', 'service'), ('piegādes', 'delivery'),
    ('pozicionēšanas', 'positioning'),
    ('lāzergravēšana', 'laser engraving'), ('lāzergriešana', 'laser cutting'),
    ('gravēšana', 'engraving'), ('griešana', 'cutting'),
    ('marķēšana', 'marking'), ('dzesēšana', 'cooling'),
    ('apstrāde', 'processing'), ('ražošana', 'production'),
    ('uzstādīšana', 'installation'), ('apmācība', 'training'),
    ('apkalpošana', 'service'), ('piegāde', 'delivery'),
    ('savienojamība', 'connectivity'), ('sertifikācija', 'certification'),
    ('precizitāte', 'accuracy'), ('atkārtojamība', 'repeatability'),
    ('izšķirtspēja', 'resolution'), ('veiktspēja', 'performance'),
    ('efektivitāte', 'efficiency'), ('ilgmūžība', 'durability'),
    ('aizsardzība', 'protection'), ('drošība', 'safety'),
    ('saderība', 'compatibility'), ('tehnoloģija', 'technology'),
    ('funkcija', 'feature'), ('priekšrocība', 'advantage'),
    ('kvalitāte', 'quality'),
    # Inflected forms
    ('lāzera iekārtas', 'laser machines'), ('lāzera iekārta', 'laser machine'),
    ('iekārtām', 'machines'), ('iekārtas', 'machines'), ('iekārta', 'machine'),
    ('lāzeri', 'lasers'), ('lāzera', 'laser'), ('lāzeru', 'laser'),
    ('dzesētāji', 'chillers'), ('dzesētājs', 'chiller'),
    ('marķētāji', 'markers'), ('marķētājs', 'marker'),
    ('marķieri', 'markers'),
    ('sertificēts', 'certified'), ('sertificēta', 'certified'),
    ('garantija', 'warranty'), ('garantiju', 'warranty'),
    ('piegādi', 'delivery'), ('atbalsts', 'support'),
    ('apmācību', 'training'), ('uzstādīšanu', 'installation'),
    ('apkalpošanu', 'service'),
    ('noliktavas', 'warehouse'), ('noliktavā', 'in stock'),
    ('ražotājs', 'manufacturer'), ('ražotāja', 'manufacturer'),
    ('uzņēmums', 'company'), ('uzņēmumu', 'company'),
    ('inženieri', 'engineers'), ('inženieru', 'engineers'),
    ('pieredzi', 'experience'), ('pieredze', 'experience'),
    ('pārstāvis', 'dealer'), ('pārstāvi', 'dealer'),
    ('ražotne', 'factory'), ('rūpnīca', 'factory'),
    ('pieejamas', 'available'), ('pieejami', 'available'),
    ('nepieciešams', 'requires'), ('nepieciešama', 'required'),
    ('piemērots', 'suitable for'), ('piemēroti', 'suitable'),
    ('izstrādāts', 'designed'), ('izstrādāta', 'designed'),
    ('nodrošina', 'provides'), ('nodrošināta', 'provided'),
    ('aprīkots', 'equipped'), ('aprīkota', 'equipped'),
    ('iekļauts', 'included'), ('iekļauta', 'included'),
    ('iebūvēts', 'built-in'), ('iebūvēta', 'built-in'),
    ('automātiska', 'automatic'), ('manuāla', 'manual'),
    ('regulējama', 'adjustable'),
    ('kompakts', 'compact'), ('kompakta', 'compact'),
    ('portatīvs', 'portable'), ('portatīva', 'portable'),
    ('universāls', 'universal'), ('universāla', 'universal'),
    ('izturīgs', 'durable'), ('izturīga', 'durable'),
    ('uzticams', 'reliable'), ('uzticama', 'reliable'),
    ('jaudīgs', 'powerful'), ('jaudīga', 'powerful'),
    ('profesionāls', 'professional'), ('profesionāla', 'professional'),
    ('mūsdienīgs', 'modern'), ('mūsdienīga', 'modern'),
    ('inovatīva', 'innovative'), ('unikāla', 'unique'),
    ('pilnībā', 'fully'), ('viegli', 'easily'), ('ātri', 'quickly'),
    ('precīzi', 'precisely'), ('pastāvīgi', 'constantly'),
    ('vienkārša', 'simple'), ('elastīga', 'flexible'),
    ('ilgstoša', 'long-lasting'), ('efektīva', 'efficient'),
    ('oriģinālā', 'genuine'), ('oriģinālie', 'genuine'),
    ('oriģinālais', 'genuine'), ('oriģinālo', 'the genuine'),
    ('populārākais', 'most popular'), ('populārākā', 'most popular'),
    ('vispārdotākais', 'best-selling'),
    # Remainder words with diacritics
    ('Latvijā', 'in Latvia'), ('Latvija', 'Latvia'), ('Ķīna', 'China'),
    ('ražošanai', 'for production'), ('ražošanu', 'production'),
    ('gada', 'years'), ('gadi', 'years'), ('gadu', 'year'),
    ('valstīs', 'countries'), ('valstis', 'countries'),
    ('pārdotas', 'sold'), ('pārdoti', 'sold'),
    ('pasūtījumiem', 'orders'), ('pasūtījumu', 'order'),
    ('stundas', 'hours'), ('stundu', 'hour'),
    ('nedēļas', 'weeks'), ('nedēļu', 'week'),
    ('modeļa', 'model'), ('modeļiem', 'models'),
    ('konfigurācijas', 'configuration'),
    ('klientiem', 'customers'), ('pasūtītājiem', 'customers'),
    ('kokam', 'wood'), ('ādai', 'leather'), ('akrilam', 'acrylic'),
    ('saplāksnim', 'plywood'), ('gumijai', 'rubber'),
    ('tekstilam', 'textiles'), ('papīram', 'paper'), ('kartonam', 'cardboard'),
    ('vietējais', 'local'), ('vietējo', 'local'), ('vietējā', 'local'),
    ('visā pasaulē', 'worldwide'), ('vairāk nekā', 'more than'),
    ('tiešā ceļā', 'directly'), ('jūsu ražošanai', 'for your production'),
    ('jūsu ražošanu', 'your production'), ('pats projektē', 'designs'),
    ('ražo un pārdod savas', 'manufactures and sells its own'),
    ('tiek piegādātas', 'are supplied'), ('tiek nodrošināta', 'is provided'),
    ('tiek nodrošināts', 'is provided'),
    ('atkarībā no', 'depending on'),
    ('ekspluatācijas apstākļiem', 'operating conditions'),
    ('kalpošanas laiks', 'service life'), ('kalpošanas laiku', 'service life'),
    ('augstas kvalitātes', 'high-quality'), ('augstu precizitāti', 'high precision'),
    ('augsta precizitāte', 'high precision'),
    ('rūpnieciskais', 'industrial'), ('rūpnieciska', 'industrial'),
    ('stikla lāzera caurule', 'glass laser tube'), ('stikla', 'glass'),
    ('paaudzes tehnoloģija', 'generation technology'),
    ('staru kūļa kvalitāti', 'beam quality'), ('staru kūlis', 'beam'),
    ('saķepināšanu', 'frit sealing'),
    ('darba stacijas', 'workstations'), ('darba stacija', 'workstation'),
    ('lietotājam', 'user'), ('lietotājiem', 'users'),
    ('lietošana', 'operation'), ('vadība', 'control'),
    ('dzesēšanas jaudu', 'cooling capacity'), ('dzesēšanas jauda', 'cooling capacity'),
    ('temperatūras precizitāti', 'temperature accuracy'),
    ('temperatūras precizitāte', 'temperature accuracy'),
    ('temperatūra', 'temperature'),
    ('spriegums', 'voltage'), ('strāva', 'current'), ('patēriņš', 'consumption'),
    ('ražīgums', 'productivity'), ('risinājums', 'solution'),
    # MARQUEE
    ('Piegāde Latvijā', 'Delivery Across Latvia'), ('CE Sertificēts', 'CE Certified'),
    ('CO2 Lāzeris', 'CO2 Laser'), ('CNC Frēze', 'CNC Router'),
    ('CNC Frēzes', 'CNC Routers'), ('Lāzermetināšana', 'Laser Welding'),
    ('Metāla griešana', 'Metal Cutting'), ('Šķiedru lāzeris', 'Fiber Laser'),
    ('Lāzergravēšana', 'Laser Engraving'),
    # Footer link texts
    ('>CO2 Lāzeri<', '>CO2 Lasers<'), ('>Marķieri<', '>Markers<'),
    ('>CNC Frēzes<', '>CNC Routers<'), ('>Lāzermetināšana<', '>Laser Welding<'),
    ('>Par uzņēmumu<', '>About Company<'), ('>Atbalsts<', '>Support<'),
    ('>Dīleris Latvijā<', '>Dealer in Latvia<'), ('>Blogs<', '>Blog<'),
    ('>Par mums<', '>About Us<'), ('>Privātuma politika<', '>Privacy Policy<'),
    ('>Lietošanas noteikumi<', '>Terms of Service<'),
    # Footer content
    ('Officiālais pārstāvis Latvijā', 'Official dealer in Latvia'),
    ('SEO optimizāciju un mājaslapas izstrādi veica', 'SEO & website development by'),
    # Form
    ('sazinies-ar-mums', 'contact-us'),
    ('Aizpildiet formu, lai saņemtu konsultāciju par lāzera iekārtām',
     'Fill out the form to receive a consultation about laser machines'),
    ('Aizpildiet formu un saņemiet personalizētu piedāvājumu ar piegādi Latvijā 24 stundu laikā.',
     'Fill out the form and receive a personalized quote with delivery across Latvia within 24 hours.'),
    # Hero text
    ('Industriāla\n      lāzertehnoloģija\n      jūsu ražošanai',
     'Industrial-grade\n      laser technology\n      for your production'),
    ('CO2 lāzeri, metāla griešanas iekārtas un marķētāji — Eiropas kvalitātes CNC aprīkojums ar piegādi un atbalstu Latvijā caur <strong style="color:rgba(255,255,255,0.75)">Bratus.lv</strong>.',
     'CO2 lasers, metal cutting machines, and laser markers — European-quality CNC equipment with delivery and support across Latvia through <strong style="color:rgba(255,255,255,0.75)">Bratus.lv</strong>.'),
    ('Wattsan — Oficiālais pārstāvis Latvijā', 'Wattsan — Official Dealer in Latvia'),
    ('Gadi tirgū', 'Years in Business'), ('Pārdotas iekārtas', 'Machines Sold'),
    ('Valstis pasaulē', 'Countries Worldwide'),
    # Banner
    ('🇱🇻 <strong>Bratus.lv</strong> — Wattsan oficiālais pārstāvis Latvijā. Piegāde, uzstādīšana un garantijas apkalpošana.',
     '🇱🇻 <strong>Bratus.lv</strong> — Official Wattsan dealer in Latvia. Delivery, installation, and warranty service.'),
    ('Apmeklēt bratus.lv →', 'Visit bratus.lv →'),
    # About
    ('Par Wattsan Latvijā', 'About Wattsan in Latvia'),
    ('Ražotājs ar <strong>21 gada</strong> pieredzi', 'A Manufacturer with <strong>21 Years</strong> of Experience'),
    ('Pēdējo reizi atjaunots: 2026. gada 15. jūlijā', 'Last updated: July 15, 2026'),
    ('SIA Bratus, Reģ. nr. 40203628316, PVN maksātājs', 'SIA Bratus, Reg. No. 40203628316, VAT-registered'),
    ('Inženieri', 'Engineers'),
    # CTA
    ('Gatavi sākt?<br><strong>Sazinieties</strong> <em>ar mums</em>',
     'Ready to Get Started?<br><strong>Get in Touch</strong> <em>with Us</em>'),
    ('Mūsu speciālisti palīdzēs izvēlēties piemērotāko iekārtu jūsu ražošanas vajadzībām un aprēķinās izmaksas.',
     'Our specialists will help you select the right machine for your production needs and provide a detailed cost estimate.'),
    # Contact
    ('Pieteikt iekārtu<br>vai <em>konsultāciju</em>', 'Request a Machine<br>or <em>Consultation</em>'),
    ('Aizpildiet formu — mūsu speciālisti sazināsies ar jums 24 stundu laikā ar iekārtu rekomendācijām un cenu aprēķinu.',
     'Fill out the form — our specialists will get back to you within 24 hours with machine recommendations and a detailed price quote.'),
    ('Wattsan pārstāvis Latvijā', 'Wattsan Dealer in Latvia'),
    ('E-pasts', 'Email'), ('Tālrunis', 'Phone'),
    ('Vārds, uzvārds *', 'Full Name *'), ('Interesē iekārta', 'Machine of Interest'),
    ('Izvēlieties tipu...', 'Select a type...'),
    ('Projekta apraksts *', 'Project Description *'),
    ('Aprakstiet savu ražošanas vajadzību — materiāls, izmēri, apjoms...',
     'Describe your production requirements — material, dimensions, volume...'),
    # About text
    ('Wattsan ir CNC iekārtu ražotājs no Jinan, Ķīna. Mēs neesam tālākpārdevējs — mēs projektējam, ražojam un pārdodam savas iekārtas tiešā ceļā uz jūsu ražošanu. Mūsu rūpnīcā strādā <strong>185 inženieri</strong>, un mēs esam pārdevuši vairāk nekā <strong>20,000 iekārtu</strong> klientiem <strong>100+ valstīs</strong> visā pasaulē.',
     'Wattsan is a CNC equipment manufacturer based in Jinan, China. We are not a reseller — we design, manufacture, and sell our own machines directly to your production floor. Our factory employs <strong>185 engineers</strong>, and we have delivered over <strong>20,000 machines</strong> to customers in <strong>100+ countries</strong> worldwide.'),
    ('Latvijā esam Wattsan bāzes dīleris ar <strong>vairāk nekā 5 gadu pieredzi</strong> lāzertehnoloģijā. Mēs piedāvājam pilnu atbalstu — no iekārtas izvēles līdz uzstādīšanai, apmācībai un garantijas apkalpošanai. <strong>Mūsu klientu vidū ir gan mazie uzņēmumi, gan lielās rūpnīcas</strong> visā Latvijā.',
     'In Latvia, we are the official Wattsan base dealer with <strong>over 5 years of hands-on experience</strong> in laser technology. We provide full support — from machine selection through installation, training, and warranty service. <strong>Our customers range from small workshops to large-scale factories</strong> across Latvia.'),
    # Comparison table
    ('Raksturojums', 'Specification'), ('Šķiedru Lāzeris', 'Fiber Laser'),
    ('UV Marķētājs', 'UV Marker'), ('Viļņa garums', 'Wavelength'),
    ('Tērauds, alumīnijs, varš', 'Steel, aluminum, copper'),
    ('Stikls, plastmasa, keramika', 'Glass, plastic, ceramics'),
    ('Maks. griešanas biezums', 'Max. Cutting Thickness'),
    ('Līdz 30 mm (akrils)', 'Up to 30 mm (acrylic)'),
    ('Līdz 25 mm (tērauds)', 'Up to 25 mm (steel)'),
    ('Marķēšana (negriež)', 'Marking only (non-cutting)'),
    ('Jaudas diapazons', 'Power Range'),
    ('Izmaksas (sākuma)', 'Starting Price'),
    ('CE Sertifikācija', 'CE Certification'),
    ('✓ Visiem modeļiem', '✓ All Models'),
    # Definition list
    ('Gāzes lāzers ar 10.6 µm viļņa garumu, kas izmanto CO2 gāzes maisījumu. Piemērots nemetālisku materiālu griešanai un gravēšanai: koks, āda, akrils, audums.',
     'A gas laser with a 10.6 µm wavelength that uses a CO2 gas mixture. Ideal for cutting and engraving non-metal materials: wood, leather, acrylic, fabric.'),
    ('Cietvielu lāzers ar 1.06 µm viļņa garumu. Izmanto optisko šķiedru kā pastiprināšanas vidi. Paredzēts metālu griešanai ar augstu precizitāti un ātrumu.',
     'A solid-state laser with a 1.06 µm wavelength. Uses optical fiber as the gain medium. Designed for high-precision, high-speed metal cutting.'),
    ('Mērījums vatos (W), kas nosaka lāzera griešanas spēju. Lielāka jauda ļauj griezt biezākus materiālus un strādāt ātrāk. CO2: 55–700W, Fiber: 1–120kW.',
     'Measured in watts (W), this determines the laser\'s cutting capability. Higher power allows cutting thicker materials at higher speeds. CO2: 55–700W, Fiber: 1–120kW.'),
    ('Datorizēta vadības sistēma, kas automātiski kontrolē iekārtas kustības. CNC nodrošina atkārtojamu precizitāti un iespēju darbināt iekārtu bez manuālas iejaukšanās.',
     'A computerized control system that automatically manages machine movements. CNC delivers repeatable precision and enables unattended operation.'),
    # Sākums
    ('>Sākums<', '>Home<'), ('Sākums', 'Home'),
    # Nav display text
    ('>Iekārtas<', '>Machines<'), ('>Rezerves daļas<', '>Spare Parts<'),
    ('>Par mums<', '>About Us<'), ('>Kontakti<', '>Contact<'),
    ('>Oficiālais pārstāvis ↗<', '>Official Dealer ↗<'),
    ('>Pieteikt<', '>Get a Quote<'),
    # Cat tabs
    ('Skatīt →', 'View All →'), ('modeļi', 'models'),
    ('Spiest ↓', 'Tap ↓'), ('Aktīvs', 'Active'),
    # JSON-LD FAQ names
    ('"name": "Kas ir Wattsan?"', '"name": "What is Wattsan?"'),
    ('"name": "Kādas lāzera iekārtas pieejamas Latvijā?"', '"name": "What laser machines are available in Latvia?"'),
    ('"name": "Kā sazināties ar Wattsan pārstāvi Latvijā?"', '"name": "How to contact the Wattsan dealer in Latvia?"'),
    ('"name": "Vai tiek nodrošināta garantija un vietējais serviss?"', '"name": "Is warranty and local service provided?"'),
    ('"name": "Kāds ir CO2 lāzera iekārtu kalpošanas laiks?"', '"name": "What is the lifespan of CO2 laser machines?"'),
    ('"name": "Kāds ir CO2 laser iekārtu service laiks?"', '"name": "What is the lifespan of CO2 laser machines?"'),
    ('"name": "Kādi materiāli ir piemēroti CO2 lāzera griešanai un gravēšanai?"', '"name": "What materials are suitable for CO2 laser cutting and engraving?"'),
    ('"name": "Cik ilgā laikā tiek piegādāta iekārta Latvijā?"', '"name": "How long does delivery take in Latvia?"'),
    # Meta
    ('SIA Bratus — Wattsan Oficiālais Pārstāvis Latvijā', 'SIA Bratus — Official Wattsan Dealer in Latvia'),
    ('Wattsan Latvija — Lāzera iekārtas | Bratus.lv', 'Wattsan Latvia — Laser Machines | Bratus.lv'),
    ('"description": "Profesionālas lāzergriešanas, marķēšanas un CO2 lāzera iekārtas Latvijā. Wattsan oficiālais pārstāvis Latvijā — SIA Bratus (bratus.lv). 21+ gadu pieredze, 20k+ pārdotas iekārtas, 100+ valstīs."',
     '"description": "Professional laser cutting, marking and CO2 laser equipment in Latvia. Official Wattsan dealer in Latvia — SIA Bratus (bratus.lv). 21+ years of experience, 20k+ machines sold across 100+ countries."'),
    ('"name": "Wattsan Latvija"', '"name": "Wattsan Latvia"'),
    ('"name": "Wattsan Latvija — Lāzera iekārtas"', '"name": "Wattsan Latvia — Laser Equipment"'),
    ('"inLanguage": "lv"', '"inLanguage": "en"'),
    ('property="og:locale" content="lv_LV"', 'property="og:locale" content="en_US"'),
    ('property="og:site_name" content="Wattsan Latvija"', 'property="og:site_name" content="Wattsan Latvia"'),
    # Footer
    ('Wattsan — profesionālas CNC lāzera iekārtas ar 21 gadu pieredzi. Officiālais pārstāvis Latvijā: SIA Bratus.',
     'Wattsan — professional CNC laser equipment backed by 21 years of experience. Official dealer in Latvia: SIA Bratus.'),
    ('Wattsan oficiālais pārstāvis Latvijā', 'Official Wattsan dealer in Latvia'),
    # JS
    ('// Initializējam abus blokus', '// Initialize both blocks'),
    ("' — Aktīvs'", "' — Active'"),
    # Alt texts
    ('alt="marķētājs"', 'alt="Laser marker"'), ('alt="CO2 Lampa"', 'alt="CO2 Tube"'),
    ('alt="Perifērija"', 'alt="Peripheral equipment"'), ('alt="Rezerves daļas"', 'alt="Spare parts"'),
    ('Metāla griešana', 'Metal Cutting'),
    # Title/description special
    ('title="Latviešu"', 'title="Latvian"'),
    # Remaining CO2 Panel headers
    ('Griešana <strong>&amp;</strong> gravēšana<br><em>kokam, ādai, akrilam</em>',
     'Cutting <strong>&amp;</strong> Engraving<br><em>for wood, leather, acrylic</em>'),
    ('Koks, āda, gumija, akrils — CO2 lāzera iekārtas materiālu apstrādei ar augstu precizitāti.',
     'Wood, leather, rubber, acrylic — CO2 laser machines for high-precision material processing.'),
    # Metal panel
    ('Šķiedru lāzers <em>metālam</em><br><strong>precīzi un ātri</strong>',
     'Fiber Laser <em>for metal</em><br><strong>precise and fast</strong>'),
    ('Alumīnijs, nerūsējošai tērauds, misiņš, varš un oglekļa tērauds. Griešana līdz 25 mm biezumam.',
     'Aluminum, stainless steel, brass, copper, and carbon steel. Cutting up to 25 mm thickness.'),
    # Marker panel
    ('<strong>Marķētāji</strong><br><em>metālam un ne tikai</em>',
     '<strong>Laser Markers</strong><br><em>for metal and beyond</em>'),
    ('Svītrkodi, QR kodi, logotipi un teksts uz metāla, plastmasas, keramikas un stikla.',
     'Barcodes, QR codes, logos, and text on metal, plastic, ceramics, and glass.'),
    # CO2 tubes panel
    ('Oriģinālās <strong>CO2 lampas</strong><br><em>un komponentes</em>',
     'Genuine <strong>CO2 Tubes</strong><br><em>and components</em>'),
    ('Mēs piedāvājam tikai oriģinālos Reci, Lasea avotus ar rūpnīcas garantiju un ilgu kalpošanas laiku.',
     'We supply only original Reci and Lasea sources with full factory warranty and extended service life.'),
    # Peripherals panel
    ('Papildaprīkojums <em>jūsu</em><br><strong>ražošanas efektivitātei</strong>',
     'Accessories <em>for your</em><br><strong>production efficiency</strong>'),
    ('Industriālie dzesētāji (Chiller), droši izplūdes ventilatori un kompresori, kas uztur optimālu iekārtas darbību.',
     'Industrial chillers, safe exhaust fans, and compressors that keep your equipment running at peak performance.'),
    # Spare parts panel
    ('Augstas precizitātes<br><strong>komponentes</strong>',
     'High-Precision<br><strong>Components</strong>'),
    ('Lēcas ar augstu caurlaidību, tīri atstarojoši spoguļi un izturīgas siksnas jūsu lāzera aprīkojumam.',
     'High-transmission lenses, clean reflective mirrors, and durable belts for your laser equipment.'),
    # More product page content
    ('Šķiedru marķētājs ·', 'Fiber Marker ·'),
    ('CO2 lāzeris ·', 'CO2 Laser ·'),
    ('Šķiedru lāzeris ·', 'Fiber Laser ·'),
    ('Dzesētājs ·', 'Chiller ·'),
    ('CO2 Lampa ·', 'CO2 Tube ·'),
    ('Profesionālas', 'Professional'),
    ('profesionāla lāzera iekārta', 'professional laser machine'),
    ('lāzera iekārta', 'laser machine'),
    ('ar uzlabotu precizitāti', 'with enhanced precision'),
    ('koka lāzergriešanai', 'wood laser cutting'),
    ('Populārākā koka lāzergriešanai', 'Most popular for wood laser cutting'),
    ('Populārākā koka laser cuttingi', 'Most popular for wood laser cutting'),
    ('hour laikā', 'hours'),
    ('stundu laikā', 'hours'),
    ('Aizpildiet formu un saņemiet personalizētu piedāvājumu ar piegādi Latvijā 24 stundu laikā.',
     'Fill out the form and receive a personalized quote with delivery across Latvia within 24 hours.'),
    ('Aizpildiet formu un saņemiet personalizētu piedāvājumu ar', 'Fill out the form and receive a personalized quote with'),
    ('personalizētu piedāvājumu', 'personalized quote'),
    ('stundu laikā', 'hours'),
    ('24 stundu laikā', '24 hours'),
    ('Metāla griešanai', 'Metal cutting'),
    ('šķiedru lāzers', 'fiber laser'), ('šķiedru lāzera', 'fiber laser'),
    ('CO2 lāzera iekārtas', 'CO2 Laser Machines'),
    ('Lāzera iekārtas Latvijā', 'Laser Machines in Latvia'),
    ('caur ', 'through '), ('Caur ', 'Through '),
    # ── Final contact form / consultation phrases ──
    ('Aizpildiet formu — mūsu', 'Fill out the form — our'),
    ('sazināsies ar jums', 'will contact you'),
    ('ar iekārtu rekomendācijām', 'with machine recommendations'),
    ('cenu aprēķinu', 'price quote'),
    ('lai saņemtu konsultāciju', 'to receive a consultation'),
    ('konsultāciju par', 'consultation about'),
    ('Aizpildiet', 'Fill out'), ('formu', 'form'),
    ('mūsu', 'our'), ('speciālisti', 'specialists'),
    ('sazināsies', 'will contact'), ('jums', 'you'),
    ('rekomendācijām', 'recommendations'),
    ('aprēķinu', 'quote'), ('saņemtu', 'receive'),
]


def translate(text):
    """Apply all translations safely."""
    # First do long phrase matches
    for lv, en in TR:
        text = text.replace(lv, en)
    # Then safe word-level
    for lv, en in SAFE_WORDS:
        text = text.replace(lv, en)
    return text


def restore_ids_and_hrefs(text):
    """Restore HTML IDs and href values that must stay in Latvian."""
    replacements = [
        ('href="#machines"', 'href="#iekārtas"'),
        ('href="/#machines"', 'href="/#iekārtas"'),
        ('href="/en/#machines"', 'href="/en/#iekārtas"'),
        ('href="#spare-parts"', 'href="#rezerves-dalas"'),
        ('href="/#spare-parts"', 'href="/#rezerves-dalas"'),
        ('href="/en/#spare-parts"', 'href="/en/#rezerves-dalas"'),
        ('href="#spare-dalas"', 'href="#rezerves-dalas"'),
        ('href="/#spare-dalas"', 'href="/#rezerves-dalas"'),
        ('href="/en/#spare-dalas"', 'href="/en/#rezerves-dalas"'),
        ('id="spare-parts"', 'id="rezerves-dalas"'),
        ('id="spare-dalas"', 'id="rezerves-dalas"'),
        ("initTabs('machines'", "initTabs('iekārtas'"),
        ("initTabs('spare-parts'", "initTabs('rezerves-dalas'"),
        ("initTabs('spare-dalas'", "initTabs('rezerves-dalas'"),
        ('id="machines"', 'id="iekārtas"'),
        # Fix diacritic-stripped IDs
        ('id="iekartas"', 'id="iekārtas"'),
        ('href="#iekartas"', 'href="#iekārtas"'),
        ('href="/en/#iekartas"', 'href="/en/#iekārtas"'),
        ("initTabs('iekartas'", "initTabs('iekārtas'"),
        ('id="rezerves-dalas"', 'id="rezerves-dalas"'),  # preserve
        ('href="#rezerves-dalas"', 'href="#rezerves-dalas"'),  # preserve
        ('href="/en/#rezerves-dalas"', 'href="/en/#rezerves-dalas"'),  # preserve
    ]
    for old, new in replacements:
        text = text.replace(old, new)
    return text


def build_en_homepage():
    src = os.path.join(BASE, "index.html")
    os.makedirs(EN, exist_ok=True)
    dst = os.path.join(EN, "index.html")
    with open(src, 'r', encoding='utf-8') as f:
        c = f.read()

    c = c.replace('<html lang="lv">', '<html lang="en">')
    c = c.replace(
        '<link rel="canonical" href="https://lazergriezeji.lv/">',
        '<link rel="canonical" href="https://lazergriezeji.lv/en/">'
    )
    c = c.replace(
        'property="og:url" content="https://lazergriezeji.lv/"',
        'property="og:url" content="https://lazergriezeji.lv/en/"'
    )
    c = c.replace(
        'name="twitter:url" content="https://lazergriezeji.lv/"',
        'name="twitter:url" content="https://lazergriezeji.lv/en/"'
    )
    # Lang switcher
    c = c.replace(
        '<a href="/" class="lang-switch active-lang" aria-label="Latviešu valoda" title="Latviešu">LV</a>',
        '<a href="/" class="lang-switch" aria-label="Latvian" title="Latvian">LV</a>'
    )
    c = c.replace(
        '<a href="/en/" class="lang-switch" aria-label="English language" title="English">EN</a>',
        '<a href="/en/" class="lang-switch active-lang" aria-label="English" title="English">EN</a>'
    )
    # Breadcrumb home link
    c = c.replace(
        '<li><a href="/" style="color:var(--ink2);transition:color 0.2s;">',
        '<li><a href="/en/" style="color:var(--ink2);transition:color 0.2s;">'
    )
    # ── PRESERVE ENGLISH: Redirect nav links to /en/ ──
    c = c.replace('href="/#iekārtas"', 'href="/en/#iekārtas"')
    c = c.replace('href="/#rezerves-dalas"', 'href="/en/#rezerves-dalas"')
    c = c.replace('href="/#par-mums"', 'href="/en/#par-mums"')
    c = c.replace('href="/#kontakts"', 'href="/en/#kontakts"')

    c = translate(c)
    c = final_latvian_sweep(c)
    c = restore_ids_and_hrefs(c)

    with open(dst, 'w', encoding='utf-8') as f:
        f.write(c)
    print("  ✓ English homepage")


def build_en_products():
    src_dir = os.path.join(BASE, "products")
    dst_dir = os.path.join(EN, "products")
    count = 0
    for root, dirs, files in os.walk(src_dir):
        for f in files:
            if f == 'index.html':
                src = os.path.join(root, f)
                rel = os.path.relpath(root, src_dir)
                d = os.path.join(dst_dir, rel)
                os.makedirs(d, exist_ok=True)
                dst = os.path.join(d, f)
                slug = rel

                with open(src, 'r', encoding='utf-8') as fh:
                    c = fh.read()

                c = c.replace('<html lang="lv">', '<html lang="en">')
                c = re.sub(
                    r'href="https://lazergriezeji\.lv/products/([^"]+)/"',
                    r'href="https://lazergriezeji.lv/en/products/\1/"',
                    c
                )

                # ── PRESERVE ENGLISH: Redirect all root-relative links to /en/ ──
                # Nav links: /#iekārtas → /en/#iekārtas
                c = c.replace('href="/#iekārtas"', 'href="/en/#iekārtas"')
                c = c.replace('href="/#rezerves-dalas"', 'href="/en/#rezerves-dalas"')
                c = c.replace('href="/#par-mums"', 'href="/en/#par-mums"')
                c = c.replace('href="/#kontakts"', 'href="/en/#kontakts"')
                # Logo link: href="/" → href="/en/"
                c = c.replace('href="/">', 'href="/en/">')
                # Breadcrumb home
                c = c.replace('<li><a href="/" ', '<li><a href="/en/" ')
                c = c.replace('<a href="../">', '<a href="/en/">')
                # CTA buttons pointing to /#kontakts
                c = c.replace('href="/#kontakts" class="btn-accent"', 'href="/en/#kontakts" class="btn-accent"')
                c = c.replace('href="/#kontakts" class="btn-primary"', 'href="/en/#kontakts" class="btn-primary"')
                c = c.replace('href="/#kontakts" class="btn-hero-primary"', 'href="/en/#kontakts" class="btn-hero-primary"')

                # Lang switcher
                c = c.replace(
                    f'<a href="/products/{slug}/" class="lang-switch active-lang" aria-label="Latviešu valoda" title="Latviešu">LV</a>',
                    f'<a href="/products/{slug}/" class="lang-switch" aria-label="Latvian" title="Latvian">LV</a>'
                )
                c = c.replace(
                    f'<a href="/en/products/{slug}/" class="lang-switch" aria-label="English language" title="English">EN</a>',
                    f'<a href="/en/products/{slug}/" class="lang-switch active-lang" aria-label="English" title="English">EN</a>'
                )

                c = translate(c)
                c = final_latvian_sweep(c)
                c = restore_ids_and_hrefs(c)

                with open(dst, 'w', encoding='utf-8') as fh:
                    fh.write(c)
                count += 1
    print(f"  ✓ {count} English product pages")


def final_latvian_sweep(text):
    """Remove ALL remaining Latvian words from text content."""
    sweep = [
        ('neesam', 'are not'), ('tālākpārdevējs', 'reseller'),
        ('projektējam', 'design'), ('ražojam', 'manufacture'),
        ('pārdodam', 'sell'), ('strādā', 'work'),
        ('esam', 'have'), ('klientiem', 'customers'),
        ('piedāvājam', 'offer'), ('izvēlēties', 'select'),
        ('piemērotāko', 'most suitable'), ('vajadzībām', 'needs'),
        ('aprēķinās', 'calculate'), ('izmaksas', 'costs'),
        ('izvēles', 'selection'), ('līdz', 'to'),
        ('servisam', 'service'), ('darbiniekus', 'staff'),
        ('tehniķi', 'technicians'), ('uzstāda', 'install'),
        ('apmāca', 'train'), ('visu', 'everything'),
        ('apstiprinātā', 'confirmed'), ('pasūtīta', 'ordered'),
        ('saņemat', 'receive'), ('detalizētu', 'detailed'),
        ('konfigurāciju', 'configuration'), ('izvērtē', 'assess'),
        ('vajadzības', 'needs'), ('Konsultācija', 'Consultation'),
        ('Piedāvājums', 'Proposal'), ('Pasūtījums', 'Order'),
        ('Piegāde', 'Delivery'), ('Uzstādīšana', 'Installation'),
        ('apmācība', 'Training'), ('universālāki', 'more versatile'),
        ('nemetāliskiem', 'non-metal'), ('materiāliem', 'materials'),
        ('lielāku', 'higher'), ('apstrādē', 'processing'),
        ('tēraudam', 'steel'), ('alumīnijam', 'aluminum'),
        ('varšam', 'copper'), ('misiņam', 'brass'),
        ('atšķirībā', 'unlike'), ('projektē', 'designs'),
        ('ražo', 'manufactures'), ('pārdotas', 'sold'),
        ('oficiālais', 'official'), ('pilnu', 'full'),
        ('atbalstu', 'support'), ('atšķirība', 'difference'),
        ('starp', 'between'), ('paredzēti', 'designed'),
        ('ātrumu', 'speed'), ('notiek', 'works'),
        ('iegādes', 'purchasing'), ('process', 'process'),
        ('iespējas', 'options'), ('tiek', 'are'),
        ('nodrošinātas', 'provided'), ('piegādātas', 'supplied'),
        ('pēcgarantijas', 'post-warranty'), ('remonts', 'repair'),
        ('daļu', 'part'), ('tehniskās', 'technical'),
        ('konsultācijas', 'consultations'), ('valodā', 'language'),
        ('apstrādā', 'processes'), ('efektīvi', 'efficiently'),
        ('veic', 'performs'), ('negriež', 'does not cut'),
        ('izmanto', 'uses'), ('komponentes', 'components'),
        ('nozares', 'industry'), ('līderus', 'leaders'),
        ('atbilstība', 'compliance'), ('drošības', 'safety'),
        ('standartiem', 'standards'), ('komanda', 'team'),
        ('nepārtrauktu', 'continuous'), ('produktu', 'product'),
        ('uzlabošanu', 'improvement'), ('nozīmē', 'means'),
        ('jāgaida', 'wait'), ('rezerves', 'spare'),
        ('atbildes', 'answers'), ('biežākajiem', 'most common'),
        ('jautājumiem', 'questions'), ('iegādi', 'purchasing'),
        ('apkalpošanu', 'servicing'), ('izvēli', 'selection'),
        ('kāds', 'what'), ('cik', 'how'),
        ('ilgā', 'long'), ('kādi', 'which'),
        ('kāpēc', 'why'), ('lētāku', 'cheaper'),
        ('alternatīvu', 'alternative'),
        # Single Latvian chars/words with diacritics
        ('ā', 'a'), ('ē', 'e'), ('ī', 'i'), ('ū', 'u'),
        ('š', 's'), ('ģ', 'g'), ('ķ', 'k'), ('ļ', 'l'),
        ('ž', 'z'), ('č', 'c'), ('ņ', 'n'),
        ('Ā', 'A'), ('Ē', 'E'), ('Ī', 'I'), ('Ū', 'U'),
        ('Š', 'S'), ('Ģ', 'G'), ('Ķ', 'K'), ('Ļ', 'L'),
        ('Ž', 'Z'), ('Č', 'C'), ('Ņ', 'N'),
    ]
    for lv, en in sweep:
        text = text.replace(lv, en)
    return text


if __name__ == '__main__':
    print("=" * 50)
    print("Building English version...")
    build_en_homepage()
    build_en_products()
    print("DONE")
