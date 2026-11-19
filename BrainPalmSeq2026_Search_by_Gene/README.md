# BrainPalmSeq — Search by Gene

GitHub Pages-ready, standalone static gene-expression explorer.

## Files

- `index.html`: explorer (header-free version). All data used by the explorer are embedded.
- `data/all_explorer_expression.csv`: every gene/population expression record the page held at its original release (5 November 2026), including units and the embedded metadata as JSON. Not limited to top-20 views.
- `data/brainwide_biccn_source.csv`: the separately supplied BICCN source matrix with descriptor and neuron-type columns; retained for provenance and comparison.
- `BrainPalmSeq2026_Search_by_Gene_iframe.html`: ready-to-paste WordPress embed for the live page.

## Live page

https://angie13-doc.github.io/BrainPalmSeq-heatmaps/BrainPalmSeq2026_Search_by_Gene/ — paste `BrainPalmSeq2026_Search_by_Gene_iframe.html` into a WordPress Custom HTML block to embed it. The old address, `BrainPalmSeq_Search_by_Gene/`, forwards here.

## Data provenance and limitations

`data/all_explorer_expression.csv` was exported with the original Search by Gene release (5 November 2026) and lists the expression records the page held then, across all genes and datasets, with their dataset-specific units. This is not a merged raw single-cell matrix. Different expression units must not be directly compared. The separate BICCN source CSV contains richer metadata, but **do not assume that every descriptor from the source CSV is present in the packaged HTML hover**; the HTML's embedded metadata is separately preserved in the all-explorer CSV.

This package does not modify the separately approved individual heatmaps. Annotation provenance and live browser interactions have not been independently validated.

## Included expression record counts

- `Yao2023_BICCN_Subclasses`: 13,520 gene-population records
- `Zeisel2018_MouseBrain`: 10,600 gene-population records
- `Saunders2018_DropViz`: 4,040 gene-population records
- `Siletti2023_HumanBrain`: 1,240 gene-population records
- `Sjostedt2020_ProteinAtlas`: 507 gene-population records
