# Midterm Exam — Study Guide

**When:** Week 7, lab day (75 minutes) · **Covers:** Weeks 1–6 · **AI-Free, closed book**
**Provided:** the [formula sheet](formula-sheet.md) · **Bring:** pencil and any non-graphing, non-programmable calculator (no phones, laptops, smartwatches, or AI tools)

## Format (100 points)
| Part | What | Points |
|---|---|---|
| A | 12 multiple-choice questions on concepts and vocabulary | 30 |
| B | 4 short-answer questions (2–5 sentences each) | 30 |
| C | 5 short problems: a cost value, one gradient-descent step, a tiny forward pass + parameter counts, reading a learning curve, a confusion matrix | 40 |

The exam rewards **understanding** — explaining *why* — more than memorizing. Calculations are short and use the formula sheet.

## Practice
- **[Practice midterm](practice-midterm.md)** — same format, different numbers. Do it timed (75 min), then check the **[solutions](practice-midterm-solutions.md)**.
- Redo the **Check yourself** questions at the bottom of each week's lecture page (Weeks 1–6).
- Re-run the key cells in Labs 03–06 and explain each output out loud.

## Checklist: you should be able to…

### Week 1 — What AI is (and isn't)
- [ ] Use **autonomy** and **adaptivity** to decide whether a system is AI, not AI, or "kind of" AI — and explain why.
- [ ] Draw the nested map AI ⊃ machine learning ⊃ deep learning ⊃ generative AI, and name AI branches outside machine learning (search/planning, logic/rules, optimization, robotics).
- [ ] Explain why an engineer stays responsible for work done with AI tools.

### Week 2 — Machine learning, deep learning, generative AI
- [ ] Contrast traditional programming (rules + data → answers) with machine learning (data + answers → rules).
- [ ] Identify **features (X)** and the **target (y)** in an engineering dataset.
- [ ] Classify a task as supervised (**regression** or **classification**), **unsupervised**, or **reinforcement learning**, with CE/ARCE examples.
- [ ] Explain what makes deep learning different (it learns its own features) and why it took off (data, compute, algorithms).
- [ ] Explain why data quality and representativeness matter.

### Weeks 3–4 — How machines learn
- [ ] Use the linear model ŷ = w·x + b to make predictions and compute errors.
- [ ] Compute the cost J(w, b) for a few data points, and explain what the cost measures.
- [ ] Explain the "bowl" shape of the cost and why we want its lowest point.
- [ ] Do **one gradient-descent step** by hand, and explain the update rule in words.
- [ ] Describe what happens when the learning rate is too small, about right, or too large; read a learning curve (cost vs. iterations).
- [ ] Explain why we scale features and why we split data into training and test sets — and why the scaler is fit on the training data only (otherwise test information leaks into training).
- [ ] Recognize **underfitting** and **overfitting** from training vs. test error.
- [ ] Compute and interpret MAE, RMSE (in the target's units, e.g., MPa) and R²; explain why RMSE grows more than MAE when a few errors are large.

### Week 5 — Neural networks
- [ ] Compute a neuron's output: weighted sum + bias, then activation.
- [ ] Explain why activation functions must be **nonlinear**.
- [ ] Do a forward pass through a tiny network with ReLU, and **count parameters** of a fully connected network.
- [ ] Explain training as "the same recipe": a loss + gradient descent, with backpropagation passing blame backward.
- [ ] Explain epochs, learning rate, network width/depth, and early stopping.

### Week 6 — CNNs and sequence models
- [ ] Explain how a convolution filter slides over an image to detect local patterns (e.g., crack edges) and why this suits images.
- [ ] Describe the CNN stack (convolution → pooling → … → fully connected → output).
- [ ] Explain **transfer learning** and why it works with small datasets like 1,200 crack photos — and one risk.
- [ ] Explain why sequence data (hourly traffic, building load) needs models with memory (RNN/LSTM) or sliding windows; turn a time series into sliding-window training examples (inputs and target) and name a simple baseline such as "same hour last week".
- [ ] Read a **confusion matrix**: accuracy, precision, recall; decide which error type matters more for a given engineering use.

## Exam-day tips
- Write units on every number. Show your work on calculations — partial credit is generous.
- If a question seems ambiguous, write down your assumption and answer it.
- Budget ~20 min for Part A, ~20 min for Part B, ~30 min for Part C, 5 min to check.
