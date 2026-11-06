# BrainPalmSeq hover metadata alignment

The original heatmap HTML/CSS, embedded expression values, filters and filenames are retained. Where a source matrix is available, hover field labels and values are drawn from its metadata rows in source order. Empty metadata values are omitted. The original `Population` identifier and expression are also displayed.

**Important:** Consult `HOVER_METADATA_AUDIT.csv`. Some BICCN, Zeisel 2018, Marques and Cembrowski data retain the annotations embedded in the original HTML because their complete original source metadata matrices were not available or did not have a one-to-one population-column mapping. These have not been independently verified against source metadata.

This package has not been tested in a live browser.
