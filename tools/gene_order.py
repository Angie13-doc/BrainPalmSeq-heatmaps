"""Order heatmap genes by function, and fix the Lypla2 spelling.

Gene rows (and gene ticks, CSV) were sorted alphabetically. They now run:
  de-S-acylating enzymes:  Abhd4 ... Abhd17c, Lypla1, Lypla2, Ppt1
  accessory proteins:      Selenok (Selk in three datasets), Golga7, Golga7b
  S-acylating enzymes:     Zdhhc1 ... Zdhhc25
with numbers in numeric order inside each group. Human gene symbols
(Siletti2023) sort the same way.

The Sjostedt2020 (Human Protein Atlas) data spelled Lypla2 as "Lylpa2", so it
sorted above Lypla1 and Search by Gene's Lypla2 missed that dataset. Fixed in
the heatmap page, its CSV, Search by Gene and Search by Gene's CSV.

Run from the repository root:  python3 tools/gene_order.py
"""
import glob
import re
import sys

OLD_SORT = "geneNames=[...new Set(rows.map(r=>r.Gene))].sort(collator.compare)"
NEW_SORT = ("geneNames=[...new Set(rows.map(r=>r.Gene))].sort((a,b)=>bpsGeneGroup(a)-bpsGeneGroup(b)||collator.compare(a,b))")
GROUP_FN = ("// Gene order: de-S-acylating enzymes, then accessory proteins, then ZDHHC S-acylating enzymes.\n"
            "const bpsGeneGroup=g=>{const s=String(g).toLowerCase();return /^abhd/.test(s)?0:/^lypla\\d/.test(s)?1:/^ppt/.test(s)?2:"
            "/^(selenok|selk)$/.test(s)?3:/^golga/.test(s)?4:/^zdhhc/.test(s)?5:6};\n")
TYPO = "Lylpa2"


def replace_once(t, old, new, path):
    if t.count(old) != 1:
        sys.exit(f"{path}: expected exactly one of {old[:70]!r}, found {t.count(old)}")
    return t.replace(old, new)


def main():
    pages = sorted(p for p in glob.glob("BrainPalmSeq2026_*/BrainPalmSeq2026_*.html") if not p.endswith("_iframe.html"))
    if not pages:
        sys.exit("No heatmap pages found; run from the repository root.")
    for path in pages:
        t = open(path, encoding="utf-8").read()
        if "bpsGeneGroup" in t:
            sys.exit(f"{path}: already updated")
        t = replace_once(t, OLD_SORT, NEW_SORT, path)
        i = t.index(NEW_SORT)
        line = t.rfind("\n", 0, i) + 1
        t = t[:line] + GROUP_FN + t[line:]
        if "Sjostedt2020" in path:
            t = replace_once(t, '"Lypla1","Lylpa2"', '"Lypla1","Lypla2"', path)
        open(path, "w", encoding="utf-8").write(t)
    print(len(pages), "pages reordered")

    search = "BrainPalmSeq2026_Search_by_Gene/index.html"
    t = open(search, encoding="utf-8").read()
    t = replace_once(t, '"Lylpa2":[', '"Lypla2":[', search)
    open(search, "w", encoding="utf-8").write(t)
    for path, pattern in [("BrainPalmSeq2026_Sjostedt2020_ProteinAtlas/BrainPalmSeq2026_Sjostedt2020_ProteinAtlas_data.csv", r"(?m)^Lylpa2,"),
                          ("BrainPalmSeq2026_Search_by_Gene/data/all_explorer_expression.csv", r",Lylpa2,")]:
        t = open(path, encoding="utf-8", newline="").read()
        t, n = re.subn(pattern, lambda m: m.group(0).replace(TYPO, "Lypla2"), t)
        if n != 13:
            sys.exit(f"{path}: expected 13 Lylpa2 rows, found {n}")
        open(path, "w", encoding="utf-8", newline="").write(t)
    print("Lylpa2 -> Lypla2 fixed")


if __name__ == "__main__":
    main()
