# HW3 — Neural Networks on Engineering Data

**Posted:** Week 6 · **Due:** Sunday 11:59 pm (Arizona time) at the end of Week 8, on Brightspace · **100 points** · Individual · about 5 hours

Late work: see the syllabus late-work table (two grace days per semester, then −10% per day, up to 3 days).

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/TensorBuildLab/AI-Literacy-CE-ARCE/blob/main/homework/hw3-neural-networks/HW3_Neural_Networks.ipynb)

Starter notebook: [`HW3_Neural_Networks.ipynb`](HW3_Neural_Networks.ipynb) · Builds on: [Lab 05](../../labs/lab05-first-neural-network/) and [Lab 06](../../labs/lab06-cnn-crack-detection/) · [Python cheat sheet](../../resources/python-cheatsheet.md)

## Overview

In Labs 05 and 06 you computed a neural network by hand, trained one to predict building heating loads, and used a pretrained CNN to find cracks in concrete. This homework asks you to do the same things more independently and to think like an engineer about the results:

- compute a forward pass and count parameters **by hand**;
- train a neural network on **concrete compressive strength** and compare it fairly with linear regression;
- run an **overfitting** study (bigger networks, smaller data sets);
- interpret a **confusion matrix** from a realistic inspection and a pair of **feature maps**;
- write a short essay: **when would you *not* use a neural network?**

Part A is also good practice for the **Week 7 midterm** (which covers Weeks 1–6). Do it before the exam.

## Learning goals

By completing this homework you will be able to:
1. Compute a forward pass and count the parameters of a small neural network by hand.
2. Train and evaluate a neural network (`MLPRegressor`) and compare it fairly with linear regression using training and test metrics.
3. Diagnose overfitting from training and test error as network size and data size change.
4. Interpret a confusion matrix (accuracy, recall, precision) and convolution feature maps.
5. Argue, with evidence, when a neural network is or is not appropriate in engineering practice.

## AI-use labels

| Part | Label | What it means here |
|---|---|---|
| A — By hand | **AI-Free** | No AI tools and no code. Use a calculator and show your arithmetic. |
| B — MLP vs. linear regression | **AI-Assisted** | You may ask an AI tool to explain concepts or help debug. |
| C — Overfitting study | **AI-Assisted** | Same. |
| D — Interpreting a classifier | **AI-Assisted** | Same. |
| E — Essay | **AI-Assisted** | You may use AI to brainstorm or check grammar; the ideas, evidence, and wording must be yours. |

Complete the **AI-use acknowledgment** at the end of the notebook with the course template: *"I acknowledge the use of [tool and version] to [specific use]. Prompts I used included [paste or summarize]. I checked the output by [how I verified it]. I am responsible for this work."* — or *"I did not use AI tools for this assignment."* **A missing acknowledgment costs 5 points.** You are responsible for every line of code and every sentence you submit.

## Tasks

All tasks are in the starter notebook. Cells marked `# TODO` are yours to complete; ✍️ cells are written answers.

### Part A — Neural networks by hand (25 points, AI-Free) · about 1 h
- **A1. Forward pass (15 pts).** A 2 → 3 → 1 network with ReLU predicts concrete strength from two scaled inputs. Compute every hidden neuron's z and h (6), the prediction ŷ in MPa (3), the squared-error loss (2), ŷ without the activation function (2), and explain what an "off" ReLU neuron means for gradient descent (2).
- **A2. Parameter counting (10 pts).** Count weights + biases for four networks (2 each) — including one with **two output neurons** and one that takes a whole photo as input — and explain why CNNs need far fewer parameters (2).

### Part B — Neural network vs. linear regression on concrete strength (25 points) · about 1 h
Use all 8 inputs of `concrete_strength.csv` to predict strength (MPa).
- **B1 (3 pts).** Split (80/20, `random_state=42`) and scale the inputs correctly.
- **B2 (5 pts).** A linear-regression **baseline** (a simple reference model the network must beat) with training and test MAE, RMSE, and R².
- **B3 (8 pts).** An `MLPRegressor` with two hidden layers of 32 neurons: scores, a labeled learning-curve plot (fill in the blanks), and a parameter count that matches A2(b).
- **B4 (4 pts).** Side-by-side predicted-vs-actual plots for both models on the test set (fill in the blanks).
- **B5 (5 pts).** Written comparison (4–6 sentences): which is better and by how much, a physical reason, signs of overfitting, and whether this accuracy is good enough for accepting a structural mix.

### Part C — Overfitting study (20 points) · about 40 min
- **C1 (8 pts).** With only 100 training mixes, train six networks from 1 neuron to two layers of 128; tabulate and plot training and test error against the number of parameters.
- **C2 (8 pts).** With a fixed big network (128, 128), vary the number of training mixes from 50 to 824; tabulate and plot training and test error.
- **C3 (4 pts).** Explain what you found (3–5 sentences) and recommend a model for a plant with only 60 test results.

### Part D — Interpreting a crack classifier (15 points) · about 45 min
- **D1 (8 pts).** A drone inspection of a parking-garage deck: 1,000 photos, 50 with cracks. Compute accuracy, the accuracy of always answering "no crack," recall, and precision (you met recall and precision in Lab 06) (2), then answer three questions about what the numbers mean for safety and how to set the decision threshold (6).
- **D2 (7 pts).** Compute two 3 × 3 filter outputs by hand (2), identify which filter highlights a crack in a photo and why (3), and compare learned and hand-made filters (2).

### Part E — Essay: when would you NOT use a neural network? (15 points) · about 45 min
150–250 words. Describe two specific CE/ARCE situations where a neural network is a poor choice and what you would use instead; one situation where it is a good choice and one check you would require; and cite at least one result from this homework or Labs 05–06.

## Deliverables

1. Your completed notebook **`HW3_Neural_Networks.ipynb`**, run top to bottom (**Runtime → Restart session and run all**) so every output and plot is visible.
2. *(Optional)* A clear photo or PDF of your handwritten Part A work, if you did not type it into the notebook.

## Rubric

| Part | Full credit looks like | Points | CLO / ABET SO |
|---|---|---|---|
| A1 | Every weighted sum shown; correct z, h, ŷ, loss, no-ReLU ŷ; clear "off neuron → zero gradient" explanation. Arithmetic slips with a correct method lose 1 point each. | 15 | CLO3 / SO 1 |
| A2 | Correct totals with per-layer counts; explanation mentions small, shared filters. | 10 | CLO3 / SO 1 |
| B1–B2 | Scaler fitted on training data only; correct baseline metrics on both sets. | 8 | CLO3 / SO 6 |
| B3 | Correct architecture and settings; scores shown; learning curve with title and labeled axes (units); parameter count matches A2(b). | 8 | CLO3 / SO 6 |
| B4 | Two labeled panels with a perfect-prediction line, test data only. | 4 | CLO3 / SO 6 |
| B5 | Uses the actual numbers; a physical reason (e.g., strength gain with age levels off); judges overfitting from train vs. test; sensible view on acceptance testing. | 5 | CLO3 / SO 6 |
| C1–C2 | Loops complete; tables and both plots produced and readable. | 16 | CLO3 / SO 6 |
| C3 | Correct trends described with numbers; recommendation fits 60 data points and is justified. | 4 | CLO3 / SO 6 |
| D1 | Correct four numbers; explains why accuracy misleads here; consequences of FN vs. FP; threshold trade-off and a human-in-the-loop use. | 8 | CLO7 / SO 6 |
| D2 | Correct hand calculation; identifies the right filter with a reason tied to edge direction; balanced pros/cons of learned filters. | 7 | CLO3 / SO 1 |
| E | Two specific situations with course-based reasons and alternatives (8); a good use with a required check (3); evidence from HW/labs (3); clear, within length (1). | 15 | CLO7 / SO 4 |
| | **Total** | **100** | |

A missing AI-use acknowledgment costs 5 points. Code that does not run top to bottom: the affected parts are graded on what is visible.

## Submission

1. In Colab: **Runtime → Restart session and run all**. Fix any errors.
2. **File → Download → Download .ipynb**.
3. Upload it (and the optional Part A photo/PDF) to the **HW3** assignment on **Brightspace** by **Sunday 11:59 pm (Arizona time) at the end of Week 8**.

## Tips

- The whole notebook runs in about 5–10 minutes on Colab's free CPU. The loops in Part C train 11 networks; be patient.
- Reuse your Lab 05 and Lab 06 code: the learning curve, predicted-vs-actual plot, and precision/recall ideas are the same.
- Start Part A early — it is the best midterm practice in this assignment.
- Stuck? Come to office hours or post on the Brightspace discussion board (describe the problem; don't post your solution code).
