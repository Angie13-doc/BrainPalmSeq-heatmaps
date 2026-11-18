"""Add an "Expression scale" option (original values or log2(value + 1)) to the
BrainPalmSeq pages whose units are not already logged.

Same control as CellPalmSeq's CCLE, Sanger and HPA pages. The log option
changes colours only: heatmap tiles, the summary band, the legend and its
maximum, "Fit current selection", and SVG/PNG figure colours. CSV export and
ranking keep the original values. The hover shows the original value with its
unit and, when the log scale is on, the log value too, e.g.
"39.850000 FPKM (log₂(FPKM + 1) = 5.352)". Reset returns to original values.

Run from the repository root:  python3 tools/add_log_scale_option.py
"""
import sys

# Pages whose expression is not already on a log scale, and their unit.
PAGES = {
    "BrainPalmSeq2026_Zhang2014_Cortex": "FPKM",
    "BrainPalmSeq2026_Cembrowski2016_Hipposeq": "FPKM",
    "BrainPalmSeq2026_Sjostedt2020_ProteinAtlas": "pTPM",
}


def edits(unit, legend):
    log_label = f"log₂({unit} + 1)"
    return [
        ('<option value="dynamic">Fit current selection</option></select></div>',
         '<option value="dynamic">Fit current selection</option></select></div>\n'
         '<div class="colour-transform-control" style="display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin:8px 0">'
         '<label for="colour-transform-select">Expression scale</label><select id="colour-transform-select" aria-label="Expression scale">'
         f'<option value="raw">Original {unit} (default)</option><option value="log">{log_label}</option></select>'
         '<span style="font-size:11px;color:#657080">Hover and CSV retain original values</span></div>'),
        ("const fixedMax=rows.reduce(",
         "// Expression scale: colours use original values or log2(value + 1); hover, CSV and ranking keep originals.\n"
         "const colourTransform=$('#colour-transform-select');const colourValue=r=>{const v=Number(r.Expression);"
         "return Number.isFinite(v)?(colourTransform.value==='log'?Math.log2(Math.max(0,v)+1):v):NaN};"
         "colourTransform.addEventListener('change',()=>render());\n"
         "const fixedMax=rows.reduce("),
        ("const high=scale.value==='fixed'?fixedMax:filtered.reduce((v,r)=>Math.max(v,Number.isFinite(r.Expression)?r.Expression:0),0);"
         "$('.high').textContent=high.toFixed(3);",
         "const high=scale.value==='fixed'?(colourTransform.value==='log'?Math.log2(fixedMax+1):fixedMax)"
         ":filtered.reduce((v,r)=>{const c=colourValue(r);return Number.isFinite(c)?Math.max(v,c):v},0);"
         "$('.high').textContent=high.toFixed(3);"
         f"$('.legend span:first-child').textContent=colourTransform.value==='log'?'Colour: {log_label}':'{legend}';"),
        ("colour:r=>Number(r.Expression)", "colour:r=>colourValue(r)"),
        ("const color=Number.isFinite(r.Expression)?hex(r.Expression):'#333333';",
         "const cval=colourValue(r),color=Number.isFinite(cval)?hex(cval):'#333333';"),
        ("['Expression',Number.isFinite(r.Expression)?r.Expression.toFixed(6):'NA']",
         f"['Expression',Number.isFinite(r.Expression)?r.Expression.toFixed(6)+' {unit}'+(colourTransform.value==='log'"
         f"?' ({log_label} = '+Math.log2(Math.max(0,r.Expression)+1).toFixed(3)+')':''):'NA']"),
        ("scale.value='fixed';", "scale.value='fixed';colourTransform.value='raw';"),
    ]


def main():
    for folder, unit in PAGES.items():
        path = f"{folder}/{folder}.html"
        t = open(path, encoding="utf-8").read()
        if "colour-transform-select" in t:
            sys.exit(f"{path}: already has an Expression scale option")
        start = t.find('<div class="legend"><span>') + len('<div class="legend"><span>')
        legend = t[start:t.index("</span>", start)]
        for old, new in edits(unit, legend):
            if t.count(old) != 1:
                sys.exit(f"{path}: expected exactly one of {old[:70]!r}, found {t.count(old)}")
            t = t.replace(old, new)
        open(path, "w", encoding="utf-8").write(t)
        print("added to", path, f"({unit}; legend '{legend}')")


if __name__ == "__main__":
    main()
