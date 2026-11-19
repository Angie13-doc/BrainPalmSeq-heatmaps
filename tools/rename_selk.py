"""Rename Selk to Selenok in the three datasets that used the former symbol.

Cembrowski2016_Hipposeq, Li2019_Microglia and Zhang2014_Cortex labelled
Selenok (selenoprotein K) by its former symbol, Selk. The heatmap page's
gene list and its _data.csv now use Selenok, like the other datasets.

Run from the repository root:  python3 tools/rename_selk.py
"""
import re
import sys

DATASETS = {"Cembrowski2016_Hipposeq": 20, "Li2019_Microglia": 9, "Zhang2014_Cortex": 7}


def main():
    for name, csv_rows in DATASETS.items():
        base = f"BrainPalmSeq2026_{name}/BrainPalmSeq2026_{name}"
        t = open(base + ".html", encoding="utf-8").read()
        if t.count('"Selk"') != 1:
            sys.exit(f"{base}.html: expected one \"Selk\", found {t.count(chr(34) + 'Selk' + chr(34))}")
        open(base + ".html", "w", encoding="utf-8").write(t.replace('"Selk"', '"Selenok"'))
        t = open(base + "_data.csv", encoding="utf-8", newline="").read()
        t, n = re.subn(r"(?m)^Selk,", "Selenok,", t)
        if n != csv_rows or re.search(r"\bSelk\b", t):
            sys.exit(f"{base}_data.csv: expected {csv_rows} Selk rows, found {n}")
        open(base + "_data.csv", "w", encoding="utf-8", newline="").write(t)
        print("renamed in", name)


if __name__ == "__main__":
    main()
