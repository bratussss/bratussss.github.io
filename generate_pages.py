#!/usr/bin/env python3
"""Generate all product pages from product data."""
import os

PRODUCTS_DIR = "products"
os.makedirs(PRODUCTS_DIR, exist_ok=True)

# ── ALL PRODUCT DATA ──
# Each product: (filename, model_name, label, cat_class, cat_lv, work_area, power, speed, source, wattsan_slug, main_img, gallery_imgs, features, optics_specs, mech_specs, dim_specs, materials, description)

CO2_PRODUCTS = [
    ("wattsan-1820-conveyor-pro", "Wattsan 1820", "Conveyor PRO", "CO2 lāzeris · Konveijera / Audumam",
     "Konveijera / Audumam", "1800 × 2000 mm", "150–180 W", "1200 mm/s", "CO2",
     "wattsan-1820-conveyor-pro",
     "laser-co2-machine-wattsan-1820-conveyor-pro-wattsan-titul.webp",
     ["laser-co2-machine-wattsan-1820-conveyor-pro-wattsan-titul.webp"]),
    ("wattsan-6090-pro", "Wattsan 6090", "PRO", "CO2 lāzeris · PRO Sērija",
     "PRO Sērija", "900 × 600 mm", "100–120 W", "1000 mm/s", "Reci W4 / Lasea F4",
     "wattsan-6090-pro",
     "laser-co2-6090-pro-1-result.webp",
     ["6090-PRO-38.webp", "6090-PRO-11.webp", "6090-PRO-6-e1757493445533.webp", "6090-PRO-47.webp", "09-cnc-machines-products-gallery.webp", "laser-co2-6090-pro-1-result.webp"]),
    ("wattsan-1290-pro", "Wattsan 1290", "PRO", "CO2 lāzeris · PRO Sērija",
     "PRO Sērija", "1200 × 900 mm", "100–120 W", "1000 mm/s", "Reci W4 / Lasea F4",
     "wattsan-1290-pro",
     "laser-co2-1290-pro-1-result.webp",
     ["laser-co2-1290-pro-1-result.webp"]),
    ("wattsan-1610-pro", "Wattsan 1610", "PRO", "CO2 lāzeris · PRO Sērija",
     "PRO Sērija", "1600 × 1000 mm", "100–120 W", "1000 mm/s", "Reci W4 / Lasea F4",
     "wattsan-1610-pro",
     "laser-co2-1610-pro-1-result-1.webp",
     ["laser-co2-1610-pro-1-result-1.webp"]),
    ("wattsan-1630-flat-bed-pro", "Wattsan 1630", "Flat Bed PRO", "CO2 lāzeris · Flat Bed PRO",
     "Flat Bed PRO", "1600 × 3000 mm", "360–700 W", "800 mm/s", "CO2",
     "wattsan-flat-bed-1630-pro",
     "laser-co2-flat-bed-pro-1630-1-result.webp",
     ["laser-co2-flat-bed-pro-1630-1-result.webp"]),
    ("wattsan-2030-flat-bed-pro", "Wattsan 2030", "Flat Bed PRO", "CO2 lāzeris · Flat Bed PRO",
     "Flat Bed PRO", "3000 × 2000 mm", "360–700 W", "800 mm/s", "CO2",
     "wattsan-flat-bed-2030-pro",
     "laser-co2-flat-bed-pro-2030-1-result.webp",
     ["laser-co2-flat-bed-pro-2030-1-result.webp"]),
    ("wattsan-0503-hobby-t", "Wattsan 0503", "Hobby-T", "CO2 lāzeris · Galda / Desktop",
     "Galda / Desktop", "500 × 300 mm", "55 W", "500 mm/s", "CO2",
     "wattsan-0503-hobby-t",
     "Titul1-1.webp",
     ["Titul1-1.webp"]),
    ("wattsan-6090-st", "Wattsan 6090", "ST", "CO2 lāzeris · ST Sērija",
     "ST Sērija", "900 × 600 mm", "80–90 W", "500 mm/s", "Reci / Lasea",
     "wattsan-6090-st-2",
     "6090-1-1.png",
     ["6090-1-1.png"]),
    ("wattsan-1290-duos-st", "Wattsan 1290", "DUOS ST", "CO2 lāzeris · DUOS ST (Divas lampas)",
     "DUOS ST", "1200 × 900 mm", "100–120 W ×2", "500 mm/s", "Reci W4 ×2",
     "wattsan-1290-duos-st-2",
     "laser-co2-1290-duos-st-redesign-1.webp",
     ["laser-co2-1290-duos-st-redesign-1.webp"]),
    ("wattsan-1290-st", "Wattsan 1290", "ST", "CO2 lāzeris · ST Sērija",
     "ST Sērija", "1200 × 900 mm", "100–120 W", "500 mm/s", "Reci / Lasea",
     "wattsan-1290-st-2",
     "1290-1-result.webp",
     ["1290-1-result.webp"]),
    ("wattsan-6090-lt", "Wattsan 6090", "LT", "CO2 lāzeris · LT Sērija",
     "LT Sērija", "900 × 600 mm", "80–90 W", "500 mm/s", "Reci / Lasea",
     "wattsan-6090-lt-2",
     "laser-co2-machine-6090-lt-redesign-1.webp",
     ["laser-co2-machine-6090-lt-redesign-1.webp"]),
    ("wattsan-1290-duos-lt", "Wattsan 1290", "DUOS LT", "CO2 lāzeris · DUOS LT (Divas lampas)",
     "DUOS LT", "1200 × 900 mm", "100–120 W ×2", "500 mm/s", "Reci W4 ×2",
     "wattsan-1290-duos-lt-2",
     "laser-co2-1290-duos-lt-redesign-1.webp",
     ["laser-co2-1290-duos-lt-redesign-1.webp"]),
    ("wattsan-1290-lt", "Wattsan 1290", "LT", "CO2 lāzeris · LT Sērija",
     "LT Sērija", "1200 × 900 mm", "100–120 W", "500 mm/s", "Reci / Lasea",
     "wattsan-1290-lt-2",
     "1290-1-result.webp",
     ["1290-1-result.webp"]),
    ("wattsan-1610-duos-lt", "Wattsan 1610", "DUOS LT", "CO2 lāzeris · DUOS LT (Divas lampas)",
     "DUOS LT", "1600 × 1000 mm", "100–120 W ×2", "500 mm/s", "Reci W4 ×2",
     "wattsan-1610-duos-lt-2",
     "laser-co2-1610-duos-lt-redesign-1.webp",
     ["laser-co2-1610-duos-lt-redesign-1.webp"]),
    ("wattsan-1610-lt", "Wattsan 1610", "LT", "CO2 lāzeris · LT Sērija",
     "LT Sērija", "1600 × 1000 mm", "100–120 W", "500 mm/s", "Reci / Lasea",
     "wattsan-1610-lt-2",
     "1610-1.webp",
     ["1610-1.webp"]),
    ("wattsan-1610-duos-st", "Wattsan 1610", "DUOS ST", "CO2 lāzeris · DUOS ST (Divas lampas)",
     "DUOS ST", "1600 × 1000 mm", "100–120 W ×2", "500 mm/s", "Reci W4 ×2",
     "wattsan-1610-duos-st-2",
     "laser-co2-1610-duos-st-redesign-1.webp",
     ["laser-co2-1610-duos-st-redesign-1.webp"]),
    ("wattsan-1610-st", "Wattsan 1610", "ST", "CO2 lāzeris · ST Sērija",
     "ST Sērija", "1600 × 1000 mm", "100–120 W", "500 mm/s", "Reci / Lasea",
     "wattsan-1610-st-2",
     "1610-1.png",
     ["1610-1.png"]),
]

METAL_PRODUCTS = [
    ("wattsan-1313-a-cabin", "Wattsan 1313", "A Cabin", "Šķiedru lāzeris · A Sērija ar kabīni",
     "Ar kabīni", "1300 × 1300 mm", "līdz 6 kW", "80 m/min", "Raycus / IPG",
     "wattsan-1313-a-cabin",
     "laser-metal-cutter-machine-wattsan-1313a-with-cabin-titul.webp",
     ["laser-metal-cutter-machine-wattsan-1313a-with-cabin-titul.webp"]),
    ("wattsan-3214-l", "Wattsan 3214", "L", "Šķiedru lāzeris · Lielformāta",
     "Lielformāta", "14000 × 3200 mm", "1.5–12 kW", "80 m/min", "Raycus / IPG",
     "wattsan-3214-l",
     "large-metal-cutter-nocabin-titul-result-1.webp",
     ["large-metal-cutter-nocabin-titul-result-1.webp"]),
    ("wattsan-3214-lc", "Wattsan 3214", "LC", "Šķiedru lāzeris · Lielformāta HP",
     "Lielformāta HP", "14000 × 3200 mm", "20–100 kW", "80 m/min", "Raycus / IPG",
     "wattsan-3214-lc",
     "large-metal-cutter-cabin-titul-result.webp",
     ["large-metal-cutter-cabin-titul-result.webp"]),
    ("wattsan-2060-hard-ultra", "Wattsan 2060", "Hard Ultra", "Šķiedru lāzeris · Hard Ultra",
     "Hard Ultra", "2000 × 6000 mm", "20–120 kW", "240 m/min", "Raycus / IPG",
     "wattsan-2060-hard-ultra",
     "hard-ultra-titul-for-pluses-edit-result.webp",
     ["hard-ultra-titul-for-pluses-edit-result.webp"]),
    ("wattsan-1530-hard", "Wattsan 1530", "Hard", "Šķiedru lāzeris · Hard Sērija",
     "Hard Sērija", "1500 × 3000 mm", "līdz 30 kW", "100–140 m/min", "Raycus / IPG",
     "wattsan-1530-hard",
     "wattsan-hard-blue-cabin-titul.png",
     ["wattsan-hard-blue-cabin-titul.png"]),
    ("wattsan-2040-hard", "Wattsan 2040", "Hard", "Šķiedru lāzeris · Hard Sērija",
     "Hard Sērija", "2000 × 4000 mm", "līdz 30 kW", "100–140 m/min", "Raycus / IPG",
     "wattsan-2040-hard",
     "wattsan-hard-blue-cabin-titul.png",
     ["wattsan-hard-blue-cabin-titul.png"]),
    ("wattsan-2060-hard", "Wattsan 2060", "Hard", "Šķiedru lāzeris · Hard Sērija",
     "Hard Sērija", "2000 × 6000 mm", "līdz 30 kW", "100–140 m/min", "Raycus / IPG",
     "wattsan-2060-hard",
     "wattsan-hard-blue-cabin-titul.png",
     ["wattsan-hard-blue-cabin-titul.png"]),
    ("wattsan-1309-mini", "Wattsan 1309", "MINI", "Šķiedru lāzeris · MINI",
     "MINI", "1300 × 900 mm", "līdz 6 kW", "50 m/min", "Raycus / IPG",
     "wattsan-1309-mini",
     "1309-mini-titul.png",
     ["1309-mini-titul.png"]),
    ("wattsan-1313-a", "Wattsan 1313", "A", "Šķiedru lāzeris · A Sērija",
     "A Sērija", "1300 × 1300 mm", "līdz 6 kW", "80 m/min", "Raycus / IPG",
     "wattsan-1313-a",
     "1313-a-main-titul.png",
     ["1313-a-main-titul.png"]),
    ("wattsan-1530-a", "Wattsan 1530", "A", "Šķiedru lāzeris · A Sērija",
     "A Sērija", "1500 × 3000 mm", "līdz 6 kW", "80 m/min", "Raycus / IPG",
     "wattsan-1530-a",
     "1530-a-main-titul.png",
     ["1530-a-main-titul.png"]),
    ("wattsan-1313-s", "Wattsan 1313", "S", "Šķiedru lāzeris · S Sērija",
     "S Sērija", "1300 × 1300 mm", "līdz 12 kW", "100–120 m/min", "Raycus / IPG",
     "wattsan-1313-s",
     "1313-s-titul.png",
     ["1313-s-titul.png"]),
    ("wattsan-1325-s", "Wattsan 1325", "S", "Šķiedru lāzeris · S Sērija",
     "S Sērija", "1300 × 2500 mm", "līdz 12 kW", "100–120 m/min", "Raycus / IPG",
     "wattsan-1325-s",
     "1325-s.webp",
     ["1325-s.webp"]),
    ("wattsan-1530-s", "Wattsan 1530", "S", "Šķiedru lāzeris · S Sērija",
     "S Sērija", "1500 × 3000 mm", "līdz 12 kW", "100–120 m/min", "Raycus / IPG",
     "wattsan-1530-s",
     "metall-cutter-plus-3.png",
     ["metall-cutter-plus-3.png"]),
    ("wattsan-1313-e", "Wattsan 1313", "E", "Šķiedru lāzeris · E Sērija (Ekonomiskā)",
     "E Sērija", "1300 × 1300 mm", "līdz 3 kW", "80 m/min", "Raycus / IPG",
     "wattsan-1313-e",
     "1313-e-titul.png",
     ["1313-e-titul.png"]),
    ("wattsan-1325-e", "Wattsan 1325", "E", "Šķiedru lāzeris · E Sērija (Ekonomiskā)",
     "E Sērija", "1300 × 2500 mm", "līdz 3 kW", "80 m/min", "Raycus / IPG",
     "wattsan-1325-e",
     "metall-cutter-plus-2.png",
     ["metall-cutter-plus-2.png"]),
    ("wattsan-1530-e", "Wattsan 1530", "E", "Šķiedru lāzeris · E Sērija (Ekonomiskā)",
     "E Sērija", "1500 × 3000 mm", "līdz 3 kW", "80 m/min", "Raycus / IPG",
     "wattsan-1530-e",
     "1530-e-1-1.png",
     ["1530-e-1-1.png"]),
]

MARKER_PRODUCTS = [
    ("wattsan-fm", "Wattsan", "FM", "Šķiedru marķētājs · Statīvs",
     "Statīvs", "200 × 200 mm", "5–100 W", "—", "JPT / RAYCUS / DAVI",
     "wattsan-fm",
     "laser-marker-wattsan-fm-series-titul.webp",
     ["laser-marker-wattsan-fm-series-titul.webp"]),
    ("wattsan-fl-gt", "Wattsan", "FL GT", "Šķiedru marķētājs · Lielformāta",
     "Lielformāta", "1000 × 1000 mm", "3–300 W", "—", "JPT / IPG / RAYCUS",
     "wattsan-fl-gt",
     "fl-gt-titul-result.webp",
     ["fl-gt-titul-result.webp"]),
    ("wattsan-fl-compact", "Wattsan", "FL Compact", "Šķiedru marķētājs · Galda / Kompakts",
     "Galda / Kompakts", "200 × 200 mm", "3–60 W", "—", "JPT / IPG / RAYCUS",
     "wattsan-fl-compact",
     "fl-compact-titul-1-result.webp",
     ["fl-compact-titul-1-result.webp"]),
    ("wattsan-fl-hh", "Wattsan", "FL HH", "Šķiedru marķētājs · Rokas / Portatīvs",
     "Rokas / Portatīvs", "140 × 140 mm", "20–100 W", "—", "JPT / RAYCUS",
     "wattsan-fl-hh",
     "laser-marker-fl-hh-new-titul-result.webp",
     ["laser-marker-fl-hh-new-titul-result.webp"]),
    ("wattsan-uv-tt", "Wattsan", "UV TT", "UV marķētājs · Galda",
     "UV · Galda", "200 × 200 mm", "5–20 W", "—", "JPT UV",
     "wattsan-uv-tt",
     "UF-TT-titul-1.webp",
     ["UF-TT-titul-1.webp"]),
    ("wattsan-fl-box", "Wattsan", "FL BOX", "Šķiedru marķētājs · Galda / Slēgts",
     "Galda / Slēgts", "200 × 200 mm", "20–100 W", "—", "IPG / MAX / RAYCUS / JPT",
     "wattsan-fl-box",
     "fl-bo-titul-render-main.webp",
     ["fl-bo-titul-render-main.webp"]),
    ("wattsan-3d", "Wattsan", "3D", "Šķiedru marķētājs · 3D Dinamiskais",
     "3D Dinamiskais", "100 × 100 mm", "5–100 W", "—", "JPT / IPG / RAYCUS",
     "wattsan-3d",
     "laser-marker-wattsan-3d-titul.webp",
     ["laser-marker-wattsan-3d-titul.webp"]),
    ("wattsan-fl-ht", "Wattsan", "FL HT", "Šķiedru marķētājs · Rokas / Portatīvs",
     "Rokas / Portatīvs", "100 × 100 mm", "20–50 W", "—", "RayMax / Maxphotonics",
     "wattsan-fl-ht-2",
     "laser-marker-wattsan-ht-titul-main.webp",
     ["laser-marker-wattsan-ht-titul-main.webp"]),
    ("wattsan-fl-tt", "Wattsan", "FL TT", "Šķiedru marķētājs · Galda",
     "Galda", "200 × 200 mm", "20–100 W", "—", "JPT / IPG / MAX / RAYCUS",
     "wattsan-fl-tt",
     "FL-TT-2.png",
     ["FL-TT-2.png"]),
    ("wattsan-co2-lt", "Wattsan", "CO2 LT", "CO2 marķētājs · Galda",
     "CO2 · Galda", "110 × 110 mm", "20–50 W", "—", "CO2",
     "wattsan-co2-lt",
     "co2-lt-1.png",
     ["co2-lt-1.png"]),
    ("wattsan-fl-st", "Wattsan", "FL ST", "Šķiedru marķētājs · Statīvs",
     "Statīvs", "200 × 200 mm", "20–100 W", "—", "JPT / IPG / MAX / RAYCUS",
     "wattsan-fl-st",
     "st-1-2.png",
     ["st-1-2.png"]),
]

CO2_MATERIALS = "Koks, Saplāksnis, MDF, Akrils, Āda, Gumija, Audums, Akmens, Granīts, Plastmasa, Bambuss, Keramika"
METAL_MATERIALS = "Alumīnijs, Nerūsējošais tērauds, Misiņš, Varš, Oglekļa tērauds, Cinks, Titāns"
MARKER_MATERIALS = "Metāls, Plastmasa, Keramika, Stikls, Āda, Gumija, Akrils"

CO2_FEATURES = [
    ("Wattsan SAS Drošība", "Safety Assurance System ar FOX ugunsgrēka detektoru un rūdīta stikla vāku."),
    ("Precīza Jaudas Kontrole", "Digitālais potenciometrs ar precizitāti līdz 0.001 A smalkai gravēšanai."),
    ("Ātrgaitas Gravēšana", "Līdz pat 1000 mm/s gravēšanas ātrums — maksimāla produktivitāte."),
    ("Caurstaigājams Galds", "Y-ass caurlaide ļauj apstrādāt garākus materiālus."),
    ("Leadshine Servo Motori", "Precīzi servo motori ar pozicionēšanas precizitāti 0.03 mm."),
    ("Globāls Atbalsts", "21 gada pieredze, 185 inženieri, 20 000+ iekārtu 100+ valstīs."),
]
METAL_FEATURES = [
    ("Augsta Griešanas Jauda", "Šķiedru lāzera avots līdz pat 120 kW jaudai — griež līdz 25+ mm."),
    ("Raycus / IPG Avoti", "Pasaules klases lāzera avoti ar ilgu darbmūžu un stabilitāti."),
    ("Ātrgaitas Pozicionēšana", "Līdz 240 m/min traversa ātrums — maksimāla produktivitāte."),
    ("Auto Fokusa Sistēma", "Automātiska fokusa regulēšana dažāda biezuma materiāliem."),
    ("Industriāla Konstrukcija", "Pastiprināta tērauda gulta un precīzas lineārās vadotnes."),
    ("Globāls Atbalsts", "21 gada pieredze, 185 inženieri, 20 000+ iekārtu 100+ valstīs."),
]
MARKER_FEATURES = [
    ("Precīza Marķēšana", "Augstas izšķirtspējas marķējums ar 0.01 mm precizitāti."),
    ("Daudzpusīgi Materiāli", "Metāls, plastmasa, keramika, stikls un citi materiāli."),
    ("Kompakts Dizains", "Viegli integrējams jebkurā ražošanas līnijā vai darbnīcā."),
    ("JPT / IPG Avoti", "Pasaules klases lāzera avoti ar ilgu kalpošanas laiku."),
    ("Vienkārša Programmatūra", "Intuitīva EZCAD/LaserWork programmatūra ātrai uzstādīšanai."),
    ("Globāls Atbalsts", "21 gada pieredze, 185 inženieri, 20 000+ iekārtu 100+ valstīs."),
]

CO2_OPTICS = [
    ("Lāzera jauda", "{power}"),
    ("Lāzera caurule", "Reci W4 / Lasea F4"),
    ("Spoguļa diametrs", "25 mm"),
    ("ZnSe lēca", "ZnSe D20 f50"),
    ("Fokusa attālums", "50 mm"),
    ("Caurules darbmūžs", "~10 000 h"),
    ("Min. gravēšanas izmērs", "1.5 × 1.5 mm"),
]
CO2_MECH = [
    ("Darba virsma", "Asmeņu galds"),
    ("Griešanas ātrums", "0–500 mm/s"),
    ("Gravēšanas ātrums", "0–{speed}"),
    ("Pozicionēšanas precizitāte", "0.03 mm"),
    ("Dzesēšana", "Ūdens"),
    ("Barošana", "220V ±10% 50Hz"),
    ("Jaudas patēriņš", "~2000 W"),
    ("Caurstaigājams galds", "Jā (Y-ass)"),
    ("Kontrolieris", "Ruida RDC"),
    ("Programmatūra", "RDL (LaserWork 8)"),
    ("Savienojamība", "LAN, USB, Wi-Fi"),
]
CO2_DIMS = [
    ("Darba zona", "{work_area}"),
    ("Atbalstītie formāti", "AI, DXF, PLT, PDF, BMP, GIF, JPEG, PNG"),
]

METAL_OPTICS = [
    ("Lāzera jauda", "{power}"),
    ("Lāzera avots", "{source}"),
    ("Viļņa garums", "1064 nm"),
    ("Griešanas biezums", "līdz 25+ mm (atkarīgs no jaudas)"),
    ("Asistējošā gāze", "O₂, N₂, Gaiss"),
]
METAL_MECH = [
    ("Traversa ātrums", "{speed}"),
    ("Pozicionēšanas precizitāte", "±0.03 mm"),
    ("Atkārtojamība", "±0.02 mm"),
    ("Dzesēšana", "Ūdens (Chiller)"),
    ("Barošana", "380V 50Hz 3-fāžu"),
    ("Kontrolieris", "CypCut / FSCUT"),
    ("Programmatūra", "CypCut / LaserWork"),
    ("Savienojamība", "LAN, USB"),
]
METAL_DIMS = [
    ("Darba zona", "{work_area}"),
    ("Atbalstītie formāti", "DXF, DWG, AI, PLT"),
]

MARKER_OPTICS = [
    ("Lāzera jauda", "{power}"),
    ("Lāzera avots", "{source}"),
    ("Viļņa garums", "1064 nm (Fiber) / 355 nm (UV) / 10640 nm (CO2)"),
    ("Marķēšanas dziļums", "0.01–0.5 mm"),
    ("Atkārtojamība", "±0.001 mm"),
]
MARKER_MECH = [
    ("Marķēšanas ātrums", "līdz 8000 mm/s"),
    ("Pozicionēšanas precizitāte", "±0.001 mm"),
    ("Dzesēšana", "Gaiss (integrēts ventilators)"),
    ("Barošana", "220V ±10% 50Hz"),
    ("Kontrolieris", "EZCAD / LaserWork"),
    ("Programmatūra", "EZCAD2 / LaserWork"),
    ("Savienojamība", "USB"),
]
MARKER_DIMS = [
    ("Darba zona", "{work_area}"),
    ("Atbalstītie formāti", "DXF, AI, PLT, BMP, JPG, PNG, SVG"),
]

IMG_BASE = "https://wattsan.com/wp-content/uploads"


def make_page(filename, name, label, cat, cat_lv, work_area, power, speed, source, slug, main_img, gallery_imgs, features, optics_specs, mech_specs, dim_specs, materials, desc_text=None):
    """Generate a product page HTML."""
    full_title = f"{name} {label}"
    nav_sub_html = "{nav_sub_html}"  # placeholder, filled after generation
    page_title = f"{full_title} — {'CO2 Lāzera Iekārta' if 'CO2' in cat else 'Metāla Griešanas Iekārta' if 'lāzeris' in cat else 'Marķēšanas Iekārta'} | Bratus.lv"
    
    main_src = f"{IMG_BASE}/{main_img}"
    gallery_html = ""
    for i, img in enumerate(gallery_imgs[:6]):
        lazy = ' loading="lazy"' if i > 0 else ""
        gallery_html += f'''
        <div class="showcase-card sr{" d1" if i==1 else " d2" if i==2 else ""}" onclick="openLightbox({i})">
          <img src="{IMG_BASE}/{img}" alt="{full_title}"{lazy}>
          <div class="showcase-card-label"><span>{"Pilns iekārtas skats" if i==0 else "Darba zona" if i==2 else "Vadības panelis" if i==3 else "Ražošanas kvalitāte" if i==4 else "Priekšskats" if i==5 else "Lāzera detaļa"}</span></div>
        </div>'''
    
    features_html = ""
    for f in features[:6]:
        features_html += f'''
      <div class="feature-card sr">
        <div class="feature-card-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg></div>
        <h4>{f[0]}</h4>
        <p>{f[1]}</p>
      </div>'''
    
    def build_specs_table(specs):
        html = ""
        for label, val in specs:
            v = val.replace("{work_area}", work_area).replace("{power}", power).replace("{speed}", speed).replace("{source}", source)
            html += f'\n          <div class="specs-row"><span class="specs-row-l">{label}</span><span class="specs-row-v">{v}</span></div>'
        return html
    
    optics_html = build_specs_table(optics_specs)
    mech_html = build_specs_table(mech_specs)
    dims_html = build_specs_table(dim_specs)
    
    materials_tags = ""
    for m in materials.split(", ")[:18]:
        materials_tags += f'\n      <span class="material-tag sr">{m}</span>'
    
    # Thumbnails for hero gallery
    thumbs = ""
    for i, img in enumerate(gallery_imgs[:5]):
        active = ' active' if i == 0 else ""
        thumbs += f'''
      <img class="gallery-thumb{active}" src="{IMG_BASE}/{img}" onclick="document.getElementById('mainImg').src=this.src; document.querySelectorAll('.gallery-thumb').forEach(t=>t.classList.remove('active')); this.classList.add('active')">'''
    
    desc = desc_text or f"Profesionāla {'CO2 lāzera' if 'CO2' in cat else 'šķiedru lāzera metāla griešanas' if 'lāzeris' in cat else 'lāzera marķēšanas'} iekārta {full_title} ar {work_area} darba zonu{' un ' + power + ' jaudu' if power else ''}. Wattsan oficiālais pārstāvis Latvijā — Bratus.lv."
    
    html = f'''<!DOCTYPE html>
<html lang="lv">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{page_title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700&family=Inter:wght@300;400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
<style>
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
html{{scroll-behavior:smooth}}
body{{font-family:'Inter',sans-serif;background:#fff;color:#1a1a1a;overflow-x:hidden;-webkit-font-smoothing:antialiased}}
a{{text-decoration:none;color:inherit}}
img{{display:block}}
:root{{--bg:#fff;--bg2:#f5f5f5;--bg3:#eee;--ink:#1a1a1a;--ink2:#555;--ink3:#999;--accent:#E63C32;--border:rgba(0,0,0,0.09);--border2:rgba(0,0,0,0.15);--max:1280px;--ease:cubic-bezier(.22,1,.36,1);--gutter:clamp(20px,5vw,64px)}}
/* NAV */
.nav{{position:fixed;top:0;left:0;right:0;z-index:300;height:64px;display:flex;align-items:center;justify-content:space-between;padding:0 var(--gutter);background:rgba(255,255,255,0.96);backdrop-filter:blur(20px);border-bottom:1px solid var(--border)}}
.nav-logo{{display:flex;align-items:center;gap:14px}}
.nav-logo img{{height:22px;width:auto}}
.nav-logo-sep{{width:1px;height:18px;background:var(--border2)}}
.nav-logo-lv{{font-family:'Plus Jakarta Sans',sans-serif;font-size:0.72rem;letter-spacing:0.14em;text-transform:uppercase;color:var(--ink2);font-weight:400}}
.nav-logo-lv em{{font-style:normal;color:var(--accent)}}
.nav-links{{display:flex;align-items:center;gap:28px}}
.nav-links a{{font-size:0.73rem;letter-spacing:0.08em;text-transform:uppercase;color:var(--ink2);transition:color 0.2s;font-weight:400}}
.nav-links a:hover,.nav-links a.active{{color:var(--accent)}}
.nav-cta{{display:flex;align-items:center;gap:10px}}
.btn-ghost{{padding:8px 18px;font-size:0.7rem;letter-spacing:0.08em;text-transform:uppercase;border:1px solid var(--border2);color:var(--ink2);transition:all 0.2s;font-weight:400;white-space:nowrap}}
.btn-ghost:hover{{border-color:var(--ink);color:var(--ink)}}
.btn-accent{{padding:9px 20px;font-size:0.7rem;letter-spacing:0.08em;text-transform:uppercase;background:var(--accent);color:#fff;font-weight:500;transition:background 0.2s;white-space:nowrap}}
.btn-accent:hover{{background:#c42e25}}
.nav-mobile-btn{{display:none;background:none;border:none;cursor:pointer;color:var(--ink)}}
@media(max-width:860px){{.nav-links{{display:none}}.nav-mobile-btn{{display:flex;align-items:center}}.btn-ghost{{display:none}}}}
@media(max-width:860px){{.nav-links.open{{display:flex;flex-direction:column;position:absolute;top:64px;left:0;right:0;background:#fff;border-bottom:1px solid var(--border);padding:12px 0;gap:0}}.nav-links.open a{{padding:12px var(--gutter);font-size:0.85rem}}}}
/* NAV SUB - product navigation between models */
.nav-sub{{background:var(--bg2);border-bottom:1px solid var(--border);padding:8px 0;margin-top:64px;overflow-x:auto;-webkit-overflow-scrolling:touch;scrollbar-width:none}}
.nav-sub::-webkit-scrollbar{{display:none}}
.nav-sub-inner{{max-width:var(--max);margin:0 auto;padding:0 var(--gutter);display:flex;gap:6px;align-items:center}}
.nav-sub span{{font-size:0.56rem;letter-spacing:0.12em;text-transform:uppercase;color:var(--ink3);white-space:nowrap;margin-right:8px}}
.nav-sub a{{font-size:0.62rem;padding:5px 10px;border:1px solid var(--border);color:var(--ink2);white-space:nowrap;transition:all 0.15s;letter-spacing:0.04em;flex-shrink:0}}
.nav-sub a:hover,.nav-sub a.active{{border-color:var(--accent);color:var(--accent);background:rgba(230,60,50,0.04)}}
/* BREADCRUMB */
.breadcrumb{{padding:0 var(--gutter);max-width:var(--max);margin:0 auto}}
.breadcrumb-inner{{display:flex;align-items:center;gap:8px;font-size:0.62rem;letter-spacing:0.08em;text-transform:uppercase;color:var(--ink3);padding:16px 0;border-bottom:1px solid var(--border);flex-wrap:wrap}}
.breadcrumb-inner a{{color:var(--ink3);transition:color 0.2s;white-space:nowrap}}
.breadcrumb-inner a:hover{{color:var(--accent)}}
.breadcrumb-current{{color:var(--ink);font-weight:500}}
/* PRODUCT HERO */
.product-hero{{max-width:var(--max);margin:0 auto;padding:32px var(--gutter);display:grid;grid-template-columns:1.2fr 1fr;gap:48px;align-items:start}}
@media(max-width:860px){{.product-hero{{grid-template-columns:1fr;gap:28px}}}}
.product-gallery{{position:relative}}
.gallery-main{{width:100%;aspect-ratio:4/3;object-fit:contain;background:var(--bg2);border:1px solid var(--border)}}
.gallery-thumbs{{display:flex;gap:8px;margin-top:10px;overflow-x:auto}}
.gallery-thumb{{width:70px;height:52px;object-fit:cover;border:1px solid var(--border);cursor:pointer;opacity:0.6;transition:opacity 0.2s,border-color 0.2s;flex-shrink:0}}
.gallery-thumb:hover,.gallery-thumb.active{{opacity:1;border-color:var(--accent)}}
.product-info{{display:flex;flex-direction:column;gap:16px}}
.product-badge{{display:inline-flex;align-items:center;gap:7px;background:rgba(230,60,50,0.1);border:1px solid rgba(230,60,50,0.25);padding:5px 12px;font-size:0.6rem;letter-spacing:0.12em;text-transform:uppercase;color:var(--accent);font-weight:600;width:fit-content}}
.product-badge-dot{{width:5px;height:5px;border-radius:50%;background:var(--accent);animation:pulse 2s ease infinite}}
@keyframes pulse{{0%,100%{{opacity:1}}50%{{opacity:.35}}}}
.product-title{{font-family:'Plus Jakarta Sans',sans-serif;font-size:clamp(1.8rem,3.2vw,2.8rem);font-weight:300;letter-spacing:-0.03em;line-height:1.08;color:var(--ink)}}
.product-title strong{{font-weight:700}}
.product-subtitle{{font-size:0.9rem;color:var(--ink2);line-height:1.7;font-weight:300}}
.key-specs{{display:flex;gap:20px;flex-wrap:wrap;padding:16px 0;border-top:1px solid var(--border);border-bottom:1px solid var(--border)}}
.key-spec{{display:flex;flex-direction:column;gap:3px}}
.key-spec-l{{font-size:0.55rem;letter-spacing:0.1em;text-transform:uppercase;color:var(--ink3)}}
.key-spec-v{{font-size:1rem;font-weight:400;color:var(--ink);font-family:'Plus Jakarta Sans',sans-serif}}
.product-cta{{display:flex;gap:10px;flex-wrap:wrap}}
.btn-primary{{display:inline-flex;align-items:center;gap:10px;padding:14px 28px;background:var(--accent);color:#fff;font-size:0.72rem;letter-spacing:0.1em;text-transform:uppercase;font-weight:500;transition:all 0.22s var(--ease)}}
.btn-primary:hover{{background:#c42e25;transform:translateY(-2px)}}
.btn-outline{{display:inline-flex;align-items:center;gap:10px;padding:14px 24px;border:1px solid var(--border2);color:var(--ink2);font-size:0.72rem;letter-spacing:0.1em;text-transform:uppercase;font-weight:400;transition:all 0.22s}}
.btn-outline:hover{{border-color:var(--accent);color:var(--accent)}}
/* SECTIONS */
.section{{padding:clamp(40px,6vw,72px) var(--gutter)}}
.section-max{{max-width:var(--max);margin:0 auto}}
.section-title{{font-family:'Plus Jakarta Sans',sans-serif;font-size:clamp(1.6rem,3vw,2.2rem);font-weight:300;letter-spacing:-0.03em;line-height:1.1;color:var(--ink);margin-bottom:10px}}
.section-title strong{{font-weight:700}}
.section-title em{{font-style:italic;color:var(--ink2)}}
.eyebrow{{display:inline-flex;align-items:center;gap:10px;font-size:0.6rem;letter-spacing:0.2em;text-transform:uppercase;color:var(--ink3);margin-bottom:14px}}
.eyebrow::before{{content:'';width:20px;height:1px;background:var(--accent);display:block}}
/* SPECS */
.specs-grid{{display:grid;grid-template-columns:1fr 1fr;gap:32px}}
@media(max-width:700px){{.specs-grid{{grid-template-columns:1fr}}}}
.specs-block h3{{font-family:'Plus Jakarta Sans',sans-serif;font-size:0.8rem;font-weight:600;letter-spacing:0.05em;text-transform:uppercase;color:var(--ink);margin-bottom:14px;padding-bottom:8px;border-bottom:2px solid var(--accent);display:inline-block}}
.specs-row{{display:flex;justify-content:space-between;padding:10px 0;border-bottom:1px solid var(--border);font-size:0.82rem}}
.specs-row-l{{color:var(--ink2);font-weight:300}}
.specs-row-v{{color:var(--ink);font-weight:400;text-align:right}}
/* FEATURES */
.features-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:16px}}
.feature-card{{padding:20px;background:var(--bg2);border:1px solid var(--border);transition:border-color 0.2s}}
.feature-card:hover{{border-color:rgba(230,60,50,0.25)}}
.feature-card-icon{{width:28px;height:28px;display:flex;align-items:center;justify-content:center;background:rgba(230,60,50,0.1);margin-bottom:10px}}
.feature-card-icon svg{{width:14px;height:14px;color:var(--accent)}}
.feature-card h4{{font-family:'Plus Jakarta Sans',sans-serif;font-size:0.88rem;font-weight:500;color:var(--ink);margin-bottom:5px}}
.feature-card p{{font-size:0.74rem;color:var(--ink2);line-height:1.55;font-weight:300}}
/* SHOWCASE */
.showcase-wrap{{position:relative}}
.showcase-scroll{{display:flex;gap:12px;overflow-x:auto;scroll-snap-type:x mandatory;-webkit-overflow-scrolling:touch;scrollbar-width:none;margin-top:24px;padding-bottom:6px;scroll-behavior:smooth}}
.showcase-scroll::-webkit-scrollbar{{display:none}}
.showcase-card{{flex:0 0 clamp(280px,38vw,480px);scroll-snap-align:start;position:relative;overflow:hidden;border:1px solid var(--border);background:var(--bg2);cursor:pointer;transition:border-color 0.25s}}
.showcase-card:hover{{border-color:var(--accent)}}
.showcase-card img{{width:100%;height:280px;object-fit:cover;transition:transform 0.5s var(--ease)}}
.showcase-card:hover img{{transform:scale(1.04)}}
.showcase-card-label{{position:absolute;bottom:0;left:0;right:0;padding:12px 16px;background:linear-gradient(to top,rgba(0,0,0,0.7),transparent)}}
.showcase-card-label span{{font-size:0.62rem;letter-spacing:0.1em;text-transform:uppercase;color:#fff;font-weight:500}}
.showcase-arrow{{position:absolute;top:50%;transform:translateY(-50%);z-index:10;width:40px;height:40px;border-radius:50%;background:#fff;border:1px solid var(--border);display:flex;align-items:center;justify-content:center;cursor:pointer;box-shadow:0 2px 12px rgba(0,0,0,0.08);transition:all 0.2s;opacity:0.85}}
.showcase-arrow:hover{{opacity:1;border-color:var(--accent);box-shadow:0 4px 20px rgba(230,60,50,0.15)}}
.showcase-arrow svg{{width:16px;height:16px;color:var(--ink)}}
.showcase-arrow.prev{{left:-6px}}.showcase-arrow.next{{right:-6px}}
@media(max-width:700px){{.showcase-arrow{{display:none}}}}
.showcase-hint{{display:none;align-items:center;gap:8px;justify-content:flex-end;margin-top:12px;font-size:0.6rem;letter-spacing:0.12em;text-transform:uppercase;color:var(--ink3)}}
@media(max-width:700px){{.showcase-hint{{display:flex}}}}
/* MATERIALS */
.materials-list{{display:flex;gap:8px;flex-wrap:wrap}}
.material-tag{{padding:6px 12px;background:var(--bg2);border:1px solid var(--border);font-size:0.66rem;color:var(--ink2);letter-spacing:0.04em;transition:all 0.2s}}
.material-tag:hover{{border-color:var(--accent);color:var(--accent)}}
/* LIGHTBOX */
.lightbox{{display:none;position:fixed;inset:0;z-index:9999;background:rgba(0,0,0,0.92);align-items:center;justify-content:center}}
.lightbox.open{{display:flex}}
.lightbox img{{max-width:92vw;max-height:90vh;object-fit:contain}}
.lightbox-close{{position:absolute;top:24px;right:32px;background:none;border:none;color:#fff;font-size:2rem;cursor:pointer;opacity:0.6;transition:opacity 0.2s;font-family:'Inter',sans-serif}}
.lightbox-close:hover{{opacity:1}}
.lightbox-prev,.lightbox-next{{position:absolute;top:50%;transform:translateY(-50%);background:rgba(255,255,255,0.1);border:none;color:#fff;font-size:2rem;cursor:pointer;padding:12px 16px;transition:background 0.2s}}
.lightbox-prev:hover,.lightbox-next:hover{{background:rgba(255,255,255,0.2)}}
.lightbox-prev{{left:20px}}.lightbox-next{{right:20px}}
/* CTA */
.cta-band{{background:#1a1a1a;padding:clamp(40px,6vw,70px) var(--gutter);position:relative;overflow:hidden}}
.cta-band::before{{content:'';position:absolute;top:0;left:0;right:0;height:1px;background:linear-gradient(90deg,transparent,rgba(230,60,50,0.5),transparent)}}
.cta-inner{{max-width:var(--max);margin:0 auto;display:flex;align-items:center;justify-content:space-between;gap:32px;flex-wrap:wrap}}
.cta-text h2{{font-family:'Plus Jakarta Sans',sans-serif;font-size:clamp(1.4rem,2.5vw,2rem);font-weight:300;letter-spacing:-0.03em;color:#fff;margin-bottom:6px;line-height:1.1}}
.cta-text h2 strong{{font-weight:700}}
.cta-text h2 em{{font-style:italic;color:rgba(255,255,255,0.35)}}
.cta-text p{{font-size:0.82rem;color:rgba(255,255,255,0.4);font-weight:300;max-width:360px;line-height:1.7}}
.cta-btns{{display:flex;gap:10px;flex-wrap:wrap}}
/* FOOTER */
footer{{background:#1a1a1a;padding:40px var(--gutter) 20px}}
.footer-grid{{max-width:var(--max);margin:0 auto;display:grid;grid-template-columns:1.8fr 1fr 1fr;gap:32px;padding-bottom:32px;border-bottom:1px solid rgba(255,255,255,0.08)}}
.footer-brand img{{height:18px;filter:brightness(10);opacity:0.65;margin-bottom:12px}}
.footer-brand p{{font-size:0.74rem;color:rgba(255,255,255,0.3);line-height:1.7;font-weight:300;max-width:200px}}
.footer-col h5{{font-size:0.56rem;letter-spacing:0.16em;text-transform:uppercase;color:rgba(255,255,255,0.22);margin-bottom:12px;font-weight:500}}
.footer-col a,.footer-col p{{display:block;font-size:0.74rem;color:rgba(255,255,255,0.32);margin-bottom:6px;transition:color 0.2s;font-weight:300}}
.footer-col a:hover{{color:rgba(255,255,255,0.65)}}
.footer-bar{{max-width:var(--max);margin:18px auto 0;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:8px}}
.footer-bar p{{font-size:0.64rem;color:rgba(255,255,255,0.22);font-weight:300}}
.footer-bar a{{color:rgba(255,255,255,0.3);transition:color 0.2s}}
.footer-bar a:hover{{color:rgba(255,255,255,0.55)}}
.footer-bar .fa{{color:rgba(230,60,50,0.55)}}
@media(max-width:860px){{.footer-grid{{grid-template-columns:1fr 1fr}}.footer-brand{{grid-column:1/-1}}}}
/* SCROLL REVEAL */
.sr{{opacity:0;transform:translateY(16px);transition:opacity 0.6s var(--ease),transform 0.6s var(--ease)}}
.sr.in{{opacity:1;transform:translateY(0)}}
.d1{{transition-delay:0.07s}}.d2{{transition-delay:0.14s}}.d3{{transition-delay:0.21s}}
</style>
</head>
<body>

<nav class="nav">
  <div class="nav-logo">
    <a href="../index.html"><img src="https://wattsan.com/wp-content/uploads/wattsan_logo-1.svg" alt="Wattsan"></a>
    <div class="nav-logo-sep"></div>
    <div class="nav-logo-lv">Latvija <em>·</em> LV</div>
  </div>
  <div class="nav-links">
    <a href="../index.html#iekārtas">Iekārtas</a>
    <a href="../index.html#rezerves-dalas">Rezerves daļas</a>
    <a href="../index.html#par-mums">Par mums</a>
    <a href="../index.html#kontakts">Kontakti</a>
    <a href="https://bratus.lv" target="_blank">bratus.lv ↗</a>
  </div>
  <div class="nav-cta">
    <a href="https://bratus.lv" target="_blank" class="btn-ghost">Oficiālais pārstāvis ↗</a>
    <a href="../index.html#kontakts" class="btn-accent">Pieteikt</a>
  </div>
</nav>

{nav_sub_html}

<div class="breadcrumb">
  <div class="breadcrumb-inner">
    <a href="../index.html">Sākums</a>
    <span style="color:var(--ink3)">/</span>
    <a href="../index.html#iekārtas">Iekārtas</a>
    <span style="color:var(--ink3)">/</span>
    <span class="breadcrumb-current">{full_title}</span>
  </div>
</div>

<section class="product-hero">
  <div class="product-gallery sr">
    <img class="gallery-main" id="mainImg" src="{main_src}" alt="{full_title}">
    <div class="gallery-thumbs">{thumbs}
    </div>
  </div>
  <div class="product-info sr d1">
    <div class="product-badge"><span class="product-badge-dot"></span>Jaunais Modelis</div>
    <h1 class="product-title">{name} <strong>{label}</strong><br><em>{cat_lv}</em></h1>
    <p class="product-subtitle">{desc}</p>
    <div class="key-specs">
      <div class="key-spec"><div class="key-spec-l">Darba zona</div><div class="key-spec-v">{work_area}</div></div>
      <div class="key-spec"><div class="key-spec-l">Jauda</div><div class="key-spec-v">{power}</div></div>
      <div class="key-spec"><div class="key-spec-l">Ātrums</div><div class="key-spec-v">{speed}</div></div>
      <div class="key-spec"><div class="key-spec-l">Avots</div><div class="key-spec-v">{source}</div></div>
    </div>
    <div class="product-cta">
      <a href="../index.html#kontakts" class="btn-primary">Pieprasīt cenu <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg></a>
      <a href="https://wattsan.com/product/{slug}/" target="_blank" class="btn-outline">Skatīt wattsan.com ↗</a>
    </div>
  </div>
</section>

<section class="section" style="background:var(--bg2);border-top:1px solid var(--border)">
  <div class="section-max">
    <div class="eyebrow sr">Galvenās īpašības</div>
    <h2 class="section-title sr d1">Kāpēc <strong>{full_title}</strong>?</h2>
    <div class="features-grid" style="margin-top:28px">{features_html}
    </div>
  </div>
</section>

<section class="section" style="background:var(--bg);border-top:1px solid var(--border)">
  <div class="section-max">
    <div class="eyebrow sr">Galerija</div>
    <h2 class="section-title sr d1"><strong>Produkta</strong> <em>attēli</em></h2>
    <div class="showcase-wrap">
      <button class="showcase-arrow prev" onclick="scrollShowcase(-1)" aria-label="Iepriekšējais"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 18 9 12 15 6"/></svg></button>
      <div class="showcase-scroll" id="showcaseScroll">{gallery_html}
      </div>
      <button class="showcase-arrow next" onclick="scrollShowcase(1)" aria-label="Nākamais"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"/></svg></button>
    </div>
    <div class="showcase-hint"><span>Velc, lai redzētu vairāk</span><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg></div>
  </div>
</section>

<div class="lightbox" id="lightbox">
  <button class="lightbox-close" onclick="closeLightbox()">✕</button>
  <button class="lightbox-prev" onclick="navLightbox(-1)">‹</button>
  <img id="lightboxImg" src="" alt="">
  <button class="lightbox-next" onclick="navLightbox(1)">›</button>
</div>

<section class="section" style="background:#fff">
  <div class="section-max">
    <div class="eyebrow sr">Tehniskie parametri</div>
    <h2 class="section-title sr d1">Detalizēta <strong>specifikācija</strong></h2>
    <div class="specs-grid" style="margin-top:28px">
      <div class="specs-block sr"><h3>Optika</h3><div class="specs-table">{optics_html}
        </div>
      </div>
      <div class="specs-block sr d1"><h3>Mehānika & Elektronika</h3><div class="specs-table">{mech_html}
        </div>
      </div>
    </div>
    <div class="specs-block sr d2" style="margin-top:32px"><h3>Izmēri</h3><div class="specs-table">{dims_html}
      </div>
    </div>
  </div>
</section>

<section class="section" style="background:var(--bg2);border-top:1px solid var(--border)">
  <div class="section-max">
    <div class="eyebrow sr">Materiāli</div>
    <h2 class="section-title sr d1">Apstrādājamie <strong>materiāli</strong></h2>
    <div class="materials-list" style="margin-top:20px">{materials_tags}
    </div>
  </div>
</section>

<div class="cta-band">
  <div class="cta-inner">
    <div class="cta-text sr"><h2>Interesē <strong>{full_title}</strong>?<br><em>Pieprasiet cenu tūlīt</em></h2><p>Aizpildiet formu un saņemiet personalizētu piedāvājumu ar piegādi Latvijā 24 stundu laikā.</p></div>
    <div class="cta-btns sr d1"><a href="../index.html#kontakts" class="btn-primary">Pieprasīt cenu <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg></a><a href="https://bratus.lv" target="_blank" class="btn-outline" style="border-color:rgba(255,255,255,0.2);color:rgba(255,255,255,0.5)">bratus.lv ↗</a></div>
  </div>
</div>

<footer>
  <div class="footer-grid">
    <div class="footer-brand"><img src="https://wattsan.com/wp-content/uploads/wattsan_logo-1.svg" alt="Wattsan"><p>Wattsan — profesionālas CNC lāzera iekārtas. Officiālais pārstāvis Latvijā: SIA Bratus.</p></div>
    <div class="footer-col"><h5>Iekārtas</h5><a href="../index.html#iekārtas">CO2 Lāzeri</a><a href="../index.html#iekārtas">Metāla griešana</a><a href="../index.html#iekārtas">Marķieri</a></div>
    <div class="footer-col"><h5>Kontakti</h5><a href="tel:+37124424434">+371 24 424 434</a><a href="mailto:sales@bratus.lv">sales@bratus.lv</a><a href="https://bratus.lv" target="_blank">bratus.lv</a></div>
  </div>
  <div class="footer-bar"><p>© <span id="yr"></span> SIA <a href="https://bratus.lv" target="_blank">Bratus</a> · Wattsan oficiālais pārstāvis Latvijā</p></div>
</footer>

<script>
document.getElementById('yr').textContent=new Date().getFullYear();
const obs=new IntersectionObserver(e=>{{e.forEach(x=>{{if(x.isIntersecting){{x.target.classList.add('in');obs.unobserve(x.target)}}}})}},{{threshold:0.07}});
document.querySelectorAll('.sr').forEach(el=>obs.observe(el));
const galleryImages=[{",".join(f'"{IMG_BASE}/{img}"' for img in gallery_imgs[:6])}];
let currentIdx=0;
const lb=document.getElementById('lightbox'),lbImg=document.getElementById('lightboxImg');
function openLightbox(idx){{currentIdx=idx;lbImg.src=galleryImages[idx];lb.classList.add('open');document.body.style.overflow='hidden'}}
function closeLightbox(){{lb.classList.remove('open');document.body.style.overflow=''}}
function navLightbox(dir){{currentIdx=(currentIdx+dir+galleryImages.length)%galleryImages.length;lbImg.src=galleryImages[currentIdx]}}
lb.addEventListener('click',e=>{{if(e.target===lb)closeLightbox()}});
document.addEventListener('keydown',e=>{{if(lb.classList.contains('open')){{if(e.key==='Escape')closeLightbox();if(e.key==='ArrowLeft')navLightbox(-1);if(e.key==='ArrowRight')navLightbox(1);return}}if(e.key==='ArrowLeft')scrollShowcase(-1);if(e.key==='ArrowRight')scrollShowcase(1)}});
function scrollShowcase(dir){{const el=document.getElementById('showcaseScroll'),card=el.querySelector('.showcase-card');if(card)el.scrollBy({{left:dir*(card.offsetWidth+12),behavior:'smooth'}})}}
</script>
</body>
</html>'''
    
    path = os.path.join(PRODUCTS_DIR, f"{filename}.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  ✓ {filename}.html")


def generate_nav_sub(products, current_file, group_label):
    """Generate the sub-navigation bar for switching between models."""
    links = ""
    for p in products:
        fn, name, label = p[0], p[1], p[2]
        active = ' class="active"' if fn == current_file else ""
        links += f'<a href="{fn}.html"{active}>{label}</a>'
    return f'''<div class="nav-sub"><div class="nav-sub-inner"><span>{group_label}:</span>{links}</div></div>'''

# ── GENERATE ALL PAGES ──
print("Generating CO2 laser pages...")
for p in CO2_PRODUCTS:
    fn, name, label, cat, cat_lv, wa, power, speed, source, slug, main_img, gallery_imgs = p
    nav = generate_nav_sub(CO2_PRODUCTS, fn, "CO2 lāzeri")
    make_page(fn, name, label, cat, cat_lv, wa, power, speed, source, slug, main_img, gallery_imgs, CO2_FEATURES, CO2_OPTICS, CO2_MECH, CO2_DIMS, CO2_MATERIALS)
    # Inject nav_sub into the generated file
    path = os.path.join(PRODUCTS_DIR, f"{fn}.html")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    content = content.replace("{nav_sub_html}", nav)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("\nGenerating metal cutter pages...")
for p in METAL_PRODUCTS:
    fn, name, label, cat, cat_lv, wa, power, speed, source, slug, main_img, gallery_imgs = p
    nav = generate_nav_sub(METAL_PRODUCTS, fn, "Metāla griezēji")
    make_page(fn, name, label, cat, cat_lv, wa, power, speed, source, slug, main_img, gallery_imgs, METAL_FEATURES, METAL_OPTICS, METAL_MECH, METAL_DIMS, METAL_MATERIALS)
    path = os.path.join(PRODUCTS_DIR, f"{fn}.html")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    content = content.replace("{nav_sub}", nav)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("\nGenerating marker pages...")
for p in MARKER_PRODUCTS:
    fn, name, label, cat, cat_lv, wa, power, speed, source, slug, main_img, gallery_imgs = p
    nav = generate_nav_sub(MARKER_PRODUCTS, fn, "Marķieri")
    make_page(fn, name, label, cat, cat_lv, wa, power, speed, source, slug, main_img, gallery_imgs, MARKER_FEATURES, MARKER_OPTICS, MARKER_MECH, MARKER_DIMS, MARKER_MATERIALS)
    path = os.path.join(PRODUCTS_DIR, f"{fn}.html")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    content = content.replace("{nav_sub_html}", nav)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print(f"\n✅ Done! Generated {len(CO2_PRODUCTS) + len(METAL_PRODUCTS) + len(MARKER_PRODUCTS)} product pages in '{PRODUCTS_DIR}/'")
