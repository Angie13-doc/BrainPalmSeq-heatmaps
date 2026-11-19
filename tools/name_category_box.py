"""Give the category box one consistent name per kind of grouping.

The category dropdown (#bps-broad-label) said "Cell categories" on every
page, also where its categories are regions. Names now follow one scheme
on both sites (BrainPalmSeq and CellPalmSeq):
  cell types -> "Cell categories"   anatomical -> "Regions"
  cancer/disease -> "Primary disease"   tissues -> "Tissues"   samples -> "Samples"
Its heading, its "All ..." button and dropdown text, and its "All ...
selected" count change together. Cembrowski2016 ("Experiments"), Marques2016
("Developmental stages") and the cell-type pages already fit and are unchanged.

Zeisel2015_CA1 and _S1: every population has the same Region2 (CA1
hippocampus / SS-cortex), so the box offered a single region. It now groups
by Class, which holds the metadata's "Cell Type".

Run from the repository root:  python3 tools/name_category_box.py
"""
import re
import sys


def rename(path, heading, all_text, extra=()):
    t = open(path, encoding="utf-8").read()
    m = re.search(r'<label id="bps-broad-label">([^<]*)</label>', t)
    old_all = re.search(r'class="broad-all">([^<]*)<', t).group(1)
    n = t.count(old_all)
    if n not in (3, 4):
        sys.exit(f"{path}: expected 3-4 of {old_all!r}, found {n}")
    for old, new in extra:
        if t.count(old) != 1:
            sys.exit(f"{path}: expected exactly one of {old[:60]!r}")
        t = t.replace(old, new)
    t = t.replace(m.group(0), f'<label id="bps-broad-label">{heading}</label>')
    if old_all != all_text:
        t = t.replace(old_all, all_text)
    open(path, "w", encoding="utf-8").write(t)
    print(f"{path.split('/')[0]}: {m.group(1)!r} -> {heading!r}; {old_all!r} -> {all_text!r}")

PAGES = {
    "OLeary2020_Amygdala": ("Regions", "All regions"),
    "Phillips2019_ThalamusNuclei": ("Regions", "All regions"),
    "Saunders2018_DropViz": ("Regions", "All regions"),
    "Sjostedt2020_ProteinAtlas": ("Regions", "All regions"),
    "Zeisel2018_MouseBrain": ("Regions", "All regions"),
    # Single cells retrogradely labelled from five cortical areas (auditory, motor, ...).
    "Phillips2019_ThalamusSingleCell": ("Cortical projection targets", "All cortical projection targets"),
}
BY_CELL_TYPE = ["Zeisel2015_CA1", "Zeisel2015_S1"]
OLD_FIELD = "const broadField=[...cells.values()].some(r=>String(r.Region2||'').trim())?'Region2':'Class';"
NEW_FIELD = "const broadField='Class';"


def main():
    for name, (heading, all_text) in PAGES.items():
        rename(f"BrainPalmSeq2026_{name}/BrainPalmSeq2026_{name}.html", heading, all_text)
    for name in BY_CELL_TYPE:
        rename(f"BrainPalmSeq2026_{name}/BrainPalmSeq2026_{name}.html", "Cell categories", "All cell categories",
               extra=[(OLD_FIELD, NEW_FIELD)])


if __name__ == "__main__":
    main()
