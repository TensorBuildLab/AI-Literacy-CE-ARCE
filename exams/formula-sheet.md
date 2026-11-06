# Midterm Formula Sheet

*This sheet is printed and handed out with the exam. You do not need to memorize these formulas — you need to know what they mean and how to use them.*

## Linear regression (one feature)
- Model (prediction): **ŷ = f₍w,b₎(x) = w·x + b**
- Error for example *i*: **e⁽ⁱ⁾ = f₍w,b₎(x⁽ⁱ⁾) − y⁽ⁱ⁾**  (prediction minus true value)
- Cost (mean squared error, halved): **J(w, b) = (1 / 2m) · Σᵢ (f₍w,b₎(x⁽ⁱ⁾) − y⁽ⁱ⁾)²**, where *m* = number of examples

## Gradient descent
- Gradients: **∂J/∂w = (1/m) · Σᵢ (f₍w,b₎(x⁽ⁱ⁾) − y⁽ⁱ⁾) · x⁽ⁱ⁾**  **∂J/∂b = (1/m) · Σᵢ (f₍w,b₎(x⁽ⁱ⁾) − y⁽ⁱ⁾)**
- Update (both at the same time): **w ← w − α · ∂J/∂w**  **b ← b − α · ∂J/∂b**  (α = learning rate)

## Evaluation (regression)
- Mean absolute error: **MAE = (1/m) · Σ |ŷ⁽ⁱ⁾ − y⁽ⁱ⁾|**
- Root mean squared error: **RMSE = √[ (1/m) · Σ (ŷ⁽ⁱ⁾ − y⁽ⁱ⁾)² ]**
- Coefficient of determination: **R² = 1 − Σ (y⁽ⁱ⁾ − ŷ⁽ⁱ⁾)² / Σ (y⁽ⁱ⁾ − ȳ)²**  (ȳ = mean of y)

## Neural networks
- One neuron: **z = w₁x₁ + w₂x₂ + … + b**, then output **a = g(z)**
- Activation functions: **ReLU(z) = max(0, z)**  **sigmoid(z) = 1 / (1 + e⁻ᶻ)**
- Parameters in one fully connected layer with *n_in* inputs and *n_out* neurons: **n_in × n_out + n_out** (weights + biases)

## Evaluation (classification)
| | Predicted positive | Predicted negative |
|---|---|---|
| **Actually positive** | True positive (TP) | False negative (FN) |
| **Actually negative** | False positive (FP) | True negative (TN) |

- **Accuracy = (TP + TN) / (TP + TN + FP + FN)**
- **Precision = TP / (TP + FP)** — of the items flagged positive, the fraction that really are
- **Recall = TP / (TP + FN)** — of the real positives, the fraction we found
