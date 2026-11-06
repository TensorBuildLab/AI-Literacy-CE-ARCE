# Practice Midterm — Solutions

*Try the [practice midterm](practice-midterm.md) under exam conditions before reading this.*

## Part A
| Q | Answer | Why |
|---|---|---|
| A1 | (b) | It acts on its own once installed (some autonomy) but never learns (no adaptivity). |
| A2 | (b) | AI ⊃ ML ⊃ DL ⊃ GenAI. Search is AI but not ML. |
| A3 | (c) | No labels + looking for unusual records = unsupervised anomaly detection. |
| A4 | (b) | The output is a category (yes/no). |
| A5 | (a) | The cost summarizes how wrong the predictions are. |
| A6 | (b) | Steps overshoot the bottom of the bowl and grow — divergence. |
| A7 | (b) | Great on training data, poor on unseen data. |
| A8 | (b) | Features on very different scales make the cost bowl long and narrow, so gradient descent zig-zags or crawls. |
| A9 | (b) | A stack of linear functions is still linear. |
| A10 | (b) | Local filters + weight sharing detect edges/cracks anywhere in the image with few parameters. |
| A11 | (a) | Sequences need memory of the past (RNN/LSTM) or past values fed as a sliding window. |
| A12 | (b) | Reuse features learned on a big dataset (e.g., ImageNet) for a new, smaller task. |

## Part B (model answers — other wordings earn full credit)
**B1.** In traditional programming, an engineer writes the rules — e.g., "heating energy = U·A·ΔT summed over the season" — and the program applies them to data to get answers. In machine learning, we give the computer examples of inputs (building geometry, weather) *and* the measured answers (energy use), and an algorithm finds the rules (the model's parameters) that best map inputs to answers. The ML model can then predict energy use for new buildings.

**B2.** Gradient descent finds parameters (w, b) that make the cost small. At the current parameters it computes the slope of the cost (the gradient), then takes a step downhill — opposite to the slope — and repeats until the cost stops decreasing. The learning rate α sets the step size: too small is slow; too large overshoots the minimum and can diverge.

**B3.** A neuron multiplies each input by a **weight**, adds them up, adds a **bias**, and passes that sum z through an **activation** function (such as ReLU, max(0, z)) to produce its output. The weights and bias are learned during training; the nonlinear activation lets networks of neurons model curved relationships.

**B4.** *Helped:* the pretrained network already learned general visual features (edges, textures) from millions of images, so only a small classifier needed training on 1,200 photos. *May not hold:* the bridge photos come from a different distribution — dirt, shadows, stains, joints, different camera height and lighting — so the model may confuse stains or shadows with cracks or miss cracks (distribution shift). It must be tested on labeled bridge photos before use.

## Part C
**C1.** (a) ŷ = 78 − 70x: 0.45 → **46.5 MPa**; 0.55 → **39.5 MPa**; 0.65 → **32.5 MPa**.
(b) Errors ŷ − y: **1.5, 1.5, 2.5 MPa**.
(c) J = (1/(2·3))·(1.5² + 1.5² + 2.5²) = (1/6)(2.25 + 2.25 + 6.25) = 10.75/6 = **1.79 MPa²**.

**C2.** At w = b = 0, both predictions are 0; errors = 0 − 2 = −2 and 0 − 4 = −4.
(a) ∂J/∂w = (1/2)[(−2)(1) + (−4)(3)] = (1/2)(−14) = **−7**; ∂J/∂b = (1/2)(−2 − 4) = **−3**.
(b) w = 0 − 0.05(−7) = **0.35**; b = 0 − 0.05(−3) = **0.15**.
(c) Before: J = (1/4)(2² + 4²) = **5.0**. After: predictions 0.35·1 + 0.15 = 0.50 and 0.35·3 + 0.15 = 1.20; errors −1.5 and −2.8; J = (1/4)(2.25 + 7.84) = **2.52**. Yes, the cost went down.

**C3.** (a) z₁ = 0.5·1 + 0.5·3 − 1 = **1**, h₁ = ReLU(1) = **1**; z₂ = 1·1 − 1·3 + 0 = **−2**, h₂ = ReLU(−2) = **0**; ŷ = −1·1 + 4·0 + 2 = **1**.
(b) 2·2 + 2 = 6 (hidden) + 2·1 + 1 = 3 (output) → **9**.
(c) 4·8 + 8 = 40; 8·1 + 1 = 9 → **49**.
(d) 2·3 + 3 = 9; 3·3 + 3 = 12; 3·2 + 2 = 8 → **29**.

**C4.** (a) **Underfitting.** Training and validation errors are close to each other (9.3 vs 9.6) but both stay high and stop improving. An MAE of ~9.3 kWh/m² is no better than always predicting the average, and far worse than linear regression (2.2) — the network has learned almost nothing (too simple, under-trained, or poorly set up, e.g., unscaled inputs). (b) Any two: a larger network (more neurons or layers), better or more informative features, scaling inputs, tuning the learning rate, training longer if still improving, trying a different model type.

**C5.** (a) Accuracy = (48 + 84)/150 = **88%**. Precision = 48/(48 + 6) = **88.9%**. Recall = 48/(48 + 12) = **80%**.
(b) **False negatives** (missed cracks) are more dangerous: a missed crack is never shown to the inspector and could hide real deterioration. False positives cost inspector time but are caught at review. So for screening we want high recall, even at some loss of precision.
