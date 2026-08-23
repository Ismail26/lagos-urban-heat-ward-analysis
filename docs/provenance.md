# Data provenance and redistribution notes

## Included processed materials

The four workbooks in `data/derived/` are the processed tables used to create the manuscript figures. They contain ward-level or corridor-level summaries rather than individual-level survey records; no direct personal identifiers were found in the published fields.

The profile-map panels in `assets/profile_maps/` are derived visualization inputs from the project workflow. Publication-quality composites and statistical charts are in `figures/`.

The `v1.0.0` release also contains selected analysis-ready LST, LULC, and spectral-index GeoTIFFs under `data/derived/`, plus GRID3/LandScan/WorldPop population-density inputs under `data/raw/`. These raster files retain their source-provider terms and are not relicensed by this repository.

## Excluded materials

- **Original Landsat scenes and the complete raster working archive:** excluded because the original project contains tens of gigabytes of raster data. Landsat scenes should be obtained from USGS EarthExplorer; additional derivatives can be regenerated following the manuscript methods.
- **Boundary datasets:** not redistributed here because the source folders contain several third-party administrative and operational-ward products with differing provenance and terms. Users should obtain the relevant boundaries from their original providers.
- **Satellite-image panels:** excluded because each local file exceeds GitHub's normal per-file limit and third-party reuse terms require separate confirmation. Their expected filenames are documented in `assets/satellite_images/README.md`.
- **Working documents, PDFs, ArcGIS projects, caches, and temporary exports:** excluded because they are not required to reproduce the reported analysis.

## Local source archive

The authors' working archive was maintained separately from this curated repository. Its folder structure and absolute Windows paths are intentionally not part of the public workflow. The publication notebook uses repository-relative paths.

## Reproducibility boundary

Figures based only on the four derived workbooks can be regenerated directly after installing the Python dependencies. LST and LULC raster panels require the analysis-ready inputs and folder structure documented in `data/raw/README.md`. Corridor composites also require the separately licensed satellite-image panels. The final versions of all figures are retained in `figures/` so the archived release records the exact publication outputs.
