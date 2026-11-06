"""Decode a raw FHWA National Bridge Inventory (NBI) file into the same plain-English columns as the
course file `data/arizona_bridges_nbi2024.csv`.

Why: raw NBI files use numbered "items" and numeric codes (Item 43A material "1" = Concrete, Item 22 owner
"02" = County highway agency, ...). This helper turns them into readable columns, exactly the way the course
file was made, so a second state or an earlier year lines up with the course data.

Use it in Colab:

    import urllib.request
    urllib.request.urlretrieve("https://raw.githubusercontent.com/TensorBuildLab/AI-Literacy-CE-ARCE/main/"
                               "project/tools/nbi_decode.py", "nbi_decode.py")
    from nbi_decode import read_nbi

    az2019 = read_nbi("https://www.fhwa.dot.gov/bridge/nbi/2019/delimited/AZ19.txt")   # about 3.4 MB
    az2019.head()

File names on the FHWA site follow the pattern  https://www.fhwa.dot.gov/bridge/nbi/<YEAR>/delimited/<ST><YY>.txt
(for example NM24.txt = New Mexico 2024). The list of years is at https://www.fhwa.dot.gov/bridge/nbi/ascii.cfm.
Codes follow FHWA's "Recording and Coding Guide for the Structure Inventory and Appraisal of the Nation's
Bridges" (https://www.fhwa.dot.gov/bridge/mtguide.pdf). Check a few decoded rows against the guide yourself —
that is part of the "Sources" check.

Joining two years (for example, 2019 features -> 2024 rating):

    both = az2019.merge(az2024, on="structure_id", suffixes=("_2019", "_2024"))
"""
import numpy as np
import pandas as pd

# Item 43A — kind of material / design of the main span
MATERIAL = {"1": "Concrete", "2": "Concrete (continuous)", "3": "Steel", "4": "Steel (continuous)",
            "5": "Prestressed concrete", "6": "Prestressed concrete (continuous)",
            "7": "Wood or timber", "8": "Masonry", "9": "Aluminum/iron", "0": "Other"}

# Item 43B — type of design / construction of the main span
DESIGN = {"00": "Other", "01": "Slab", "02": "Stringer/multi-beam or girder",
          "03": "Girder and floorbeam", "04": "Tee beam", "05": "Box beam (multiple)",
          "06": "Box beam (single/spread)", "07": "Frame", "08": "Orthotropic",
          "09": "Truss (deck)", "10": "Truss (thru)", "11": "Arch (deck)", "12": "Arch (thru)",
          "13": "Suspension", "14": "Stayed girder", "15": "Movable (lift)",
          "16": "Movable (bascule)", "17": "Movable (swing)", "18": "Tunnel", "19": "Culvert",
          "20": "Mixed types", "21": "Segmental box girder", "22": "Channel beam"}

# Item 22 — owner
OWNER = {"01": "State highway agency", "02": "County highway agency", "03": "Town or township",
         "04": "City or municipal", "11": "State park or forest", "12": "Local park or forest",
         "21": "Other state agency", "25": "Other local agency", "26": "Private", "27": "Railroad",
         "31": "State toll authority", "32": "Local toll authority", "60": "Other federal agency",
         "61": "Indian tribal government", "62": "Bureau of Indian Affairs", "64": "U.S. Forest Service",
         "66": "National Park Service", "68": "Bureau of Land Management", "69": "Bureau of Reclamation",
         "70": "Corps of Engineers", "72": "Air Force", "73": "Navy/Marines", "74": "Army", "80": "Unknown"}

OWNER_GROUP = {"01": "State", "11": "State", "21": "State", "31": "State",
               "02": "Local", "03": "Local", "04": "Local", "12": "Local", "25": "Local", "32": "Local",
               "61": "Tribal or BIA", "62": "Tribal or BIA",
               "60": "Federal", "64": "Federal", "66": "Federal", "68": "Federal", "69": "Federal",
               "70": "Federal", "72": "Federal", "73": "Federal", "74": "Federal",
               "26": "Private or railroad", "27": "Private or railroad"}


def _dms(value, width):
    """Convert an NBI latitude/longitude written as degrees-minutes-seconds digits to decimal degrees."""
    try:
        v = str(value).strip().zfill(width)
        deg = int(v[:width - 6])
        minutes = int(v[width - 6:width - 4])
        seconds = int(v[width - 4:]) / 100
        return deg + minutes / 60 + seconds / 3600
    except (ValueError, TypeError):
        return np.nan


def read_nbi(source, min_year=1850, max_year=2025):
    """Read a raw NBI delimited file (a local path or a URL) and return a DataFrame with plain-English columns.

    Condition ratings are 0 (failed) to 9 (excellent); "N" (not applicable, e.g. a culvert has no deck rating)
    becomes a blank (NaN). Rows with an impossible year built are dropped, as in the course file.
    """
    raw = pd.read_csv(source, dtype=str, quotechar="'", encoding="latin-1", low_memory=False)
    raw.columns = [c.strip() for c in raw.columns]

    def num(col):
        return pd.to_numeric(raw[col].str.strip(), errors="coerce")

    owner_code = raw["OWNER_022"].str.strip().str.zfill(2)
    out = pd.DataFrame({
        "structure_id": raw["STRUCTURE_NUMBER_008"].str.strip(),
        "latitude": raw["LAT_016"].apply(lambda v: _dms(v, 8)).round(5),
        "longitude": (-raw["LONG_017"].apply(lambda v: _dms(v, 9))).round(5),   # west longitudes are negative
        "year_built": num("YEAR_BUILT_027"),
        "year_reconstructed": num("YEAR_RECONSTRUCTED_106").replace(0, np.nan),
        "avg_daily_traffic": num("ADT_029"),
        "pct_truck_traffic": num("PERCENT_ADT_TRUCK_109"),
        "lanes_on": num("TRAFFIC_LANES_ON_028A"),
        "material": raw["STRUCTURE_KIND_043A"].str.strip().map(MATERIAL),
        "design_type": raw["STRUCTURE_TYPE_043B"].str.strip().str.zfill(2).map(DESIGN),
        "main_spans": num("MAIN_UNIT_SPANS_045"),
        "max_span_m": num("MAX_SPAN_LEN_MT_048"),
        "length_m": num("STRUCTURE_LEN_MT_049"),
        "deck_width_m": num("DECK_WIDTH_MT_052"),
        "deck_condition": num("DECK_COND_058"),
        "superstructure_condition": num("SUPERSTRUCTURE_COND_059"),
        "substructure_condition": num("SUBSTRUCTURE_COND_060"),
        "culvert_condition": num("CULVERT_COND_062"),
        "owner": owner_code.map(OWNER).fillna("Other"),
        "owner_group": owner_code.map(OWNER_GROUP).fillna("Other"),
    })
    return out[out["year_built"].between(min_year, max_year)].reset_index(drop=True)


if __name__ == "__main__":
    import sys
    df = read_nbi(sys.argv[1])
    print(df.shape)
    print(df.head())
