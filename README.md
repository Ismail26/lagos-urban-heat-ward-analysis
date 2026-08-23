# Urban differentiation and land-surface temperature dynamics in Lagos

This repository contains the processed data, analysis code, and figure outputs supporting the manuscript **“Urban Differentiation and Land Surface Temperature Dynamics in Lagos Metropolis: A Ward-Level Analysis Using Multi-Temporal Landsat Imagery (2002–2022)”** by Olajide Ismail Olayinka, Mayowa Fasona, and Akinlabi Akintuyi.

The study evaluates ward-scale land-surface temperature (LST), land-use/land-cover change, NDVI, NDBI, MNDWI, building density, population density, and planning characteristics across Lagos Metropolis for 2002, 2013, and 2022.

## Repository contents

- `notebooks/generate_rsase_figures.ipynb` — cleaned notebook used to generate Figures 2–10.
- `scripts/run_figures.py` — non-interactive notebook runner.
- `data/derived/` — four processed Excel workbooks used by the figure workflow.
- `data/raw/README.md` — expected filenames and instructions for obtaining or placing large/raw inputs.
- `assets/profile_maps/` — corridor LST profile-map panels.
- `figures/` — publication-quality figure outputs, including the study-area map.
- `docs/data_dictionary.md` — workbook and variable descriptions.
- `docs/provenance.md` — data provenance, redistribution boundaries, and reproducibility notes.

## Quick start

1. Clone the repository and create a Python 3.11 or newer environment.
2. Install the dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

3. Obtain the source rasters listed in `data/raw/README.md` and place them in the stated folders.
4. Open `notebooks/generate_rsase_figures.ipynb` and run its cells from the repository root, or run:

   ```bash
   python scripts/run_figures.py
   ```

The corridor composites additionally require the satellite-image panels described in `docs/provenance.md`. They are not redistributed here because their third-party reuse terms must be checked separately. The final corridor composites are available in `figures/`.

## Data availability

Processed data, analysis code, supporting profile maps, and final figure outputs are provided in this repository. The original Landsat scenes and large derived GeoTIFFs are not stored in GitHub. Landsat data can be obtained from [USGS EarthExplorer](https://earthexplorer.usgs.gov/); users should recreate or supply the raster inputs using the filenames documented under `data/raw/`.

## Citation

Until the associated article and Zenodo archive receive persistent identifiers, cite this repository using `CITATION.cff`. A versioned Zenodo DOI will be added after the first public GitHub release.

## Licenses

Repository code is released under the MIT License. Original processed tables and figure outputs produced by the authors are released under CC BY 4.0, subject to the exclusions in `DATA_LICENSE.md`. No license is granted here for third-party Landsat scenes, boundary data, satellite basemaps, or other externally sourced materials.

## Contact

Olajide Ismail Olayinka — corresponding author: ismailolajide1992@gmail.com
