# Week 4 — How Machines Learn, Part 2: Gradient Descent and Generalization

**Slides:** [PDF](Week04_How-Machines-Learn-2.pdf) · [PowerPoint](Week04_How-Machines-Learn-2.pptx) · **Lab:** [Lab 04 — Gradient Descent](../../labs/lab04-gradient-descent/) · **Homework:** [HW2 — Fit, Measure, Descend](../../homework/hw2-fit-measure-descend/) (posted this week, due end of Week 5)

## Learning objectives
By the end of this week you can:
1. Explain gradient descent in words and apply the update rule w ← w − α·∂J/∂w (and the same for b).
2. Choose a learning rate α by reading a learning curve.
3. Use several features at once (ŷ = w·x + b with one weight per feature) and explain why we scale them.
4. Split data into training and test sets, and recognize underfitting and overfitting.
5. Report MAE, RMSE, and R², and fit a model in a few lines of scikit-learn.

## The big ideas
- **Gradient descent** finds the bottom of the cost bowl when there is no formula: start anywhere, compute the slope, step downhill, repeat — like walking down a foggy hillside by feeling the ground.
- The update rule (both parameters updated together, using the old slopes): **w ← w − α·∂J/∂w** and **b ← b − α·∂J/∂b**. For a line, **∂J/∂w = (1/m) Σ (f(x⁽ⁱ⁾) − y⁽ⁱ⁾)·x⁽ⁱ⁾** and **∂J/∂b = (1/m) Σ (f(x⁽ⁱ⁾) − y⁽ⁱ⁾)** — the average error (weighted by x for w).
- The **learning rate α** sets the step size. Too small: slow. Too large: each step overshoots and the cost grows (on the concrete w/c data with w and b both moving, the limit is about 1.25: α = 1.3 diverges while α = 1.0 converges; the lecture's one-parameter picture, with b held fixed, has a higher limit). Check the **learning curve** (cost vs iteration): it should go down and flatten.
- **Multiple features:** ŷ = w₁x₁ + … + w₈x₈ + b = **w·x + b**. Same cost, same gradient descent, one slope per weight. **Standardize** features, z = (x − mean) ÷ std, so they share a scale; otherwise the cost valley is long and narrow and descent zig-zags. Fit the scaler on the training data only.
- **Generalization:** judge a model on data it never saw. Split the data (here 80% training, 20% test, `random_state=42`); use a validation set for tuning; use the test set only once, at the end. **Underfitting** = too simple, high error everywhere. **Overfitting** = too flexible, low training error but high test error (a degree-9 polynomial through 12 mixes).
- **Metrics** in engineering units: **MAE** (average miss), **RMSE** (like MAE but big misses count more), **R²** (share of variation explained). With all 8 concrete inputs, a linear model reaches about **MAE 7.7 MPa, RMSE 9.8 MPa, R² 0.63 on the test set**, versus MAE 11.3 MPa and R² 0.27 with the w/c ratio alone (also on the test set; last week's 11.9 MPa and 0.25 were on all the data). Every model should also beat a **baseline** — always predicting the average strength — and both models do — better, but still not good enough to replace cylinder tests.
- Read learned weights carefully: after standardizing, each weight is the change in strength (MPa) when that input rises by one standard deviation, others fixed — an association in *this dataset*, not a physical law. Water's bar is short (−2.9 MPa per SD) because water varies little here (SD ≈ 21 kg/m³ vs ≈ 107 for cement); per kg, its effect matches Abrams' law.
- **scikit-learn** does it all in a few lines (`train_test_split`, `StandardScaler`, `LinearRegression`). **Logistic regression** turns the same weighted sum into a probability with the sigmoid for yes/no questions (will this mix reach 40 MPa?). And **model + cost + gradient descent** is exactly the recipe that trains neural networks and large language models.

## Key terms
| Term | Plain-language meaning |
|---|---|
| Gradient descent | Repeatedly stepping the parameters downhill on the cost surface |
| Gradient / partial derivative (∂J/∂w) | The slope of the cost in one parameter's direction |
| Learning rate (α) | How big each gradient-descent step is |
| Iteration | One step of gradient descent |
| Convergence | When the cost stops going down noticeably |
| Learning curve | A plot of cost vs iteration, used to check that training works |
| Feature scaling / standardization | Rescaling each feature to mean 0 and standard deviation 1 |
| Training set / test set | Data used to fit the model / data held back to estimate performance on new cases |
| Baseline | The simplest reference model a real model must beat — here, always predicting the average strength of the training mixes |
| Validation set | Part of the training data used to choose settings such as α or model size |
| Underfitting | A model too simple to capture the pattern; high error on training and test data |
| Overfitting | A model that memorizes training noise; low training error, high test error |
| RMSE | Root mean squared error: like MAE, in the target's units, but large misses weigh more |
| Logistic regression | A classification model: weighted sum → sigmoid → probability → threshold |
| scikit-learn | The standard Python library for classic machine learning (`fit`, `predict`) |

## Read / watch
**Required (≈ 45 min total)**
- **Google ML Crash Course: "Linear regression" — Gradient descent and Hyperparameters pages** — <https://developers.google.com/machine-learning/crash-course/linear-regression/gradient-descent> and <https://developers.google.com/machine-learning/crash-course/linear-regression/hyperparameters> (about 30 minutes together, with interactive exercises on the learning rate).
- **Google ML Crash Course: "Datasets, generalization, and overfitting"** — <https://developers.google.com/machine-learning/crash-course/overfitting> (whole module about 105 minutes). Read only "Dividing the original dataset" for this week (about 15 minutes).

**Optional**
- The "Overfitting" page of the same Google module (about 20 minutes).
- **3Blue1Brown: "Gradient descent, how neural networks learn"** — <https://www.youtube.com/watch?v=IHZwWFHWa-w> (video, about 21 minutes). The same idea applied to a neural network — a bridge to Week 5.
- **scikit-learn user guide: "Linear Models"** — <https://scikit-learn.org/stable/modules/linear_model.html> (reference; read the first section on ordinary least squares, about 10 minutes).

## Check yourself
1. At the current w, ∂J/∂w = −20 MPa, α = 0.5, and w = −10 MPa. What is the new w? Which way did it move, and why?
   <details><summary>Answer</summary>w_new = −10 − 0.5 × (−20) = 0 MPa. It increased, because a negative slope means the cost goes down to the right, so the step goes right.</details>
2. Your learning curve is still falling steadily after 1,000 iterations. Your classmate's curve shoots up to `inf`. What should each of you change?
   <details><summary>Answer</summary>Yours: α is probably too small — increase it (e.g., ×10) or run more iterations. Your classmate's: α is too large — decrease it (e.g., ÷10).</details>
3. Why do we fit the `StandardScaler` on the training set only?
   <details><summary>Answer</summary>The test set must stay unseen to give an honest estimate of performance on new data. If the scaler learned the mean and standard deviation from the test data, information from the test set would leak into training.</details>
4. A degree-9 polynomial has a training MAE of 5 MPa and a test MAE of 19 MPa; a degree-2 polynomial has 7 MPa and 9 MPa. Which would you use, and what is happening to the first one?
   <details><summary>Answer</summary>Use the degree-2 model: its test error is much lower. The degree-9 model is overfitting — it bends to pass near the training points (memorizing noise) and swings wildly between them, so it fails on new mixes.</details>
5. The 8-feature concrete model has a test MAE of about 7.7 MPa. A supplier wants to use it instead of 28-day cylinder tests. Give two reasons to say no and one good use of the model.
   <details><summary>Answer</summary>Reasons to say no (any two): an average miss of ~8 MPa (and larger worst cases) is big compared with specified strengths of roughly 20–40 MPa; the training data are laboratory mixes from one 1998 study, not this supplier's materials and site conditions; the engineer of record remains responsible and acceptance testing is required. Good uses: screening trial mixes before testing, flagging suspicious test results, planning.</details>

## Coming up
- **Lab 04 (this week's lab day):** code gradient descent from scratch, compare learning rates (0.001, 0.01, 0.1, 1.0, and a diverging 1.3), scale features, then use scikit-learn on all 8 concrete inputs with a train/test split. It ends with an **exit ticket**: 3 short questions you answer alone, without AI (AI-Free), during the last 10 minutes of lab.
- **Homework 2** is posted: Part A (by hand) is AI-Free; Parts B–D are AI-Assisted. **Due end of Week 5, Sunday 11:59 pm** on Brightspace.
- **Next week:** Neural Networks, Part 1 — from a line to a neuron. The model changes; the recipe (model + cost + gradient descent) does not. Short quiz on this week at the start of the Week 5 lecture day.
