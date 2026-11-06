# Lab 13 — Stress-Testing Models

**Week 13 lab · about 75 minutes · AI-Assisted** · **Due:** Sunday 11:59 pm (Arizona time) of this week, on Brightspace. · Lecture: [Week 13 — Responsible AI](../../lectures/week13-responsible-ai/)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/TensorBuildLab/AI-Literacy-CE-ARCE/blob/main/labs/lab13-stress-testing-models/Lab13_Stress_Testing_Models.ipynb)

A model that scores well on its test set can still fail in the field. Today you stress-test models from earlier labs — the way an engineer load-tests a new design — and write a **model card**, a one-page spec sheet that says what a model is for and where it breaks. The work is organized with the four functions of the NIST AI Risk Management Framework: **Govern, Map, Measure, Manage**.

## What you'll do
| Part | What | Status |
|---|---|---|
| 1 | **Robustness (Measure):** two crack classifiers — pretrained ResNet-18 features (Lab 06) and the lecture's raw-pixel model — tested on darker, brighter, blurred, shaded, stained, partly covered, and heavily compressed photos | **Core** |
| 2 | **Extrapolation (Measure → Manage):** a heating-load model trained only on compact buildings, used on the others — compared with simply predicting the average; then a simple input range check | **Core** |
| 3 | **Subgroup error (Measure):** the Lab 11 bridge model audited by **owner** (State, Local, Tribal or BIA, Federal), material, age, and traffic using 5-fold cross-validation | **Core** |
| 3b | Calibration: can the predicted probabilities be trusted? | Optional |
| 4 | Permutation importance: what does the bridge model really rely on? | Optional |
| 5 | **Model card (Map, Govern, Manage)** for the bridge model, from a template | **Core** |
| ⭐ | Challenge: train on State bridges only, test on other owners | Optional |

**Project check-ins (wave 2) happen during this lab.** If your team is called, skip the optional parts and come back to them afterward.

**Why "low ≤ 5" here and "poor ≤ 4" in Lab 11?** Lab 11's poor target (deck rating ≤ 4) has only 41 rated decks — too few to split into owner or material groups. The audit uses **low deck = rating ≤ 5** (399 decks), the same definition as the Week 13 lecture. Your Lab 13 numbers will differ from the lecture slides because the lab uses cross-validation and a slightly different model; the pattern is the same.

## Before the lab
- [ ] Have your Lab 11 notebook handy (numbers for the model card).
- [ ] Skim the Week 13 lecture slides on distribution shift, subgroup error, and the NIST AI RMF.
- [ ] Bring a charged laptop; sign in to Google so you can save a copy in Drive.
- [ ] Final-project teams in check-in wave 2: have your data and baseline running.

## Data used
- `concrete_cracks_sample.zip` — concrete surface photos (Özgenel 2019, CC BY 4.0); we use 320 of them.
- `building_energy_efficiency.csv` — 768 simulated building shapes (Tsanas & Xifara 2012, CC BY 4.0).
- `arizona_bridges_nbi2024.csv` — FHWA National Bridge Inventory 2024, Arizona, including the `owner_group` column (U.S. Government work).
- ResNet-18 ImageNet weights from torchvision (about 45 MB, downloaded automatically). Model downloads happen on Google's computers, not on your laptop or phone data plan.

See the [data README](../../data/README.md) for sources and column meanings.

## How it's graded
Completion (all core cells run, TODOs done, written answers and model card present) + the **exit ticket**: 3 short questions you answer alone, without AI (AI-Free), during the last 10 minutes of lab. Optional parts are not graded. The rest of the lab is **AI-Assisted** — fill in the AI-use acknowledgment in the last cell. Submit the downloaded `.ipynb` on Brightspace by **Sunday 11:59 pm (Arizona time) of this week**. Late work: see the syllabus late-work table (two grace days per semester, then −10% per day, up to 3 days).

## Troubleshooting
- **The stress tests are slow (about a minute per setting group on Colab's CPU, ~6 minutes for Part 1 in total):** the CPU recomputes ResNet-18 features for 120 photos per setting. A GPU runtime (**Runtime → Change runtime type → T4 GPU**) is faster but not required.
- **Out of memory:** **Runtime → Restart session**, then run from the top. The notebook frees the image model before Part 2.
- **`display` is not defined (outside Colab/Jupyter):** replace `display(x)` with `print(x)`.
- **Your numbers differ slightly from a classmate's:** check `random_state=42` everywhere. With 120 test photos, one photo is 0.8 accuracy points, and subgroups with few low decks swing a lot — say so in your model card.
