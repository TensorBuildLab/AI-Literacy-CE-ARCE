# Lab 05 — Your First Neural Network

**Week 5 lab day · about 75 minutes · AI-Assisted** (exit ticket is AI-Free) · **Due:** Sunday 11:59 pm (Arizona time) of this week, on Brightspace.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/TensorBuildLab/AI-Literacy-CE-ARCE/blob/main/labs/lab05-first-neural-network/Lab05_First_Neural_Network.ipynb)

Notebook: [`Lab05_First_Neural_Network.ipynb`](Lab05_First_Neural_Network.ipynb) · Lecture: [Week 5 — Neural Networks, Part 1](../../lectures/week05-neural-networks-1/)

## What you'll do

In Weeks 3–4 you trained a straight line, ŷ = w·x + b, by minimizing a cost J with gradient descent. Today you stack those little models into a neural network.

| Part | Time | What happens |
|---|---|---|
| 1. TensorFlow Playground | 15 min | Watch a network learn in your browser. **Experiments 1–3:** 0 vs. 1 hidden layer, ReLU vs. linear activation. Experiment 4 (learning rate too big or too small) and two challenges are optional. Record what you see. |
| 2. A forward pass by hand | 20 min | Compute the 2 → 2 → 1 network from lecture in NumPy (x₁ = 1, x₂ = 2 → ŷ = −1.5), write `relu`, redo it with matrices (`W @ x + b`), and count its 9 parameters — including a network with 2 outputs. |
| 3. A network for building energy | 30 min | Train scikit-learn's `MLPRegressor` to predict the heating load (kWh/m²) of 768 building designs. Compare it with a linear-regression **baseline** (a simple reference model the network must beat), try different network sizes, plot the learning curve, and watch a big network overfit when it gets only 40 buildings. |
| Exit ticket | 10 min | 3 short questions you answer alone, without AI (AI-Free), during the last 10 minutes of lab. If you must leave early, answer them on your own before you submit. |

Questions marked 🏠 in the notebook may be finished at home before the deadline.

## Before the lab

- [ ] Review the Week 5 slides: neuron = weighted sum + activation, ReLU, forward pass, parameter counting, overfitting.
- [ ] Keep the [Python cheat sheet](../../resources/python-cheatsheet.md) open in a tab.
- [ ] Bring a laptop with a web browser and a Google account (for Colab).
- [ ] Open the notebook with the **Open in Colab** button, then **File → Save a copy in Drive**.
- [ ] Open <https://playground.tensorflow.org> in a second tab to check it loads.

## Data

`building_energy_efficiency.csv` — heating and cooling loads of 768 building shapes simulated in Ecotect (Tsanas & Xifara, *Energy and Buildings* 49, 2012; UCI, CC BY 4.0). All buildings have the same volume and materials; only shape, glazing, and orientation change. Details: [data README](../../data/README.md).

The notebook downloads it automatically with `get_data(...)` (about 40 kB). Nothing to install: everything runs on Colab's free CPU runtime.

## How it's graded

- **Completion (most of the grade):** every `# TODO` cell runs, and every required ✍️ question has a thoughtful answer in your own words (optional ones are marked). The AI-use acknowledgment statement is part of completion.
- **Exit ticket:** 3 short questions you answer alone, without AI (AI-Free), in the last 10 minutes of lab.
- **AI-use acknowledgment:** labs are AI-Assisted — you may use AI for explanations or debugging. Fill in the last cell with the course template: *"I acknowledge the use of [tool and version] to [specific use]. Prompts I used included [paste or summarize]. I checked the output by [how I verified it]. I am responsible for this work."* — or *"I did not use AI tools for this assignment."*
- **Due:** Sunday 11:59 pm (Arizona time) of this week, on Brightspace. Late work: see the syllabus late-work table (two grace days per semester, then −10% per day, up to 3 days).

## Troubleshooting

- **A Playground link opens the default network** instead of the settings described: reload the page (the settings are stored after the `#` in the link). You can also set them by hand: Activation box, Learning rate box, and the `+`/`−` buttons next to HIDDEN LAYERS.
- **Playground results differ from a classmate's.** The starting weights are random, so numbers vary a little. If a network seems stuck, press the reset button (↺) and run again.
- **`NameError: name 'relu' is not defined`** (or another name): you skipped a cell. Run the cells above it, or use **Runtime → Run before**.
- **A self-check fails:** read its message; it says what value it expected and the most common mistake. Check for any `None` you didn't replace.
- **How do I add a code cell?** Click **+ Code** at the top of the notebook (or hover between two cells). The notebook already gives you an empty cell for the `count_params` check.
- **`hidden_layer_sizes` error:** a single layer needs a comma: `(10,)`, not `(10)`.
- **Training seems slow:** each network takes a few seconds; the loop in §3.5 trains six. Wait for the `[*]` next to the cell to turn into a number.
- **Something is badly broken:** **Runtime → Restart session**, then run all cells from the top.
