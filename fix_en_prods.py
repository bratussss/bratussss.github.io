"""SAFE fixes for EN product pages - only multi-char replacements, NO short words."""
import os

DIR = r"d:\VS KODI\ROzo github\en\products"

FIXES = [
    # ── Reci lamps ──
    ('Gravesanai', 'for Engraving'), ('Gravesanas', 'Engraving'),
    ('nominala jauda', 'rated power'), ('Nominala jauda', 'Rated Power'),
    ('Nominala izejas jauda', 'Rated Output Power'), ('izejas jauda', 'output power'),
    ('Izejas jauda', 'Output Power'), ('Originala Reci', 'Genuine Reci'),
    ('Originala ', 'Genuine '), ('Originalas ', 'Genuine '),
    ('W Serijas lampa', 'W Series Tube'), ('serijas ', 'series '),
    ('Serijas ', 'Series '), ('paaudzes ', 'generation '),
    ('paaudze', 'generation'), ('Paaudzes ', 'Generation '),
    ('iebuvetu katalizatoru', 'built-in catalyst'), ('produkcija', 'product'),
    ('Produkcija', 'Product'), ('caurule ', 'tube '), ('Caurule ', 'Tube '),
    ('Nepieciesama ', 'Need a '),
    ('Sazinieties ar mums cenu un delivery jautajumos', 'Contact us for pricing and delivery inquiries'),
    ('Sazinieties ar mums', 'Contact us'),
    ('cenu un delivery jautajumos', 'for pricing and delivery inquiries'),
    ('jautajumos', 'inquiries'), ('ar warranty', 'with warranty'),
    # ── Chiller ──
    (' jauda', ' power'), ('jauda,', 'power,'), ('jauda.', 'power.'),
    ('1430W jauda', '1430W power'), ('Dzesesanas jauda', 'Cooling Capacity'),
    ('Skaidas jauda', 'Cooling Power'), ('Aukstumagents', 'Refrigerant'),
    ('Trokšņa limenis', 'Noise Level'), ('Trokšņu līmenis', 'Noise Level'),
    ('Barosanas avots', 'Power Supply'), ('Spriegums', 'Voltage'),
    ('Stravas paterins', 'Current Consumption'), ('Tvertnes tilpums', 'Tank Volume'),
    ('Darba spiediens', 'Working Pressure'), ('Izmantojama temperatura', 'Operating Temperature'),
    ('Sutnis', 'Pump'), ('Sutna jauda', 'Pump Power'),
    # ── Specs ──
    ('Temperaturas precizitate', 'Temperature Accuracy'),
    ('Ekspluatacijas apstakli', 'Operating Conditions'),
    ('Darba temperatura', 'Working Temperature'),
    ('Uzglabasanas temperatura', 'Storage Temperature'),
    ('Relativais mitrums', 'Relative Humidity'),
    ('Udensk dzesesana', 'Water Cooling'), ('Gaisa dzesesana', 'Air Cooling'),
    ('Dzesesanas tipa', 'Cooling Type'), ('Piesleguma veids', 'Connection Type'),
    ('Ieejas jauda', 'Input Power'), ('Maksimalais paterins', 'Max Consumption'),
    ('Maksimala jauda', 'Max Power'), ('Minimalais', 'Minimum'),
    ('Maksimalais', 'Maximum'), ('Sertifikacija', 'Certification'),
    # ── Laser tube ──
    ('Lazera caurules tips', 'Laser Tube Type'), ('Caurules diameters', 'Tube Diameter'),
    ('Caurules garums', 'Tube Length'), ('Dzesesana', 'Cooling'),
    ('Kalpošanas laiks', 'Service Life'), ('Darbmūžs', 'Service Life'),
    # ── Metal cutter ──
    ('Griesanas galva', 'Cutting Head'), ('Skiedru lazers', 'Fiber Laser'),
    ('Lazera avots', 'Laser Source'), ('Metala griešana', 'Metal Cutting'),
    ('Griesanas ātrums', 'Cutting Speed'),
    ('Pozicionesanas precizitate', 'Positioning Accuracy'),
    ('Atkartojamiba', 'Repeatability'), ('Paātrinājums', 'Acceleration'),
    ('Asistējošā gāze', 'Assist Gas'), ('Skābeklis', 'Oxygen'),
    ('Slāpeklis', 'Nitrogen'), ('Gaisa kompresors', 'Air Compressor'),
    # ── Marker ──
    ('Marķēšanas lauks', 'Marking Field'), ('Marķēšanas ātrums', 'Marking Speed'),
    ('Lazera veids', 'Laser Type'), ('Impulsu frekvence', 'Pulse Frequency'),
    ('Impulsa ilgums', 'Pulse Duration'), ('Stara diametrs', 'Beam Diameter'),
    # ── Headers ──
    ('Galvenas ipasibas', 'Key Features'), ('Galvenas Ipasibas', 'Key Features'),
    ('Tehniskie parametri', 'Technical Specifications'),
    ('Tehniskie Parametri', 'Technical Specifications'),
    ('Detalizeta specifikacija', 'Detailed Specifications'),
    ('Detalizeta Specifikacija', 'Detailed Specifications'),
    ('Pieejamie modeli', 'Available Models'),
    ('Saistitie produkti', 'Related Products'),
    # ── General ──
    ('Nodrosina', 'Provides'), ('Aizsardziba', 'Protection'),
    ('Drosiba', 'Safety'), ('Videja', 'Average'),
    ('darba mūžs', 'service life'), ('Darba mūžs', 'Service Life'),
    ('Pilns katalogs', 'Full Catalog'), ('Pieprasīt cenu', 'Request Pricing'),
    ('Skatīt wattsan.com', 'View on wattsan.com'), ('Interesē ', 'Interested in '),
    ('Speciālisti', 'Specialists'), ('Katalogs', 'Catalog'),
    ('Pieprasīt', 'Request'), ('Pieteikums', 'Application'),
    ('Apraksts', 'Description'), ('Prieksrocibas', 'Advantages'),
    ('Ipasibas', 'Features'), ('Specifikacija', 'Specification'),
    ('Informacija', 'Information'), ('Piegade', 'Delivery'),
    ('Uzstadisana', 'Installation'), ('Apmaciba', 'Training'),
    (' Garantija', ' Warranty'), ('Kontakti', 'Contact'), ('Adrese', 'Address'),
    ('Garantija', 'Warranty'), ('garantija', 'warranty'),
    # ── Alt texts ──
    ('CO2 laser lampa', 'CO2 laser tube'), ('laser lampa"', 'laser tube"'),
    ('laser lampas"', 'laser tubes"'), ('lampa"', 'tube"'),
    # ── Product descriptions ──
    ('TEYU chiller CO2 laser engraving machines', 'TEYU chiller for CO2 laser engraving machines'),
    ('Reci W serijas CO2 glass laser', 'Reci W-series CO2 glass laser'),
    ('technology ar metala-glass', 'technology with metal-glass'),
    ('beam quality un iebuvetu', 'beam quality and built-in'),
]

count = 0
for root, dirs, files in os.walk(DIR):
    for f in files:
        if f == 'index.html':
            src = os.path.join(root, f)
            slug = os.path.basename(root)
            with open(src, 'r', encoding='utf-8') as fh:
                c = fh.read()
            changed = False
            for old, new in FIXES:
                if old in c:
                    c = c.replace(old, new)
                    changed = True
            if changed:
                with open(src, 'w', encoding='utf-8') as fh:
                    fh.write(c)
                count += 1
                print(f"  OK: {slug}")

print(f"\nFixed {count} product pages")
