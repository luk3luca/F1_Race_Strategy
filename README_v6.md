# F1 Race Strategy Simulator — V6

## Problema risolto: Cliff Detection

### Il bug del V5 (survivorship bias)

XGBoost è addestrato su dati storici in cui i piloti **hanno sempre pittato prima del cliff**. I team non lasciano mai una gomma degradare fino al collasso: quindi il training set non contiene quasi mai l'anomalia `+0.4 s/lap` post-cliff.

Risultato: XGBoost linearizza la degradazione, non apprende la curva esponenziale, e quindi CLIFF_LAPS hardcoded `{SOFT:22, MEDIUM:38, HARD:55}` non hanno alcun fondamento nei dati.

---

## Soluzione V6: Dual-Cliff Detection

### A) NN-Sweep (Soluzione Primaria)

```
compute_nn_cliff(nn_model, nn_features, ref_lap_df, compound, threshold=0.35)
```

**Idea**: La NN è stata addestrata sulle *decisioni pit* dei team, che avvengono appena prima del cliff. Sweepando `tyre_age` da 1 a 60 con feature neutrali (green flag, SC=0, posizione mediana), la probabilità della NN sale esattamente quando i team storicamente decidevano di rientrare.

- Threshold `0.35` = warning cliff (sotto il decision threshold `0.45`)
- Il cliff pratico ≈ "quando i team iniziavano a pensare al pit"
- Cattura implicitamente: circuito, temperature, compound

**Output tipico:**

| Circuito       | SOFT (V5→V6) | MEDIUM (V5→V6) | HARD (V5→V6) |
|----------------|-------------|----------------|--------------|
| Monaco         | 22 → 18     | 38 → 32        | 55 → 48      |
| Monza          | 22 → 15     | 38 → 28        | 55 → 42      |
| Silverstone    | 22 → 17     | 38 → 30        | 55 → 45      |

*(Valori indicativi — i cliff V6 variano per circuito)*

### B) Polynomial Fit (Validazione)

```
compute_pace_cliff_from_data(df_encoded, compound, gp_name)
```

Fit polinomio grado-3 sulla mediana di `LapDeltaSeconds` vs età gomma.
L'inflection point (seconda derivata = 0) è il punto di massima accelerazione della degradazione.

- Usato come **cross-check**: se diverge dal NN cliff di più di 5 laps → warning in console
- Fallback a dati globali se dati per circuito insufficienti (<30 righe)

### Merge

```
build_cliff_laps(nn_model, nn_features, ref_lap_df, df_encoded, gp_name)
→ {'SOFT': N, 'MEDIUM': N, 'HARD': N}
```

- Usa NN come primario
- Logga divergenze NN vs Poly
- Fallback hardcoded `{22, 38, 55}` solo se NN non converge

---

## XAI Perturbativo

```
xai_sensitivity(nn_model, nn_features, lap_df, sigma_dict)
→ dict ordinato per |sensitivity| decrescente
```

Per ogni feature `f`:
```
sensitivity[f] = (P(f + σ) - P(f - σ)) / (2σ)
```

Dove `σ` = deviazione standard della feature nel training set (via `build_sigma_dict`).

- **Positivo**: aumentare questa feature → più probabile il pit
- **Negativo**: aumentare questa feature → meno probabile il pit
- Chiamato solo per le decisioni pit (2-3 per gara) → overhead minimo

### Plot XAI

```
plot_xai_decision(sensitivities, lap_num, compound, base_prob)
```

Bar chart orizzontale: rosso = spinge verso pit, blu = frena pit.

---

## Simulatore V3

```python
sim_df = run_stochastic_dynamic_strategy_v3(
    df_master, gp_name, driver_code, year,
    nn_model, xgb_model, xgb_features, nn_features,
    sc_prob_matrix,
    df_encoded=df_race,      # per poly cliff
    sigma_dict=sigma_dict_v6 # per XAI calibrato
)
```

### Differenze rispetto a V2

| Funzionalità                  | V2                    | V3                              |
|------------------------------|-----------------------|---------------------------------|
| CLIFF_LAPS                   | Hardcoded {22,38,55}  | NN-sweep dinamico per circuito  |
| Cliff validation             | Nessuna               | Polynomial cross-check          |
| XAI per decisioni pit        | Solo colonne EV base  | Sensitivity analysis completa   |
| Output DataFrame             | 10 colonne            | 15 colonne (+NN_Cliff_*, +XAI_*)|
| Logica EV / rollout          | Invariata             | Invariata                       |
| SC probability matrix        | Invariata             | Invariata                       |
| NN Veto threshold            | 0.70                  | 0.70 (invariato)                |

### Colonne aggiuntive nel DataFrame output

| Colonna          | Descrizione                                    |
|------------------|------------------------------------------------|
| `NN_Cliff_SOFT`  | Cliff NN-sweep per SOFT (costante per gara)    |
| `NN_Cliff_MEDIUM`| Cliff NN-sweep per MEDIUM                     |
| `NN_Cliff_HARD`  | Cliff NN-sweep per HARD                        |
| `XAI_Top_Feature`| Feature con maggiore impatto nella decisione pit |
| `XAI_Top_Delta`  | Valore sensitivity (NaN per STAY OUT)          |

---

## Plot Finale

```python
plot_simulation_vs_reality_v2(sim_df, real_df, driver_code, gp_name, year)
```

**Invariato**: 2 panel (pace + NN), nessun altro plot.

**Aggiunto (V6)**:
- Marker viola `⚠S/M/H` al giro in cui la gomma raggiunge il cliff NN
- Legenda aggiornata con "NN Cliff Warning (V6)"
- `cliff_laps` letto automaticamente dalle colonne `NN_Cliff_*` del sim_df

---

## Uso Completo

```python
# 1. Sigma dict per XAI calibrato
sigma_dict_v6 = build_sigma_dict(df_race, nn_features)

# 2. Simulazione V3
sim_df_v6 = run_stochastic_dynamic_strategy_v3(
    df_master=df_race, gp_name='Monaco Grand Prix',
    driver_code='VER', year=2025,
    nn_model=nn_model, xgb_model=best_xgb_model,
    xgb_features=xgb_features, nn_features=nn_features,
    sc_prob_matrix=sc_prob_matrix,
    df_encoded=df_race, sigma_dict=sigma_dict_v6,
)

# 3. Plot finale (cliff auto-letto dal sim_df)
plot_simulation_vs_reality_v2(sim_df_v6, real_race_data, 'VER', 'Monaco Grand Prix', 2025)

# 4. XAI per ogni pit decision
for _, row in sim_df_v6[sim_df_v6['Action'].str.contains('BOX')].iterrows():
    sens = xai_sensitivity(nn_model, nn_features, lap_df_for_row, sigma_dict_v6)
    plot_xai_decision(sens, lap_num=row['Lap'], compound='MEDIUM', base_prob=row['AI_Pit_Prob'])
```

---

## File

| File                              | Contenuto                              |
|-----------------------------------|----------------------------------------|
| `pitstop_strategy_NN_V2.ipynb`    | Tutto il codice (cells 91-96 = V6)    |
| `f1_pace_model_v6_optimized.joblib` | XGBoost pace model                  |
| `f1_strategic_model_m10_v4.keras`  | NN pit prediction model              |
| `f1_data/f1_strategy_NN_XGB_19_25_encoded.csv` | Training data           |
| `f1_data/f1_dataset_encoded_22_25.csv` | Encoded race data (per poly cliff) |
