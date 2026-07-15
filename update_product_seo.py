"""
Update all product pages with:
1. Correct canonical URL (lazergriezeji.lv)
2. SEO-optimized title (≤65 chars)
3. SEO-optimized meta description (≤155 chars)
Uses Latvian keywords: lāzergravēšanas iekārta, lāzergriešanas iekārtas, gravēšana, etc.
"""
import os
import re

BASE_DIR = r"d:\VS KODI\ROzo github\products"
BASE_URL = "https://lazergriezeji.lv"

# ── SEO DATA PER PRODUCT ──
# Format: (title, description)
# Title max 65 chars, Description max 155 chars
# Keywords used: lāzergravēšanas iekārta, lāzergriešanas iekārtas, gravēšana, lāzergravēšana,
#   lāzergriešana, koka lāzergriešana, gravēšana metālā, gravēšana stiklā

SEO_DATA = {
    # ── CHILLERS (7) ──
    "chiller-cw-5200": (
        "CW-5200 — Industriālais Dzesētājs Lāzeriekārtām | Bratus.lv",
        "CW-5200 TEYU dzesētājs CO2 lāzergravēšanas iekārtām. 1430W jauda, ±0.3°C precizitāte. CE/REACH/RoHS sertificēts. Piegāde Latvijā — Bratus.lv."
    ),
    "chiller-cw-6200bn": (
        "CW-6200BN — Industriālais Dzesētājs 5030W UL | Bratus.lv",
        "CW-6200BN TEYU dzesētājs lāzergriešanas iekārtām. 5030W dzesēšanas jauda, ±0.5°C, UL sertificēts. Oficiālais pārstāvis Latvijā — Bratus.lv."
    ),
    "chiller-cwfl-15000kn": (
        "CWFL-15000KN — Dzesētājs Fiber Lāzeram 15kW UL | Bratus.lv",
        "CWFL-15000KN TEYU dzesētājs šķiedru lāzergriešanas iekārtām līdz 15kW. UL sertificēts, 210L tvertne. Piegāde un serviss Latvijā — Bratus.lv."
    ),
    "chiller-cwfl-20000kt": (
        "CWFL-20000KT — Dzesētājs Fiber Lāzeram 20kW SGS | Bratus.lv",
        "CWFL-20000KT TEYU dzesētājs jaudīgām lāzergriešanas iekārtām līdz 20kW. SGS sertificēts, 210L tvertne. Oficiālais pārstāvis Latvijā — Bratus.lv."
    ),
    "chiller-cwfl-30000kt": (
        "CWFL-30000KT — Dzesētājs Fiber Lāzeram 30kW SGS | Bratus.lv",
        "CWFL-30000KT TEYU industriālais dzesētājs lāzergriešanas iekārtām līdz 30kW. SGS sertificēts, 250L tvertne. Piegāde Latvijā — Bratus.lv."
    ),
    "chiller-cwfl-3000hnp": (
        "CWFL-3000HNP — Dzesētājs Fiber Lāzeram 3kW SGS | Bratus.lv",
        "CWFL-3000HNP TEYU dzesētājs 3kW šķiedru lāzergriešanas iekārtām. SGS sertificēts, ±0.5°C, 40L tvertne. Oficiālais pārstāvis Latvijā — Bratus.lv."
    ),
    "chiller-cwfl-6000knp": (
        "CWFL-6000KNP — Dzesētājs Fiber Lāzeram 6kW SGS | Bratus.lv",
        "CWFL-6000KNP TEYU dzesētājs lāzergriešanas iekārtām līdz 6kW. SGS sertificēts, ±1°C, 70L tvertne. Piegāde un serviss Latvijā — Bratus.lv."
    ),

    # ── RECI CO2 LAMPAS (5) ──
    "reci-w1": (
        "Reci W1 — CO2 Lāzera Lampa 75W Gravēšanai | Bratus.lv",
        "Reci W1 CO2 lāzera lampa lāzergravēšanas iekārtām. 75W nominālā jauda, 90W max, 540 dienu garantija. Oriģinālā Reci — oficiālais pārstāvis Bratus.lv."
    ),
    "reci-w2": (
        "Reci W2 — CO2 Lāzera Lampa 90W Populārākā | Bratus.lv",
        "Reci W2 CO2 lāzera lampa lāzergravēšanas un lāzergriešanas iekārtām. 90W nominālā jauda, 100W max, 540 dienu garantija. Piegāde Latvijā — Bratus.lv."
    ),
    "reci-w4": (
        "Reci W4 — CO2 Lāzera Lampa 100W Lieljaudas | Bratus.lv",
        "Reci W4 CO2 lāzera lampa jaudīgām lāzergravēšanas iekārtām. 100W nominālā jauda, 130W max, 360 dienu garantija. Oriģinālā Reci — Bratus.lv."
    ),
    "reci-w6": (
        "Reci W6 — CO2 Lāzera Lampa 130W Industriāla | Bratus.lv",
        "Reci W6 CO2 lāzera lampa profesionālām lāzergriešanas iekārtām. 130W nominālā jauda, 160W max, 360 dienu garantija. Piegāde Latvijā — Bratus.lv."
    ),
    "reci-w8": (
        "Reci W8 — CO2 Lāzera Lampa 150W Industriāla | Bratus.lv",
        "Reci W8 CO2 lāzera lampa lieljaudas lāzergravēšanas iekārtām. 150W nominālā jauda, 180W max, 360 dienu garantija. Oriģinālā Reci — Bratus.lv."
    ),

    # ── CO2 LASER MACHINES (18) ──
    "wattsan-0503-hobby-t": (
        "Wattsan 0503 Hobby-T — Lāzergravēšanas Iekārta | Bratus.lv",
        "Wattsan 0503 Hobby-T galda CO2 lāzergravēšanas iekārta kokam un ādai. 500×300mm, 55W. Perfekta koka lāzergriešanai maziem uzņēmumiem. Bratus.lv — oficiālais pārstāvis."
    ),
    "wattsan-1290-duos-lt": (
        "Wattsan 1290 DUOS LT — Lāzergravēšanas Iekārta | Bratus.lv",
        "Wattsan 1290 DUOS LT CO2 lāzergravēšanas iekārta ar divām lampām. 1200×900mm, 100–120W×2. Profesionāla koka lāzergriešana un gravēšana. Bratus.lv."
    ),
    "wattsan-1290-duos-st": (
        "Wattsan 1290 DUOS ST — Lāzergravēšanas Iekārta | Bratus.lv",
        "Wattsan 1290 DUOS ST CO2 lāzergravēšanas iekārta ar divām lampām. 1200×900mm, 100–120W×2. Koka lāzergriešana un gravēšana — Bratus.lv."
    ),
    "wattsan-1290-lt": (
        "Wattsan 1290 LT — CO2 Lāzergravēšanas Iekārta LT | Bratus.lv",
        "Wattsan 1290 LT CO2 lāzergravēšanas iekārta kokam, ādai, akrilam. 1200×900mm, 100–120W. Profesionāla gravēšana un lāzergriešana. Bratus.lv."
    ),
    "wattsan-1290-pro": (
        "Wattsan 1290 PRO — Lāzergravēšanas Iekārta PRO | Bratus.lv",
        "Wattsan 1290 PRO CO2 lāzergravēšanas iekārta ar uzlabotu precizitāti. 1200×900mm, 100–120W. Koka lāzergriešana un gravēšana uzņēmumiem. Bratus.lv."
    ),
    "wattsan-1290-st": (
        "Wattsan 1290 ST — CO2 Lāzergravēšanas Iekārta ST | Bratus.lv",
        "Wattsan 1290 ST CO2 lāzergravēšanas iekārta par pieejamu cenu. 1200×900mm, 100–120W. Koka, ādas, akrila gravēšana un lāzergriešana. Bratus.lv."
    ),
    "wattsan-1610-duos-lt": (
        "Wattsan 1610 DUOS LT — Lāzergravēšanas Iekārta | Bratus.lv",
        "Wattsan 1610 DUOS LT CO2 lāzergravēšanas iekārta ar divām lampām. 1600×1000mm, 100–120W×2. Liela formāta koka lāzergriešana. Bratus.lv."
    ),
    "wattsan-1610-duos-st": (
        "Wattsan 1610 DUOS ST — Lāzergravēšanas Iekārta | Bratus.lv",
        "Wattsan 1610 DUOS ST CO2 lāzergravēšanas iekārta ar divām lampām. 1600×1000mm, 100–120W×2. Gravēšana un lāzergriešana uzņēmumiem. Bratus.lv."
    ),
    "wattsan-1610-lt": (
        "Wattsan 1610 LT — CO2 Lāzergravēšanas Iekārta LT | Bratus.lv",
        "Wattsan 1610 LT CO2 lāzergravēšanas iekārta lieliem materiāliem. 1600×1000mm, 100–120W. Profesionāla koka lāzergriešana un gravēšana. Bratus.lv."
    ),
    "wattsan-1610-pro": (
        "Wattsan 1610 PRO — Lāzergravēšanas Iekārta PRO | Bratus.lv",
        "Wattsan 1610 PRO CO2 lāzergravēšanas iekārta ar augstu precizitāti. 1600×1000mm, 100–120W. Koka lāzergriešana, gravēšana akrilā un ādā. Bratus.lv."
    ),
    "wattsan-1610-st": (
        "Wattsan 1610 ST — CO2 Lāzergravēšanas Iekārta ST | Bratus.lv",
        "Wattsan 1610 ST CO2 lāzergravēšanas iekārta par optimālu cenu. 1600×1000mm, 100–120W. Gravēšana, koka lāzergriešana un akrila apstrāde. Bratus.lv."
    ),
    "wattsan-1630-flat-bed-pro": (
        "Wattsan 1630 Flat Bed PRO — Lāzergravēšanas Iekārta | Bratus.lv",
        "Wattsan 1630 Flat Bed PRO industriāla CO2 lāzergravēšanas iekārta. 1600×3000mm, 360–700W. Liela formāta koka lāzergriešana un gravēšana. Bratus.lv."
    ),
    "wattsan-1820-conveyor-pro": (
        "Wattsan 1820 Conveyor PRO — Lāzergravēšanas Iekārta | Bratus.lv",
        "Wattsan 1820 Conveyor PRO CO2 lāzergravēšanas iekārta ar konveijeru. 1800×2000mm, 150–180W. Auduma lāzergriešana un gravēšana. Bratus.lv."
    ),
    "wattsan-2030-flat-bed-pro": (
        "Wattsan 2030 Flat Bed PRO — Lāzergravēšanas Iekārta | Bratus.lv",
        "Wattsan 2030 Flat Bed PRO industriāla CO2 lāzergravēšanas iekārta. 3000×2000mm, 360–700W. Liela formāta koka lāzergriešana. Bratus.lv."
    ),
    "wattsan-6090-lt": (
        "Wattsan 6090 LT — CO2 Lāzergravēšanas Iekārta LT | Bratus.lv",
        "Wattsan 6090 LT CO2 lāzergravēšanas iekārta maziem uzņēmumiem. 900×600mm, 80–90W. Koka lāzergriešana, gravēšana akrilā un ādā. Bratus.lv."
    ),
    "wattsan-6090-pro": (
        "Wattsan 6090 PRO — Lāzergravēšanas Iekārta PRO | Bratus.lv",
        "Wattsan 6090 PRO CO2 lāzergravēšanas iekārta ar uzlabotu precizitāti. 900×600mm, 100–120W. Populārākā koka lāzergriešanai. Bratus.lv."
    ),
    "wattsan-6090-st": (
        "Wattsan 6090 ST — CO2 Lāzergravēšanas Iekārta ST | Bratus.lv",
        "Wattsan 6090 ST CO2 lāzergravēšanas iekārta par pieejamu cenu. 900×600mm, 80–90W. Lieliska koka lāzergriešanai un gravēšanai iesācējiem. Bratus.lv."
    ),
    "wattsan-co2-lt": (
        "Wattsan CO2 LT — Lāzergravēšanas Iekārta Galda | Bratus.lv",
        "Wattsan CO2 LT kompakta galda CO2 lāzergravēšanas iekārta. 110×110mm, 20–50W. Gravēšana stiklā, kokā un plastmasā. Bratus.lv — oficiālais pārstāvis."
    ),

    # ── METAL CUTTERS (16) ──
    "wattsan-1309-mini": (
        "Wattsan 1309 MINI — Metāla Lāzergriešanas Iekārta | Bratus.lv",
        "Wattsan 1309 MINI šķiedru lāzergriešanas iekārta metālam. 1300×900mm, līdz 6kW. Tērauda, alumīnija lāzergriešana maziem uzņēmumiem. Bratus.lv."
    ),
    "wattsan-1313-a": (
        "Wattsan 1313 A — Metāla Lāzergriešanas Iekārta A | Bratus.lv",
        "Wattsan 1313 A šķiedru lāzergriešanas iekārta metālam. 1300×1300mm, līdz 6kW. Precīza tērauda un alumīnija lāzergriešana. Bratus.lv — oficiālais pārstāvis."
    ),
    "wattsan-1313-a-cabin": (
        "Wattsan 1313 A Cabin — Lāzergriešanas Iekārta Ar Kabīni | Bratus.lv",
        "Wattsan 1313 A Cabin šķiedru lāzergriešanas iekārta metālam ar aizsargkabīni. 1300×1300mm, līdz 6kW. Droša tērauda lāzergriešana. Bratus.lv."
    ),
    "wattsan-1313-e": (
        "Wattsan 1313 E — Metāla Lāzergriešanas Iekārta E | Bratus.lv",
        "Wattsan 1313 E ekonomiskā šķiedru lāzergriešanas iekārta. 1300×1300mm, līdz 3kW. Pieejama metāla lāzergriešana jūsu budžetam. Bratus.lv."
    ),
    "wattsan-1313-s": (
        "Wattsan 1313 S — Metāla Lāzergriešanas Iekārta S | Bratus.lv",
        "Wattsan 1313 S šķiedru lāzergriešanas iekārta metālam. 1300×1300mm, līdz 12kW. Ātra un precīza tērauda lāzergriešana. Bratus.lv."
    ),
    "wattsan-1325-e": (
        "Wattsan 1325 E — Metāla Lāzergriešanas Iekārta E | Bratus.lv",
        "Wattsan 1325 E ekonomiskā šķiedru lāzergriešanas iekārta. 1300×2500mm, līdz 3kW. Pieejama cena metāla lāzergriešanai. Bratus.lv."
    ),
    "wattsan-1325-s": (
        "Wattsan 1325 S — Metāla Lāzergriešanas Iekārta S | Bratus.lv",
        "Wattsan 1325 S šķiedru lāzergriešanas iekārta vidējam formātam. 1300×2500mm, līdz 12kW. Profesionāla tērauda lāzergriešana. Bratus.lv."
    ),
    "wattsan-1530-a": (
        "Wattsan 1530 A — Metāla Lāzergriešanas Iekārta A | Bratus.lv",
        "Wattsan 1530 A šķiedru lāzergriešanas iekārta standarta formātam. 1500×3000mm, līdz 6kW. Universāla metāla lāzergriešana. Bratus.lv."
    ),
    "wattsan-1530-e": (
        "Wattsan 1530 E — Metāla Lāzergriešanas Iekārta E | Bratus.lv",
        "Wattsan 1530 E ekonomiskā šķiedru lāzergriešanas iekārta. 1500×3000mm, līdz 3kW. Izdevīga metāla lāzergriešana jūsu ražošanai. Bratus.lv."
    ),
    "wattsan-1530-hard": (
        "Wattsan 1530 Hard — Metāla Lāzergriešanas Iekārta Hard | Bratus.lv",
        "Wattsan 1530 Hard industriāla šķiedru lāzergriešanas iekārta. 1500×3000mm, līdz 30kW. Smagā metāla lāzergriešana 24/7 režīmā. Bratus.lv."
    ),
    "wattsan-1530-s": (
        "Wattsan 1530 S — Metāla Lāzergriešanas Iekārta S | Bratus.lv",
        "Wattsan 1530 S šķiedru lāzergriešanas iekārta ar paaugstinātu ātrumu. 1500×3000mm, līdz 12kW. Ātra metāla lāzergriešana. Bratus.lv."
    ),
    "wattsan-2040-hard": (
        "Wattsan 2040 Hard — Metāla Lāzergriešanas Iekārta Hard | Bratus.lv",
        "Wattsan 2040 Hard industriāla šķiedru lāzergriešanas iekārta. 2000×4000mm, līdz 30kW. Liela formāta tērauda lāzergriešana. Bratus.lv."
    ),
    "wattsan-2060-hard": (
        "Wattsan 2060 Hard — Metāla Lāzergriešanas Iekārta Hard | Bratus.lv",
        "Wattsan 2060 Hard industriāla šķiedru lāzergriešanas iekārta. 2000×6000mm, līdz 30kW. Smagā metāla lāzergriešana lieliem pasūtījumiem. Bratus.lv."
    ),
    "wattsan-2060-hard-ultra": (
        "Wattsan 2060 Hard Ultra — Lāzergriešanas Iekārta | Bratus.lv",
        "Wattsan 2060 Hard Ultra augstākās klases šķiedru lāzergriešanas iekārta. 2000×6000mm, 20–120kW. Maksimālā jauda metāla lāzergriešanai. Bratus.lv."
    ),
    "wattsan-3214-l": (
        "Wattsan 3214 L — Lielformāta Lāzergriešanas Iekārta | Bratus.lv",
        "Wattsan 3214 L lielformāta šķiedru lāzergriešanas iekārta. 14000×3200mm, 1.5–12kW. Lielu metāla lokšņu lāzergriešana. Bratus.lv."
    ),
    "wattsan-3214-lc": (
        "Wattsan 3214 LC — Lielformāta Lāzergriešanas Iekārta | Bratus.lv",
        "Wattsan 3214 LC lielformāta šķiedru lāzergriešanas iekārta ar kabīni. 14000×3200mm, 20–100kW. Industriāla metāla lāzergriešana. Bratus.lv."
    ),

    # ── MARKERS (11) ──
    "wattsan-3d": (
        "Wattsan 3D — Lāzermarķēšanas Iekārta 3D | Bratus.lv",
        "Wattsan 3D dinamiskā lāzermarķēšanas iekārta 3D gravēšanai. 100×100mm, 5–100W. Gravēšana metālā, gravēšana stiklā un plastmasā. Bratus.lv."
    ),
    "wattsan-fl-box": (
        "Wattsan FL BOX — Lāzermarķēšanas Iekārta Slēgta | Bratus.lv",
        "Wattsan FL BOX slēgta tipa lāzermarķēšanas iekārta gravēšanai. 200×200mm, 20–100W. Droša gravēšana metālā un gravēšana stiklā. Bratus.lv."
    ),
    "wattsan-fl-compact": (
        "Wattsan FL Compact — Lāzermarķēšanas Iekārta Galda | Bratus.lv",
        "Wattsan FL Compact kompakta galda lāzermarķēšanas iekārta. 200×200mm, 3–60W. Gravēšana metālā cenas ziņā pieejama. Bratus.lv."
    ),
    "wattsan-fl-gt": (
        "Wattsan FL GT — Lielformāta Lāzermarķēšanas Iekārta | Bratus.lv",
        "Wattsan FL GT lielformāta lāzermarķēšanas iekārta gravēšanai. 1000×1000mm, 3–300W. Gravēšana metālā cenas un liela formāta apstrāde. Bratus.lv."
    ),
    "wattsan-fl-hh": (
        "Wattsan FL HH — Rokas Lāzermarķēšanas Iekārta | Bratus.lv",
        "Wattsan FL HH portatīva rokas lāzermarķēšanas iekārta. 140×140mm, 20–100W. Mobilā gravēšana metālā un gravēšana stiklā. Bratus.lv."
    ),
    "wattsan-fl-ht": (
        "Wattsan FL HT — Rokas Lāzermarķēšanas Iekārta HT | Bratus.lv",
        "Wattsan FL HT portatīva rokas lāzermarķēšanas iekārta. 100×100mm, 20–50W. Pieejama gravēšana metālā cenas ziņā. Bratus.lv."
    ),
    "wattsan-fl-st": (
        "Wattsan FL ST — Lāzermarķēšanas Iekārta Statīvs | Bratus.lv",
        "Wattsan FL ST lāzermarķēšanas iekārta uz statīva. 200×200mm, 20–100W. Profesionāla gravēšana metālā un gravēšana stiklā. Bratus.lv."
    ),
    "wattsan-fl-tt": (
        "Wattsan FL TT — Lāzermarķēšanas Iekārta Galda | Bratus.lv",
        "Wattsan FL TT galda lāzermarķēšanas iekārta dažādiem materiāliem. 200×200mm, 20–100W. Universāla gravēšana metālā, stikla gravēšana. Bratus.lv."
    ),
    "wattsan-fm": (
        "Wattsan FM — Lāzermarķēšanas Iekārta Statīvs | Bratus.lv",
        "Wattsan FM lāzermarķēšanas iekārta uz statīva ar JPT/IPG avotu. 200×200mm, 5–100W. Kvalitatīva gravēšana metālā. Bratus.lv."
    ),
    "wattsan-uv-tt": (
        "Wattsan UV TT — UV Lāzermarķēšanas Iekārta | Bratus.lv",
        "Wattsan UV TT ultravioletā lāzermarķēšanas iekārta smalkai gravēšanai. 200×200mm, 5–20W. Stikla gravēšana un plastmasas marķēšana. Bratus.lv."
    ),
    "wattsan-co2-lt": (
        "Wattsan CO2 LT — CO2 Marķēšanas Iekārta | Bratus.lv",
        "Wattsan CO2 LT galda CO2 marķēšanas iekārta. 110×110mm, 20–50W. Gravēšana stiklā, kokā un organiskos materiālos. Bratus.lv — oficiālais pārstāvis."
    ),
}


def update_page(dir_path, title, description):
    """Update a single product page's title, meta description, and canonical."""
    filepath = os.path.join(dir_path, "index.html")
    if not os.path.exists(filepath):
        print(f"  SKIP: {filepath} not found")
        return False

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    slug = os.path.basename(dir_path)
    new_canonical = f'{BASE_URL}/products/{slug}/'
    changes = 0

    # 1. Replace canonical URL
    old_canonical_pattern = re.compile(
        r'<link rel="canonical" href="https://bratussss\.github\.io/products/[^"]+/">'
    )
    new_canonical_tag = f'<link rel="canonical" href="{new_canonical}">'
    if old_canonical_pattern.search(content):
        content = old_canonical_pattern.sub(new_canonical_tag, content)
        changes += 1
    elif f'href="{new_canonical}"' not in content:
        # Try to find any canonical
        old_canon = re.search(r'<link rel="canonical" href="([^"]+)"', content)
        if old_canon:
            content = content.replace(old_canon.group(1), new_canonical)
            changes += 1

    # 2. Replace title
    old_title = re.search(r'<title>([^<]+)</title>', content)
    if old_title and old_title.group(1) != title:
        content = content.replace(old_title.group(1), title)
        changes += 1

    # 3. Replace meta description
    old_desc = re.search(r'<meta name="description" content="([^"]+)"', content)
    if old_desc and old_desc.group(1) != description:
        content = content.replace(old_desc.group(1), description)
        changes += 1

    if changes > 0:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  OK: {slug} ({changes} changes)")
    else:
        print(f"  NO CHANGE: {slug}")
    return True


def main():
    print("=" * 60)
    print("UPDATING ALL PRODUCT PAGES")
    print(f"Base URL: {BASE_URL}")
    print("=" * 60)

    updated = 0
    skipped = 0

    for slug, (title, desc) in sorted(SEO_DATA.items()):
        dir_path = os.path.join(BASE_DIR, slug)
        if not os.path.isdir(dir_path):
            print(f"  MISSING DIR: {slug}")
            skipped += 1
            continue

        # Verify title length
        if len(title) > 65:
            print(f"  WARNING: Title too long ({len(title)} chars): {slug}")
        if len(desc) > 155:
            print(f"  WARNING: Desc too long ({len(desc)} chars): {slug}")

        if update_page(dir_path, title, desc):
            updated += 1
        else:
            skipped += 1

    print("=" * 60)
    print(f"DONE: {updated} updated, {skipped} skipped")
    print("=" * 60)


if __name__ == "__main__":
    main()
