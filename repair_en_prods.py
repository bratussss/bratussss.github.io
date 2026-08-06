"""REPAIR HTML corruption caused by short-word replacements (ar→with, etc.)"""
import os

DIR = r"d:\VS KODI\ROzo github\en\products"

# Revert the dangerous short-word corruptions
REPAIRS = [
    # Font corruption
    ('Plus+Jakwithta+Sans', 'Plus+Jakarta+Sans'),
    ('Plus Jakwithta Sans', 'Plus Jakarta Sans'),
    # HTML attribute corruption
    ('chwithset=', 'charset='),
    # Warranty corruption
    ('wwithranty', 'warranty'),
    ('wwithranties', 'warranties'),
    # Any other common corruptions
    ('backwithground', 'background'),
    ('backwithground-', 'background-'),
    (' withiable', ' variable'),
    ('fwithst', 'first'),
    ('fwith', 'first'),
    ('vwith', 'var '),
    ('stwitht', 'start'),
    ('mwithgin', 'margin'),
    ('pwithding', 'padding'),
    ('withgba', 'rgba'),
    ('withray', 'array'),
    ('chwith', 'char'),
    ('chwithCode', 'charCode'),
    ('clwithity', 'clarity'),
    ('populwith', 'popular'),
    ('regulwith', 'regular'),
    ('singulwith', 'singular'),
    ('pwithticulwith', 'particular'),
    ('similwith', 'similar'),
    ('familiwith', 'familiar'),
    ('linewith', 'linear'),
    ('clewith', 'clear'),
    ('appewith', 'appear'),
    ('hewith', 'hear'),
    ('yeith', 'year'),
    ('yeiths', 'years'),
    ('neith', 'near'),
    ('geith', 'gear'),
    ('beith', 'bear'),
    ('weith', 'wear'),
    ('peith', 'pear'),
    ('teith', 'tear'),
    ('withtist', 'artist'),
    ('withticle', 'article'),
    ('withtifact', 'artifact'),
    ('withea', 'area'),
    ('withound', 'around'),
    ('withen', 'arena'),
    ('withmy', 'army'),
    ('withgue', 'argue'),
    ('withrow', 'arrow'),
    ('withise', 'arise'),
    ('withrive', 'arrive'),
    ('withomatic', 'aromatic'),
    ('pwithty', 'party'),
    ('pwitht', 'part'),
    ('pwithtner', 'partner'),
    ('pwithticip', 'particip'),
    ('pwithticul', 'particular'),
    ('stwith', 'star'),
    ('stwithtup', 'startup'),
    ('stwithter', 'starter'),
    ('withgent', 'argent'),
    ('withch', 'arch'),
    ('withc', 'arc'),
    ('witht', 'art'),
    ('withd', 'ard'),
    ('withm', 'arm'),
    ('wth', 'war'),
    ('gwithden', 'garden'),
    ('gwithbage', 'garbage'),
    ('cwithbon', 'carbon'),
    ('cwithd', 'card'),
    ('cwithgo', 'cargo'),
    ('cwithpet', 'carpet'),
    ('cwitht', 'cart'),
    ('cwithve', 'carve'),
    ('pwithk', 'park'),
    ('pwithse', 'parse'),
    ('spwithk', 'spark'),
    ('spwithse', 'sparse'),
    ('shwithp', 'sharp'),
    ('shwithk', 'shark'),
    ('shwithe', 'share'),
    ('smwitht', 'smart'),
    ('standwithd', 'standard'),
    ('standwithrd', 'standard'),
    ('collwith', 'collar'),
    ('dollwith', 'dollar'),
    ('pillwith', 'pillar'),
    ('cellulwith', 'cellular'),
    ('singulwith', 'singular'),
    ('regulwith', 'regular'),
    ('populwith', 'popular'),
    ('pwithallel', 'parallel'),
    ('withbit', 'arbit'),
    ('rwithity', 'rarity'),
    ('rwithely', 'rarely'),
    ('bwith', 'bar'),
    ('cwith', 'car'),
    ('fwith', 'far'),
    ('jwith', 'jar'),
    ('mwith', 'mar'),
    ('pwith', 'par'),
    ('twith', 'tar'),
    ('wwith', 'war'),
    ('withtget', 'target'),
    ('withtist', 'artist'),
    ('withtistic', 'artistic'),
    ('withtillery', 'artillery'),
    ('depwitht', 'depart'),
    ('apwitht', 'apart'),
    ('compwitht', 'compart'),
    ('compwithe', 'compare'),
    ('prepwithe', 'prepare'),
    ('declwith', 'declare'),
    ('withsenal', 'arsenal'),
    ('withsenic', 'arsenic'),
    # Other short-word corruptions  
    ('isfirst', 'first'),  # 'ir' was never replaced
    ('function', 'function'),  # should be fine
]

count = 0
for root, dirs, files in os.walk(DIR):
    for f in files:
        if f == 'index.html':
            src = os.path.join(root, f)
            with open(src, 'r', encoding='utf-8') as fh:
                c = fh.read()
            changed = False
            for old, new in REPAIRS:
                if old in c:
                    c = c.replace(old, new)
                    changed = True
            if changed:
                with open(src, 'w', encoding='utf-8') as fh:
                    fh.write(c)
                count += 1
                slug = os.path.basename(root)
                print(f"  REPAIRED: {slug}")

print(f"\nRepaired {count} files")
