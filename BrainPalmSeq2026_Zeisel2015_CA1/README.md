# BrainPalmSeq2026_Zeisel2015_CA1

Zeisel et al. (2015) CA1 hippocampus — BrainPalmSeq interactive heatmap.

## Relationship to S1

This heatmap was made by reusing the **exact HTML/CSS/JavaScript template** from `BrainPalmSeq2026_Zeisel2015_S1` in the existing BrainPalmSeq 2026 GitHub release, replacing only the embedded dataset and dataset-specific naming.

- 40 genes × 26 CA1 metacell populations = 1,040 expression records.
- Original input: `BPSmatrix_Zeisel2015_CA1.csv` (included unchanged).
- The template retains the same controls, palettes, hover design, rank/filter functions, zoom, downloads and layout as S1.
- The generated long-form CSV matches the S1 release schema (`Gene`, `ClusterName`, `Region`, `Class`, `Region2`, `Probable_location`, `Neurotransmitter`, `MarkerGenes`, `Description`, `Expression`, `SourceFile`).
- The descriptive metadata is drawn from the source CSV; unprovided neurotransmitter and marker-gene fields remain empty, not inferred.

## Publishing

Upload the entire `BrainPalmSeq2026_Zeisel2015_CA1` folder to the root of your `BrainPalmSeq-heatmaps` repository, alongside `BrainPalmSeq2026_Zeisel2015_S1`.

GitHub Pages URL:
`https://angie13-doc.github.io/BrainPalmSeq-heatmaps/BrainPalmSeq2026_Zeisel2015_CA1/BrainPalmSeq2026_Zeisel2015_CA1.html`

Paste `BrainPalmSeq2026_Zeisel2015_CA1_iframe.html` into a WordPress Custom HTML block.

## Notes

Values are preserved as supplied; no unit conversion was applied. The source matrix does not specify expression units. The HTML was structurally matched to the existing S1 template, but a live browser interaction test has not been performed.
