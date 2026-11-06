# Lab 01 — Python On-Ramp

**Week 1 lab day · about 75 minutes · AI-Assisted** (exit ticket is AI-Free) · **Due:** Sunday 11:59 pm (Arizona time) of Week 1, on Brightspace

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/TensorBuildLab/AI-Literacy-CE-ARCE/blob/main/labs/lab01-python-onramp/Lab01_Python_OnRamp.ipynb)
Notebook: [`Lab01_Python_OnRamp.ipynb`](Lab01_Python_OnRamp.ipynb)

## What you will do
1. **Tour Google Colab** — run cells, read text cells, save your own copy.
2. **Python basics with engineering numbers** — variables, lists, loops, `if`, dictionaries, functions, and a first plot, using a beam's bending moment and a concrete mix's water–cement ratio.
3. **Activity 1: a vision model** — run CLIP, a model trained on internet images and captions, on photos of concrete. Can it tell cracked from intact concrete without any training on our photos? Does the wording of its labels matter?
4. **Activity 2: a language model** — run a small large language model (Qwen2.5-0.5B-Instruct) from Python, ask it engineering questions, and check its answers against your own calculations.

No coding experience is needed.

## Before the lab
- [ ] Bring a charged laptop (a tablet is not enough).
- [ ] Sign in to a Google account at <https://colab.research.google.com>.
- [ ] Optional: skim Chapter 1 of [Elements of AI](https://www.elementsofai.com/).

## Data
`concrete_cracks_sample.zip` — 1,200 photos of concrete surfaces (600 with cracks, 600 without), CC BY 4.0. Details in [`data/README.md`](../../data/README.md). The notebook downloads it for you.

## How it is graded
Completion (all `# TODO` cells done and the notebook runs) + the **exit ticket** — three short questions you answer alone, without AI, in the last 10 minutes of lab. Submit the `.ipynb` file on Brightspace by **Sunday 11:59 pm** of Week 1. Late work: see the syllabus late-work table (two grace days per semester, then −10% per day, up to 3 days).

## Troubleshooting
- **"NameError: name ... is not defined"** — run the cells above it first (or **Runtime → Run before**).
- **The model download is slow** — the first download of each model takes 1–3 minutes. It is cached for the rest of your session. Downloads happen on Google's computers, not on your laptop or phone data plan.
- **Colab disconnected / "Runtime restarted"** — re-run the setup cell and the cells you need, top to bottom.
- **"Your session crashed after using all available RAM"** — run **Runtime → Restart session**, then run the cells again; make sure the cell that deletes the vision model (`del vision`) ran before loading the language model.
- **Colab says the notebook is not from Google** — that's normal for course notebooks; choose **Run anyway**.
