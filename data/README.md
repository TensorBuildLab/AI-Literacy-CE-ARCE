# Course Datasets

All datasets used in labs, homework, and suggested final projects live in this folder, so notebooks keep working even if an outside website changes. Each one is either licensed **CC BY 4.0** (free to reuse with credit) or a **U.S. Government work** (public domain). We cleaned them lightly: renamed columns to plain English with units and converted units where noted. Other cleaning is described per file. (The concrete file keeps 25 exact duplicate rows from the original — finding them is part of Lab 02.)

**Loading a file in Colab:**

```python
import pandas as pd
BASE = "https://raw.githubusercontent.com/TensorBuildLab/AI-Literacy-CE-ARCE/main/data/"
df = pd.read_csv(BASE + "concrete_strength.csv")
```

| File | Discipline | Rows | What one row is | Used in |
|---|---|---|---|---|
| `concrete_strength.csv` | Structures / materials | 1,030 | One concrete mix tested at one age | Weeks 2–5, Labs 02–04 & 10, HW3, HW5, midterm, project starter |
| `building_energy_efficiency.csv` | Building energy (ARCE) | 768 | One simulated building shape | Weeks 3, 5 & 13, Labs 05 & 13, HW1–HW2 |
| `concrete_cracks_sample.zip` | Inspection / computer vision | 1,200 images | One 227×227 photo of a concrete surface | Week 6, Labs 01, 06 & 13, HW3 |
| `metro_traffic_volume.csv` | Transportation | 40,575 | One hour of traffic on I‑94 | Week 6, Lab 06 (bonus), projects |
| `house_energy_hourly.csv` | Building operation (ARCE) | 3,290 | One hour in a low-energy house | Projects |
| `arizona_bridges_nbi2024.csv` | Infrastructure asset management | 8,573 | One Arizona bridge | Weeks 11 & 13, Labs 11 & 13, projects |
| `osha/` | Construction safety (text) | 2 documents | OSHA excavation and fall-protection rules | Week 8, Labs 08, 10 & 12, HW4–HW5 |

---

## concrete_strength.csv

Laboratory compressive strength of concrete mixes. Inputs are the amount of each ingredient (kg per m³ of concrete) and the age at testing.

| Column | Meaning | Units |
|---|---|---|
| `cement_kg_m3` | Portland cement | kg/m³ |
| `slag_kg_m3` | Blast-furnace slag | kg/m³ |
| `fly_ash_kg_m3` | Fly ash | kg/m³ |
| `water_kg_m3` | Water | kg/m³ |
| `superplasticizer_kg_m3` | Superplasticizer (water-reducing admixture) | kg/m³ |
| `coarse_agg_kg_m3` | Coarse aggregate (gravel) | kg/m³ |
| `fine_agg_kg_m3` | Fine aggregate (sand) | kg/m³ |
| `age_days` | Age at testing | days (1–365) |
| `strength_mpa` | **Target:** compressive strength | MPa |

Source: I‑C. Yeh, "Modeling of strength of high-performance concrete using artificial neural networks," *Cement and Concrete Research* 28(12), 1998. Dataset: UCI Machine Learning Repository, <https://archive.ics.uci.edu/dataset/165/concrete+compressive+strength>. License: CC BY 4.0.

## building_energy_efficiency.csv

Heating and cooling loads of 768 building shapes, simulated in Ecotect. All buildings have the same volume and materials; only shape, glazing, and orientation change. Useful for "predict energy from design choices."

| Column | Meaning | Units |
|---|---|---|
| `relative_compactness` | Volume-to-surface ratio compared with the most compact shape | – |
| `surface_area_m2`, `wall_area_m2`, `roof_area_m2` | Envelope areas | m² |
| `overall_height_m` | Building height (3.5 or 7) | m |
| `orientation` | 2 = North, 3 = East, 4 = South, 5 = West | category |
| `glazing_area_ratio` | Window area as a fraction of floor area (0, 0.10, 0.25, 0.40) | – |
| `glazing_distribution` | How windows are spread across façades (0 = none, 1 = uniform, 2–5 = mostly one side) | category |
| `heating_load_kwh_m2` | **Target:** annual heating load | kWh/m² |
| `cooling_load_kwh_m2` | **Target:** annual cooling load | kWh/m² |

Source: A. Tsanas and A. Xifara, "Accurate quantitative estimation of energy performance of residential buildings using statistical machine learning tools," *Energy and Buildings* 49, 2012. Dataset: UCI, <https://archive.ics.uci.edu/dataset/242/energy+efficiency>. License: CC BY 4.0.

## concrete_cracks_sample.zip

A random sample of 600 "crack" and 600 "no crack" images (227×227 px RGB) from a 40,000-image dataset of concrete surfaces photographed on campus buildings at Middle East Technical University. Unzips to `concrete_cracks/crack/` and `concrete_cracks/no_crack/`.

Source: Ç. F. Özgenel, "Concrete Crack Images for Classification," Mendeley Data, v2, 2019, <https://data.mendeley.com/datasets/5y9wdsg2zt/2>. Related paper: Ç. F. Özgenel and A. Gönenç Sorguç, "Performance comparison of pretrained convolutional neural networks on crack detection in buildings," ISARC 2018. License: CC BY 4.0. Sample drawn with random seed 42.

## metro_traffic_volume.csv

Hourly westbound traffic volume on Interstate 94 between Minneapolis and St. Paul, MN (2012–2018), with weather and holidays.

| Column | Meaning | Units |
|---|---|---|
| `date_time` | Hour (local time) | timestamp |
| `holiday` | U.S. national/regional holiday name, or `None` | text |
| `temp_c` | Air temperature (converted from Kelvin) | °C |
| `rain_mm_1h`, `snow_mm_1h` | Precipitation in the hour | mm |
| `cloud_cover_pct` | Cloud cover | % |
| `weather_main` | Short weather description (Clear, Rain, Snow, …) | text |
| `traffic_volume` | **Target:** vehicles in the hour | vehicles/h |

Cleaning: removed duplicate timestamps (the original repeats an hour when several weather descriptions apply) and blanked a few impossible 0 K temperatures. There are gaps in the record (missing hours), which is realistic and worth noticing.

Source: J. Hogue, "Metro Interstate Traffic Volume," UCI, <https://archive.ics.uci.edu/dataset/492/metro+interstate+traffic+volume>. Data from MN DoT ATR station 301 and OpenWeatherMap. License: CC BY 4.0.

## house_energy_hourly.csv

Hourly appliance and lighting energy use in a low-energy house in Belgium (Jan–May 2016), with temperature and relative humidity in nine rooms plus outdoor weather. Aggregated from the original 10-minute records: energy columns are hourly sums (Wh), all others are hourly means.

Source: L. M. Candanedo, V. Feldheim, D. Deramaix, "Data driven prediction models of energy use of appliances in a low-energy house," *Energy and Buildings* 140, 2017. Dataset: UCI, <https://archive.ics.uci.edu/dataset/374/appliances+energy+prediction>. License: CC BY 4.0.

## arizona_bridges_nbi2024.csv

Every bridge in Arizona in the Federal Highway Administration's 2024 National Bridge Inventory, with a selection of easy-to-understand fields.

| Column | Meaning |
|---|---|
| `structure_id` | NBI structure number |
| `latitude`, `longitude` | Location (decimal degrees) |
| `year_built`, `year_reconstructed` | Year (blank = never reconstructed) |
| `avg_daily_traffic`, `pct_truck_traffic` | Average daily traffic (vehicles/day) and % trucks |
| `lanes_on` | Traffic lanes on the structure |
| `material`, `design_type` | Main material (Concrete, Steel, Prestressed concrete, …) and structural form (Slab, Girder, Culvert, …) |
| `main_spans`, `max_span_m`, `length_m`, `deck_width_m` | Geometry |
| `deck_condition`, `superstructure_condition`, `substructure_condition` | Inspector condition ratings, 0 (failed) to 9 (excellent); blank = not applicable |
| `culvert_condition` | Condition rating for culverts (0–9); blank for non-culverts |
| `owner` | Agency that owns the bridge (State highway agency, County, City, Bureau of Indian Affairs, U.S. Forest Service, …) |
| `owner_group` | Owner grouped as State, Local, Tribal or BIA, Federal, Private or railroad, Other |

*Condition ratings:* FHWA classifies a bridge component as **Good** (7–9), **Fair** (5–6), or **Poor** (≤ 4). Most bridges have no "poor" rating, so a model that predicts "poor" faces very imbalanced classes. Condition also differs a lot by owner — something to examine when you ask whether a model works equally well for everyone.

Source: U.S. DOT Federal Highway Administration, National Bridge Inventory, 2024 delimited file for Arizona, <https://www.fhwa.dot.gov/bridge/nbi/ascii.cfm>. U.S. Government work (public domain). Codes translated using the FHWA *Recording and Coding Guide for the Structure Inventory and Appraisal of the Nation's Bridges*.

## osha/

Plain-text versions of two OSHA construction rules, used as a "document collection" for the retrieval-augmented generation (RAG) and AI-agent labs:

- `osha_1926_subpartP_excavations.txt` — 29 CFR 1926 Subpart P (Excavations), including soil classification (Appendix A) and sloping and benching (Appendix B).
- `osha_1926_subpartM_fall_protection.txt` — 29 CFR 1926 Subpart M (Fall Protection).

Source: Electronic Code of Federal Regulations, <https://www.ecfr.gov>. U.S. Government work (public domain). In the eCFR, Table B‑1 (maximum allowable slopes) is an image; we added a text transcription where the table is referenced. **These files are for learning only. Always use the current official text for real work.**

---

*Regenerating the files:* the instructor's build scripts download the raw sources and produce these files reproducibly.
