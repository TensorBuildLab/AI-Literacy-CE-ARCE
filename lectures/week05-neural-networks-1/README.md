# Week 5 — Neural Networks, Part 1: Neurons, Layers, and Training

**Slides:** [PDF](Week05_Neural-Networks-1.pdf) · [PowerPoint](Week05_Neural-Networks-1.pptx) · **Lab:** [Lab 05 — Your First Neural Network](../../labs/lab05-first-neural-network/) · **Homework:** [HW2 — Fit, Measure, Descend](../../homework/hw2-fit-measure-descend/) is due this week (Sunday 11:59 pm)

## Learning objectives
By the end of this week you can:
1. Explain a neuron as a weighted sum plus an activation function, and explain why the activation must be nonlinear.
2. Compute a forward pass by hand for a tiny network and count its parameters (weights + biases).
3. Describe training in words: loss, gradient descent, backpropagation, epochs, and batches.
4. Recognize overfitting in a learning curve and explain early stopping.
5. Compare a neural network with linear regression on a building-energy dataset.

## The big ideas
- **A neuron is Week 3's line plus a bend.** It computes a weighted sum **z = w₁x₁ + w₂x₂ + … + b** (exactly ŷ = w·x + b) and then applies an **activation function**: **a = g(z)**. The weights and biases are the numbers training adjusts.
- **Why the bend matters:** stacking layers *without* an activation collapses into one straight line — e.g., h = 2x + 1 followed by ŷ = −0.5h + 3 is just ŷ = −x + 2.5. With a nonlinear activation such as **ReLU(z) = max(0, z)**, a network can bend to follow curves like the fast early strength gain of concrete. Sigmoid (0 to 1) and tanh (−1 to 1) are the other classic activations.
- **Layers:** an input layer (the features), one or more **hidden layers** (new combinations the network invents), and an output layer (the prediction). When every neuron connects to every neuron in the previous layer, the network is a **multilayer perceptron (MLP)**. "Deep" learning = many hidden layers.
- **Forward pass, worked example** (2 inputs → 2 ReLU hidden neurons → 1 linear output), with x₁ = 1.0, x₂ = 2.0:
  hidden 1: z₁ = 0.5·1.0 − 1.0·2.0 + 0 = −1.5 → h₁ = ReLU(−1.5) = 0;
  hidden 2: z₂ = 1.0·1.0 + 0.5·2.0 − 1 = 1.0 → h₂ = 1.0;
  output: ŷ = 1.0·0 − 2.0·1.0 + 0.5 = **−1.5**. In matrix form a whole layer is **h = ReLU(W x + b)**.
- **Counting parameters:** each layer has (inputs × neurons) weights + one bias per neuron. The 2–2–1 network has 4 + 2 + 2 + 1 = **9** parameters; a heating-load network with layers 8 → 32 → 16 → 1 has 833; a network with **two outputs** (heating and cooling load), 4 → 3 → 3 → 2, has 15 + 12 + 8 = 35 (each output neuron has its own weights and bias); a linear model with 8 inputs has 9; small language models have hundreds of millions.
- **Training is the same recipe as Week 4:** forward pass → loss (e.g., average squared error) → **backpropagation** (the chain rule passes "blame" for the error backward, giving ∂J/∂w for every weight) → update **w ← w − α·∂J/∂w** → repeat for many **epochs** (full passes through the data), usually in **batches** (small groups of examples per update). You choose the knobs (learning rate, width, depth, epochs, batch size); training chooses the weights. Unlike linear regression's single bowl, a network's cost landscape has many valleys: different random starting weights land in different, usually similar, ones — which is why results change a little with the random seed.
- **Overfitting:** a big network trained on 20 concrete mixes drove its training error down while its error on unseen mixes rose from about 9 MPa (best, near epoch 80) to about 16 MPa. **Early stopping** keeps the weights from the best validation point; smaller networks, more data, and regularization also help.
- **Case study:** on 768 simulated building shapes, a (32, 16) network predicted annual heating load on 154 unseen buildings with **MAE ≈ 0.98 kWh/m² (R² ≈ 0.98)**, versus **MAE ≈ 2.18 kWh/m² (R² ≈ 0.91)** for linear regression. A network is worth it only when it clearly beats a **baseline** (the simplest sensible model, here linear regression) on test data; with tiny datasets, a trusted physics equation (heat loss = U·A·ΔT), or a need to explain every coefficient, think twice.

## Key terms
| Term | Plain-language meaning |
|---|---|
| Neuron | A weighted sum of inputs plus a bias, passed through an activation function |
| Weight / bias | The adjustable numbers in a neuron; weights scale inputs, the bias shifts the result |
| Activation function | The "bend" applied to a neuron's weighted sum (ReLU, sigmoid, tanh) |
| ReLU | Rectified linear unit: max(0, z) — negatives become 0, positives pass through |
| Layer (input, hidden, output) | A group of neurons that all take the same inputs; hidden layers sit between input and output |
| Multilayer perceptron (MLP) | A fully connected network: every neuron uses all outputs of the previous layer |
| Forward pass | Running inputs through the network, layer by layer, to get a prediction |
| Parameters | All the weights and biases the network learns |
| Loss | The error measure training tries to reduce (the cost J from Weeks 3–4) |
| Backpropagation | Computing every weight's slope ∂J/∂w by passing the error backward with the chain rule |
| Epoch | One full pass through all the training examples |
| Batch | A small group of examples used for one gradient-descent update |
| Hyperparameter | A setting you choose before training (learning rate, layers, neurons, epochs) |
| Early stopping | Stopping training when the validation error stops improving |
| Baseline | The simplest sensible model or rule (e.g., linear regression, or "predict the average"); a new model must beat it to be worth using |

## Read / watch
**Required (≈ 30 min total)**
- **3Blue1Brown: "But what is a neural network?" (Deep learning, chapter 1)** — <https://www.youtube.com/watch?v=aircAruvnKk> (video, about 19 minutes). Neurons, layers, weights, and biases, clearly animated. Watch before the lab.
- **TensorFlow Playground** — <https://playground.tensorflow.org> (about 10 minutes: try the spiral data with different numbers of layers and neurons).

**Optional**
- **3Blue1Brown: "Backpropagation, intuitively" (chapter 3)** — <https://www.youtube.com/watch?v=Ilg3gGewQ5U> (video, about 13 minutes). The "passing blame backward" idea in pictures; helpful for HW3.
- **Google ML Crash Course: "Neural networks" module** — <https://developers.google.com/machine-learning/crash-course/neural-networks> (about 1 hour, with interactive exercises on nodes, hidden layers, and activation functions).

## Check yourself
1. A neuron has weights 2 and −1, bias 0.5, and a ReLU activation. What does it output for inputs x₁ = 1 and x₂ = 3?
   <details><summary>Answer</summary>z = 2·1 + (−1)·3 + 0.5 = −0.5, so the output is ReLU(−0.5) = 0.</details>
2. Why does a network with five layers but no activation functions do no better than linear regression?
   <details><summary>Answer</summary>Each layer is a linear function, and a linear function of a linear function is still linear. The five layers collapse into one straight-line (linear) model, so depth adds nothing. A nonlinear activation such as ReLU is what lets the network bend.</details>
3. How many parameters does a network with 4 inputs, one hidden layer of 3 neurons, and 1 output neuron have?
   <details><summary>Answer</summary>Hidden layer: 4 × 3 weights + 3 biases = 15. Output layer: 3 weights + 1 bias = 4. Total = 19. (With 2 output neurons instead — e.g., heating and cooling load — the output layer has 3 × 2 + 2 = 8, so the total is 23.)</details>
4. During training, the training error keeps falling, but the validation error reaches its lowest value at epoch 80 and then rises. What is happening, and what should you do?
   <details><summary>Answer</summary>The network is overfitting: after epoch 80 it starts memorizing the training examples (including their noise) instead of learning the general pattern. Use early stopping (keep the weights from about epoch 80), or use a smaller network, more data, or regularization.</details>
5. A neural network predicts heating load with test MAE 0.98 kWh/m², and linear regression gets 2.18 kWh/m². Give one reason to prefer the network and one reason an engineer might still choose the linear model.
   <details><summary>Answer</summary>Prefer the network: it more than halves the error on buildings it never saw. Choose the linear model if (any one): you must explain each coefficient to a client or reviewer; the data set is small or the new buildings are outside the training range; 2.18 kWh/m² is already accurate enough for the decision; the simple model is easier to check and maintain.</details>

## Coming up
- **Lab 05 (this week's lab day):** TensorFlow Playground experiments, the 2–2–1 forward pass in NumPy (check ŷ = −1.5), then train scikit-learn's `MLPRegressor` on heating load, compare with linear regression, and watch train vs test error as you change the network size. The lab ends with an **exit ticket**: 3 short questions you answer alone, without AI (AI-Free), during the last 10 minutes of lab. **Due:** Sunday 11:59 pm (Arizona time) of this week, on Brightspace.
- **HW2 is due Sunday 11:59 pm** on Brightspace.
- **Next week:** Neural Networks, Part 2 — CNNs for images (crack detection) and sequence models for time series (traffic). HW3 is posted. Short quiz on this week at the start of the Week 6 lecture day.
