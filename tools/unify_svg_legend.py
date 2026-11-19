"""Make BrainPalmSeq's SVG/PNG figure export match CellPalmSeq's.

- Scale bar: one rectangle with a smooth gradient (was 160-250 one-pixel
  strips), 160-220 px wide and 12 px tall, lined up under the first heatmap
  column, no outline. Caption ("Expression (unit)") and fonts unchanged.
- Title: "BrainPalmSeq: <dataset>" from the page's file name. It came from
  document.title, which the pages don't set, so the title line was empty.
  The figure widens to fit it.
- Group divider lines between comparison groups, as on screen.
- "Transparent background" option under the export buttons (SVG and PNG).

Run from the repository root:  python3 tools/unify_svg_legend.py
"""
import glob
import sys

EDITS = [
    (" const title=document.title.replace(/\\s+/g,' ').trim();",
     " const title='BrainPalmSeq: '+(location.pathname.split('/').filter(Boolean).pop()||'').replace(/\\.html$/,'').replace(/^BrainPalmSeq2026_/,'');"),
    (" const maxLabel=max.toFixed(3),bar=Math.min(250,Math.max(160,L.width-left));\n",
     " const maxLabel=max.toFixed(3),bar=Math.min(220,Math.max(160,L.width-left-right)),lx=pad+left;\n"),
    (" const W=Math.ceil(Math.max(L.width,legendW)+pad*2),unitY=head+L.height+16,by=unitY+8,barH=11,labelY=by+barH+13,H=Math.ceil(labelY+12);",
     " const W=Math.ceil(Math.max(pad+L.width,lx+legendW+right,pad+measureText(title,'bold 16px Arial'))+pad),"
     "unitY=head+L.height+16,by=unitY+8,barH=12,labelY=by+barH+13,H=Math.ceil(labelY+12);"),
    ("`<rect width=\"100%\" height=\"100%\" fill=\"white\"/>`,",
     "...($('.figure-transparent')?.checked?[]:[`<rect width=\"100%\" height=\"100%\" fill=\"white\"/>`]),"),
    (" parts.push(`<text x=\"${pad}\" y=\"${unitY}\" font-family=\"Arial\" font-size=\"12\" fill=\"#263649\">${esc(unit)}</text>`);\n"
     " for(let i=0;i<bar;i++)parts.push(`<rect x=\"${pad+i}\" y=\"${by}\" width=\"1\" height=\"${barH}\" fill=\"${palette[Math.floor(i/Math.max(1,bar-1)*(palette.length-1))]}\"/>`);\n"
     " parts.push(`<text x=\"${pad}\" y=\"${labelY}\" font-family=\"Arial\" font-size=\"11\" fill=\"#263649\">0</text>`,`<text x=\"${pad+bar}\" y=\"${labelY}\"",
     " // Separate comparison groups at their visual gaps.\n"
     " for(let i=1;i<L.cols.length;i++)if(L.positions[i]-L.positions[i-1]>cw+2){const x=x0+(L.positions[i-1]+cw+L.positions[i])/2;"
     "parts.push(`<line x1=\"${x}\" y1=\"${y0+top-4}\" x2=\"${x}\" y2=\"${y0+top+L.genes.length*rh+2}\" stroke=\"#8b9db0\" stroke-width=\"1.5\"/>`)}\n"
     " parts.push(`<text x=\"${lx}\" y=\"${unitY}\" font-family=\"Arial\" font-size=\"12\" fill=\"#263649\">${esc(unit)}</text>`);\n"
     " const stops=palette.map((c,i)=>`<stop offset=\"${(100*i/Math.max(1,palette.length-1)).toFixed(3)}%\" stop-color=\"${esc(c)}\"/>`).join('');\n"
     " parts.push(`<defs><linearGradient id=\"bps-legend-gradient\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"0\">${stops}</linearGradient></defs>`,"
     "`<rect x=\"${lx}\" y=\"${by}\" width=\"${bar}\" height=\"${barH}\" fill=\"url(#bps-legend-gradient)\"/>`);\n"
     " parts.push(`<text x=\"${lx}\" y=\"${labelY}\" font-family=\"Arial\" font-size=\"11\" fill=\"#263649\">0</text>`,`<text x=\"${lx+bar}\" y=\"${labelY}\""),
    ('<button type="button" class="export">Export CSV</button><button type="button" class="reset">Reset</button>',
     '<button type="button" class="export">Export CSV</button>'
     '<label style="font-size:11px;font-weight:400;display:flex;align-items:center;gap:4px;flex-basis:100%;margin:0">'
     '<input type="checkbox" class="figure-transparent"> Transparent background</label>'
     '<button type="button" class="reset">Reset</button>'),
]


def main():
    pages = sorted(p for p in glob.glob("BrainPalmSeq2026_*/BrainPalmSeq2026_*.html") if not p.endswith("_iframe.html"))
    if not pages:
        sys.exit("No heatmap pages found; run from the repository root.")
    for path in pages:
        t = open(path, encoding="utf-8").read()
        if "bps-legend-gradient" in t:
            sys.exit(f"{path}: already updated")
        for old, new in EDITS:
            if t.count(old) != 1:
                sys.exit(f"{path}: expected exactly one of {old[:70]!r}, found {t.count(old)}")
            t = t.replace(old, new)
        open(path, "w", encoding="utf-8").write(t)
    print(len(pages), "pages updated")


if __name__ == "__main__":
    main()
