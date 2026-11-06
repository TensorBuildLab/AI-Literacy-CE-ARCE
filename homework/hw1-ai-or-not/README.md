# HW1 — AI or Not? Exploring Engineering Data

**Posted:** Week 2 · **Due:** Sunday 11:59 pm (Arizona time) at the end of Week 3, on Brightspace · **Individual** · **100 points** · Plan about **4 hours**

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/TensorBuildLab/AI-Literacy-CE-ARCE/blob/main/homework/hw1-ai-or-not/HW1_AI_or_Not.ipynb)

## Overview

This homework checks two skills from Weeks 1–2. First, **talking about AI precisely**: how much autonomy and adaptivity a system really has, and which kind of machine learning fits a task. Second, **exploring data before modeling it**: you apply your Lab 02 pandas and plotting skills to a new dataset from building energy (ARCE). Everything is done in the starter notebook (Open in Colab above); written answers go in the notebook's text cells. A suggested time budget: Parts A–B about 1 hour, Part C about 2 hours, Part D about 45 minutes.

## Learning goals

1. Judge a system's autonomy and adaptivity and justify it with the course definitions.
2. Classify engineering tasks as supervised (regression or classification), unsupervised, or reinforcement learning, and name their inputs and outputs.
3. Explore a new engineering dataset with pandas and matplotlib, and explain what the numbers and plots show.
4. Reflect on where AI could help in civil or architectural engineering — and where it needs checking.

## AI-use rules for this assignment

| Part | Label | What it means |
|---|---|---|
| A — Autonomy–adaptivity map | **AI-Free** | Do not use AI tools to produce your answers. You may use them beforehand to study the concepts. |
| B — What kind of learning? | **AI-Free** | Same as Part A. |
| C — Exploring building energy data | **AI-Assisted** | You may ask an AI tool for coding or debugging help. Say so in the acknowledgment. You are responsible for every line. |
| D — Reflection | **AI-Free** | Write it in your own words. |

**AI-use acknowledgment (required):** use the template in the last cell of the notebook (the same one as in the [AI-use guide](../../resources/ai-use-guide.md)), or write "I did not use AI tools for this assignment." A missing acknowledgment costs **5 points**.

## Tasks

### Part A — The autonomy–adaptivity map (24 points, AI-Free)

The notebook lists 8 systems (BIM clash detection, occupancy-sensor lighting, a survey drone, a water-main risk model, a learning thermostat, an AI chat assistant, adaptive traffic signals, and a site-monitoring robot).

- **A1.** Score each system from 0 to 10 for **autonomy** (performs tasks in complex environments without constant guidance by a user) and **adaptivity** (improves performance by learning from experience). Run the provided cell to draw your map.
- **A2.** In the table, give low / medium / high for each property with a one-sentence reason that uses the definitions.

*3 points per system.* Reasonable answers that differ from the key earn full credit when the reasoning is sound. Be careful with one point: **reacting to a sensor is not learning**.

### Part B — What kind of learning is it? (18 points, AI-Free)

For each of 6 CE/ARCE tasks, give the type of learning (supervised / unsupervised / reinforcement), the sub-type (regression, classification, clustering, anomaly detection, or —), and the inputs → output (or why it is not supervised). *3 points per task.*

### Part C — Exploring building energy data (40 points, AI-Assisted)

Dataset: `building_energy_efficiency.csv` (768 simulated buildings; heating and cooling loads in kWh/m²).

| Task | What to do | Points |
|---|---|---|
| C1 | Load the data, show the first rows, print the shape | 4 |
| C2 | Summary statistics; identify categories stored as numbers | 5 |
| C3 | Count the 7 m tall buildings; mean heating load by height (`groupby`) | 6 |
| C4 | Mean heating and cooling load by glazing ratio; explain the trend | 6 |
| C5 | Histogram of heating load (a starter cell is given); explain its shape | 6 |
| C6 | Scatter of heating load vs relative compactness, colored by height (a starter cell is given); explain the pattern | 8 |
| C7 | Build X and y for predicting heating load; explain why cooling load is not a feature | 5 |

Every plot needs a title and axis labels with units.

### Part D — Reflection (18 points, AI-Free)

In 120–200 words: (1) one task in your studies or future work where an AI method could help — which kind of learning, what inputs and output; (2) one place where you would not trust AI output without checking, and how you would check; (3) what data the method would need and one data-quality problem to watch for.

## Deliverables

One file: your completed notebook `HW1_AI_or_Not.ipynb`, run from top to bottom with all outputs visible.

## Rubric

| Part | Full credit | Partial credit | Points | CLO / ABET SO |
|---|---|---|---|---|
| A | All 8 systems scored and placed; each reason uses the autonomy and adaptivity definitions correctly | Levels given but reasons vague, or reacting to a sensor is called learning | 24 | CLO1 / SO 7 |
| B | Correct type and sub-type; inputs/output or reasoning stated for all 6 | Type right but sub-type or reasoning missing | 18 | CLO1 / SO 7 |
| C | Code runs; numbers correct; plots titled and labeled with units; explanations connect numbers to buildings | Code runs but labels/units missing or explanations thin | 40 | CLO2 (practice) |
| D | Specific task, learning type, inputs/output; a concrete way to check AI output; a realistic data need and data-quality issue; clear writing within 120–200 words | Generic, or missing one of the three items | 18 | CLO1, CLO7 (supporting) |
| AI-use acknowledgment | Present, using the course template | — | missing: −5 | — |
| **Total** | | | **100** | |

## How to submit

1. In Colab: **Runtime → Restart session and run all**. Fix any errors.
2. **File → Download → Download .ipynb**.
3. Upload the file to **HW1** on Brightspace by **Sunday of Week 3, 11:59 pm (Arizona time)**.

Late work: see the syllabus late-work table (two grace days per semester, then −10% per day, up to 3 days). Questions? Ask in lab or in office hours.
