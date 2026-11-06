# HW2 — Fit, Measure, Descend

**Posted:** Week 4 · **Due:** Sunday 11:59 pm (Arizona time) at the end of Week 5, on Brightspace · **Individual** · **100 points** · Plan about **5 hours**

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/TensorBuildLab/AI-Literacy-CE-ARCE/blob/main/homework/hw2-fit-measure-descend/HW2_Fit_Measure_Descend.ipynb)

## Overview

You will run the whole Weeks 3–4 recipe yourself — **model → cost → gradient descent → evaluation → communication** — first by hand on three concrete mixes, then in code on 768 simulated buildings, predicting the yearly **heating load** (kWh/m²). Along the way you will meet a common data problem: a hidden variable that reverses a trend. Everything is done in the starter notebook (Open in Colab above); Parts B and C give you starter cells with blanks to fill, like the labs. A suggested time budget: Part A 1 hour, Part B 2 hours, Part C 1 hour, Part D 45 minutes.

## Learning goals

1. Compute predictions, errors, the cost J(w, b), the gradients, and one gradient-descent step by hand.
2. Implement `predict`, `compute_cost`, `compute_gradient`, and `gradient_descent`, and choose a learning rate from learning curves.
3. Fit and evaluate a multiple linear regression with a train/test split and MAE, RMSE, and R².
4. Recognize a confounding variable and explain why regression coefficients are not design rules.
5. Communicate a model's accuracy and limits in a short engineering memo.

## AI-use rules for this assignment

| Part | Label | What it means |
|---|---|---|
| A — By hand | **AI-Free** | No AI tools, and no software that does the algebra for you. A basic calculator is fine. Show your work. |
| B — From scratch | **AI-Assisted** | AI help for explanations and debugging is allowed; acknowledge it. You are responsible for every line. |
| C — scikit-learn | **AI-Assisted** | Same as Part B. |
| D — Memo | **AI-Assisted** | You may ask for feedback on clarity, but the numbers, caveats, and recommendation must be yours — and correct. |

**AI-use acknowledgment (required):** use the template in the last cell of the notebook (the same one as in the [AI-use guide](../../resources/ai-use-guide.md)), or write "I did not use AI tools for this assignment." A missing acknowledgment costs **5 points**.

## Formulas (same as the lectures)

- Model: ŷ = f_{w,b}(x) = w·x + b
- Cost: J(w, b) = (1/2m) Σ (f(x⁽ⁱ⁾) − y⁽ⁱ⁾)²
- Gradients: ∂J/∂w = (1/m) Σ (f(x⁽ⁱ⁾) − y⁽ⁱ⁾)·x⁽ⁱ⁾ and ∂J/∂b = (1/m) Σ (f(x⁽ⁱ⁾) − y⁽ⁱ⁾)
- Update (simultaneous): w ← w − α·∂J/∂w, b ← b − α·∂J/∂b

## Tasks

### Part A — Cost and one descent step by hand (20 points, AI-Free)

Three concrete mixes: (w/c, strength) = (0.40, 49 MPa), (0.50, 41 MPa), (0.60, 36 MPa). Line 1: w = −50 MPa, b = 68 MPa. Line 2: w = −60 MPa, b = 73 MPa.

| Task | What to do | Points |
|---|---|---|
| A1 | Table of predictions, errors, squared errors for Line 1; J with units | 6 |
| A2 | J for Line 2; which line fits better and why | 4 |
| A3 | ∂J/∂w and ∂J/∂b at Line 1, showing the sums | 6 |
| A4 | One gradient-descent step from Line 1 with α = 0.5: new w, b, and J; why both went down | 4 |

Type your answers in the notebook's text cells (or upload a clear photo of handwritten work in the same Brightspace submission). An optional check cell tells you ✓/✗ without revealing the answers.

### Part B — One-feature linear regression from scratch (35 points, AI-Assisted)

Predict heating load (kWh/m²) from **relative compactness** (RC) in `building_energy_efficiency.csv`.

| Task | What to do | Points |
|---|---|---|
| B1 | Load the data, make arrays x and y, scatter plot with units | 4 |
| B2 | Write `predict`, `compute_cost`, `compute_gradient`, `gradient_descent` (self-checks use Part A's numbers) | 10 |
| B3 | Gradient descent (α = 1.0, 3,000 iterations); compare with `np.polyfit`; plot the line; MAE, RMSE, R²; interpret w with units (starter cell with blanks) | 8 |
| B4 | Learning-rate experiment (α = 0.01, 0.1, 1.0, and 1.3); learning curves; choose α and explain (starter cell with blanks) | 8 |
| B5 | Fit a line within each building height; explain why the trend reverses | 5 |

### Part C — Multiple regression with scikit-learn (30 points, AI-Assisted)

| Task | What to do | Points |
|---|---|---|
| C1 | X = 8 design columns (not cooling load), y = heating load; `train_test_split(test_size=0.2, random_state=42)`; `StandardScaler` fitted on training data only | 6 |
| C2 | Fit `LinearRegression`; predict train and test; comparison table vs baseline and the RC line | 8 |
| C3 | Predicted-vs-actual plot for the test set | 6 |
| C4 | Interpret: (a) model comparison and overfitting, (b) why the RC coefficient changed sign, (c) a multiple-choice question on redundant (collinear) area columns | 10 |

### Part D — Engineering memo (15 points, AI-Assisted)

One paragraph (120–180 words) to a design-team lead: *Can we use a quick model instead of a full energy simulation at the concept stage?* Include what you modeled, test accuracy in kWh/m² (MAE and R²) compared with the one-feature model, **at least three specific caveats**, and a clear recommendation. Then complete the AI-use acknowledgment cell at the end of the notebook.

## Deliverables

Your completed notebook `HW2_Fit_Measure_Descend.ipynb`, run from top to bottom with all outputs visible (plus a photo/PDF of handwritten Part A work, if you did it on paper).

## Rubric

| Part | Full credit | Partial credit | Points | CLO / ABET SO |
|---|---|---|---|---|
| A | Correct numbers with units and clear work for A1–A4 | Method right, arithmetic slip (lose 1 pt per slip) | 20 | CLO2 / SO 1 |
| B1–B3, B5 | Functions pass the self-checks; gradient descent matches polyfit; plots labeled with units; confounding explained | Code works but explanations missing or not tied to the plots | 27 | CLO2 / **SO 1** (gradient descent from scratch) |
| B4 | Learning-rate choice justified with evidence from the learning curves; divergence explained | Curves shown but the choice is not justified | 8 | CLO2 / **SO 6** (experimentation) |
| C | Correct split and scaling (no test-set information used in training); metrics table; labeled plot; interpretations correct and specific | Code works but interpretation vague or wrong | 30 | CLO2 / **SO 6** (data analysis) |
| D | Memo has test-set numbers with units, ≥ 3 specific caveats, and a clear, appropriately limited recommendation | Missing numbers, generic caveats, or claims the data cannot support | 15 | CLO2, CLO7 / **SO 6** (engineering judgment) |
| AI-use acknowledgment | Present, using the course template | — | missing: −5 | — |
| **Total** | | | **100** | |

## How to submit

1. In Colab: **Runtime → Restart session and run all**. Fix any errors.
2. **File → Download → Download .ipynb**.
3. Upload the file (and any Part A photo/PDF) to **HW2** on Brightspace by **Sunday of Week 5, 11:59 pm (Arizona time)**.

Late work: see the syllabus late-work table (two grace days per semester, then −10% per day, up to 3 days).
