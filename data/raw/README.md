# Raw and large inputs

Large raster inputs are intentionally excluded from GitHub. After obtaining or recreating them, place them under this directory with the structure below:

```text
data/raw/
├── lst/
│   ├── 2002_LST.tif
│   ├── 2013_LST.tif
│   └── 2022_LST.tif
└── lulc/
    ├── 2002LULC.tif
    ├── 2013LULC.tif
    └── 2022LULC.tif
```

The local source files used for the submitted figures correspond to:

| Repository filename | Local project source |
|---|---|
| `lst/2002_LST.tif` | `2002/LST/2002_LST.tif` |
| `lst/2013_LST.tif` | `2013/NEW/LST.tif` |
| `lst/2022_LST.tif` | `2022/NEW/LST.tif` |
| `lulc/2002LULC.tif` | `2002/Classification/2002LULC.tif` |
| `lulc/2013LULC.tif` | `2013/Classification/2013LULC.tif` |
| `lulc/2022LULC.tif` | `2022/Classification/2022LULC.tif` |

Original Landsat data are available from [USGS EarthExplorer](https://earthexplorer.usgs.gov/). Processing details should be read together with the associated manuscript.
