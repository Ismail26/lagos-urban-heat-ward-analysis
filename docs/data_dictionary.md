# Data dictionary

## `New Updated Zonal Statistics.xlsx`

The worksheet `New Updated Zonal Statistics` contains 300 ward records and 21 fields.

| Field | Description |
|---|---|
| `ward_name` | Operational ward name |
| `Area(m2)` | Ward area in square metres |
| `Buildings`, `Building_1` | Building-count/density source fields retained from the zonal-statistics workflow |
| `_PopCountm` | Estimated ward population count |
| `PopDensity`, `PopDensi_1`, `PopDensi_2` | Population-density source/derived fields retained for reproducibility |
| `AreaSqKm` | Ward area in square kilometres |
| `_2002LST_m`, `_2013LST_m`, `_2022LST_m` | Mean ward land-surface temperature for each study year (°C) |
| `_NDVI2002_`, `_NDVI2013_`, `_NDVI2022_` | Mean ward NDVI for each study year |
| `_NDBI2002_`, `_NDBI2013_`, `_NDBI2022_` | Mean ward NDBI for each study year |
| `_MNDWI2002`, `_MNDWI2013`, `_MNDWI2022` | Mean ward MNDWI for each study year |

## `Ward_Socio_Economic_Data.xlsx`

The worksheet `Ward Socio-Economic Data` contains eight selected ward records with planning status, mean LST, NDVI, NDBI, MNDWI, building density, and population density. It supports the socio-environmental profile chart.

## `LST Statistics summary.xlsx`

- `Sheet2` provides the selected corridor wards and their mean LST values for 2002, 2013, and 2022.
- `Ikeja_Oshodi`, `Apapa_Ajeromi Ifelodun`, `UNILAG_Iwaya`, and `Obalende_Ikoyi` retain the corridor subsets alongside the full ward LST table used during selection and verification.

## `Profile Graph_2002_2023.xlsx`

`Sheet1`–`Sheet4` contain along-corridor distance coordinates and sampled LST values for 2002, 2013, and 2022. The sheets correspond, in notebook order, to the Oshodi–Ikeja, Ajeromi–Apapa, Makoko–UNILAG, and Obalende–Ikoyi profiles.

## Interpretation notes

- LST values are in degrees Celsius.
- NDVI, NDBI, and MNDWI are dimensionless spectral indices.
- Field names inherited from GIS zonal-statistics exports are retained to preserve direct compatibility with the analysis notebook.
- These workbooks are processed research outputs, not raw satellite imagery.
