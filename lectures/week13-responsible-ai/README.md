# Week 13 — Responsible AI: Reliability, Bias, and Transparency

**Slides:** [PDF](Week13_Responsible-AI.pdf) · [PowerPoint](Week13_Responsible-AI.pptx) · **Lab:** [Lab 13 — Stress-Testing Models](../../labs/lab13-stress-testing-models/) · **Homework:** [HW5 — Responsible AI in Practice](../../homework/hw5-responsible-ai-in-practice/) (due end of Week 14, Sunday 11:59 pm)

*Project:* check-in wave 2 happens during the Week 13 lab (wave 1 was in the last 25 minutes of Lab 12). Upload the check-in form and notebook link on Brightspace before your check-in, and have your data loading and a baseline model running.

*Note:* Lab 13 repeats this week's demos with a different split/model (5-fold cross-validation for the bridges, a ResNet-18 crack model), so your numbers will differ from the slides.

## Learning objectives

By the end of this week, you can:

1. Explain **distribution shift** and **shortcut learning** with engineering examples, and test for them.
2. Identify where **bias** enters infrastructure data, and check a model's errors by subgroup.
3. Interpret **calibration**, **feature importance**, and **stress tests** — and their limits.
4. Name privacy, security, environmental, and human-factor risks of AI in CE/ARCE.
5. Use the **NIST AI Risk Management Framework** (Govern, Map, Measure, Manage) and a **model card** to manage and document a model.

## The big ideas

- **A test score only holds for data like the training data (distribution shift).** In our demo, a linear model trained only on compact buildings (relative compactness ≥ 0.75) from the building-energy dataset had a test error of about 2.6 kWh/m² — but about 91 kWh/m² on the spread-out buildings it never saw (about 35× worse), with no warning. The hidden difference: all the spread-out buildings are 3.5 m tall, and training saw only 7 m buildings. The same model trained on all shapes did fine, so the problem was data coverage, not the algorithm.
- **Models take shortcuts.** They may learn a cue that happens to go with the label (snow behind wolves, the hospital that took an X-ray, chalk marks next to cracks) instead of the real task. Test on data from a *new source* — a new building, site, or camera — to expose shortcuts.
- **Bias can enter at every step:** what is measured, who reports, how it is labeled, how it is modeled, and how predictions are used. In Arizona's 2024 bridge inventory, Tribal/BIA-owned bridges are about 5% of the bridges with deck ratings, yet 7.9% of their decks are rated poor (vs 0.4% for state-owned bridges). Those differences reflect age, funding, terrain, and history — not ownership itself — but they mean a model must be checked where needs are highest.
- **An overall score can hide a weak subgroup.** For subgroup checks we use **low deck = rating ≤ 5** (399 decks, 10.6% of rated bridges), not Lab 11's poor ≤ 4 — only 41 decks are that low, too few to measure errors for each group. A random forest that caught 62% of low decks overall caught only 4 of 16 among prestressed-concrete bridges; for Tribal/BIA bridges it caught most low-rated decks but raised more false alarms. Report misses *and* false alarms by subgroup, with counts.
- **How sure? Ask for calibrated uncertainty.** A calibrated model's "70%" cases come true about 70% of the time. Our random forest with balanced class weights was overconfident (≈ 69% predicted vs ≈ 37% observed in its top bin). Engineers already design for uncertainty (required average strength above f′c, load factors, the 1%-annual-chance flood) — ask AI models for ranges and warnings too.
- **Explanations show what a model uses, not how the world works.** Permutation importance (shuffle a column, watch the score drop) and saliency maps help find problems such as shortcuts, but they do not prove cause and effect or that a model is safe.
- **Stress-test for robustness.** A simple pixel-based crack classifier went from 85% accuracy on clean photos to 50% — no better than guessing — on darkened photos, and 59% with a shadow over half the image. The ResNet-18 model in Lab 13 holds up much better (about 99% → 93–95%): different models break in different ways. Adversarial noise — small deliberate changes — can fool vision models on purpose.
- **Beyond accuracy:** privacy (occupancy sensors, site cameras, drones — collect only what you need), security (prompt injection and data leakage), environmental footprint (data centers used about 4.4% of U.S. electricity in 2023 per LBNL; water for cooling matters in Arizona), and people (automation bias, deskilling, and clear accountability). The **NIST AI RMF** organizes all of this into four functions — **Govern, Map, Measure, Manage** — and a **model card** documents a model's intended use, data, performance by subgroup, and limits. (America's AI Action Plan of July 2025 directed NIST to revise AI RMF 1.0; as of late 2026 the revision is pending, so some wording may change.)

## Key terms

| Term | Plain-language meaning |
|---|---|
| Distribution shift | The data a model meets in use differ from the data it learned from, so its test score no longer applies |
| Extrapolation | Predicting outside the range of the training data |
| Shortcut learning / spurious correlation | The model uses a cue that happens to go with the label in training data but is not the real reason |
| Bias (in data or models) | Systematic error — consistently worse for some places, groups, or asset types |
| Subgroup analysis | Measuring a model's errors separately for each group (e.g., material, owner, age) |
| Low deck (this week) | A bridge deck rated 5 or lower on the 0–9 scale; Lab 11's "poor" is 4 or lower |
| Random forest | A model made of many decision trees that each vote; the majority (or average) is the prediction |
| ROC AUC | A 0.5–1.0 score for how well a model ranks positives above negatives; 0.5 = random guessing |
| k-fold cross-validation | Split the data into k parts; train on k − 1 and test on the remaining one, k times; average the results |
| Recall / false alarm rate | Share of true positives the model catches / share of true negatives it wrongly flags |
| Calibration | Whether predicted probabilities match how often things actually happen |
| Permutation feature importance | How much a model's score drops when one input column is shuffled |
| Saliency map | An image highlighting which pixels most affected a vision model's output |
| Robustness / stress test | How well a model holds up when conditions change (blur, lighting, noise); a test that changes them on purpose |
| Adversarial example | An input changed slightly and deliberately to make a model fail |
| Prompt injection | Text inside a document or web page that an AI tool mistakes for instructions |
| Automation bias | Over-trusting an automated tool and not looking for what it missed |
| NIST AI RMF | The U.S. NIST AI Risk Management Framework (AI RMF 1.0, Jan 2023): Govern, Map, Measure, Manage |
| Model card | A short document that travels with a model: intended use, data, performance, limits, owner |

## Read / watch

### Required (≈ 45 min total)

- **NIST AI Risk Management Framework** — <https://www.nist.gov/itl/ai-risk-management-framework>. Overview page with links to AI RMF 1.0 and the Generative AI Profile (NIST AI 600-1, July 2024). Skim the four functions; about 20 minutes. NIST updates its guidance — check for the current version.
- **Mitchell et al., "Model Cards for Model Reporting" (2019)** — <https://arxiv.org/abs/1810.03993>. Read the list of model-card sections and one example card; about 15 minutes. You will write a model card in Lab 13.
- **scikit-learn: Permutation feature importance** — <https://scikit-learn.org/stable/modules/permutation_importance.html>. How the importance tool in Lab 13 works, including its caution about correlated features; about 10 minutes.

### Optional

- **Google Machine Learning Crash Course: Fairness** — <https://developers.google.com/machine-learning/crash-course/fairness>. Types of bias and how to evaluate for them; about 1 hour with exercises.
- **LBNL 2024 United States Data Center Energy Usage Report** — <https://eta-publications.lbl.gov/publications/2024-lbnl-data-center-energy-usage-report>. Source of the U.S. data-center electricity and water estimates; read the executive summary (15 minutes).

## Check yourself

1. An energy model trained on homes in a mild climate is used for offices in Phoenix. Name the problem and one way to check for it before trusting the predictions.
   <details><summary>Answer</summary>Distribution shift (the inputs — weather, building type, loads — differ from the training data). Check whether each new case falls inside the range of the training data (climate, building type, size, each input), and test the model on some real Phoenix offices with known energy use before relying on it.</details>

2. A pavement model is 97% accurate, but all "pothole" photos came from residents' phones and all "good pavement" photos from a survey van. What could the model really be learning, and how would you test it?
   <details><summary>Answer</summary>A shortcut: phone photo vs van camera (angle, resolution, lighting) instead of pavement condition. Test it on van photos of potholes and phone photos of good pavement — or split train/test by camera source. If accuracy collapses, the model learned the source, not the pavement.</details>

3. A model says 70% for a group of bridges, but only 35% of them actually have low deck ratings (≤ 5). Is the model calibrated? Why does it matter for an engineer?
   <details><summary>Answer</summary>No — it is overconfident. If you use its probabilities to estimate how many bridges need repair, set budgets, or decide when to warn, you will overestimate badly. Its ranking may still be useful, but its numbers are not probabilities you can plan with until it is recalibrated on held-out data.</details>

4. Permutation importance ranks *age* first for a bridge deck-condition model. Can you conclude that age causes deterioration? What does the result tell you?
   <details><summary>Answer</summary>No. It tells you the model relies heavily on age when predicting. Age stands in for many things (weathering, traffic history, older design standards, maintenance), and correlated inputs share or hide importance. Explanations show what the model uses, not cause and effect in the world.</details>

5. Name the four functions of the NIST AI RMF and give one example action for each for an AI camera system that flags missing hard hats on a construction site.
   <details><summary>Answer</summary><b>Govern:</b> a named owner and written rules (footage used for safety, retention limits, worker notice). <b>Map:</b> identify who is affected (workers, visitors), costly errors (missed hazards vs false alarms), and conditions (night, rain). <b>Measure:</b> detection and false-alarm rates by lighting, distance, and worker group; re-test as the site changes. <b>Manage:</b> human review of alerts, face blurring in stored video, a plan and a stop rule if performance drops.</details>

## Coming up

- **Lab 13 — Stress-Testing Models (this week's lab day):** stress-test a ResNet-18 crack classifier with brightness, blur, and shadow changes; ask the energy model to extrapolate; analyze the Arizona bridge model's errors by subgroup (material, age, owner group) with 5-fold cross-validation; compute permutation feature importance; write a one-page model card. **Due:** Sunday 11:59 pm (Arizona time) of this week, on Brightspace.
- **Project check-in, wave 2:** teams not checked in during Lab 12 meet the instructor during Lab 13.
- **HW5 — Responsible AI in Practice:** due end of Week 14 (Sunday 11:59 pm).
- **Week 14 — AI Policy, Ethics, and Professional Practice:** the EU AI Act and the U.S. approach, standards, NSPE and ASCE codes of ethics, intellectual property, and the engineer's responsibility for sealed work.
