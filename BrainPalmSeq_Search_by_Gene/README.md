# BrainPalmSeq — Search by Gene

GitHub Pages-ready, standalone static gene-expression explorer.

## Files

- `index.html`: explorer (header-free version). All data used by the explorer are embedded.
- `data/all_explorer_expression.csv`: **every gene/population expression record embedded in the HTML**, including units and the HTML's embedded metadata as JSON. Not limited to top-20 views.
- `data/brainwide_biccn_source.csv`: the separately supplied BICCN source matrix with descriptor and neuron-type columns; retained for provenance and comparison.
- `iframe_embed.html`: copy/paste WordPress iframe example. Replace `YOUR_GITHUB_USERNAME` and `YOUR_REPOSITORY` with your actual GitHub Pages path.

## GitHub Pages setup

Unzip, then upload `index.html`, `README.md`, `iframe_embed.html`, and the `data/` folder to a GitHub repository. Enable **Settings → Pages → Deploy from a branch → main → /(root)**. The explorer is at `https://YOUR_GITHUB_USERNAME.github.io/YOUR_REPOSITORY/`. Paste the iframe from `iframe_embed.html` into a WordPress Custom HTML block and replace the placeholder URL.

## Data provenance and limitations

The CSV exports exactly the expression records in the packaged HTML, across all genes and datasets, with their dataset-specific units. This is not a merged raw single-cell matrix. Different expression units must not be directly compared. The separate BICCN source CSV contains richer metadata, but **do not assume that every descriptor from the source CSV is present in the packaged HTML hover**; the HTML's embedded metadata is separately preserved in the all-explorer CSV.

This package does not modify the separately approved individual heatmaps. Annotation provenance and live browser interactions have not been independently validated.

## Included expression record counts

- `Yao2023_BICCN_Subclasses`: 13,520 gene-population records
- `Zeisel2018_MouseBrain`: 10,600 gene-population records
- `Saunders2018_DropViz`: 4,040 gene-population records
- `Siletti2023_HumanBrain`: 1,240 gene-population records
- `Sjostedt2020_ProteinAtlas`: 507 gene-population records
