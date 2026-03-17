import json, uuid

with open('test_regressor.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

fn_code = '''import pandas as pd

def compute_compound_max_tyre_life(df_master):
    """
    Calcola il max tyre life medio storico per compound.
    Ogni compound e' in one-hot (Compound_SOFT, Compound_MEDIUM, Compound_HARD).
    Per ogni gara (GP, Year) e compound, prende il max TyreAge osservato.
    Poi media tra tutte le gare.
    Usato come normalizzatore per TyreLifeProgress in inferenza,
    coerente con il training XGBoost e senza data leakage.
    """
    records = []
    for (gp, year), gdf in df_master.groupby(["GP", "Year"]):
        for comp in ["SOFT", "MEDIUM", "HARD"]:
            col = f"Compound_{comp}"
            if col not in gdf.columns:
                continue
            subset = gdf[gdf[col] == 1]
            if subset.empty:
                continue
            max_life = subset["TyreAge"].max()
            records.append({"Compound": comp, "MaxLife": max_life})

    df_records = pd.DataFrame(records)
    result = df_records.groupby("Compound")["MaxLife"].agg(["mean", "median", "std", "count"])
    result.columns = ["Mean", "Median", "Std", "N_races"]
    result = result.round(2)
    return result

compound_life_stats = compute_compound_max_tyre_life(df_master)
print(compound_life_stats)
'''

new_cell = {
    "cell_type": "code",
    "execution_count": None,
    "id": uuid.uuid4().hex[:8],
    "metadata": {},
    "outputs": [],
    "source": fn_code
}

# Insert after cell 104 (markdown "## v4 VER fix with final")
nb["cells"].insert(105, new_cell)

with open("test_regressor.ipynb", "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print(f"Done. Total cells: {len(nb['cells'])}")
for i in range(104, 112):
    cell = nb["cells"][i]
    src = ''.join(cell["source"])[:70].replace('\n', ' ')
    print(f"  Cell {i} [{cell['cell_type']}]: {src}")
