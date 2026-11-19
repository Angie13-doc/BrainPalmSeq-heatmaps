"""Correct Zeisel2015 cell-type labels.

CA1: three neighbouring populations carried each other's cell type
(Oligo6 "Endothelial-mural", Peric "Microglia", Pvm1 "Oligodendrocytes").
Their names, the S1 labelling and their expression profiles (each best
matches the S1 population of the same name) show only the labels moved.
Now: Oligo6 -> Oligodendrocytes, Peric (pericytes) -> Endothelial-mural.

CA1 and S1: microglia (Mgl) and perivascular macrophages (Pvm) are grouped
as "Microglia/macrophages" (was "Microglia"). CA1's "Interneuron" becomes
"Interneurons", as in S1.

Changes the cell type in the population name ("Peric CA1 | ..."), Class,
hover "Cell Type", the description, and the _data.csv rows.

Run from the repository root:  python3 tools/fix_zeisel2015_cell_types.py
"""
import json
import re
import sys

FIX = {
    "Zeisel2015_CA1": {"Oligo6 CA1": "Oligodendrocytes", "Peric CA1": "Endothelial-mural",
                       "Pvm1 CA1": "Microglia/macrophages", "Mgl2 CA1": "Microglia/macrophages",
                       **{f"Int{i} CA1": "Interneurons" for i in (2, 3, 4, 5, 6, 7, 8, 13)}},
    "Zeisel2015_S1": {"Mgl1 S1": "Microglia/macrophages", "Mgl2 S1": "Microglia/macrophages",
                      "Pvm1 S1": "Microglia/macrophages", "Pvm2 S1": "Microglia/macrophages"},
}
SCRIPT = re.compile(r'(<script type="application/json" class="bps-data">)(.*?)(</script>)', re.S)


def main():
    for name, fixes in FIX.items():
        base = f"BrainPalmSeq2026_{name}/BrainPalmSeq2026_{name}"
        t = open(base + ".html", encoding="utf-8").read()
        m = SCRIPT.search(t)
        d = json.loads(m.group(2))
        if json.dumps(d, separators=(",", ":"), ensure_ascii=False) != m.group(2):
            sys.exit(f"{base}.html: data does not round-trip; not editing")
        C = d["compact"]
        ck = C["ck"]
        name_i, class_i = ck.index("ClusterName"), ck.index("Class")
        old_of = {}
        for row in C["cells"]:
            mid, _, old = row[name_i].partition(" | ")
            if mid not in fixes:
                continue
            new = fixes[mid]
            if old != row[class_i]:
                sys.exit(f"{base}: {mid} name and Class disagree")
            if old == new:
                sys.exit(f"{base}: {mid} is already {new}; already fixed?")
            old_of[mid] = old
            old_name, new_name = row[name_i], f"{mid} | {new}"
            for i, v in enumerate(row):
                if isinstance(v, str):
                    row[i] = v.replace(f"Cell Type: {old};", f"Cell Type: {new};")
            row[name_i], row[class_i] = new_name, new
            hm = d["hoverMetadata"]
            hm[new_name] = [[k, new if k == "Cell Type" else v] for k, v in hm.pop(old_name)]
        if set(old_of) != set(fixes):
            sys.exit(f"{base}: populations not found: {set(fixes) - set(old_of)}")
        t = t[:m.start(2)] + json.dumps(d, separators=(",", ":"), ensure_ascii=False) + t[m.end(2):]
        open(base + ".html", "w", encoding="utf-8").write(t)

        lines = open(base + "_data.csv", encoding="utf-8", newline="").read().split("\n")
        changed = 0
        for i, line in enumerate(lines):
            for mid, new in fixes.items():
                old = old_of[mid]
                prefix = f",{mid} | {old},"
                if prefix in line:
                    line = line.replace(prefix, f",{mid} | {new},", 1)
                    line = line.replace(f",{old},", f",{new},", 1)  # Class column
                    line = line.replace(f"Cell Type: {old};", f"Cell Type: {new};")
                    lines[i] = line
                    changed += 1
        if changed != 40 * len(fixes):
            sys.exit(f"{base}_data.csv: expected {40 * len(fixes)} rows, changed {changed}")
        open(base + "_data.csv", "w", encoding="utf-8", newline="").write("\n".join(lines))
        print(name, {k: f"{old_of[k]} -> {v}" for k, v in fixes.items()})


if __name__ == "__main__":
    main()
