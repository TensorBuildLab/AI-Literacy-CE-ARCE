# Week 3 — How Machines Learn, Part 1: Linear Regression and the Cost Function

**Slides:** [PDF](Week03_How-Machines-Learn-1.pdf) · [PowerPoint](Week03_How-Machines-Learn-1.pptx) · **Lab:** [Lab 03 — Model Representation and Cost](../../labs/lab03-model-and-cost/) · **Homework:** [HW1 — AI or Not? Exploring Engineering Data](../../homework/hw1-ai-or-not/) is **due this Sunday, 11:59 pm**

## Learning objectives
By the end of this week you can:
1. Write a linear model ŷ = f_{w,b}(x) = w·x + b and explain w (slope) and b (intercept) in engineering units.
2. Use the notation x⁽ⁱ⁾, y⁽ⁱ⁾, m, and ŷ to describe a dataset.
3. Compute the squared-error cost J(w, b) by hand for a few points.
4. Read a cost curve and a contour map, and say where the best (w, b) is.
5. Judge a fit with MAE (in MPa) and R², and name the limits of a straight line.

## The big ideas
- The running example: predict concrete **compressive strength** (MPa) from the **water–cement ratio** (w/c = water ÷ cement, both in kg/m³) for 1,030 laboratory mixes. More water per kg of cement → weaker concrete.
- The simplest machine-learning model is a straight line, **ŷ = f_{w,b}(x) = w·x + b**. The **parameters** w (slope, MPa per unit of w/c) and b (intercept, MPa) are what the machine learns. Notation: m = number of examples (1,030), x⁽ⁱ⁾ and y⁽ⁱ⁾ = the i-th example (the superscript is an index, not a power), ŷ = prediction.
- For each example the **error** (residual) is ŷ⁽ⁱ⁾ − y⁽ⁱ⁾. Over-predicting strength is on the unsafe side.
- The **cost function** scores a whole line with one number: **J(w, b) = (1/2m) Σ (f_{w,b}(x⁽ⁱ⁾) − y⁽ⁱ⁾)²** — prediction minus truth, squared, summed, averaged, halved. Squaring stops positive and negative errors from canceling and punishes big misses; the ½ makes next week's math simpler. Units: MPa².
- Plotting J for every possible line gives a **bowl** (J vs w) or a 3-D bowl / contour map (J over w and b). The **bottom of the bowl is the best-fit line**: for our data w ≈ −26.6 MPa and b ≈ 55.8 MPa — each +0.1 in w/c costs about 2.7 MPa of strength.
- Engineers need errors in engineering units: **MAE** (average size of a miss) ≈ 11.9 MPa and **R²** (share of variation explained) ≈ 0.25, both computed on all 1,030 mixes (all data). Right trend, but errors too large to design with.
- A line is an approximation. The real relationship is **curved** (Abrams' law, 1918: strength ≈ A / B^(w/c)), and age and the other ingredients matter too. Fixes come next: more features (Week 4) and more flexible models (Week 5). Always plot the data before trusting one number.
- The machine-learning recipe: **model → cost → optimize → evaluate.** The same four steps train neural networks and large language models.

## Key terms
| Term | Plain-language meaning |
|---|---|
| Linear regression | Fitting a straight line (or flat surface) to predict a number |
| Parameters (w, b) | The numbers inside the model that learning adjusts: weight (slope) and bias (intercept) |
| m | The number of examples in the dataset |
| x⁽ⁱ⁾, y⁽ⁱ⁾ | The input and true output of the i-th example |
| ŷ ("y-hat") | The model's prediction |
| Error / residual | Prediction minus truth, ŷ − y |
| Cost function J(w, b) | One number that scores how badly a model fits: here, half the average squared error |
| Cost bowl / contour map | Plots of J over the parameters; the lowest point is the best fit |
| Least squares | Choosing the line with the lowest sum of squared errors (what `numpy.polyfit` does) |
| MAE | Mean absolute error: the average size of a miss, in the target's units |
| R² | Coefficient of determination: the share of the variation in y the model explains (1 = perfect, 0 = no better than the average) |
| Abrams' law | The 1918 finding that concrete strength falls roughly exponentially as the w/c ratio rises |

## Read / watch
**Required (≈ 45 min total)**
- **Google ML Crash Course: "Linear regression"** — <https://developers.google.com/machine-learning/crash-course/linear-regression> (whole module about 80 minutes). Read only the first page and the **Loss** page this week (about 30 minutes); save the Gradient descent and Hyperparameters pages for Week 4. Note: they call J the "loss."
- **Elements of AI, Chapter 4, Section III: "Regression"** — <https://course.elementsofai.com/4/3> (free; about 15 minutes). A gentle, non-coding take on fitting a line.

**Optional**
- **Course data README** — [`data/README.md`](../../data/README.md) (5 minutes). Where the concrete data come from and what each column means.

## Check yourself
1. In ŷ = w·x + b for strength (MPa) vs w/c ratio, what are the units of w and b, and what sign do you expect for w?
   <details><summary>Answer</summary>The w/c ratio has no units, so w is in MPa (MPa per 1.0 change in w/c) and b is in MPa. w should be negative: more water per unit of cement gives lower strength.</details>
2. What does x⁽²⁾ mean? Is it "x squared"?
   <details><summary>Answer</summary>It is the input (here, the w/c ratio) of the second example in the dataset. The superscript in parentheses is an index, not a power.</details>
3. Three mixes have (x, y) = (0.4, 50), (0.6, 38), (0.8, 30) MPa. Compute J for the line ŷ = −50x + 70.
   <details><summary>Answer</summary>Predictions 50, 40, 30 MPa → errors 0, 2, 0 → squares 0, 4, 0 → sum 4 → J = 4 / (2 × 3) ≈ 0.67 MPa².</details>
4. Why do we square the errors instead of just adding them up?
   <details><summary>Answer</summary>Plain errors can be positive or negative and cancel out, so a bad line could have a total error near zero. Squares are never negative, they punish large misses more than small ones, and they make a smooth bowl-shaped cost that calculus (gradient descent) can minimize.</details>
5. The best line (all data) has MAE ≈ 11.9 MPa and R² ≈ 0.25. Would you use it to approve a mix for a structural slab? Why or why not?
   <details><summary>Answer</summary>No. An average miss of about 12 MPa is large compared with typical specified strengths of roughly 20–40 MPa, and the line explains only about a quarter of the variation. It ignores age and other ingredients, misses the curved (Abrams' law) shape, and is based on laboratory data. Acceptance should rely on standard tests; the model could at most help screen ideas.</details>

## Coming up
- **Lab 03 (this week's lab day):** write `predict` and `compute_cost`, plot the cost bowl and contour map, search for the best (w, b), and compare with `numpy.polyfit`. It ends with an **exit ticket**: 3 short questions you answer alone, without AI (AI-Free), during the last 10 minutes of lab.
- **Homework 1 is due Sunday at 11:59 pm** on Brightspace.
- **Next week:** How Machines Learn, Part 2 — gradient descent, the learning rate, more features, train/test splits, and overfitting. Short quiz on this week at the start of the Week 4 lecture day. Homework 2 is posted.
