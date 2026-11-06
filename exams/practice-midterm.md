# Practice Midterm (Weeks 1–6)

*75 minutes · closed book · formula sheet and basic calculator allowed · 100 points*
*Solutions: [practice-midterm-solutions.md](practice-midterm-solutions.md) — try the whole exam first!*

---

## Part A — Multiple choice (12 × 2.5 = 30 points)
Circle the **best** answer.

**A1.** A parking garage gate opens whenever a ticket is inserted and never changes its behavior. On the autonomy–adaptivity map it is:
(a) high autonomy, high adaptivity (b) some autonomy, no adaptivity (c) no autonomy, high adaptivity (d) generative AI

**A2.** Which statement is correct?
(a) All AI is machine learning. (b) Generative AI is a branch of deep learning. (c) Deep learning does not use neural networks. (d) Route-finding search is a kind of deep learning.

**A3.** An engineer has 300 bridge sensor records with no labels and wants to find records that look unusual. This is:
(a) supervised regression (b) supervised classification (c) unsupervised learning (anomaly detection) (d) reinforcement learning

**A4.** Predicting whether a pavement section will need repair next year (yes/no) is:
(a) regression (b) classification (c) clustering (d) generation

**A5.** In ML, the cost function:
(a) measures how far predictions are from the true values across the data (b) stores the training data (c) sets the learning rate (d) counts the features

**A6.** During gradient descent the cost goes *up* every iteration and quickly becomes huge. The most likely cause:
(a) too many data points (b) learning rate too large (c) learning rate too small (d) features were scaled

**A7.** A model has R² = 0.98 on the training set and R² = 0.41 on the test set. This suggests:
(a) underfitting (b) overfitting (c) a perfect model (d) the learning rate is too small

**A8.** Why do we scale features (e.g., cement in kg/m³ and age in days) before gradient descent?
(a) To change the units to SI (b) So gradient descent converges faster and more evenly (c) To remove outliers (d) To make the model nonlinear

**A9.** If every neuron in a deep network used a *linear* activation (no ReLU), the network would:
(a) be able to fit any curve (b) still be equivalent to a single linear model (c) train faster and more accurately (d) become a CNN

**A10.** A CNN suits photos of concrete better than a plain fully connected network mainly because:
(a) it uses fewer images (b) its small filters slide across the image and detect the same local pattern anywhere (c) it needs no training (d) it only works on color images

**A11.** For forecasting tomorrow's hourly traffic volume from the past week of hourly counts, the most natural architecture discussed in class is:
(a) a sequence model such as an RNN/LSTM (or a model fed sliding windows) (b) a CNN for images (c) k-means clustering (d) a spreadsheet formula

**A12.** "Transfer learning" means:
(a) moving data between computers (b) reusing a model pretrained on a large dataset and adapting it to a new task (c) training two models at once (d) converting a regression model into a classifier

---

## Part B — Short answer (4 × 7.5 = 30 points)
Answer in 2–5 sentences.

**B1.** Explain the difference between traditional programming and machine learning using a building-energy example.

**B2.** In your own words, what does gradient descent do, and what is the role of the learning rate α?

**B3.** What does a single artificial neuron compute? Use the words *weights*, *bias*, and *activation*.

**B4.** A team trains a crack classifier by transfer learning on 1,200 close-up photos of clean campus walls and gets 98% test accuracy. They want to use it on drone photos of dirty, shadowed bridge decks. Give one reason transfer learning helped, and one reason the 98% may not hold on the bridges.

---

## Part C — Problems (40 points). Show your work and units.

**C1. Cost (8 pts).** Three concrete mixes (x = water–cement ratio, y = strength in MPa): (0.45, 45), (0.55, 38), (0.65, 30). Model: w = −70 MPa, b = 78 MPa.
(a) Compute the three predictions ŷ. (b) Compute the three errors (ŷ − y). (c) Compute J(w, b).

**C2. One gradient-descent step (8 pts).** Data: (x, y) = (1, 2) and (3, 4). Start at w = 0, b = 0, learning rate α = 0.05.
(a) Compute ∂J/∂w and ∂J/∂b. (b) Compute the new w and b. (c) Compute the cost before and after the step. Did it go down?

**C3. Forward pass and parameters (10 pts).** Inputs x₁ = 1, x₂ = 3. Hidden neuron 1: weights (0.5, 0.5), bias −1. Hidden neuron 2: weights (1, −1), bias 0. Both hidden neurons use ReLU. Output neuron (linear): weights (−1, 4), bias 2.
(a) Compute z₁, h₁, z₂, h₂, and ŷ. (b) How many parameters does this 2-2-1 network have? (c) How many parameters does a fully connected 4-8-1 network have? (d) A 2-3-3-2 network?

**C4. Learning curves (7 pts).** A neural network predicting heating load (kWh/m²) gives these errors (MAE):

| Epoch | 10 | 20 | 40 | 80 | 160 |
|---|---|---|---|---|---|
| Training MAE | 9.8 | 9.5 | 9.4 | 9.3 | 9.3 |
| Validation MAE | 10.1 | 9.8 | 9.7 | 9.6 | 9.6 |

For reference: always predicting the average heating load gives MAE ≈ 9.3 kWh/m², and a simple linear regression gives MAE ≈ 2.2 kWh/m² on the same data.

(a) Is the model overfitting, underfitting, or about right? Explain using the numbers. (b) Suggest two changes that could help.

**C5. Confusion matrix (7 pts).** A crack detector is tested on 150 images:

| | Predicted crack | Predicted no crack |
|---|---|---|
| **Actual crack (60)** | 48 | 12 |
| **Actual no crack (90)** | 6 | 84 |

(a) Compute accuracy, precision (crack), and recall (crack). (b) For a tool that screens bridge photos before an inspector reviews them, which error is more dangerous — false negatives or false positives? Why?
