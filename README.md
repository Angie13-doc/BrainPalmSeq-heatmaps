# BrainPalmSeq heatmaps

Interactive heatmaps of how the genes that control **protein S-palmitoylation** are expressed across cell types and regions of the nervous system, built from published RNA-seq datasets. Each dataset is a self-contained web page, served with GitHub Pages and embedded in the BrainPalmSeq WordPress site.

## Goal

S-palmitoylation is a reversible lipid modification that controls where proteins go and how they behave. It is added by the ZDHHC palmitoyl acyltransferases (with accessory proteins) and removed by depalmitoylating enzymes. BrainPalmSeq curates the expression of these genes from public RNA-seq datasets so researchers can see which cell types and regions express which enzymes. The resource and its analysis are described in Wild et al., *eLife* 2022 ([Citation](#citation)).

This repository holds the 2026 heatmap release: one interactive heatmap per dataset, plus a Search by Gene page that compares one gene across datasets.

**Genes shown (40):** the ZDHHC enzymes (*Zdhhc1*–*9* and *11*–*25* in mouse; *ZDHHC1*–*9*, *11*, *11B* and *12*–*24* in human), the depalmitoylating enzymes *Lypla1*, *Lypla2* and *Ppt1*, ABHD-family hydrolases (*Abhd4*, *Abhd6*, *Abhd10*, *Abhd11*, *Abhd12*, *Abhd13*, *Abhd16a*, *Abhd17a*–*c*), and the accessory proteins *Golga7*, *Golga7b* and *Selenok*. Gene symbols keep the source dataset's spelling: mouse datasets use *Zdhhc1*, the human dataset (Siletti 2023) uses *ZDHHC1*.

## Live pages

Each heatmap lives at
`https://angie13-doc.github.io/BrainPalmSeq-heatmaps/<folder>/<folder>.html`,
for example [Chen 2017 hypothalamus](https://angie13-doc.github.io/BrainPalmSeq-heatmaps/BrainPalmSeq2026_Chen2017_Hypothalamus/BrainPalmSeq2026_Chen2017_Hypothalamus.html). The Search by Gene page is at [`BrainPalmSeq_Search_by_Gene/`](https://angie13-doc.github.io/BrainPalmSeq-heatmaps/BrainPalmSeq_Search_by_Gene/).

`WORDPRESS_EMBEDS.md` has a ready-to-paste `<iframe>` for every dataset, and each dataset folder has the same snippet as `<folder>_iframe.html`. The iframes load the live page from GitHub Pages, so a change merged into `main` reaches the WordPress pages without editing them. GitHub Pages lets browsers keep a page for up to 10 minutes, so an update can take that long to appear; a hard refresh (Cmd/Ctrl+Shift+R) on the page itself shows it at once.

## Datasets

All folders start with `BrainPalmSeq2026_`. Columns are populations as defined by each study; units are the study's own and are **not comparable across datasets**.

| Folder | Populations | Expression units | Notes |
|---|---:|---|---|
| `Batiuk2020_Astrocytes` | 9 | Mean log₂(counts per 10,000 + 1) | |
| `Cembrowski2016_Hipposeq` | 20 | FPKM | Four related but distinct experiments; compare across them cautiously. Short axis labels; full names in hover and CSV. Optional log₂(FPKM + 1) colours. |
| `Chen2017_Hypothalamus` | 47 | Mean log₂(counts per 10,000 + 1) | |
| `Gokce2016_Striatum` | 10 | Mean log₂(counts per 10,000 + 1) | |
| `Kozareva2021_Cerebellum` | 46 | Mean log₂(counts per 10,000 + 1) | |
| `Li2019_Microglia` | 9 | Mean log₂(counts per 10,000 + 1) | |
| `Marques2016_Oligodendrocytes` | 22 | Mean log₂(counts per 10,000 + 1) | Juvenile and adult are categorical age groups, not a continuous trajectory. |
| `OLeary2020_Amygdala` | 6 | Mean log₂(counts per 10,000 + 1) | |
| `Phillips2019_ThalamusNuclei` | 22 | Mean log₂(counts per 10,000 + 1) | Normalisation provisionally assigned, not independently verified. |
| `Phillips2019_ThalamusSingleCell` | 17 | Mean log₂(counts per 10,000 + 1) | |
| `Rosenberg2018_Neonatal` | 73 | Mean log₂(counts per 10,000 + 1) | |
| `Saunders2018_DropViz` | 565 | Mean log₂(counts per 10,000 + 1) | |
| `Siletti2023_HumanBrain` | 461 | Mean log₂(counts per 10,000 + 1) | Human; uppercase gene symbols. |
| `Sjostedt2020_ProteinAtlas` | 13 | Protein-coding transcripts per million (pTPM) | Optional log₂(pTPM + 1) colours. |
| `Yao2020_AllenBrainMap` | 387 | Trimmed mean (25%–75%) log₂(CPM + 1) | |
| `Yao2023_BICCN_Astrocyte` | 60 | Mean log₂(counts per million; CPM) | Allen whole-brain transcriptomic clusters |
| `Yao2023_BICCN_GABAergic` | 2,025 | Mean log₂(counts per million; CPM) | Allen clusters |
| `Yao2023_BICCN_Glutamatergic` | 2,597 | Mean log₂(counts per million; CPM) | Allen clusters |
| `Yao2023_BICCN_Immune` | 11 | Mean log₂(counts per million; CPM) | Allen clusters |
| `Yao2023_BICCN_Neuromodulatory` | 583 | Mean log₂(counts per million; CPM) | Allen clusters |
| `Yao2023_BICCN_OlfactoryEnsheathing` | 4 | Mean log₂(counts per million; CPM) | Allen clusters |
| `Yao2023_BICCN_Oligodendrocyte` | 23 | Mean log₂(counts per million; CPM) | Allen clusters |
| `Yao2023_BICCN_Subclasses` | 338 | Mean log₂(counts per million; CPM) | Allen subclasses |
| `Yao2023_BICCN_Vascular` | 19 | Mean log₂(counts per million; CPM) | Allen clusters |
| `Zeisel2015_CA1` | 26 | Mean log₂(counts per 10,000 + 1) | |
| `Zeisel2015_S1` | 36 | Mean log₂(counts per 10,000 + 1) | |
| `Zeisel2018_MouseBrain` | 265 | Mean log₂(counts per 10,000 + 1) | Zeisel metacell types |
| `Zhang2014_Cortex` | 7 | FPKM | Optional log₂(FPKM + 1) colours. |

Each folder contains:

- `<folder>.html`: the heatmap page, with its data embedded.
- `<folder>_data.csv`: the same expression records as a table (one row per population and gene, with the population's annotations).
- `<folder>_iframe.html`: the WordPress embed snippet.

## Using a heatmap

Genes are rows and populations are columns, coloured on the reversed Hawaii scale (pale cyan = low, dark magenta = high).

- **Search** one or more cell types or regions. Each extra search becomes a labelled comparison group. Suggestions come from the dataset's own annotations, such as population names, classes, marker genes and descriptions.
- **Filter** by the dataset's categories, and choose which genes to show (all, ZDHHC only, non-ZDHHC, or any set).
- **Colour scale:** *Fixed across all cells* uses the dataset maximum, which is best for comparing searches. *Fit current selection* uses the maximum across everything selected, on screen or not.
- **Expression scale** (Zhang 2014, HippoSeq and Sjöstedt 2020, the datasets not already in log units): original values, or log₂(value + 1) for colours. It changes the heatmap, summary band, legend and SVG/PNG colours. The hover shows the original value and, with log₂ on, the log value too (e.g. "39.85 FPKM (log₂(FPKM + 1) = 5.352)"). CSV export and ranking keep the original values.
- **Rank** genes by their mean across every population in the dataset, and/or populations by their mean over the selected genes (with one gene selected, by that gene alone). Populations are ranked within each search group. Ranking uses the original values.
- **Browse:** every matching population sits in one strip that scrolls sideways. When the strip is wider than the view, a *Whole selection* band above it summarises everything selected, with a frame for the visible part. Click or drag the band, use its ◀ Left / Right ▶ buttons, or Tab to it and use the arrow keys, Page Up/Down and Home/End. *Heatmap size* zooms.

  **How the *Whole selection* band is drawn.** The band shows every selected column, squeezed to the width of the heatmap on your screen, with genes in the same order as the heatmap rows. When there are more columns than screen pixels across the band, several neighbouring columns share one screen pixel, and that pixel takes the **highest** of their values (for each gene). So a single strongly expressing column always shows up in the band, even next to low ones. A dark spot means at least one column there reaches that level, not that every column does; the heatmap below shows each column's own value. How much the band squeezes depends on the number of columns and on your screen: its width, and how many pixels it packs into that width. On a standard screen, Yao 2023 GABAergic (2,025 clusters) puts about 2 columns in each pixel and Glutamatergic (2,597) about 3; on a high-resolution (Retina) screen, about 1 and 1.4. When each column has its own screen pixel, the band shows exact values. Thin vertical lines in the band mark the starts of categories or comparison groups.

- **Hover** (or tap) a tile for the gene, population, expression and the study's metadata.
- **Export** the whole selection as CSV, SVG or PNG. PNG is drawn from the SVG; very wide selections may need SVG.

Search by Gene shows one gene across datasets as ranked bar charts, with CSV and PNG downloads per dataset.

## How it works

Each heatmap is a single static HTML file with no server, build step or external library, which makes it easy to host and embed. The page is a `<div id="bps-compare">` holding:

1. **Styles and controls** (sidebar and heatmap area).
2. **Embedded data** in `<script type="application/json" class="bps-data">`. It is stored compactly: each population's details once, plus one value per population and gene. A small decoder at the top of the page script, `bpsData()`, rebuilds the full rows (gene, population, annotations, expression) before anything reads them. The GABAergic page went from 40 MB to 2.6 MB this way.
3. **The page script**, which builds the search, filters, gene picker, ranking, hover, CSV export and SVG/PNG figure export from those rows.
4. **The continuous-heatmap engine**, inlined from `tools/continuous_heatmap_engine.js`. It lays every selected column out in one strip and draws only the visible part on a canvas that stays fixed while the strip scrolls, so even 2,597 columns stay fast. It also draws the summary band and handles its mouse, keyboard and button navigation.

The pages share one template and differ only in their data, wording (category names, units, notes) and a few dataset-specific details, such as HippoSeq's short labels and which hover fields hold gene names.

## How it is built

The dataset pages were first generated outside this repository from each study's expression matrix and metadata, and uploaded as release folders. That generator is not in this repository. Since then, changes have been made directly to the pages with the scripts in `tools/`. Each script edits every page the same way and stops without writing anything if a page doesn't match what it expects:

| Script | What it did |
|---|---|
| `apply_hawaii_palette.py` | Set the reversed Hawaii colour map and removed the palette menu. |
| `italicize_gene_names.py` | Italicised gene names in labels, hover, suggestions and exports. |
| `apply_continuous_heatmap.py` | Replaced pages of 150 columns with the continuous heatmap and summary band. Its markup and styles live here. |
| `continuous_heatmap_engine.js` | The engine itself (see above). |
| `update_heatmap_engine.py` | Copies the current engine, summary-band markup and styles into already-converted pages. |
| `compact_heatmap_data.py` | Stored the embedded data compactly and added the decoder. Before writing a page, it checks that the decoded data matches the original exactly. |
| `verify_compact_data.js` | Repeats that check with Node.js: `node tools/verify_compact_data.js ORIGINAL.html COMPACT.html`. |
| `fix_export_scale_bar.py` | Laid out the SVG/PNG scale bar so it is never clipped. |
| `fix_population_ranking.py` | Made population ranking use the selected genes instead of the mean of all 40. |
| `add_log_scale_option.py` | Added the original / log₂(value + 1) Expression scale option to the FPKM and pTPM datasets. |

**To change the heatmap engine:** edit `tools/continuous_heatmap_engine.js` (and the markup or styles in `apply_continuous_heatmap.py` if needed), then run from the repository root:

```bash
python3 tools/update_heatmap_engine.py
```

Most scripts are one-off migrations and refuse to run twice on the same page. Changes so far were tested in headless Chromium (Playwright), loading each page and exercising scrolling, hover, search, ranking and exports. Those tests are not stored in this repository.

**Publishing:** GitHub Pages serves the `main` branch root. Merging into `main` updates the live pages and the WordPress embeds.

## Data notes

- Expression values are the source studies' own values; none were renormalised. Missing values (NA) stay missing.
- Units differ between datasets (see the table). Compare patterns within a dataset, not absolute levels across datasets.
- `Phillips2019_ThalamusNuclei`: the log₂ CP10K normalisation was assigned provisionally and not independently verified.
- Hover metadata comes from each study's source matrix where one was available. Some BICCN, Zeisel 2018, Marques and Cembrowski annotations come from the original pages instead. See `HOVER_METADATA_AUDIT.csv` and `README_HOVER_METADATA_UPDATE.md`.

## Other files

| File | Contents |
|---|---|
| `WORDPRESS_EMBEDS.md` | Embed snippets for every dataset. |
| `UPDATE_NOTES.txt` | Running list of site-wide changes. |
| `VALIDATION_REPORT.csv`, `VALIDATION_ISSUES.txt` | Per-dataset counts and omissions from the original release checks. |
| `HOVER_METADATA_AUDIT.csv`, `README_HOVER_METADATA_UPDATE.md` | Where each dataset's hover metadata comes from. |
| `BrainPalmSeq_Search_by_Gene/` | Search by Gene page (`index.html`), its embed snippet, and `data/` (every record it shows, plus the BICCN source matrix). See its README. |
| `BrainPalmSeq2026_Search_by_Gene/` | An identical copy of the Search by Gene page. |

## Citation

Wild AR, Hogg PW, Flibotte S, Nasseri GG, Hollman RB, Abazari D, Haas K, Bamji SX. Exploring the expression patterns of palmitoylating and de-palmitoylating enzymes in the mouse brain using the curated RNA-seq database BrainPalmSeq. *eLife* 2022;11:e75804. [doi:10.7554/eLife.75804](https://doi.org/10.7554/eLife.75804)

For human cell types and cell lines, see the companion resource CellPalmSeq ([Angie13-doc/CellPalmSeq-heatmaps](https://github.com/Angie13-doc/CellPalmSeq-heatmaps)).

Please also cite the original study for each dataset you use.
