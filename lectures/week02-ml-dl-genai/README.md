# Week 2 — Zooming In: Machine Learning, Deep Learning, and Generative AI

**Slides:** [PDF](Week02_Zooming-In-ML-DL-GenAI.pdf) · [PowerPoint](Week02_Zooming-In-ML-DL-GenAI.pptx) · **Lab:** [Lab 02 — Working with Data](../../labs/lab02-working-with-data/) · **Homework:** [HW1 — AI or Not? Exploring Engineering Data](../../homework/hw1-ai-or-not/) (posted this week, due end of Week 3)

## Learning objectives
By the end of this week you can:
1. Contrast traditional programming (rules + data → answers) with machine learning (data + answers → rules).
2. Identify the **features X** and the **target y** in an engineering dataset.
3. Tell supervised learning (regression, classification), unsupervised learning, and reinforcement learning apart, with a CE or ARCE example of each.
4. Explain what makes deep learning and generative AI different, and why they took off in the 2010s.
5. Judge whether a dataset is good enough for a model: quality, quantity, labels, and representativeness.

## The big ideas
- **Machine learning flips programming.** Traditionally, an engineer writes the rules (M = qL²/8, with q the distributed load in kN/m) and the computer applies them. In machine learning, we give the computer examples *with* the answers — say, 1,030 concrete mixes and their measured strengths — and it produces the rules: a **model**, ŷ = f(x).
- Write the rules when the physics or code provision is known; learn from data when the relationship is too complex to write down and you have many examples. Real tools often combine both.
- A dataset is a table: **one row = one example**, the columns we know are **features (X)**, and the column we want to predict is the **target (y)**.
- **Supervised learning** learns from examples with answers: **regression** predicts a number (strength in MPa), **classification** predicts a category (crack / no crack). **Unsupervised learning** finds structure without answers: **clustering** (groups of similar buildings) and **anomaly detection** (unusual bridge-sensor readings). **Reinforcement learning** learns a strategy from trial, error, and rewards (HVAC control, traffic-signal timing) — mostly in simulators and pilots so far.
- **Deep learning** uses neural networks with many layers that **learn their own features** from raw data such as pixels, instead of features designed by an engineer. It took off when big labeled datasets (ImageNet), GPUs, and better algorithms (including the 2017 transformer) came together.
- **Generative AI** creates new content — text, images, code, design options. It is a kind of *task*, not a fourth way of learning: large language models learn by **self-supervised learning**, where the next word in the text is the label. Its output is *plausible*, not verified. **Foundation models** are trained once on broad data and adapted to many tasks, so their strengths and blind spots show up everywhere they are used.
- **Data is a design material.** A model only knows the range of data it has seen: in our concrete data, 425 of 1,030 tests are at 28 days but only 14 at 365 days, and all are laboratory mixes. Check quality, quantity, labels, and representativeness before you trust a model.

## Key terms
| Term | Plain-language meaning |
|---|---|
| Model | A function that turns inputs into a prediction, ŷ = f(x); in ML its numbers (parameters) are learned from data |
| Feature (X) | An input column the model uses, e.g., cement content or age |
| Target / label (y) | The output we want to predict, e.g., compressive strength |
| Example | One row of data — here, one concrete mix tested at one age |
| Supervised learning | Learning from examples that include the right answers |
| Regression | Supervised learning that predicts a number (MPa, kWh/m²) |
| Classification | Supervised learning that predicts a category (crack / no crack) |
| Unsupervised learning | Finding structure (groups, unusual cases) in data without answers |
| Clustering | Grouping similar examples without being told the groups |
| Anomaly detection | Flagging examples that do not look like normal behavior |
| Reinforcement learning | Learning a strategy by acting and receiving rewards or penalties |
| Deep learning | Machine learning with many-layered neural networks that learn their own features |
| Generative AI | Models that create new content: text, images, code, designs |
| Self-supervised learning | Learning where the labels come from the data itself — e.g., the next word in a sentence; how large language models are pretrained (Week 7) |
| Foundation model | A large model pretrained on broad data and adapted to many tasks |
| Representativeness | How well the training data matches the situations where the model will be used |

## Read / watch
**Required (≈ 40 min total)**
- **Elements of AI, Chapter 4, Section I: "The types of machine learning"** — <https://course.elementsofai.com/4/1> (free; about 20 minutes). Supervised, unsupervised, and reinforcement learning, matching this week's lecture.
- **Google for Developers: "Introduction to Machine Learning"** — <https://developers.google.com/machine-learning/intro-to-ml> (about 20 minutes, Google's estimate). What ML is, the types of ML, and a short note on generative AI.

**Optional**
- **3Blue1Brown: "But what is a neural network?"** — <https://www.youtube.com/watch?v=aircAruvnKk> (video, about 19 minutes). The best visual preview of what "deep" means. We build on it in Week 5.
- **Google ML Crash Course: "Introduction to Large Language Models"** — <https://developers.google.com/machine-learning/crash-course/llm> (about 45 minutes). A preview of Week 7.

## Check yourself
1. In one sentence each, describe traditional programming and machine learning in terms of rules, data, and answers.
   <details><summary>Answer</summary>Traditional programming: an engineer writes the rules, and the computer applies them to data to produce answers. Machine learning: we give the computer data together with the correct answers, and it learns the rules (a model) that we then apply to new data.</details>
2. In the concrete dataset, name two features and the target. Why is age a feature and not the target?
   <details><summary>Answer</summary>Features: any two of cement, slag, fly ash, water, superplasticizer, coarse aggregate, fine aggregate, age. Target: compressive strength (MPa). Age is something we know or choose before the test (when we break the cylinder); strength is the unknown result we want to predict.</details>
3. Classify each task: (a) predict a footing's settlement in mm from soil tests; (b) label drone photos of roofs "hail damage" or "no damage"; (c) find groups of similar trips in unlabeled bike-share data; (d) a crane controller improves load placement by trial and error in a simulator.
   <details><summary>Answer</summary>(a) Supervised regression — the output is a number. (b) Supervised classification — the output is a category. (c) Unsupervised clustering — no labels, find groups. (d) Reinforcement learning — learns from trial, error, and reward.</details>
4. What does "deep learning learns its own features" mean, using crack detection as the example?
   <details><summary>Answer</summary>In classic machine learning an engineer designs features from the photo (for example, the fraction of dark pixels or the length of straight edges) and a simple model uses them. A deep network takes the raw pixels and its layers learn useful features themselves — edges in early layers, textures in middle layers, crack-like shapes in later layers. The trade-off is that it needs much more data and computing.</details>
5. A crack detector works well on photos of clean, dry campus walls. Why might it fail on wet, shadowed bridge piers, and what would you do before using it?
   <details><summary>Answer</summary>The new photos are not represented in the training data (different lighting, moisture, surface texture, staining), so the patterns the model learned may not apply and accuracy can drop. Before using it, collect and label a set of bridge-pier photos and test the model on them; retrain or fine-tune with such photos if needed, and keep an inspector in the loop.</details>

## Coming up
- **Lab 02 (this week's lab day):** load and explore the concrete dataset with pandas and matplotlib — the same data we model in Weeks 3 and 4. It ends with an **exit ticket**: 3 short questions you answer alone, without AI (AI-Free), during the last 10 minutes of lab. Bring a charged laptop.
- **Homework 1** is posted: Parts A–B and D are AI-Free, Part C is AI-Assisted. **Due end of Week 3, Sunday 11:59 pm** on Brightspace.
- **Next week:** How Machines Learn, Part 1 — the simplest model (a straight line), its notation, and the cost function. Short quiz on this week at the start of the Week 3 lecture day.
