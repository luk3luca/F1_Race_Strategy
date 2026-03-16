# F1 Apex Strategy Report v5

**Driver:** VER  |  **Year:** 2025  |  **Generated:** 2026-03-16  |  **MC:** 20 traj/decision  |  **Freeze:** 5 laps

---

## Abu Dhabi Grand Prix

🟢 Green flag race

### Strategy Summary

| Stop | AI Lap | Real Lap | Δ | Compound Out | Age | Decision | NN Prob |
|------|--------|----------|---|--------------|-----|----------|---------|
| 1 | 38 | 23.0 | 15.0 | MEDIUM | 37 laps | NN | 0.84 |

### Decision Analysis

#### Stop 1 — Lap 38

**Decision Driver:** NN  | **SC Risk:** 4.0%  | **Urgency Laps:** 0  | **Urgency Penalty on STAY_OUT:** +9.0s

**NN Finite-Diff Sensitivity (Δprob per +1σ)**

| Feature                             | Δ Pit Prob |
|------------------------------------|------------|
| TwoTyreCompoundsUsed                | -0.1647 |
| TyreLifeProgress                    | +0.0758 |
| CleanTrackStatus_YellowFlag         | -0.0611 |
| Position                            | -0.0500 |
| Compound_SOFT                       | -0.0500 |


**XGB SHAP Contributions (Δpace per feature)**

| Feature                             | Δ Pace (s) |
|------------------------------------|------------|
| RaceProgress                        | -0.6374 |
| Position                            | +0.4247 |
| ConstructorChampionshipPosition     | +0.3995 |
| TrackTemp                           | +0.2419 |
| TrackType                           | -0.1551 |


| Option     | EV (det.) | MC Mean  | MC σ  | Status |
|------------|-----------|----------|-------|--------|
| STAY OUT   | 56.6s     | 123.5s   | 104.9s | ✅ **BEST** |
| BOX SOFT   | 64.8s     | 110.9s   | 80.8s |  |
| BOX MEDIUM | n/a       | —        | —     |  |
| BOX HARD   | 69.5s     | 157.6s   | 104.6s |  |


---

## Azerbaijan Grand Prix

🟡 Safety Car race

*No pit stops simulated.*

---

## Bahrain Grand Prix

🟡 Safety Car race

### Strategy Summary

| Stop | AI Lap | Real Lap | Δ | Compound Out | Age | Decision | NN Prob |
|------|--------|----------|---|--------------|-----|----------|---------|
| 1 | 30 | 10.0 | 20.0 | SOFT | 29 laps | CLIFF | 0.81 |

### Decision Analysis

#### Stop 1 — Lap 30

**Decision Driver:** CLIFF  | **SC Risk:** 1.2%  | **Urgency Laps:** 0  | **Urgency Penalty on STAY_OUT:** +10.0s

**NN Finite-Diff Sensitivity (Δprob per +1σ)**

| Feature                             | Δ Pit Prob |
|------------------------------------|------------|
| TwoTyreCompoundsUsed                | -0.1459 |
| TyreLifeProgress                    | +0.0904 |
| Compound_HARD                       | -0.0903 |
| Position                            | +0.0582 |
| CleanTrackStatus_GreenFlag          | -0.0471 |


**XGB SHAP Contributions (Δpace per feature)**

| Feature                             | Δ Pace (s) |
|------------------------------------|------------|
| RaceProgress                        | -0.8272 |
| Position                            | +0.4296 |
| LapNumber                           | -0.2961 |
| ConstructorChampionshipPosition     | +0.2674 |
| TyreLifeProgress                    | +0.1553 |


| Option     | EV (det.) | MC Mean  | MC σ  | Status |
|------------|-----------|----------|-------|--------|
| STAY OUT   | 93.8s     | 144.8s   | 89.6s | ✅ **BEST** |
| BOX SOFT   | n/a       | —        | —     |  |
| BOX MEDIUM | 101.1s    | 201.0s   | 102.8s |  |
| BOX HARD   | 100.9s    | 190.4s   | 116.9s |  |


---

## Dutch Grand Prix

🟡 Safety Car race

### Strategy Summary

| Stop | AI Lap | Real Lap | Δ | Compound Out | Age | Decision | NN Prob |
|------|--------|----------|---|--------------|-----|----------|---------|
| 1 | 23 | 23.0 | 0.0 | SOFT | 22 laps | SC_VETO | 0.83 |
| 2 | 53 | 53.0 | 0.0 | HARD | 29 laps | SC_VETO | 0.85 |

### Decision Analysis

#### Stop 1 — Lap 23

**Decision Driver:** SC_VETO  | **SC Risk:** 4.2%  | **Urgency Laps:** 0  | **Urgency Penalty on STAY_OUT:** +0.0s

**NN Finite-Diff Sensitivity (Δprob per +1σ)**

| Feature                             | Δ Pit Prob |
|------------------------------------|------------|
| TyreLifeProgress                    | +0.0681 |
| CleanTrackStatus_YellowFlag         | -0.0424 |
| CleanTrackStatus_GreenFlag          | -0.0348 |
| Position                            | +0.0334 |
| CleanTrackStatus_SafetyCar          | +0.0298 |


**XGB SHAP Contributions (Δpace per feature)**

| Feature                             | Δ Pace (s) |
|------------------------------------|------------|
| Position                            | +0.5438 |
| ConstructorChampionshipPosition     | +0.4188 |
| RaceProgress                        | -0.3862 |
| LapNumber                           | -0.3590 |
| TyreLifeProgress                    | +0.2812 |


| Option     | EV (det.) | MC Mean  | MC σ  | Status |
|------------|-----------|----------|-------|--------|
| STAY OUT   | n/a       | —        | —     |  |
| BOX SOFT   | 271.4s    | 386.8s   | 133.9s |  |
| BOX MEDIUM | 265.7s    | 396.9s   | 119.8s |  |
| BOX HARD   | 260.1s    | 370.6s   | 119.4s | ✅ **BEST** |


#### Stop 2 — Lap 53

**Decision Driver:** SC_VETO  | **SC Risk:** 7.8%  | **Urgency Laps:** 0  | **Urgency Penalty on STAY_OUT:** +0.0s

**NN Finite-Diff Sensitivity (Δprob per +1σ)**

| Feature                             | Δ Pit Prob |
|------------------------------------|------------|
| Compound_HARD                       | -0.1886 |
| Compound_SOFT                       | -0.1567 |
| TrackType                           | -0.1478 |
| CleanTrackStatus_YellowFlag         | -0.1238 |
| RaceProgress                        | -0.1096 |


**XGB SHAP Contributions (Δpace per feature)**

| Feature                             | Δ Pace (s) |
|------------------------------------|------------|
| LapNumber                           | +2.6468 |
| Position                            | +0.5449 |
| ConstructorChampionshipPosition     | +0.4107 |
| RaceProgress                        | -0.2803 |
| TyreLifeProgress                    | +0.2263 |


| Option     | EV (det.) | MC Mean  | MC σ  | Status |
|------------|-----------|----------|-------|--------|
| STAY OUT   | n/a       | —        | —     |  |
| BOX SOFT   | 159.8s    | 186.5s   | 71.1s | ✅ **BEST** |
| BOX MEDIUM | 164.4s    | 208.5s   | 77.7s |  |
| BOX HARD   | 170.5s    | 212.9s   | 79.1s |  |


---

## Emilia Romagna Grand Prix

🟡 Safety Car race

### Strategy Summary

| Stop | AI Lap | Real Lap | Δ | Compound Out | Age | Decision | NN Prob |
|------|--------|----------|---|--------------|-----|----------|---------|
| 1 | 29 | 29.0 | 0.0 | MEDIUM | 28 laps | SC_VETO | 0.94 |
| 2 | 46 | 46.0 | 0.0 | HARD | 16 laps | SC_VETO | 0.81 |

### Decision Analysis

#### Stop 1 — Lap 29

**Decision Driver:** SC_VETO  | **SC Risk:** 2.6%  | **Urgency Laps:** 0  | **Urgency Penalty on STAY_OUT:** +0.0s

**NN Finite-Diff Sensitivity (Δprob per +1σ)**

| Feature                             | Δ Pit Prob |
|------------------------------------|------------|
| TwoTyreCompoundsUsed                | -0.1439 |
| Position                            | -0.0397 |
| TyreLifeProgress                    | +0.0287 |
| CleanTrackStatus_YellowFlag         | -0.0282 |
| Compound_SOFT                       | -0.0269 |


**XGB SHAP Contributions (Δpace per feature)**

| Feature                             | Δ Pace (s) |
|------------------------------------|------------|
| RaceProgress                        | -0.7845 |
| Position                            | +0.4597 |
| TrackType                           | +0.4498 |
| ConstructorChampionshipPosition     | +0.3273 |
| LapNumber                           | -0.2479 |


| Option     | EV (det.) | MC Mean  | MC σ  | Status |
|------------|-----------|----------|-------|--------|
| STAY OUT   | n/a       | —        | —     |  |
| BOX SOFT   | 207.0s    | 286.9s   | 80.8s |  |
| BOX MEDIUM | 205.5s    | 315.5s   | 123.9s |  |
| BOX HARD   | 193.3s    | 252.7s   | 92.8s | ✅ **BEST** |


#### Stop 2 — Lap 46

**Decision Driver:** SC_VETO  | **SC Risk:** 7.8%  | **Urgency Laps:** 0  | **Urgency Penalty on STAY_OUT:** +0.0s

**NN Finite-Diff Sensitivity (Δprob per +1σ)**

| Feature                             | Δ Pit Prob |
|------------------------------------|------------|
| RaceProgress                        | -0.1517 |
| Compound_HARD                       | -0.0876 |
| TwoTyreCompoundsUsed                | -0.0733 |
| Compound_SOFT                       | -0.0596 |
| Position                            | -0.0404 |


**XGB SHAP Contributions (Δpace per feature)**

| Feature                             | Δ Pace (s) |
|------------------------------------|------------|
| ConstructorChampionshipPosition     | +0.4057 |
| Position                            | +0.3675 |
| TyreLifeProgress                    | +0.3142 |
| RaceProgress                        | -0.3092 |
| TrackType                           | +0.2202 |


| Option     | EV (det.) | MC Mean  | MC σ  | Status |
|------------|-----------|----------|-------|--------|
| STAY OUT   | n/a       | —        | —     |  |
| BOX SOFT   | 145.3s    | 213.4s   | 103.2s | ✅ **BEST** |
| BOX MEDIUM | 149.1s    | 182.2s   | 84.9s |  |
| BOX HARD   | 151.9s    | 220.0s   | 93.2s |  |


---

## Hungarian Grand Prix

🟢 Green flag race

### Strategy Summary

| Stop | AI Lap | Real Lap | Δ | Compound Out | Age | Decision | NN Prob |
|------|--------|----------|---|--------------|-----|----------|---------|
| 1 | 42 | 17.0 | 25.0 | MEDIUM | 41 laps | CLIFF | 0.86 |

### Decision Analysis

#### Stop 1 — Lap 42

**Decision Driver:** CLIFF  | **SC Risk:** 2.4%  | **Urgency Laps:** 0  | **Urgency Penalty on STAY_OUT:** +12.0s

**NN Finite-Diff Sensitivity (Δprob per +1σ)**

| Feature                             | Δ Pit Prob |
|------------------------------------|------------|
| TyreLifeProgress                    | +0.0768 |
| Compound_HARD                       | -0.0579 |
| Position                            | +0.0438 |
| CleanTrackStatus_GreenFlag          | -0.0309 |
| TwoTyreCompoundsUsed                | -0.0273 |


**XGB SHAP Contributions (Δpace per feature)**

| Feature                             | Δ Pace (s) |
|------------------------------------|------------|
| RaceProgress                        | -0.7295 |
| Position                            | +0.5057 |
| ConstructorChampionshipPosition     | +0.2968 |
| TrackType                           | -0.1544 |
| TrackTemp                           | +0.1093 |


| Option     | EV (det.) | MC Mean  | MC σ  | Status |
|------------|-----------|----------|-------|--------|
| STAY OUT   | 91.5s     | 184.3s   | 81.5s | ✅ **BEST** |
| BOX SOFT   | 118.5s    | 249.8s   | 88.5s |  |
| BOX MEDIUM | n/a       | —        | —     |  |
| BOX HARD   | 103.2s    | 157.6s   | 96.4s |  |


---

## Italian Grand Prix

🟢 Green flag race

### Strategy Summary

| Stop | AI Lap | Real Lap | Δ | Compound Out | Age | Decision | NN Prob |
|------|--------|----------|---|--------------|-----|----------|---------|
| 1 | 33 | 37.0 | -4.0 | MEDIUM | 32 laps | NN | 0.81 |

### Decision Analysis

#### Stop 1 — Lap 33

**Decision Driver:** NN  | **SC Risk:** 3.5%  | **Urgency Laps:** 0  | **Urgency Penalty on STAY_OUT:** +6.0s

**NN Finite-Diff Sensitivity (Δprob per +1σ)**

| Feature                             | Δ Pit Prob |
|------------------------------------|------------|
| TwoTyreCompoundsUsed                | -0.2246 |
| TyreLifeProgress                    | +0.0879 |
| Position                            | -0.0809 |
| Compound_SOFT                       | -0.0648 |
| CleanTrackStatus_YellowFlag         | -0.0635 |


**XGB SHAP Contributions (Δpace per feature)**

| Feature                             | Δ Pace (s) |
|------------------------------------|------------|
| RaceProgress                        | -0.8003 |
| Position                            | +0.4734 |
| ConstructorChampionshipPosition     | +0.3986 |
| TyreLifeProgress                    | +0.1462 |
| TrackTemp                           | +0.1436 |


| Option     | EV (det.) | MC Mean  | MC σ  | Status |
|------------|-----------|----------|-------|--------|
| STAY OUT   | 62.9s     | 152.6s   | 86.6s | ✅ **BEST** |
| BOX SOFT   | 68.1s     | 157.8s   | 104.0s |  |
| BOX MEDIUM | n/a       | —        | —     |  |
| BOX HARD   | 73.5s     | 117.7s   | 81.7s |  |


---

## Japanese Grand Prix

🟢 Green flag race

### Strategy Summary

| Stop | AI Lap | Real Lap | Δ | Compound Out | Age | Decision | NN Prob |
|------|--------|----------|---|--------------|-----|----------|---------|
| 1 | 35 | 21.0 | 14.0 | MEDIUM | 34 laps | NN | 0.84 |

### Decision Analysis

#### Stop 1 — Lap 35

**Decision Driver:** NN  | **SC Risk:** 4.0%  | **Urgency Laps:** 0  | **Urgency Penalty on STAY_OUT:** +7.5s

**NN Finite-Diff Sensitivity (Δprob per +1σ)**

| Feature                             | Δ Pit Prob |
|------------------------------------|------------|
| Compound_HARD                       | -0.8406 |
| CleanTrackStatus_YellowFlag         | -0.8184 |
| TrackType                           | -0.7791 |
| Compound_MEDIUM                     | -0.7460 |
| CarClose                            | -0.7145 |


**XGB SHAP Contributions (Δpace per feature)**

| Feature                             | Δ Pace (s) |
|------------------------------------|------------|
| RaceProgress                        | -0.6949 |
| Position                            | +0.5149 |
| ConstructorChampionshipPosition     | +0.4660 |
| LapNumber                           | -0.1099 |
| TyreLifeProgress                    | +0.0872 |


| Option     | EV (det.) | MC Mean  | MC σ  | Status |
|------------|-----------|----------|-------|--------|
| STAY OUT   | 63.2s     | 162.3s   | 109.0s | ✅ **BEST** |
| BOX SOFT   | 69.5s     | 95.2s    | 56.9s |  |
| BOX MEDIUM | n/a       | —        | —     |  |
| BOX HARD   | 74.4s     | 147.2s   | 123.8s |  |


---

## Las Vegas Grand Prix

🟢 Green flag race

### Strategy Summary

| Stop | AI Lap | Real Lap | Δ | Compound Out | Age | Decision | NN Prob |
|------|--------|----------|---|--------------|-----|----------|---------|
| 1 | 16 | 25.0 | -9.0 | MEDIUM | 15 laps | SC_VETO | 0.72 |

### Decision Analysis

#### Stop 1 — Lap 16

**Decision Driver:** SC_VETO  | **SC Risk:** 4.2%  | **Urgency Laps:** 0  | **Urgency Penalty on STAY_OUT:** +0.0s

**NN Finite-Diff Sensitivity (Δprob per +1σ)**

| Feature                             | Δ Pit Prob |
|------------------------------------|------------|
| Compound_HARD                       | -0.7155 |
| Compound_MEDIUM                     | -0.7142 |
| CleanTrackStatus_YellowFlag         | -0.7114 |
| CarClose                            | -0.6858 |
| CleanTrackStatus_GreenFlag          | -0.6749 |


**XGB SHAP Contributions (Δpace per feature)**

| Feature                             | Δ Pace (s) |
|------------------------------------|------------|
| Position                            | +0.5863 |
| LapNumber                           | -0.5305 |
| TyreLifeProgress                    | +0.5067 |
| RaceProgress                        | -0.4374 |
| ConstructorChampionshipPosition     | +0.4034 |


| Option     | EV (det.) | MC Mean  | MC σ  | Status |
|------------|-----------|----------|-------|--------|
| STAY OUT   | n/a       | —        | —     |  |
| BOX SOFT   | 220.0s    | 299.0s   | 79.1s |  |
| BOX MEDIUM | 219.3s    | 313.6s   | 122.9s |  |
| BOX HARD   | 205.3s    | 293.0s   | 103.5s | ✅ **BEST** |


---

## Mexico City Grand Prix

🟢 Green flag race

### Strategy Summary

| Stop | AI Lap | Real Lap | Δ | Compound Out | Age | Decision | NN Prob |
|------|--------|----------|---|--------------|-----|----------|---------|
| 1 | 25 | 37.0 | -12.0 | MEDIUM | 24 laps | EV_OPTIMIZER | 0.49 |
| 2 | 35 | ? | ? | HARD | 9 laps | EV_OPTIMIZER | 0.00 |

### Decision Analysis

#### Stop 1 — Lap 25

**Decision Driver:** EV_OPTIMIZER  | **SC Risk:** 4.7%  | **Urgency Laps:** 0  | **Urgency Penalty on STAY_OUT:** +0.0s

**NN Finite-Diff Sensitivity (Δprob per +1σ)**

| Feature                             | Δ Pit Prob |
|------------------------------------|------------|
| TyreLifeProgress                    | +0.2432 |
| Position                            | +0.1194 |
| TwoTyreCompoundsUsed                | +0.0991 |
| CarClose                            | +0.0841 |
| CleanTrackStatus_YellowFlag         | -0.0682 |


**XGB SHAP Contributions (Δpace per feature)**

| Feature                             | Δ Pace (s) |
|------------------------------------|------------|
| Position                            | +0.4725 |
| RaceProgress                        | -0.4185 |
| ConstructorChampionshipPosition     | +0.3419 |
| LapNumber                           | -0.2949 |
| TyreLifeProgress                    | +0.1933 |


| Option     | EV (det.) | MC Mean  | MC σ  | Status |
|------------|-----------|----------|-------|--------|
| STAY OUT   | 166.4s    | 319.0s   | 114.2s |  |
| BOX SOFT   | 159.9s    | 307.2s   | 116.8s |  |
| BOX MEDIUM | n/a       | —        | —     |  |
| BOX HARD   | 157.0s    | 285.2s   | 125.0s | ✅ **BEST** |


#### Stop 2 — Lap 35

**Decision Driver:** EV_OPTIMIZER  | **SC Risk:** 2.6%  | **Urgency Laps:** 0  | **Urgency Penalty on STAY_OUT:** +0.0s

**NN Finite-Diff Sensitivity (Δprob per +1σ)**

| Feature                             | Δ Pit Prob |
|------------------------------------|------------|
| TyreLifeProgress                    | +0.0465 |
| Position                            | +0.0124 |
| RaceProgress                        | +0.0034 |
| Compound_HARD                       | -0.0017 |
| Compound_MEDIUM                     | -0.0016 |


**XGB SHAP Contributions (Δpace per feature)**

| Feature                             | Δ Pace (s) |
|------------------------------------|------------|
| RaceProgress                        | -0.7529 |
| ConstructorChampionshipPosition     | +0.5232 |
| TyreLifeProgress                    | +0.4997 |
| Position                            | +0.4081 |
| TrackTemp                           | -0.2420 |


| Option     | EV (det.) | MC Mean  | MC σ  | Status |
|------------|-----------|----------|-------|--------|
| STAY OUT   | 123.4s    | 181.3s   | 98.0s | ✅ **BEST** |
| BOX SOFT   | 137.2s    | 271.7s   | 96.8s |  |
| BOX MEDIUM | 123.2s    | 219.6s   | 89.4s | ✅ **BEST** |
| BOX HARD   | n/a       | —        | —     |  |


---

## Monaco Grand Prix

🟢 Green flag race

### Strategy Summary

| Stop | AI Lap | Real Lap | Δ | Compound Out | Age | Decision | NN Prob |
|------|--------|----------|---|--------------|-----|----------|---------|
| 1 | 29 | 28.0 | 1.0 | HARD | 28 laps | EV_OPTIMIZER | 0.54 |
| 2 | 60 | 77.0 | -17.0 | SOFT | 30 laps | CLIFF | 0.16 |

### Decision Analysis

#### Stop 1 — Lap 29

**Decision Driver:** EV_OPTIMIZER  | **SC Risk:** 4.7%  | **Urgency Laps:** 0  | **Urgency Penalty on STAY_OUT:** +0.0s

**NN Finite-Diff Sensitivity (Δprob per +1σ)**

| Feature                             | Δ Pit Prob |
|------------------------------------|------------|
| Compound_HARD                       | -0.4226 |
| CleanTrackStatus_YellowFlag         | -0.2909 |
| CleanTrackStatus_GreenFlag          | -0.2652 |
| TyreLifeProgress                    | +0.2462 |
| ConstructorChampionshipPosition     | -0.1712 |


**XGB SHAP Contributions (Δpace per feature)**

| Feature                             | Δ Pace (s) |
|------------------------------------|------------|
| RaceProgress                        | -0.5166 |
| Position                            | +0.4907 |
| ConstructorChampionshipPosition     | +0.3297 |
| LapNumber                           | -0.2479 |
| TyreLifeProgress                    | +0.1371 |


| Option     | EV (det.) | MC Mean  | MC σ  | Status |
|------------|-----------|----------|-------|--------|
| STAY OUT   | 161.5s    | 325.8s   | 145.5s |  |
| BOX SOFT   | 160.0s    | 283.9s   | 115.9s | ✅ **BEST** |
| BOX MEDIUM | 162.6s    | 270.8s   | 138.1s |  |
| BOX HARD   | n/a       | —        | —     |  |


#### Stop 2 — Lap 60

**Decision Driver:** CLIFF  | **SC Risk:** 9.0%  | **Urgency Laps:** 0  | **Urgency Penalty on STAY_OUT:** +0.0s

**NN Finite-Diff Sensitivity (Δprob per +1σ)**

| Feature                             | Δ Pit Prob |
|------------------------------------|------------|
| TyreLifeProgress                    | +0.3640 |
| RaceProgress                        | -0.1342 |
| CleanTrackStatus_SafetyCar          | +0.0845 |
| TrackType                           | +0.0495 |
| ConstructorChampionshipPosition     | -0.0372 |


**XGB SHAP Contributions (Δpace per feature)**

| Feature                             | Δ Pace (s) |
|------------------------------------|------------|
| Position                            | +0.4792 |
| ConstructorChampionshipPosition     | +0.3953 |
| RaceProgress                        | -0.2494 |
| TyreLifeProgress                    | +0.2363 |
| TrackTemp                           | +0.1484 |


| Option     | EV (det.) | MC Mean  | MC σ  | Status |
|------------|-----------|----------|-------|--------|
| STAY OUT   | 68.0s     | 139.0s   | 97.0s | ✅ **BEST** |
| BOX SOFT   | n/a       | —        | —     |  |
| BOX MEDIUM | 67.7s     | 144.1s   | 95.5s | ✅ **BEST** |
| BOX HARD   | 69.8s     | 102.4s   | 65.7s |  |


---

## Saudi Arabian Grand Prix

🟡 Safety Car race

### Strategy Summary

| Stop | AI Lap | Real Lap | Δ | Compound Out | Age | Decision | NN Prob |
|------|--------|----------|---|--------------|-----|----------|---------|
| 1 | 39 | 21.0 | 18.0 | MEDIUM | 36 laps | NN | 0.83 |

### Decision Analysis

#### Stop 1 — Lap 39

**Decision Driver:** NN  | **SC Risk:** 9.0%  | **Urgency Laps:** 0  | **Urgency Penalty on STAY_OUT:** +7.5s

**NN Finite-Diff Sensitivity (Δprob per +1σ)**

| Feature                             | Δ Pit Prob |
|------------------------------------|------------|
| TwoTyreCompoundsUsed                | -0.1986 |
| RaceProgress                        | -0.0879 |
| TyreLifeProgress                    | +0.0793 |
| Position                            | -0.0782 |
| CleanTrackStatus_YellowFlag         | -0.0615 |


**XGB SHAP Contributions (Δpace per feature)**

| Feature                             | Δ Pace (s) |
|------------------------------------|------------|
| TrackType                           | +0.4540 |
| Position                            | +0.4194 |
| ConstructorChampionshipPosition     | +0.4098 |
| RaceProgress                        | -0.2257 |
| TrackTemp                           | +0.0811 |


| Option     | EV (det.) | MC Mean  | MC σ  | Status |
|------------|-----------|----------|-------|--------|
| STAY OUT   | 40.5s     | 108.8s   | 64.0s | ✅ **BEST** |
| BOX SOFT   | 47.8s     | 93.1s    | 73.8s |  |
| BOX MEDIUM | n/a       | —        | —     |  |
| BOX HARD   | 52.2s     | 62.5s    | 50.1s |  |


---

## Singapore Grand Prix

🟢 Green flag race

### Strategy Summary

| Stop | AI Lap | Real Lap | Δ | Compound Out | Age | Decision | NN Prob |
|------|--------|----------|---|--------------|-----|----------|---------|
| 1 | 33 | 19.0 | 14.0 | SOFT | 32 laps | CLIFF | 0.68 |

### Decision Analysis

#### Stop 1 — Lap 33

**Decision Driver:** CLIFF  | **SC Risk:** 1.2%  | **Urgency Laps:** 0  | **Urgency Penalty on STAY_OUT:** +0.0s

**NN Finite-Diff Sensitivity (Δprob per +1σ)**

| Feature                             | Δ Pit Prob |
|------------------------------------|------------|
| TyreLifeProgress                    | +0.1288 |
| Compound_SOFT                       | -0.1046 |
| TwoTyreCompoundsUsed                | -0.0922 |
| Compound_HARD                       | -0.0715 |
| Position                            | +0.0685 |


**XGB SHAP Contributions (Δpace per feature)**

| Feature                             | Δ Pace (s) |
|------------------------------------|------------|
| RaceProgress                        | -0.9987 |
| ConstructorChampionshipPosition     | +0.4144 |
| Position                            | +0.3609 |
| TyreLifeProgress                    | +0.1445 |
| TrackType                           | -0.1400 |


| Option     | EV (det.) | MC Mean  | MC σ  | Status |
|------------|-----------|----------|-------|--------|
| STAY OUT   | 91.6s     | 196.6s   | 133.9s | ✅ **BEST** |
| BOX SOFT   | n/a       | —        | —     |  |
| BOX MEDIUM | 91.8s     | 219.6s   | 132.3s | ✅ **BEST** |
| BOX HARD   | 91.4s     | 194.6s   | 93.6s | ✅ **BEST** |


---

## Spanish Grand Prix

🟡 Safety Car race

### Strategy Summary

| Stop | AI Lap | Real Lap | Δ | Compound Out | Age | Decision | NN Prob |
|------|--------|----------|---|--------------|-----|----------|---------|
| 1 | 13 | 13.0 | 0.0 | SOFT | 12 laps | EV_OPTIMIZER | 0.02 |
| 2 | 55 | 29.0 | 26.0 | HARD | 41 laps | SC_VETO | 0.88 |

### Decision Analysis

#### Stop 1 — Lap 13

**Decision Driver:** EV_OPTIMIZER  | **SC Risk:** 3.7%  | **Urgency Laps:** 0  | **Urgency Penalty on STAY_OUT:** +0.0s

**NN Finite-Diff Sensitivity (Δprob per +1σ)**

| Feature                             | Δ Pit Prob |
|------------------------------------|------------|
| TyreLifeProgress                    | +0.4408 |
| Position                            | +0.1028 |
| RaceProgress                        | +0.0345 |
| Compound_HARD                       | -0.0195 |
| Compound_MEDIUM                     | -0.0149 |


**XGB SHAP Contributions (Δpace per feature)**

| Feature                             | Δ Pace (s) |
|------------------------------------|------------|
| Position                            | +0.7551 |
| LapNumber                           | -0.4632 |
| ConstructorChampionshipPosition     | +0.3685 |
| TrackTemp                           | -0.3150 |
| TyreLifeProgress                    | +0.2573 |


| Option     | EV (det.) | MC Mean  | MC σ  | Status |
|------------|-----------|----------|-------|--------|
| STAY OUT   | 187.8s    | 332.1s   | 147.6s | ✅ **BEST** |
| BOX SOFT   | n/a       | —        | —     |  |
| BOX MEDIUM | 188.0s    | 353.7s   | 129.7s | ✅ **BEST** |
| BOX HARD   | 187.7s    | 330.4s   | 143.3s | ✅ **BEST** |


#### Stop 2 — Lap 55

**Decision Driver:** SC_VETO  | **SC Risk:** 6.7%  | **Urgency Laps:** 0  | **Urgency Penalty on STAY_OUT:** +0.0s

**NN Finite-Diff Sensitivity (Δprob per +1σ)**

| Feature                             | Δ Pit Prob |
|------------------------------------|------------|
| RaceProgress                        | -0.1293 |
| TyreLifeProgress                    | +0.0248 |
| CleanTrackStatus_YellowFlag         | -0.0210 |
| CleanTrackStatus_SafetyCar          | +0.0193 |
| Compound_SOFT                       | -0.0154 |


**XGB SHAP Contributions (Δpace per feature)**

| Feature                             | Δ Pace (s) |
|------------------------------------|------------|
| Position                            | +0.5179 |
| ConstructorChampionshipPosition     | +0.3845 |
| TrackTemp                           | -0.3749 |
| LapNumber                           | -0.0620 |
| RaceProgress                        | -0.0434 |


| Option     | EV (det.) | MC Mean  | MC σ  | Status |
|------------|-----------|----------|-------|--------|
| STAY OUT   | n/a       | —        | —     |  |
| BOX SOFT   | 139.2s    | 160.8s   | 54.5s | ✅ **BEST** |
| BOX MEDIUM | 141.4s    | 178.8s   | 66.8s |  |
| BOX HARD   | 142.9s    | 178.4s   | 64.0s |  |


---

## Aggregate Backtesting Metrics

| Metric | Value |
|--------|-------|
| Total pit stops simulated | 17 |
| Mean Δ (AI − Real) | 5.4 laps |
| Std Dev Δ | 13.0 laps |
| \|Δ\| ≤ 3 laps | 35% (6/17) |
| \|Δ\| ≤ 5 laps | 41% (7/17) |

### Decision Driver Breakdown

- **SC_VETO**: 6 stops (33%)
- **NN**: 4 stops (22%)
- **CLIFF**: 4 stops (22%)
- **EV_OPTIMIZER**: 4 stops (22%)

### Comparative Table

| GP | Stop | AI Lap | Real Lap | Δ | Compound Out | Decision | NN Prob | Has SC |
|----|------|--------|----------|---|--------------|----------|---------|--------|
| Abu Dhabi Grand Prix | 1 | 38 | 23.0 | +15 | MEDIUM | NN | 0.84 | — |
| Bahrain Grand Prix | 1 | 30 | 10.0 | +20 | SOFT | CLIFF | 0.81 | ✅ |
| Dutch Grand Prix | 1 | 23 | 23.0 | +0 | SOFT | SC_VETO | 0.83 | ✅ |
| Dutch Grand Prix | 2 | 53 | 53.0 | +0 | HARD | SC_VETO | 0.85 | ✅ |
| Emilia Romagna Grand Prix | 1 | 29 | 29.0 | +0 | MEDIUM | SC_VETO | 0.94 | ✅ |
| Emilia Romagna Grand Prix | 2 | 46 | 46.0 | +0 | HARD | SC_VETO | 0.81 | ✅ |
| Hungarian Grand Prix | 1 | 42 | 17.0 | +25 | MEDIUM | CLIFF | 0.86 | — |
| Italian Grand Prix | 1 | 33 | 37.0 | -4 | MEDIUM | NN | 0.81 | — |
| Japanese Grand Prix | 1 | 35 | 21.0 | +14 | MEDIUM | NN | 0.84 | — |
| Las Vegas Grand Prix | 1 | 16 | 25.0 | -9 | MEDIUM | SC_VETO | 0.72 | — |
| Mexico City Grand Prix | 1 | 25 | 37.0 | -12 | MEDIUM | EV_OPTIMIZER | 0.49 | — |
| Mexico City Grand Prix | 2 | 35 | ? | ? | HARD | EV_OPTIMIZER | 0.0 | — |
| Monaco Grand Prix | 1 | 29 | 28.0 | +1 | HARD | EV_OPTIMIZER | 0.54 | — |
| Monaco Grand Prix | 2 | 60 | 77.0 | -17 | SOFT | CLIFF | 0.16 | — |
| Saudi Arabian Grand Prix | 1 | 39 | 21.0 | +18 | MEDIUM | NN | 0.83 | ✅ |
| Singapore Grand Prix | 1 | 33 | 19.0 | +14 | SOFT | CLIFF | 0.68 | — |
| Spanish Grand Prix | 1 | 13 | 13.0 | +0 | SOFT | EV_OPTIMIZER | 0.02 | ✅ |
| Spanish Grand Prix | 2 | 55 | 29.0 | +26 | HARD | SC_VETO | 0.88 | ✅ |