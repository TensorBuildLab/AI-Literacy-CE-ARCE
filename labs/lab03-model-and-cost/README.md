# Lab 03 — Model Representation and Cost

**Week 3 lab day · about 75 minutes · AI-Assisted** · **Due:** Sunday 11:59 pm (Arizona time) of this week, on Brightspace.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/TensorBuildLab/AI-Literacy-CE-ARCE/blob/main/labs/lab03-model-and-cost/Lab03_Model_and_Cost.ipynb)

You build the simplest machine-learning model — a straight line, f(x) = w·x + b — that predicts concrete strength from the water–cement ratio. More importantly, you build a way to *measure* how good a line is: the **cost function** J(w, b). Then you search for the line with the lowest cost and check it against NumPy.

## What you'll do

1. **Data and notation** — x⁽ⁱ⁾, y⁽ⁱ⁾, m, and ŷ for 1,030 concrete tests.
2. **The model** — write `predict(x, w, b)` and move a line by hand (optional sliders) until it follows the data.
3. **Errors and cost** — write `compute_cost(x, y, w, b)`, check it against the lecture's 3-mix hand calculation (J ≈ 0.67 MPa²), and compare the cost of several lines.
4. **The cost landscape** — plot J vs w (a bowl), a 3-D cost surface, and a contour map of J(w, b); find the minimum by **grid search** (trying every point on a grid).
5. **Check and limits** — compare with `numpy.polyfit`, report MAE and R², and see why a straight line cannot follow Abrams' law (and predicts negative strength outside the data).

There are 7 short `# TODO` cells, self-checks, and written questions. Questions marked 🏠 may be finished after lab; they are still part of the lab.

## Before the lab

- [ ] Finish Lab 02 (you will use the water–cement ratio column again).
- [ ] Review the Week 3 lecture slides on the model f(x) = w·x + b and the cost function.
- [ ] Keep the [Python cheat sheet](../../resources/python-cheatsheet.md) open — especially the parts on loops (indentation) and common errors.

## Data

`concrete_strength.csv` — 1,030 laboratory concrete tests (Yeh 1998, UCI Machine Learning Repository, CC BY 4.0). See [`data/README.md`](../../data/README.md).

## How it's graded

- **Completion** of the notebook: all TODO cells run, written answers filled in, and the AI-use acknowledgment at the end.
- **Exit ticket:** 3 short questions you answer alone, without AI (AI-Free), during the last 10 minutes of lab. If you must leave early, answer them on your own before you submit.
- **AI-Assisted:** AI help for explanations and debugging is fine; write the AI-use acknowledgment at the end.
- **Due:** Sunday 11:59 pm (Arizona time) of this week, on Brightspace. Late work: see the syllabus late-work table (two grace days per semester, then −10% per day, up to 3 days). The lowest lab score is dropped.

## Troubleshooting

- **`compute_cost` returns `None`** — every line marked TODO needs a formula, and the function must end with `return J`.
- **Your 3-mix cost is 6.0 instead of 0.67** — you wrote `/ 2 * m`. Python divides by 2 and then *multiplies* by m. Write `/ (2 * m)`.
- **Your cost is huge (thousands of MPa²)** — check the sign of w (the data slope downward).
- **`IndentationError`** — the lines inside an `if` or a `for` must start 4 spaces further right than the `if` / `for` line, and lines at the same level must line up exactly.
- **`TypeError: ... 'NoneType' ...`** — a TODO above still contains `None`. Finish it and run it, then run the cell again.
- **The grid cells are slow** — they compute about 8,000 costs and should take a few seconds. If they take minutes, make sure `compute_cost` uses NumPy arrays (no inner loop over the 1,030 tests).
- **The slider cell shows an error** — the sliders are optional. Skip that cell and change w and b in the cell above it.
- **Anything else** — choose **Runtime → Restart session**, then run all cells from the top.

## Related

- Lecture: [Week 3 — How Machines Learn, Part 1](../../lectures/week03-how-machines-learn-1/)
- Previous lab: [Lab 02 — Working with Data](../lab02-working-with-data/) · Next lab: [Lab 04 — Gradient Descent](../lab04-gradient-descent/)
