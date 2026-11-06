# Lab 02 — Working with Data

**Week 2 lab day · about 75 minutes · AI-Assisted** · **Due:** Sunday 11:59 pm (Arizona time) of this week, on Brightspace.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/TensorBuildLab/AI-Literacy-CE-ARCE/blob/main/labs/lab02-working-with-data/Lab02_Working_with_Data.ipynb)

Before anyone trains a model, they look at the data. In this lab you explore 1,030 real laboratory tests of concrete compressive strength with **pandas** (a Python library for tables) and **matplotlib** (a library for plots). You will use both in almost every lab from now on.

## What you'll do

1. **Meet the data** — load a CSV file, check its size, and read summary statistics (`head`, `shape`, `describe`).
2. **Select, filter, sort** — pick columns, keep the 28-day tests, and find the strongest and weakest mixes.
3. **Group and create** — average strength by age with `groupby`, and build a new column: the water–cement ratio.
4. **Plot** — a histogram of strength and scatter plots of strength vs cement, age, and water–cement ratio.
5. **Check the data like an engineer** — name the features (X) and the target (y), and investigate duplicate rows and extreme values.

There are 9 short `# TODO` cells (1–4 lines each), self-check cells that tell you when your answer is right, and a few written questions. Questions marked 🏠 may be finished after lab; they are still part of the lab.

## Before the lab

- [ ] You can open a notebook in Colab and save a copy to your Drive (Lab 01).
- [ ] You remember lists, `for` loops, and f-strings from Lab 01. If not, look at the [Python cheat sheet](../../resources/python-cheatsheet.md).
- [ ] Bring a charged laptop. You do not need to install anything; everything runs in the browser.

## Data

`concrete_strength.csv` — 1,030 concrete mixes, each tested at one age: 7 ingredient amounts (kg/m³), age (days), and compressive strength (MPa). Source: I-C. Yeh (1998), UCI Machine Learning Repository, CC BY 4.0. Details are in [`data/README.md`](../../data/README.md). The notebook downloads the file for you with `get_data(...)`.

## How it's graded

- **Completion** of the notebook: all TODO cells run, written answers filled in, and the AI-use acknowledgment at the end.
- **Exit ticket:** 3 short questions you answer alone, without AI (AI-Free), during the last 10 minutes of lab. If you must leave early, answer them on your own before you submit.
- The lab is **AI-Assisted**: you may ask an AI tool for explanations or debugging help, and you write the AI-use acknowledgment at the end. You are responsible for every line.
- **Due:** Sunday 11:59 pm (Arizona time) of this week, on Brightspace (instructions at the end of the notebook). Late work: see the syllabus late-work table (two grace days per semester, then −10% per day, up to 3 days). The lowest lab score is dropped.

## Troubleshooting

- **`NameError: name 'pd' is not defined`** or **`name 'get_data' is not defined`** — run the setup cell first (at the top of the notebook). After a restart, run the cells again from the top.
- **`TypeError: Cannot perform 'rand_' with a dtyped [float64] array and scalar of type [bool]`** — you combined two conditions with `&` without parentheses. Put each condition in its own ( ): `df[(df["age_days"] == 28) & (df["strength_mpa"] >= 40)]`.
- **`TypeError: object of type 'NoneType' has no len()`** or **`'NoneType' object has no attribute ...`** — a TODO still contains `None`. Replace it, run that cell, then run the self-check.
- **`KeyError: 'strength_mpa '`** — a column name is misspelled (look for extra spaces or missing underscores). Copy the names from `df.columns`.
- **A table does not appear** — only the **last line** of a cell is shown automatically. Put the table (for example `mix_table.head()`) on the last line, or use `print(...)`.
- **A plot does not appear** — make sure the cell ends with `plt.show()`.
- **Something is badly broken** — choose **Runtime → Restart session**, then run all cells from the top.

## Related

- Lecture: [Week 2 — Zooming In: ML, DL, and Generative AI](../../lectures/week02-ml-dl-genai/)
- Next lab: [Lab 03 — Model Representation and Cost](../lab03-model-and-cost/)
- Homework: [HW1 — AI or Not? Exploring Engineering Data](../../homework/hw1-ai-or-not/) uses the same pandas skills on building-energy data.
