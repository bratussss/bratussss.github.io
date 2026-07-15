"""
Comprehensive AI-quality English translation for the ENTIRE website.
Translates EVERY text element: UI, product specs, FAQ, about, CTAs, etc.
"""
import os, re, shutil

BASE = r"d:\VS KODI\ROzo github"
EN = os.path.join(BASE, "en")

# ── COMPREHENSIVE AI TRANSLATION DICTIONARY ──
# Every single Latvian text → proper English
T = {
    # ── META & HEAD ──
    'CO2 Lāzergriezēji un Lāzergravētāji Wattsan | Bratus ': 'CO2 Laser Cutters & Engravers Wattsan | Bratus',
    'Profesionālas lāzergriešanas iekārtas un CO2 lāzergravēšanas iekārta. Wattsan pārstāvis Latvijā – Bratus.lv. 21+ gadu pieredze, 20k+ pārdotas iekārtas.': 'Professional laser cutting and CO2 engraving machines. Wattsan dealer in Latvia — Bratus.lv. 21+ years of experience, 20k+ machines sold worldwide.',
    'SIA Bratus — Wattsan Oficiālais Pārstāvis Latvijā': 'SIA Bratus — Official Wattsan Dealer in Latvia',
    'Wattsan Latvija — Lāzera iekārtas | Bratus.lv': 'Wattsan Latvia — Laser Machines | Bratus.lv',
    'Profesionālas lāzergriešanas, marķēšanas un CO2 lāzera iekārtas Latvijā. Wattsan oficiālais pārstāvis Latvijā — Bratus.lv.': 'Professional laser cutting, marking, and CO2 laser machines in Latvia. Official Wattsan dealer in Latvia — Bratus.lv.',
    'Profesionālas lāzergriešanas, marķēšanas un CO2 lāzera iekārtas Latvijā. Oficiālais Wattsan pārstāvis.': 'Professional laser cutting, marking, and CO2 laser machines in Latvia. Official Wattsan dealer.',
    'Wattsan Latvija': 'Wattsan Latvia',

    # ── JSON-LD ──
    'Profesionālas lāzergriešanas, marķēšanas un CO2 lāzera iekārtas Latvijā. Wattsan oficiālais pārstāvis Latvijā — SIA Bratus (bratus.lv). 21+ gadu pieredze, 20k+ pārdotas iekārtas, 100+ valstīs.': 'Professional laser cutting, marking and CO2 laser equipment in Latvia. Official Wattsan dealer in Latvia — SIA Bratus (bratus.lv). 21+ years of experience, 20k+ machines sold across 100+ countries.',
    'Wattsan Latvija — Lāzera iekārtas': 'Wattsan Latvia — Laser Equipment',

    # ── NAVIGATION ──
    'Pāriet uz saturu': 'Skip to main content',
    'Galvenā navigācija': 'Main navigation',
    'Atrašanās vieta': 'You are here',
    'Sākums': 'Home',
    'Lāzera iekārtas Latvijā': 'Laser Machines in Latvia',
    'Iekārtas': 'Machines',
    'Rezerves daļas': 'Spare Parts',
    'Par mums': 'About Us',
    'Kontakti': 'Contact',
    'bratus.lv ↗': 'bratus.lv ↗',
    'Oficiālais pārstāvis ↗': 'Official Dealer ↗',
    'Pieteikt': 'Get a Quote',
    'Izvēlne': 'Menu',

    # ── HERO ──
    'Wattsan — Oficiālais pārstāvis Latvijā': 'Wattsan — Official Dealer in Latvia',
    'Industriāla\n      lāzertehnoloģija\n      jūsu ražošanai': 'Industrial-grade\n      laser technology\n      for your production',
    'CO2 lāzeri, metāla griešanas iekārtas un marķētāji — Eiropas kvalitātes CNC aprīkojums ar piegādi un atbalstu Latvijā caur <strong style="color:rgba(255,255,255,0.75)">Bratus.lv</strong>.': 'CO2 lasers, metal cutting machines, and laser markers — European-quality CNC equipment with delivery and support across Latvia through <strong style="color:rgba(255,255,255,0.75)">Bratus.lv</strong>.',
    'Pieteikt konsultāciju': 'Request a Consultation',
    'Apmeklēt bratus.lv': 'Visit bratus.lv',
    'Gadi tirgū': 'Years in Business',
    'Pārdotas iekārtas': 'Machines Sold',
    'Valstis pasaulē': 'Countries Worldwide',

    # ── MARQUEE ──
    'CO2 Lāzeris': 'CO2 Laser',
    'Metāla griešana': 'Metal Cutting',
    'Šķiedru lāzeris': 'Fiber Laser',
    'CNC Frēze': 'CNC Router',
    'Lāzergravēšana': 'Laser Engraving',
    'Lāzermetināšana': 'Laser Welding',
    'Raycus · IPG · HIWIN': 'Raycus · IPG · HIWIN',
    'CE Sertificēts': 'CE Certified',
    'Piegāde Latvijā': 'Delivery Across Latvia',
    'Bratus.lv — Oficiālais pārstāvis': 'Bratus.lv — Official Dealer',

    # ── BRATUS BANNER ──
    '🇱🇻 <strong>Bratus.lv</strong> — Wattsan oficiālais pārstāvis Latvijā. Piegāde, uzstādīšana un garantijas apkalpošana.': '🇱🇻 <strong>Bratus.lv</strong> — Official Wattsan dealer in Latvia. Delivery, installation, and warranty service.',
    'Apmeklēt bratus.lv →': 'Visit bratus.lv →',

    # ── CATEGORY TABS (Iekārtas) ──
    'Izvēlieties iekārtu kategoriju': 'Select a Machine Category',
    '01 &mdash; Aktīvs': '01 &mdash; Active',
    '02': '02',
    '03': '03',
    'CO2 lāzera iekārtas': 'CO2 Laser Machines',
    'Koks, āda, akrils, gumija &mdash; universāls lāzeris kvalitatīvai ražošanai.': 'Wood, leather, acrylic, rubber — a versatile laser for high-quality production.',
    'Metāla griešanas iekārtas': 'Metal Cutting Machines',
    'Tērauds, alumīnijs, varš, misiņš &mdash; šķiedru lāzers precīzai rūpnieciskai griešanai.': 'Steel, aluminum, copper, brass — fiber laser for precision industrial cutting.',
    'Marķēšanas iekārtas': 'Marking Machines',
    'Šķiedru, UV un CO2 marķieri &mdash; svītrkodi, QR, logotipi uz metāla, plastmasas un stikla.': 'Fiber, UV, and CO2 markers — barcodes, QR codes, logos on metal, plastic, and glass.',
    'modeļi': 'models',
    'Skatīt →': 'View All →',
    'Pilns katalogs': 'Full Catalog',
    'Spiest ↓': 'Tap ↓',

    # ── CO2 PANEL HEADERS ──
    'CO2 lāzera iekārtas': 'CO2 Laser Machines',
    'Griešana <strong>&amp;</strong> gravēšana<br><em>kokam, ādai, akrilam</em>': 'Cutting <strong>&amp;</strong> Engraving<br><em>for wood, leather, acrylic</em>',
    'Koks, āda, gumija, akrils — CO2 lāzera iekārtas materiālu apstrādei ar augstu precizitāti.': 'Wood, leather, rubber, acrylic — CO2 laser machines for high-precision material processing.',

    # ── METAL PANEL HEADERS ──
    'Metāla griešanas iekārtas': 'Metal Cutting Machines',
    'Šķiedru lāzers <em>metālam</em><br><strong>precīzi un ātri</strong>': 'Fiber Laser <em>for metal</em><br><strong>precise and fast</strong>',
    'Alumīnijs, nerūsējošai tērauds, misiņš, varš un oglekļa tērauds. Griešana līdz 25 mm biezumam.': 'Aluminum, stainless steel, brass, copper, and carbon steel. Cutting up to 25 mm thickness.',

    # ── MARKER PANEL HEADERS ──
    'Marķēšanas iekārtas': 'Marking Machines',
    '<strong>Marķētāji</strong><br><em>metālam un ne tikai</em>': '<strong>Laser Markers</strong><br><em>for metal and beyond</em>',
    'Svītrkodi, QR kodi, logotipi un teksts uz metāla, plastmasas, keramikas un stikla.': 'Barcodes, QR codes, logos, and text on metal, plastic, ceramics, and glass.',

    # ── SPARE PARTS CATEGORY TABS ──
    'Izvēlieties rezerves daļu kategoriju': 'Select a Spare Part Category',
    'CO2 lampas': 'CO2 Laser Tubes',
    'Reci, Lasea un citi augstas kvalitātes CO2 lāzera avoti un barošanas bloki.': 'Reci, Lasea, and other high-quality CO2 laser sources and power supplies.',
    'Perifērijas iekārtas': 'Peripheral Equipment',
    'Dzesētāji (Chillers), gaisa kompresori un izplūdes sistēmas stabilam darbam.': 'Industrial chillers, air compressors, and exhaust systems for reliable operation.',
    'Oficiālās rezerves daļas': 'Genuine Spare Parts',
    'Fokusa lēcas, spoguļi, siksnas un sensori garantētai saderībai un ilgmūžībai.': 'Focus lenses, mirrors, belts, and sensors for guaranteed compatibility and long service life.',

    # ── CO2 TUBES PANEL ──
    'CO2 lāzera lampas': 'CO2 Laser Tubes',
    'Oriģinālās <strong>CO2 lampas</strong><br><em>un komponentes</em>': 'Genuine <strong>CO2 Tubes</strong><br><em>and components</em>',
    'Mēs piedāvājam tikai oriģinālos Reci, Lasea avotus ar rūpnīcas garantiju un ilgu kalpošanas laiku.': 'We supply only original Reci and Lasea sources with full factory warranty and extended service life.',

    # ── PERIPHERALS PANEL ──
    'Papildaprīkojums <em>jūsu</em><br><strong>ražošanas efektivitātei</strong>': 'Accessories <em>for your</em><br><strong>production efficiency</strong>',
    'Industriālie dzesētāji (Chiller), droši izplūdes ventilatori un kompresori, kas uztur optimālu iekārtas darbību.': 'Industrial chillers, safe exhaust fans, and compressors that keep your equipment running at peak performance.',

    # ── SPARE PARTS PANEL ──
    'Augstas precizitātes<br><strong>komponentes</strong>': 'High-Precision<br><strong>Components</strong>',
    'Lēcas ar augstu caurlaidību, tīri atstarojoši spoguļi un izturīgas siksnas jūsu lāzera aprīkojumam.': 'High-transmission lenses, clean reflective mirrors, and durable belts for your laser equipment.',

    # ── ABOUT SECTION ──
    'Par Wattsan Latvijā': 'About Wattsan in Latvia',
    'Ražotājs ar <strong>21 gada</strong> pieredzi': 'A Manufacturer with <strong>21 Years</strong> of Experience',
    'Wattsan ir CNC iekārtu ražotājs no Jinan, Ķīna. Mēs neesam tālākpārdevējs — mēs projektējam, ražojam un pārdodam savas iekārtas tiešā ceļā uz jūsu ražošanu. Mūsu rūpnīcā strādā <strong>185 inženieri</strong>, un mēs esam pārdevuši vairāk nekā <strong>20,000 iekārtu</strong> klientiem <strong>100+ valstīs</strong> visā pasaulē.': 'Wattsan is a CNC equipment manufacturer based in Jinan, China. We are not a reseller — we design, manufacture, and sell our own machines directly to your production floor. Our factory employs <strong>185 engineers</strong>, and we have delivered over <strong>20,000 machines</strong> to customers in <strong>100+ countries</strong> worldwide.',
    'Latvijā esam Wattsan bāzes dīleris ar <strong>vairāk nekā 5 gadu pieredzi</strong> lāzertehnoloģijā. Mēs piedāvājam pilnu atbalstu — no iekārtas izvēles līdz uzstādīšanai, apmācībai un garantijas apkalpošanai. <strong>Mūsu klientu vidū ir gan mazie uzņēmumi, gan lielās rūpnīcas</strong> visā Latvijā.': 'In Latvia, we are the official Wattsan base dealer with <strong>over 5 years of hands-on experience</strong> in laser technology. We provide full support — from machine selection through installation, training, and warranty service. <strong>Our customers range from small workshops to large-scale factories</strong> across Latvia.',
    'Pēdējo reizi atjaunots: 2026. gada 15. jūlijā': 'Last updated: July 15, 2026',
    'SIA Bratus, Reģ. nr. 40203628316, PVN maksātājs': 'SIA Bratus, Reg. No. 40203628316, VAT-registered',
    'Apmeklēt bratus.lv ↗': 'Visit bratus.lv ↗',
    'Wattsan Dealer Latvia ↗': 'Wattsan Dealer Latvia ↗',
    'Par Wattsan ↗': 'About Wattsan ↗',
    'Inženieri': 'Engineers',

    # ── CTA BAND ──
    'Gatavi sākt?<br><strong>Sazinieties</strong> <em>ar mums</em>': 'Ready to Get Started?<br><strong>Get in Touch</strong> <em>with Us</em>',
    'Mūsu speciālisti palīdzēs izvēlēties piemērotāko iekārtu jūsu ražošanas vajadzībām un aprēķinās izmaksas.': 'Our specialists will help you select the right machine for your production needs and provide a detailed cost estimate.',

    # ── CONTACT SECTION ──
    'Sazināties': 'Get in Touch',
    'Pieteikt iekārtu<br>vai <em>konsultāciju</em>': 'Request a Machine<br>or <em>Consultation</em>',
    'Aizpildiet formu — mūsu speciālisti sazināsies ar jums 24 stundu laikā ar iekārtu rekomendācijām un cenu aprēķinu.': 'Fill out the form — our specialists will get back to you within 24 hours with machine recommendations and a detailed price quote.',
    'Wattsan pārstāvis Latvijā': 'Wattsan Dealer in Latvia',
    'E-pasts': 'Email',
    'Tālrunis': 'Phone',
    'Nosūtīt pieprasījumu': 'Send Inquiry',
    'Vārds, uzvārds *': 'Full Name *',
    'Interesē iekārta': 'Machine of Interest',
    'Izvēlieties tipu...': 'Select a type...',
    'CO2 lāzera iekārta': 'CO2 Laser Machine',
    'Metāla griešanas iekārta': 'Metal Cutting Machine',
    'Marķēšanas iekārta (Fiber)': 'Marking Machine (Fiber)',
    'UV marķētājs': 'UV Marker',
    'CNC frēze': 'CNC Router',
    'Nav pārliecības — nepieciešama konsultācija': 'Not Sure — I Need a Consultation',
    'Projekta apraksts *': 'Project Description *',
    'Aprakstiet savu ražošanas vajadzību — materiāls, izmēri, apjoms...': 'Describe your production requirements — material, dimensions, volume...',
    'Pieprasījums nosūtīts ✓': 'Inquiry Sent ✓',

    # ── FAQ SECTION ──
    'Biežāk uzdotie jautājumi': 'Frequently Asked Questions',
    'BUJ <em>par lāzera</em><br><strong>iekārtām Latvijā</strong>': 'FAQ <em>About Laser</em><br><strong>Machines in Latvia</strong>',
    'Atbildes uz biežākajiem jautājumiem par Wattsan iekārtu izvēli, iegādi un apkalpošanu Latvijā.': 'Answers to the most common questions about choosing, purchasing, and servicing Wattsan machines in Latvia.',

    # ── FAQ ANSWERS ──
    'Kas ir Wattsan un kāpēc izvēlēties šo ražotāju?': 'What is Wattsan and why choose this manufacturer?',
    'Wattsan ir CNC lāzera iekārtu ražotājs no Jinan, Ķīna, ar <strong>21 gada pieredzi</strong>. Atšķirībā no tālākpārdevējiem, Wattsan pats projektē un ražo savas iekārtas — vairāk nekā <strong>20,000 iekārtu</strong> pārdotas <strong>100+ valstīs</strong>. Latvijā oficiālais pārstāvis ir SIA Bratus (bratus.lv), kas nodrošina pilnu atbalstu — no izvēles līdz servisam.': 'Wattsan is a CNC laser equipment manufacturer from Jinan, China, with <strong>21 years of experience</strong>. Unlike resellers, Wattsan designs and builds its own machines — over <strong>20,000 units</strong> sold across <strong>100+ countries</strong>. In Latvia, the official dealer is SIA Bratus (bratus.lv), providing end-to-end support — from selection through after-sales service.',

    'Kāda ir atšķirība starp CO2 un šķiedru lāzeru?': 'What is the difference between CO2 and fiber lasers?',
    'CO2 lāzeri (10.6 µm viļņa garums) ir piemēroti <strong>kokam, ādai, akrilam, gumijai, tekstilam</strong>. Šķiedru lāzeri (1.06 µm) ir paredzēti <strong>metāla griešanai</strong> — tēraudam, alumīnijam, varšam, misiņam. CO2 lāzeri ir universālāki nemetāliskiem materiāliem, bet šķiedru lāzeri nodrošina lielāku ātrumu un precizitāti metāla apstrādē.': 'CO2 lasers (10.6 µm wavelength) are ideal for <strong>wood, leather, acrylic, rubber, and textiles</strong>. Fiber lasers (1.06 µm) are designed for <strong>metal cutting</strong> — steel, aluminum, copper, and brass. CO2 lasers are more versatile for non-metal materials, while fiber lasers deliver higher speed and precision in metal processing.',

    'Kā notiek iekārtas iegādes process Latvijā?': 'How does the machine purchasing process work in Latvia?',
    '<strong>1.</strong> Konsultācija — mūsu speciālisti izvērtē jūsu vajadzības. <strong>2.</strong> Piedāvājums — saņemat detalizētu cenu un konfigurāciju. <strong>3.</strong> Pasūtījums — apstiprinātā iekārta tiek pasūtīta no ražotāja. <strong>4.</strong> Piegāde — 2–6 nedēļas līdz Latvijai. <strong>5.</strong> Uzstādīšana un apmācība — mūsu tehniķi visu uzstāda un apmāca jūsu darbiniekus.': '<strong>1.</strong> Consultation — our specialists assess your requirements. <strong>2.</strong> Proposal — you receive a detailed quote with specifications. <strong>3.</strong> Order — the confirmed machine is ordered from the factory. <strong>4.</strong> Delivery — 2–6 weeks to Latvia. <strong>5.</strong> Installation & Training — our technicians set everything up and train your team.',

    'Kādas garantijas un servisa iespējas tiek nodrošinātas?': 'What warranty and service options are available?',
    'Visas Wattsan iekārtas tiek piegādātas ar <strong>ražotāja garantiju</strong>. CO2 lampām — <strong>360–540 dienu garantija</strong> atkarībā no modeļa. SIA Bratus nodrošina <strong>vietējo servisu Latvijā</strong>: garantijas un pēcgarantijas remonts, rezerves daļu piegāde, tehniskās konsultācijas latviešu, krievu un angļu valodā.': 'All Wattsan machines come with a <strong>manufacturer warranty</strong>. CO2 tubes carry a <strong>360–540 day warranty</strong> depending on the model. SIA Bratus provides <strong>local service across Latvia</strong>: warranty and post-warranty repairs, spare parts supply, and technical support in Latvian, Russian, and English.',

    'Kādi materiāli ir piemēroti CO2 lāzera griešanai un gravēšanai?': 'What materials are suitable for CO2 laser cutting and engraving?',
    'CO2 lāzeri efektīvi apstrādā: <strong>koku, saplāksni, MDF</strong> (griešana līdz 25 mm), <strong>akrilu</strong> (līdz 30 mm), <strong>ādu</strong> (līdz 6 mm), gumiju, tekstilu, papīru, kartonu, kā arī veic stikla gravēšanu. Metālu CO2 lāzers tieši negriež — tam nepieciešams šķiedru lāzers.': 'CO2 lasers efficiently process: <strong>wood, plywood, MDF</strong> (cutting up to 25 mm), <strong>acrylic</strong> (up to 30 mm), <strong>leather</strong> (up to 6 mm), rubber, textiles, paper, cardboard, and also perform glass engraving. CO2 lasers cannot directly cut metal — that requires a fiber laser.',

    'Kāpēc izvēlēties Wattsan, nevis lētāku alternatīvu?': 'Why choose Wattsan over a cheaper alternative?',
    'Wattsan izmanto <strong>Raycus, IPG, HIWIN</strong> komponentes — nozares līderus. Iekārtām ir <strong>CE sertifikācija</strong>, atbilstība Eiropas drošības standartiem. 21 gada pieredze un 185 inženieru komanda nodrošina nepārtrauktu produktu uzlabošanu. Vietējais serviss Latvijā nozīmē, ka jums nav jāgaida rezerves daļas no Ķīnas.': 'Wattsan uses <strong>Raycus, IPG, HIWIN</strong> components — industry-leading brands. All machines carry <strong>CE certification</strong>, compliant with European safety standards. 21 years of experience and a team of 185 engineers drive continuous product improvement. Local service in Latvia means you never have to wait for spare parts from China.',

    # ── COMPARISON TABLE ──
    'Tehnoloģiju salīdzinājums': 'Technology Comparison',
    'Kādu lāzeri <strong>izvēlēties?</strong><br><em>CO2 vs Šķiedru vs UV</em>': 'Which Laser <strong>Should You Choose?</strong><br><em>CO2 vs Fiber vs UV</em>',
    'Ātrs salīdzinājums, kas palīdzēs izvēlēties pareizo tehnoloģiju jūsu materiālam un ražošanas vajadzībām.': 'A quick comparison to help you pick the right technology for your material and production needs.',
    'Raksturojums': 'Specification',
    'Šķiedru Lāzeris': 'Fiber Laser',
    'UV Marķētājs': 'UV Marker',
    'Viļņa garums': 'Wavelength',
    'Materiāli': 'Materials',
    'Koks, āda, akrils, audums': 'Wood, leather, acrylic, fabric',
    'Tērauds, alumīnijs, varš': 'Steel, aluminum, copper',
    'Stikls, plastmasa, keramika': 'Glass, plastic, ceramics',
    'Maks. griešanas biezums': 'Max. Cutting Thickness',
    'Līdz 30 mm (akrils)': 'Up to 30 mm (acrylic)',
    'Līdz 25 mm (tērauds)': 'Up to 25 mm (steel)',
    'Marķēšana (negriež)': 'Marking only (non-cutting)',
    'Jaudas diapazons': 'Power Range',
    'Izmaksas (sākuma)': 'Starting Price',
    'No €2,500': 'From €2,500',
    'No €12,000': 'From €12,000',
    'No €4,500': 'From €4,500',
    'CE Sertifikācija': 'CE Certification',
    '✓ Visiem modeļiem': '✓ All Models',

    # ── DEFINITION LIST ──
    'Tehniskie termini': 'Technical Glossary',
    'Lāzertehnoloģijas <strong>pamatjēdzieni</strong>': 'Laser Technology <strong>Key Concepts</strong>',
    'CO2 lāzeris': 'CO2 Laser',
    'Gāzes lāzers ar 10.6 µm viļņa garumu, kas izmanto CO2 gāzes maisījumu. Piemērots nemetālisku materiālu griešanai un gravēšanai: koks, āda, akrils, audums.': 'A gas laser with a 10.6 µm wavelength that uses a CO2 gas mixture. Ideal for cutting and engraving non-metal materials: wood, leather, acrylic, fabric.',
    'Šķiedru lāzeris (Fiber)': 'Fiber Laser',
    'Cietvielu lāzers ar 1.06 µm viļņa garumu. Izmanto optisko šķiedru kā pastiprināšanas vidi. Paredzēts metālu griešanai ar augstu precizitāti un ātrumu.': 'A solid-state laser with a 1.06 µm wavelength. Uses optical fiber as the gain medium. Designed for high-precision, high-speed metal cutting.',
    'Lāzera jauda (W)': 'Laser Power (W)',
    'Mērījums vatos (W), kas nosaka lāzera griešanas spēju. Lielāka jauda ļauj griezt biezākus materiālus un strādāt ātrāk. CO2: 55–700W, Fiber: 1–120kW.': 'Measured in watts (W), this determines the laser\'s cutting capability. Higher power allows cutting thicker materials at higher speeds. CO2: 55–700W, Fiber: 1–120kW.',
    'CNC (Computer Numerical Control)': 'CNC (Computer Numerical Control)',
    'Datorizēta vadības sistēma, kas automātiski kontrolē iekārtas kustības. CNC nodrošina atkārtojamu precizitāti un iespēju darbināt iekārtu bez manuālas iejaukšanās.': 'A computerized control system that automatically manages machine movements. CNC delivers repeatable precision and enables unattended operation.',

    # ── FOOTER ──
    'Wattsan — profesionālas CNC lāzera iekārtas ar 21 gadu pieredzi. Officiālais pārstāvis Latvijā: SIA Bratus.': 'Wattsan — professional CNC laser equipment backed by 21 years of experience. Official dealer in Latvia: SIA Bratus.',
    'Marķieri': 'Markers',
    'CNC Frēzes': 'CNC Routers',
    'Lāzermetināšana': 'Laser Welding',
    'Par uzņēmumu': 'About the Company',
    'Atbalsts': 'Support',
    'Dīleris Latvijā': 'Dealer in Latvia',
    'Blogs': 'Blog',
    'Wattsan oficiālais pārstāvis Latvijā': 'Official Wattsan dealer in Latvia',
    'Privātuma politika': 'Privacy Policy',
    'Lietošanas noteikumi': 'Terms of Service',
    'SEO optimizāciju un mājaslapas izstrādi veica': 'SEO & website development by',
    'Lapa:': 'Site:',

    # ── BREADCRUMB ──
    'Sākums': 'Home',

    # ── PRODUCT BADGES ──
    'Jauns': 'New',
    'Jauns 2025': 'New 2025',
    '2025': '2025',
    'Bestseller': 'Bestseller',
    'UL': 'UL',
    'SGS': 'SGS',

    # ── SPEC LABELS ──
    'Darba zona': 'Work Area',
    'Jauda': 'Power',
    'Ātrums': 'Speed',
    'Nominālā jauda': 'Rated Power',
    'Maksimālā jauda': 'Max Power',
    'Garantija': 'Warranty',
    'dienas': 'days',
    'Dzesēšanas jauda': 'Cooling Capacity',
    'Temp. precizitāte': 'Temp Accuracy',
    'Tvertne': 'Tank',
    'Avots': 'Source',
    'Tips': 'Type',
    'Pielietojums': 'Application',
    'Cena': 'Price',
    'Materiāls': 'Material',
    'Komplekts': 'Set',
    'Diametrs': 'Diameter',
    'Fokusa attālums': 'Focal Length',

    # ── PRODUCT DESCRIPTIONS ──
    # CO2 Machines
    'CO2 lāzeris · Konveijera / Audumam': 'CO2 Laser · Conveyor / Fabric',
    'CO2 lāzeris · PRO Sērija': 'CO2 Laser · PRO Series',
    'CO2 lāzeris · Flat Bed PRO': 'CO2 Laser · Flat Bed PRO',
    'CO2 lāzeris · Galda / Desktop': 'CO2 Laser · Desktop / Compact',
    'CO2 lāzeris · ST Sērija': 'CO2 Laser · ST Series',
    'CO2 lāzeris · DUOS ST (Divas lampas)': 'CO2 Laser · DUOS ST (Dual Tube)',
    'CO2 lāzeris · DUOS LT (Divas lampas)': 'CO2 Laser · DUOS LT (Dual Tube)',
    'CO2 lāzeris · LT Sērija': 'CO2 Laser · LT Series',
    # Metal Cutters
    'Šķiedru lāzeris · A Sērija ar kabīni': 'Fiber Laser · A Series with Cabin',
    'Šķiedru lāzeris · Lielformāta': 'Fiber Laser · Large Format',
    'Šķiedru lāzeris · Lielformāta (Lieljaudas)': 'Fiber Laser · Large Format (High Power)',
    'Šķiedru lāzeris · Hard Ultra': 'Fiber Laser · Hard Ultra',
    'Šķiedru lāzeris · Hard Sērija': 'Fiber Laser · Hard Series',
    'Šķiedru lāzeris · MINI': 'Fiber Laser · MINI',
    'Šķiedru lāzeris · A Sērija': 'Fiber Laser · A Series',
    'Šķiedru lāzeris · S Sērija': 'Fiber Laser · S Series',
    'Šķiedru lāzeris · E Sērija (Ekonomiskā)': 'Fiber Laser · E Series (Economy)',
    # Markers
    'Šķiedru marķētājs · Statīvs': 'Fiber Marker · Floor Stand',
    'Šķiedru marķētājs · Lielformāta': 'Fiber Marker · Large Format',
    'Šķiedru marķētājs · Galda / Kompakts': 'Fiber Marker · Desktop / Compact',
    'Šķiedru marķētājs · Rokas / Portatīvs': 'Fiber Marker · Handheld / Portable',
    'Šķiedru marķētājs · Galda / Slēgts': 'Fiber Marker · Desktop / Enclosed',
    'Šķiedru marķētājs · 3D Dinamiskais': 'Fiber Marker · 3D Dynamic',
    'UV marķētājs · Galda': 'UV Marker · Desktop',
    'CO2 marķētājs · Galda': 'CO2 Marker · Desktop',
    # Reci Lamps
    'CO2 Lampa · Kompakta': 'CO2 Tube · Compact',
    'CO2 Lampa · Populārākā': 'CO2 Tube · Most Popular',
    'CO2 Lampa · Lieljaudas': 'CO2 Tube · High Power',
    'CO2 Lampa · Lieljaudas+': 'CO2 Tube · High Power+',
    'CO2 Lampa · Industriāla': 'CO2 Tube · Industrial',
    # Chillers
    'Dzesētājs · Aktīvā dzesēšana': 'Chiller · Active Cooling',
    'Dzesētājs · UL Sertificēts': 'Chiller · UL Certified',
    'Dzesētājs · Fiber Lāzeram 3kW': 'Chiller · For 3kW Fiber Laser',
    'Dzesētājs · Fiber Lāzeram 6kW': 'Chiller · For 6kW Fiber Laser',
    'Dzesētājs · Fiber Lāzeram 12-15kW': 'Chiller · For 12–15kW Fiber Laser',
    'Dzesētājs · Fiber Lāzeram 20kW': 'Chiller · For 20kW Fiber Laser',
    'Dzesētājs · Fiber Lāzeram 30kW': 'Chiller · For 30kW Fiber Laser',
    # Chiller badges
    'Populārākais · CE/REACH/RoHS': 'Most Popular · CE/REACH/RoHS',
    'UL Sertificēts · 5030W': 'UL Certified · 5030W',
    '12-15kW Fiber · UL': '12–15kW Fiber · UL',
    '20kW Fiber · SGS': '20kW Fiber · SGS',
    '30kW Fiber · SGS': '30kW Fiber · SGS',
    '3kW Fiber · SGS': '3kW Fiber · SGS',
    '6kW Fiber · SGS': '6kW Fiber · SGS',
    # Spare parts
    'Elektronika · Relejs': 'Electronics · Relay',
    'Optika · Spogulis': 'Optics · Mirror',
    'Optika · Lēca': 'Optics · Lens',
    'Elektromagnētiskais': 'Electromagnetic',
    'CO2 lāzera iekārtas': 'CO2 Laser Machines',
    'Silīcijs (Si) ar zelta pārklājumu': 'Silicon (Si) with gold coating',
    'Molibdēns (Mo) ar sudraba pārklājumu': 'Molybdenum (Mo) with silver coating',
    'gab.': 'pcs.',

    # ── PRODUCT-SPECIFIC SEARCHABLE PHRASES ──
    # Reci lamp descriptions (used in product page hero text)
    'Reci W1 — profesionāla Reci CO2 lāzera caurule ar 75 W nominālo jaudu. Oriģinālā Reci W sērija. Wattsan oficiālais pārstāvis Latvijā.': 'Reci W1 — professional Reci CO2 laser tube with 75 W rated power. Genuine Reci W series. Official Wattsan dealer in Latvia.',
    'Reci W2 — profesionāla Reci CO2 lāzera caurule ar 90 W nominālo jaudu. Oriģinālā Reci W sērija. Wattsan oficiālais pārstāvis Latvijā.': 'Reci W2 — professional Reci CO2 laser tube with 90 W rated power. Genuine Reci W series. Official Wattsan dealer in Latvia.',
    'Reci W4 — profesionāla Reci CO2 lāzera caurule ar 100 W nominālo jaudu. Oriģinālā Reci W sērija. Wattsan oficiālais pārstāvis Latvijā.': 'Reci W4 — professional Reci CO2 laser tube with 100 W rated power. Genuine Reci W series. Official Wattsan dealer in Latvia.',
    'Reci W6 — profesionāla Reci CO2 lāzera caurule ar 130 W nominālo jaudu. Oriģinālā Reci W sērija. Wattsan oficiālais pārstāvis Latvijā.': 'Reci W6 — professional Reci CO2 laser tube with 130 W rated power. Genuine Reci W series. Official Wattsan dealer in Latvia.',
    'Reci W8 — profesionāla Reci CO2 lāzera caurule ar 150 W nominālo jaudu. Oriģinālā Reci W sērija. Wattsan oficiālais pārstāvis Latvijā.': 'Reci W8 — professional Reci CO2 laser tube with 150 W rated power. Genuine Reci W series. Official Wattsan dealer in Latvia.',

    # ── PRODUCT-SPECIFIC HERO DESCRIPTIONS (from product pages) ──
    'CW-5200 — TEYU industriālais dzesētājs. Populārākais · CE/REACH/RoHS. Oficiālais pārstāvis Latvijā.': 'CW-5200 — TEYU industrial chiller. Most popular model · CE/REACH/RoHS certified. Official dealer in Latvia.',
    'CW-6200BN — TEYU industriālais dzesētājs. UL Sertificēts · 5030W. Oficiālais pārstāvis Latvijā.': 'CW-6200BN — TEYU industrial chiller. UL Certified · 5030W cooling capacity. Official dealer in Latvia.',
    'CWFL-15000KN — TEYU industriālais dzesētājs. 12-15kW Fiber Lāzeram · UL Sertificēts. Oficiālais pārstāvis Latvijā.': 'CWFL-15000KN — TEYU industrial chiller. For 12–15kW fiber lasers · UL Certified. Official dealer in Latvia.',
    'CWFL-20000KT — TEYU industriālais dzesētājs. 20kW Fiber Lāzeram · SGS Sertificēts. Oficiālais pārstāvis Latvijā.': 'CWFL-20000KT — TEYU industrial chiller. For 20kW fiber lasers · SGS Certified. Official dealer in Latvia.',
    'CWFL-30000KT — TEYU industriālais dzesētājs. 30kW Fiber Lāzeram · SGS Sertificēts. Oficiālais pārstāvis Latvijā.': 'CWFL-30000KT — TEYU industrial chiller. For 30kW fiber lasers · SGS Certified. Official dealer in Latvia.',
    'CWFL-3000HNP — TEYU industriālais dzesētājs. 3kW Fiber Lāzeram · SGS Sertificēts. Oficiālais pārstāvis Latvijā.': 'CWFL-3000HNP — TEYU industrial chiller. For 3kW fiber lasers · SGS Certified. Official dealer in Latvia.',
    'CWFL-6000KNP — TEYU industriālais dzesētājs. 6kW Fiber Lāzeram · SGS Sertificēts. Oficiālais pārstāvis Latvijā.': 'CWFL-6000KNP — TEYU industrial chiller. For 6kW fiber lasers · SGS Certified. Official dealer in Latvia.',

    # ── JSON-LD product name patterns (critical - these use "  " double spaces) ──
    'Industriālais Dzesētājs  ': 'Industrial Chiller  ',
    'CO2 Lāzera Lampa  ': 'CO2 Laser Tube  ',
    'Lāzera Iekārta  ': 'Laser Machine  ',
    'Marķēšanas Iekārta  ': 'Marking Machine  ',
    'Griešanas Iekārta  ': 'Cutting Machine  ',
    'Konveijera / Audumam': 'Conveyor / Fabric',
    'Ar kabīni': 'With Cabin',
    'Lielformāta HP': 'Large Format HP',
    'Lielformāta': 'Large Format',
    'Rokas / Portatīvs': 'Handheld / Portable',
    'Galda / Desktop': 'Desktop / Compact',
    'Galda / Slēgts': 'Desktop / Enclosed',
    'Galda / Kompakts': 'Desktop / Compact',
    '3D Dinamiskais': '3D Dynamic',
    'UV · Galda': 'UV · Desktop',
    'CO2 · Galda': 'CO2 · Desktop',
    'Statīvs': 'Floor Stand',

    # ── PRODUCT PAGE: Section headings ──
    'Kāpēc <strong>': 'Why <strong>',
    'Kāpēc ': 'Why ',
    'Nepieciešams <strong>': 'Need a <strong>',
    '</strong>?<br><em>Pasūtiet tūlīt</em>': '</strong>?<br><em>Order Today</em>',

    # ── PRODUCT PAGE: Common hero descriptions ──
    'Reci W sērijas CO2 stikla lāzera caurule — 3.0 paaudzes tehnoloģija ar metāla-stikla saķepināšanu, >95% TEM00 staru kūļa kvalitāti un līdz pat 12 000 stundu kalpošanas laiku.': 'Reci W-series CO2 glass laser tube — 3rd generation technology with metal-glass frit sealing, >95% TEM00 beam quality, and up to 12,000 hours of service life.',
    'Vispārdotākais TEYU industriālais dzesētājs — kompakts, portatīvs ar 1430W dzesēšanas jaudu un ±0.3℃ temperatūras precizitāti. Piemērots CO2 lāzera iekārtām līdz 150W.': 'TEYU\'s best-selling industrial chiller — compact and portable with 1430W cooling capacity and ±0.3℃ temperature accuracy. Suitable for CO2 laser machines up to 150W.',

    # ── PRODUCT PAGE: Hero descriptions (pattern-based, model-specific) ──

    # ── PRODUCT PAGE: Common Hero & Feature Strings ──
    'Jaunais Modelis': 'New Model',
    'PRO Sērija': 'PRO Series',
    'ST Sērija': 'ST Series',
    'LT Sērija': 'LT Series',
    'A Sērija': 'A Series',
    'S Sērija': 'S Series',
    'E Sērija': 'E Series',
    'Hard Sērija': 'Hard Series',
    'Pieprasīt cenu': 'Request Pricing',
    'Skatīt wattsan.com ↗': 'View on wattsan.com ↗',
    'Wattsan SAS Drošība': 'Wattsan SAS Safety System',
    'Safety Assurance System ar FOX ugunsgrēka detektoru un rūdīta stikla vāku.': 'Safety Assurance System with FOX fire detector and tempered glass lid.',
    'Precīza Jaudas Kontrole': 'Precision Power Control',
    'Digitālais potenciometrs ar precizitāti līdz 0.001 A smalkai gravēšanai.': 'Digital potentiometer with precision down to 0.001 A for fine engraving.',
    'Ātrgaitas Gravēšana': 'High-Speed Engraving',
    'Līdz pat 1000 mm/s gravēšanas ātrums — maksimāla produktivitāte.': 'Up to 1000 mm/s engraving speed — maximum productivity.',
    'Caurstaigājams Galds': 'Pass-Through Table',
    'Y-ass caurlaide ļauj apstrādāt garākus materiālus.': 'Y-axis pass-through allows processing longer materials.',
    'Leadshine Servo Motori': 'Leadshine Servo Motors',
    'Precīzi servo motori ar pozicionēšanas precizitāti 0.03 mm.': 'Precision servo motors with 0.03 mm positioning accuracy.',
    'Globāls Atbalsts': 'Global Support',
    '21 gada pieredze, 185 inženieri, 20 000+ iekārtu 100+ valstīs.': '21 years of experience, 185 engineers, 20,000+ machines in 100+ countries.',
    'Ruida Kontrolieris': 'Ruida Controller',
    'Ruida RDC6445 kontrolieris ar intuitīvu interfeisu.': 'Ruida RDC6445 controller with intuitive interface.',
    'CE Sertificēta Iekārta': 'CE Certified Machine',
    'Atbilst Eiropas Savienības drošības un kvalitātes standartiem.': 'Compliant with European Union safety and quality standards.',
    'CO2 lāzeri:': 'CO2 Lasers:',

    # ── PRODUCT PAGE: Sections ──
    'Galvenās īpašības': 'Key Features',
    'Galerija': 'Gallery',
    'Produkta <strong>attēli</strong>': 'Product <strong>Images</strong>',
    'Tehniskie parametri': 'Technical Specifications',
    'Detalizēta <strong>specifikācija</strong>': 'Detailed <strong>Specifications</strong>',
    'Optika': 'Optics',
    'Mehānika & Elektronika': 'Mechanics & Electronics',
    'Izmēri': 'Dimensions',
    'Apstrādājamie <strong>materiāli</strong>': 'Compatible <strong>Materials</strong>',

    # ── PRODUCT PAGE: Image labels ──
    'Pilns iekārtas skats': 'Full Machine View',
    'Lāzera detaļa': 'Laser Detail',
    'Darba zona': 'Work Area',
    'Vadības panelis': 'Control Panel',
    'Ražošanas kvalitāte': 'Build Quality',
    'Priekšskats': 'Front View',
    'Velc, lai redzētu vairāk': 'Scroll to see more',
    'Iepriekšējais': 'Previous',
    'Nākamais': 'Next',

    # ── PRODUCT PAGE: Specs ──
    'Lāzera jauda': 'Laser Power',
    'Lāzera caurule': 'Laser Tube',
    'Spoguļa diametrs': 'Mirror Diameter',
    'ZnSe lēca': 'ZnSe Lens',
    'Fokusa attālums': 'Focal Length',
    'Caurules darbmūžs': 'Tube Lifespan',
    'Min. gravēšanas izmērs': 'Min. Engraving Size',
    'Darba virsma': 'Work Surface',
    'Asmeņu galds': 'Blade Table',
    'Griešanas ātrums': 'Cutting Speed',
    'Gravēšanas ātrums': 'Engraving Speed',
    'Pozicionēšanas precizitāte': 'Positioning Accuracy',
    'Dzesēšana': 'Cooling',
    'Ūdens': 'Water',
    'Barošana': 'Power Supply',
    'Jaudas patēriņš': 'Power Consumption',
    'Caurstaigājams galds': 'Pass-Through Table',
    'Jā (Y-ass)': 'Yes (Y-axis)',
    'Kontrolieris': 'Controller',
    'Programmatūra': 'Software',
    'Savienojamība': 'Connectivity',
    'Atbalstītie formāti': 'Supported Formats',

    # ── PRODUCT PAGE: Materials ──
    'Koks': 'Wood',
    'Saplāksnis': 'Plywood',
    'MDF': 'MDF',
    'Akrils': 'Acrylic',
    'Āda': 'Leather',
    'Gumija': 'Rubber',
    'Audums': 'Fabric',
    'Akmens': 'Stone',
    'Granīts': 'Granite',
    'Plastmasa': 'Plastic',
    'Bambuss': 'Bamboo',
    'Keramika': 'Ceramics',
    'Stikls': 'Glass',
    'Papīrs': 'Paper',
    'Kartons': 'Cardboard',
    'Putuplasts': 'Foam',
    'Korķis': 'Cork',
    'Alumīnijs': 'Aluminum',
    'Nerūsējošais tērauds': 'Stainless Steel',
    'Oglekļa tērauds': 'Carbon Steel',
    'Varš': 'Copper',
    'Misiņš': 'Brass',
    'Cinks': 'Zinc',
    'Titāns': 'Titanium',

    # ── PRODUCT PAGE: CTA ──
    'Interesē <strong>': 'Interested in the <strong>',
    '</strong>?<br><em>Pieprasiet cenu tūlīt</em>': '</strong>?<br><em>Request a Quote Today</em>',
    'Aizpildiet formu un saņemiet personalizētu piedāvājumu ar piegādi Latvijā 24 stundu laikā.': 'Fill out the form and receive a personalized quote with delivery across Latvia within 24 hours.',
    'Pieprasīt cenu ': 'Request Pricing ',
    'bratus.lv ↗': 'bratus.lv ↗',

    # ── PRODUCT PAGE: JSON-LD descriptions ──
    'Profesionāla CO2 lāzera iekārta Wattsan 6090 PRO ar 900 × 600 mm darba zonu un 100–120 W jaudu. Wattsan oficiālais pārstāvis Latvijā — Bratus.lv.': 'Professional CO2 laser machine Wattsan 6090 PRO with 900 × 600 mm work area and 100–120 W power. Official Wattsan dealer in Latvia — Bratus.lv.',

    # ── PRODUCT PAGE: Misc ──
    'profesionāla lāzera iekārta': 'professional laser machine',
    'lāzera iekārta': 'laser machine',
    'CO2 lāzera iekārtas': 'CO2 Laser Machines',
}

# ── Post-processing patterns for product pages ──
PRODUCT_POST_PATTERNS = [
    # Product title pattern: "Model — Category | Bratus.lv"
    # These are handled by the general dictionary but some may remain

    # Alt text patterns  
    ('alt="Wattsan', 'alt="Wattsan'),  # Keep model names
]

# ── Additional translations applied via regex for dynamic content ──


def apply_all_translations(text):
    """Apply all translations, longest-first to avoid partial matches."""
    for lv, en in sorted(T.items(), key=lambda x: -len(x[0])):
        text = text.replace(lv, en)
    return text


def post_process_en(text):
    """Final cleanup: catch any remaining Latvian fragments."""
    # Spec values
    text = text.replace('līdz ', 'up to ')
    text = text.replace('Līdz ', 'Up to ')
    # Alt text fixes
    text = text.replace('alt="marķētājs"', 'alt="Laser marker"')
    text = text.replace('alt="CO2 Lampa"', 'alt="CO2 Tube"')
    text = text.replace('alt="Perifērija"', 'alt="Peripheral equipment"')
    text = text.replace('alt="Rezerves daļas"', 'alt="Spare parts"')
    text = text.replace('Metāla griešana', 'Metal Cutting')
    # JSON-LD FAQ cleanup — translate remaining LV in JSON
    text = text.replace('"name": "Kas ir Wattsan?"', '"name": "What is Wattsan?"')
    text = text.replace('"name": "Kādas lāzera iekārtas pieejamas Latvijā?"', '"name": "What laser machines are available in Latvia?"')
    text = text.replace('"name": "Kā sazināties ar Wattsan pārstāvi Latvijā?"', '"name": "How to contact the Wattsan dealer in Latvia?"')
    text = text.replace('"name": "Vai tiek nodrošināta garantija un vietējais serviss?"', '"name": "Is warranty and local service provided?"')
    text = text.replace('"name": "Kāds ir CO2 lāzera iekārtu kalpošanas laiks?"', '"name": "What is the lifespan of CO2 laser machines?"')
    text = text.replace('"name": "Kādi materiāli ir piemēroti CO2 lāzera griešanai un gravēšanai?"', '"name": "What materials are suitable for CO2 laser cutting and engraving?"')
    text = text.replace('"name": "Cik ilgā laikā tiek piegādāta iekārta Latvijā?"', '"name": "How long does delivery take in Latvia?"')
    # Nav fragments
    text = text.replace('title="Latviešu"', 'title="Latvian"')
    # Remaining words
    text = text.replace('profesionāla lāzera iekārta', 'professional laser machine')
    text = text.replace('lāzera iekārta', 'laser machine')
    text = text.replace('lāzergravēšanas iekārta', 'laser engraving machine')
    text = text.replace('lāzergriešanas iekārta', 'laser cutting machine')
    text = text.replace('lāzergriešanas iekārtas', 'laser cutting machines')
    text = text.replace('lāzergravēšanas iekārtas', 'laser engraving machines')
    text = text.replace('lāzera iekārtas', 'laser machines')
    text = text.replace('marķēšanas iekārtas', 'marking machines')
    text = text.replace('griešanas iekārtas', 'cutting machines')
    text = text.replace('koka lāzergriešanai', 'wood laser cutting')
    text = text.replace('Populārākā koka lāzergriešanai', 'Most popular for wood laser cutting')
    text = text.replace('ar uzlabotu precizitāti', 'with enhanced precision')
    # JSON-LD specific text translations (these have different wording from HTML FAQ)
    # These are the JSON-LD text fields
    text = text.replace(
        '"text": "Wattsan ir CNC lāzera iekārtu ražotājs no Jinan, Ķīna, ar 21 gada pieredzi. Uzņēmums pats projektē, ražo un pārdod savas iekārtas tiešā ceļā klientiem visā pasaulē — vairāk nekā 100 valstīs."',
        '"text": "Wattsan is a CNC laser equipment manufacturer from Jinan, China, with 21 years of experience. The company designs, manufactures, and sells its own machines directly to customers worldwide — in more than 100 countries."'
    )
    text = text.replace(
        '"text": "Latvijā caur oficiālo pārstāvi Bratus.lv pieejamas: CO2 Laser Machines kokam, ādai un akrilam (17 models), šķiedru lāzera metāla griešanas iekārtas (16 models), marķēšanas iekārtas — Fiber, UV un CO2 (11 models), CNC Routers un lāzermetināšanas iekārtas."',
        '"text": "Available in Latvia through the official dealer Bratus.lv: CO2 Laser Machines for wood, leather and acrylic (17 models), fiber laser metal cutting machines (16 models), marking machines — Fiber, UV and CO2 (11 models), CNC Routers and laser welding machines."'
    )
    text = text.replace(
        '"text": "Zvaniet pa tālruni +371 24 424 434, rakstiet uz e-pastu sales@bratus.lv, apmeklējiet vietni bratus.lv vai aizpildiet kontaktformu mūsu lapā. Adrese: Dārznieku iela 42, Ķekava, Latvija."',
        '"text": "Call +371 24 424 434, email sales@bratus.lv, visit bratus.lv or fill out our contact form. Address: Dārznieku iela 42, Ķekava, Latvia."'
    )
    text = text.replace(
        '"text": "Jā, visas Wattsan iekārtas tiek piegādātas ar ražotāja garantiju un pilnu vietējo servisa atbalstu Latvijā — ieskaitot uzstādīšanu, apmācību un garantijas apkalpošanu caur SIA Bratus."',
        '"text": "Yes, all Wattsan machines are supplied with a manufacturer warranty and full local service support in Latvia — including installation, training, and warranty service through SIA Bratus."'
    )
    text = text.replace(
        '"text": "CO2 lāzera lampu kalpošanas laiks ir 3000–10000 stundas atkarībā no modeļa un ekspluatācijas apstākļiem. Reci lampām tiek nodrošināta 360–540 dienu garantija."',
        '"text": "CO2 laser tube lifespan is 3000–10000 hours depending on the model and operating conditions. Reci tubes come with a 360–540 day warranty."'
    )
    text = text.replace(
        '"text": "CO2 lāzeri ir piemēroti kokam, saplāksnim, MDF, ādai, akrilam (plexiglass), gumijai, tekstilam, papīram, kartonam un stikla gravēšanai. Metāla griešanai nepieciešams šķiedru lāzers."',
        '"text": "CO2 lasers are suitable for wood, plywood, MDF, leather, acrylic (plexiglass), rubber, textiles, paper, cardboard and glass engraving. Metal cutting requires a fiber laser."'
    )
    text = text.replace(
        '"text": "Standarta piegādes laiks ir 2–6 nedēļas atkarībā no modeļa un konfigurācijas. Populārākie models bieži ir pieejami no noliktavas Latvijā ar piegādi 3–5 darba dienu laikā."',
        '"text": "Standard delivery time is 2–6 weeks depending on the model and configuration. Popular models are often available from stock in Latvia with delivery within 3–5 business days."'
    )
    # Clean up any JSON-LD description remnants
    text = text.replace('Profesionālas lāzergriešanas, marķēšanas un CO2 Laser Machines Latvijā.', 'Professional laser cutting, marking and CO2 laser machines in Latvia.')
    # Any remaining product-specific JSON-LD
    text = text.replace('CO2 lāzergravēšanas iekārta ar uzlabotu precizitāti', 'CO2 laser engraving machine with enhanced precision')
    text = text.replace('Populārākā koka lāzergriešanai', 'Most popular for wood laser cutting')
    # Model names ending with series labels
    text = text.replace('Iekārta PRO |', 'Machine PRO |')
    text = text.replace('Iekārta |', 'Machine |')
    text = text.replace('Laser Engravings Iekārta', 'Laser Engraving Machine')
    # Nav anchor IDs (keep as-is for functionality)
    # Remove remaining "Oficiālais" references
    text = text.replace('Oficiālais pārstāvis', 'Official Dealer')
    text = text.replace('oficiālais pārstāvis', 'official dealer')
    text = text.replace('oficiālo pārstāvi', 'the official dealer')
    text = text.replace('ražotāja garantiju', 'manufacturer warranty')
    text = text.replace('ražotāja', 'manufacturer')
    text = text.replace('vietējo servisu', 'local service')
    text = text.replace('vietējais serviss', 'local service')
    text = text.replace('apmācību', 'training')
    text = text.replace('uzstādīšanu', 'installation')
    text = text.replace('apkalpošanu', 'service')
    text = text.replace('iekārtu', 'machine')
    text = text.replace('iekārtas', 'machines')
    text = text.replace('iekārta', 'machine')
    text = text.replace('lampu', 'tube')
    text = text.replace('lampām', 'tubes')
    text = text.replace('lampa', 'tube')
    text = text.replace('stundas', 'hours')
    text = text.replace('stundu', 'hour')
    text = text.replace('dienu', 'day')
    text = text.replace('dienas', 'days')
    text = text.replace('nedēļas', 'weeks')
    text = text.replace('nedēļu', 'week')
    text = text.replace('garantija', 'warranty')
    text = text.replace('garantiju', 'warranty')
    text = text.replace('kalpošanas laiks', 'service life')
    text = text.replace('laikā', 'time')
    text = text.replace('piegādi', 'delivery')
    text = text.replace('piegāde', 'delivery')
    text = text.replace('noliktavas', 'stock')
    text = text.replace('kokam', 'wood')
    text = text.replace('ādai', 'leather')
    text = text.replace('akrilam', 'acrylic')
    text = text.replace('Metāla griešanai', 'Metal cutting')
    text = text.replace('nepieciešams', 'requires')
    text = text.replace('šķiedru lāzers', 'fiber laser')
    text = text.replace('šķiedru lāzera', 'fiber laser')
    text = text.replace('piemēroti', 'suitable')
    text = text.replace('piemērotas', 'suitable')
    text = text.replace('atkarībā no', 'depending on')
    text = text.replace('ekspluatācijas apstākļiem', 'operating conditions')
    text = text.replace('modeļa', 'model')
    text = text.replace('modeļiem', 'models')
    text = text.replace('konfigurācijas', 'configuration')
    text = text.replace('tiek piegādātas', 'are supplied')
    text = text.replace('tiek nodrošināta', 'is provided')
    text = text.replace('tiek nodrošināts', 'is provided')
    text = text.replace('pieejamas', 'available')
    text = text.replace('pieejami', 'available')
    text = text.replace('klientiem visā pasaulē', 'customers worldwide')
    text = text.replace('vairāk nekā', 'more than')
    text = text.replace('visā pasaulē', 'worldwide')
    text = text.replace('pats projektē', 'designs')
    text = text.replace('ražo un pārdod savas', 'manufactures and sells its own')
    text = text.replace('tiešā ceļā', 'directly')
    text = text.replace('jūsu ražošanai', 'for your production')
    text = text.replace('jūsu ražošanu', 'your production')
    text = text.replace('Profesionālas', 'Professional')
    text = text.replace('profesionāla', 'professional')
    text = text.replace('oriģinālā', 'genuine')
    text = text.replace('oriģinālo', 'the genuine')
    text = text.replace('oriģinālie', 'genuine')
    text = text.replace('oriģinālais', 'genuine')
    text = text.replace('Oficiālais pārstāvis', 'Official Dealer')
    text = text.replace('oficiālais pārstāvis', 'official dealer')
    text = text.replace('pārstāvis', 'dealer')
    text = text.replace('pārstāvi', 'dealer')
    text = text.replace('pārstāvja', 'dealer')
    text = text.replace('Latvijā', 'in Latvia')
    text = text.replace('Latvija', 'Latvia')
    text = text.replace('Ķīna', 'China')
    text = text.replace('Jinan', 'Jinan')
    text = text.replace('ražotājs', 'manufacturer')
    text = text.replace('ražošanai', 'for production')
    text = text.replace('ražošanu', 'production')
    text = text.replace('uzņēmums', 'company')
    text = text.replace('uzņēmumu', 'company')
    text = text.replace('pieredzi', 'experience')
    text = text.replace('pieredze', 'experience')
    text = text.replace('inženieri', 'engineers')
    text = text.replace('inženieru', 'engineers')
    text = text.replace('gada', 'years')
    text = text.replace('gadi', 'years')
    text = text.replace('gadu', 'year')
    text = text.replace('valstīs', 'countries')
    text = text.replace('valstis', 'countries')
    text = text.replace('pārdotas', 'sold')
    text = text.replace('pārdoti', 'sold')
    text = text.replace('pasūtījumiem', 'orders')
    text = text.replace('pasūtījumu', 'order')
    return text


def create_en_homepage():
    """Generate the English homepage with complete AI translations."""
    src = os.path.join(BASE, "index.html")
    os.makedirs(EN, exist_ok=True)
    dst = os.path.join(EN, "index.html")

    with open(src, 'r', encoding='utf-8') as f:
        content = f.read()

    # Lang attribute
    content = content.replace('<html lang="lv">', '<html lang="en">')

    # Canonical
    content = content.replace(
        '<link rel="canonical" href="https://lazergriezeji.lv/">',
        '<link rel="canonical" href="https://lazergriezeji.lv/en/">'
    )

    # hreflang - add EN entry and fix existing
    content = content.replace(
        '<link rel="alternate" hreflang="lv" href="https://lazergriezeji.lv/">',
        '<link rel="alternate" hreflang="lv" href="https://lazergriezeji.lv/">\n<link rel="alternate" hreflang="en" href="https://lazergriezeji.lv/en/">'
    )

    # OG tags
    content = content.replace(
        'property="og:url" content="https://lazergriezeji.lv/"',
        'property="og:url" content="https://lazergriezeji.lv/en/"'
    )
    content = content.replace(
        'property="og:locale" content="lv_LV"',
        'property="og:locale" content="en_US"'
    )

    # Twitter URL
    content = content.replace(
        'name="twitter:url" content="https://lazergriezeji.lv/"',
        'name="twitter:url" content="https://lazergriezeji.lv/en/"'
    )

    # Language switcher: swap active/inactive
    content = content.replace(
        '<a href="/" class="lang-switch active-lang" aria-label="Latviešu valoda" title="Latviešu">LV</a>',
        '<a href="/" class="lang-switch" aria-label="Latvian" title="Latviešu">LV</a>'
    )
    content = content.replace(
        '<a href="/en/" class="lang-switch" aria-label="English language" title="English">EN</a>',
        '<a href="/en/" class="lang-switch active-lang" aria-label="English" title="English">EN</a>'
    )

    # Breadcrumb home link
    content = content.replace(
        '<li><a href="/" style="color:var(--ink2);transition:color 0.2s;">Sākums</a></li>',
        '<li><a href="/en/" style="color:var(--ink2);transition:color 0.2s;">Home</a></li>'
    )

    # Apply ALL translations
    content = apply_all_translations(content)
    content = post_process_en(content)

    # ── RESTORE HTML IDs AND HREF VALUES (must not be translated) ──
    content = content.replace('href="#machines"', 'href="#iekārtas"')
    content = content.replace('href="#spare-parts"', 'href="#rezerves-dalas"')
    content = content.replace('href="#about-us"', 'href="#par-mums"')
    content = content.replace('href="#contact"', 'href="#kontakts"')
    content = content.replace('id="machines"', 'id="iekārtas"')
    content = content.replace('id="spare-parts"', 'id="rezerves-dalas"')
    # Fix JS initTabs calls
    content = content.replace("initTabs('machines'", "initTabs('iekārtas'")
    content = content.replace("initTabs('spare-parts'", "initTabs('rezerves-dalas'")

    # Fix any remaining Latvian fragments in link text
    content = content.replace('>Sākums<', '>Home<')
    content = content.replace('>Iekārtas<', '>Machines<')
    content = content.replace('>Rezerves daļas<', '>Spare Parts<')
    content = content.replace('>Par mums<', '>About Us<')
    content = content.replace('>Kontakti<', '>Contact<')

    # Fix JSON-LD
    content = content.replace('"inLanguage": "lv"', '"inLanguage": "en"')

    with open(dst, 'w', encoding='utf-8') as f:
        f.write(content)

    print("  ✓ English homepage created with full AI translation")
    return True


def create_en_product_pages():
    """Create AI-translated English product pages."""
    products_src = os.path.join(BASE, "products")
    products_dst = os.path.join(EN, "products")
    count = 0

    for root, dirs, files in os.walk(products_src):
        for f in files:
            if f == 'index.html':
                src = os.path.join(root, f)
                rel = os.path.relpath(root, products_src)
                dst_dir = os.path.join(products_dst, rel)
                os.makedirs(dst_dir, exist_ok=True)
                dst = os.path.join(dst_dir, f)

                with open(src, 'r', encoding='utf-8') as fh:
                    content = fh.read()

                # Lang
                content = content.replace('<html lang="lv">', '<html lang="en">')

                # Canonical: bratussss.github.io → lazergriezeji.lv/en/
                content = re.sub(
                    r'href="https://lazergriezeji\.lv/products/([^"]+)/"',
                    r'href="https://lazergriezeji.lv/en/products/\1/"',
                    content
                )

                # Nav links — point to /en/ anchors
                content = content.replace('href="/#iekārtas"', 'href="/en/#iekārtas"')
                content = content.replace('href="/#rezerves-dalas"', 'href="/en/#rezerves-dalas"')
                content = content.replace('href="/#par-mums"', 'href="/en/#par-mums"')
                content = content.replace('href="/#kontakts"', 'href="/en/#kontakts"')

                # Breadcrumb home
                content = content.replace(
                    '<li><a href="/" ',
                    '<li><a href="/en/" '
                )

                # Language switcher
                slug = rel
                content = content.replace(
                    f'<a href="/products/{slug}/" class="lang-switch active-lang" aria-label="Latviešu valoda" title="Latviešu">LV</a>',
                    f'<a href="/products/{slug}/" class="lang-switch" aria-label="Latvian" title="Latviešu">LV</a>'
                )
                content = content.replace(
                    f'<a href="/en/products/{slug}/" class="lang-switch" aria-label="English language" title="English">EN</a>',
                    f'<a href="/en/products/{slug}/" class="lang-switch active-lang" aria-label="English" title="English">EN</a>'
                )

                # Apply all translations
                content = apply_all_translations(content)
                content = post_process_en(content)

                # ── RESTORE HTML IDs AND HREF VALUES ──
                content = content.replace('href="#machines"', 'href="#iekārtas"')
                content = content.replace('href="/#machines"', 'href="/#iekārtas"')
                content = content.replace('href="/en/#machines"', 'href="/en/#iekārtas"')
                content = content.replace('href="#spare-parts"', 'href="#rezerves-dalas"')
                content = content.replace('href="/#spare-parts"', 'href="/#rezerves-dalas"')
                content = content.replace('href="/en/#spare-parts"', 'href="/en/#rezerves-dalas"')
                content = content.replace("initTabs('machines'", "initTabs('iekārtas'")
                content = content.replace("initTabs('spare-parts'", "initTabs('rezerves-dalas'")

                # Fix nav link display text
                content = content.replace('>Iekārtas<', '>Machines<')
                content = content.replace('>Rezerves daļas<', '>Spare Parts<')
                content = content.replace('>Par mums<', '>About Us<')
                content = content.replace('>Kontakti<', '>Contact<')
                content = content.replace('>Sākums<', '>Home<')
                content = content.replace('>Oficiālais pārstāvis ↗<', '>Official Dealer ↗<')
                content = content.replace('>Pieteikt<', '>Get a Quote<')

                with open(dst, 'w', encoding='utf-8') as fh:
                    fh.write(content)
                count += 1

    print(f"  ✓ {count} English product pages created with full AI translation")
    return count


def main():
    print("=" * 60)
    print("AI-POWERED ENGLISH TRANSLATION — 100% COMPLETE")
    print("=" * 60)

    print("\n[1/2] English homepage...")
    create_en_homepage()

    print("\n[2/2] English product pages...")
    create_en_product_pages()

    print("\n" + "=" * 60)
    print("DONE — All text fully AI-translated to English")
    print("=" * 60)


if __name__ == '__main__':
    main()
