# Lab 11 — End-to-End ML Workflow on Arizona Bridges

**Week 11 lab · about 75 minutes · AI-Assisted** · **Due:** Sunday 11:59 pm (Arizona time) of this week, on Brightspace. · Lecture: [Week 11 — AI Across Civil and Architectural Engineering](../../lectures/week11-ai-across-ce-arce/)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/TensorBuildLab/AI-Literacy-CE-ARCE/blob/main/labs/lab11-bridges-end-to-end/Lab11_Bridges_End_to_End.ipynb)

Every bridge on a public road in the U.S. is inspected and rated from 9 (excellent) to 0 (failed). Today you run a complete machine-learning project on all Arizona bridges in the 2024 National Bridge Inventory. The question: **which bridge decks are likely in poor condition (rating 4 or less), so inspectors and repair money can go there first?**

> **This notebook is also your final-project template.** Sections marked **🧩 PROJECT TEMPLATE** are the eight steps every project needs (frame → explore → features → split + baseline → models → evaluate → explain → communicate). Make a copy for your team and swap in your own data and question.

## What you'll do
1. **Frame** the question with a problem card: users, decision, target, inputs, success metric, baseline.
2. **Explore** the data: drop culverts (no deck rating), map the bridges by latitude/longitude, plot age vs. condition, and catch a hidden data code (year 9999).
3. **Build features**: age, years since last reconstruction, traffic, trucks, lanes, spans, lengths, plus one-hot encoded material and design type.
4. **Split and baseline**: a stratified train/test split and the "every deck is fine" baseline — which scores 98.9% accuracy while catching zero poor decks.
5. **Model**: logistic regression and a random forest, with and without class weights.
6. **Evaluate**: recall and precision for the poor class, a confusion matrix, and the decision threshold as a design choice.
7. **Explain**: random-forest feature importance, and why importance is not cause and effect.
8. **Communicate**: a 5-sentence engineering memo with numbers and caveats.
9. *Optional challenges* if you finish early: how much recall changes across 5-fold cross-validation, and whether the model beats a simple "oldest bridges first" rule.

**Why predict a rating the state already has?** Fair question — the notebook answers it: the model reveals risk factors, can screen structures whose ratings are missing or out of date, and is a teaching stand-in for a real forecast (2019 features → poor by 2024), which makes a good final project (idea P5 on the [project ideas page](../../project/project-ideas.md)).

## Before the lab
- [ ] Review recall, precision, and the confusion matrix from Week 6 (Lab 06) and HW3.
- [ ] Skim the `arizona_bridges_nbi2024.csv` section of the [data README](../../data/README.md).
- [ ] Bring a charged laptop; sign in to Google so you can save a copy in Drive.
- [ ] Final-project teams: sit together — you will reuse this notebook.

## Data used
`arizona_bridges_nbi2024.csv` — 8,573 Arizona structures from the FHWA National Bridge Inventory (2024). We keep the 3,762 bridges that have a deck rating; only **41 (1.1%)** have a poor deck. U.S. Government work (public domain). Source: <https://www.fhwa.dot.gov/bridge/nbi/ascii.cfm>.

## How it's graded
Completion (all cells run, TODOs done, written answers present) + the **exit ticket**: 3 short questions you answer alone, without AI (AI-Free), during the last 10 minutes of lab. The exit ticket is **AI-Free**; the rest of the lab is **AI-Assisted** — fill in the AI-use acknowledgment in the last cell. Submit the downloaded `.ipynb` on Brightspace by **Sunday 11:59 pm (Arizona time) of this week**. Late work: see the syllabus late-work table (two grace days per semester, then −10% per day, up to 3 days).

## Troubleshooting
- **`NameError` (e.g., `bridges` is not defined):** you skipped a cell. Use **Runtime → Run before** or **Runtime → Restart session and run all**.
- **A self-check fails:** read its message; compare your cell with the hint above it. Common slips: forgetting `.copy()`, using `< 4` instead of `<= 4`, or forgetting `.fit(...)`.
- **The `display(...)` table looks plain or errors outside Colab:** replace it with `print(table)`.
- **Your numbers differ slightly from a classmate's:** check that you used `random_state=42` and `stratify=y`. With only 12 poor decks in the test set, one bridge changes recall by 8 percentage points — that is a lesson, not a bug.
