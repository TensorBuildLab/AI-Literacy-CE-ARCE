# Lab 04 — Gradient Descent

**Week 4 lab day · about 75 minutes · AI-Assisted** · **Due:** Sunday 11:59 pm (Arizona time) of this week, on Brightspace.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/TensorBuildLab/AI-Literacy-CE-ARCE/blob/main/labs/lab04-gradient-descent/Lab04_Gradient_Descent.ipynb)

Grid search worked for two numbers, but it cannot work for many. Today you write **gradient descent**: start somewhere, find which way is downhill, take a step, and repeat. The same method trains neural networks and large language models. Then you fit a model with all 8 concrete inputs in **scikit-learn** and test it fairly, on mixes it has never seen.

## What you'll do

1. **Gradients** — write `compute_gradient(x, y, w, b)` and check it with a numerical slope.
2. **The descent loop** — write `gradient_descent(x, y, w0, b0, alpha, num_iters)`, plot the learning curve, and watch the path bend across the cost contour map.
3. **Learning rate** — compare α = 0.001, 0.01, 0.1, and 1.0, then see α = 1.3 diverge (the cost grows without limit).
4. **Feature scaling** — standardize the input and see gradient descent reach the same line about 10× faster.
5. **All 8 inputs with scikit-learn** — train/test split (80/20, `random_state=42`), `StandardScaler`, `LinearRegression`; MAE, RMSE, and R² compared with a **baseline** (the simplest possible model: always predict the average strength); a predicted-vs-actual plot; and a careful reading of the coefficients.

There are 8 short `# TODO` cells, self-checks, and written questions. Questions marked 🏠 may be finished after lab; they are still part of the lab.

## Before the lab

- [ ] Finish Lab 03. You will use `predict` and `compute_cost` again (they are provided at the top).
- [ ] Review the Week 4 lecture slides on the gradient formulas and the update rule.
- [ ] Keep the [Python cheat sheet](../../resources/python-cheatsheet.md) open — the parts on loops and functions help most today.

## Data

`concrete_strength.csv` — 1,030 laboratory concrete tests (Yeh 1998, UCI Machine Learning Repository, CC BY 4.0). See [`data/README.md`](../../data/README.md).

## How it's graded

- **Completion** of the notebook: all TODO cells run, written answers filled in, and the AI-use acknowledgment at the end.
- **Exit ticket:** 3 short questions you answer alone, without AI (AI-Free), during the last 10 minutes of lab. If you must leave early, answer them on your own before you submit.
- **AI-Assisted:** AI help for explanations and debugging is fine; write the AI-use acknowledgment at the end.
- **Due:** Sunday 11:59 pm (Arizona time) of this week, on Brightspace. Late work: see the syllabus late-work table (two grace days per semester, then −10% per day, up to 3 days). The lowest lab score is dropped.

## Troubleshooting

- **The self-check after `gradient_descent` says w and b are still 0** — the update lines are missing, or they are not indented inside the `for` loop (4 more spaces than the `for` line).
- **`x_scaled` does not have mean 0** — write `(x - x_mean) / x_std` with the parentheses. Without them, Python divides first.
- **The cost becomes `inf` or `nan`** — the learning rate is too large for this data (that is the point of the α = 1.3 cell). Use a smaller α.
- **`ValueError: too many values to unpack`** (or not enough) — `gradient_descent` returns four things in this lab: `w, b, J_history, path`.
- **`TypeError: ... 'NoneType' ...`** — a TODO above still contains `None`. Finish it, run it, then run the cell again.
- **`NotFittedError` from scikit-learn** — run `scaler.fit_transform(X_train)` and `model.fit(...)` before `transform` / `predict`.
- **Anything else** — choose **Runtime → Restart session**, then run all cells from the top.

## Related

- Lecture: [Week 4 — How Machines Learn, Part 2](../../lectures/week04-how-machines-learn-2/)
- Previous lab: [Lab 03 — Model Representation and Cost](../lab03-model-and-cost/)
- Homework: [HW2 — Fit, Measure, Descend](../../homework/hw2-fit-measure-descend/) repeats this method on building heating loads.
