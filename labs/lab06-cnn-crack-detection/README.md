# Lab 06 — Crack Detection with a CNN

**Week 6 lab day · about 75 minutes · AI-Assisted** (exit ticket is AI-Free) · **Due:** Sunday 11:59 pm (Arizona time) of this week, on Brightspace.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/TensorBuildLab/AI-Literacy-CE-ARCE/blob/main/labs/lab06-cnn-crack-detection/Lab06_CNN_Crack_Detection.ipynb)

Notebook: [`Lab06_CNN_Crack_Detection.ipynb`](Lab06_CNN_Crack_Detection.ipynb) · Lecture: [Week 6 — Neural Networks, Part 2](../../lectures/week06-neural-networks-2/) · Homework: [HW3 — Neural Networks on Engineering Data](../../homework/hw3-neural-networks/)

## What you'll do

| Part | Time | What happens |
|---|---|---|
| 1. A photo is a grid of numbers | 8 min | Unzip 1,200 concrete photos and look at their pixel values (227 × 227 × 3 numbers from 0 to 255). |
| 2. Convolution by hand | 20 min | Apply a 3 × 3 edge filter by hand, then slide hand-made filters over real photos to make **feature maps**; see what **pooling** does; build a simple "edge score" crack detector. |
| 3. Transfer learning | 20 min | Load **ResNet-18**, a CNN pretrained on about 1.28 million ImageNet photos; remove its last layer to get 512 features per photo; train a small logistic-regression "head"; read the **confusion matrix**, compute **precision** and **recall**, and inspect the hardest photos. §3.3 (the learned filters) and §3.9 (how many labeled photos you need) are optional. |
| 4. Forecasting traffic | 10 min | A **time series** (sequence) example: forecast next-hour traffic on I-94 with a 24-hour **sliding window** and compare it with a "same hour last week" **baseline** (a simple reference forecast any model must beat). |
| Exit ticket | 10 min | 3 short questions you answer alone, without AI (AI-Free), during the last 10 minutes of lab. If you must leave early, answer them on your own before you submit. |

Questions marked 🏠 in the notebook may be finished at home before the deadline.

## Before the lab

- [ ] Review the Week 6 slides: convolution, feature maps, pooling, CNN layers, transfer learning, the confusion matrix (precision and recall), sliding windows.
- [ ] Keep the [Python cheat sheet](../../resources/python-cheatsheet.md) open in a tab.
- [ ] Open the notebook with **Open in Colab**, then **File → Save a copy in Drive**.
- [ ] **Recommended:** switch to a GPU: **Runtime → Change runtime type → T4 GPU → Save**. Feature extraction (§3.4) then takes seconds instead of a minute or two. The notebook also works on the default CPU runtime. Free GPU time is limited, so if Colab says no GPU is available, just use the CPU.

## Data

- `concrete_cracks_sample.zip` (about 7 MB) — 600 "crack" and 600 "no crack" photos (227 × 227 pixels, RGB), a random sample from Ç. F. Özgenel, *Concrete Crack Images for Classification*, Mendeley Data, 2019 (CC BY 4.0). Unzips to `concrete_cracks/crack/` and `concrete_cracks/no_crack/`. By default the lab uses 300 photos of each class; on a GPU you can set `N_PER_CLASS = 600` to use all of them.
- `metro_traffic_volume.csv` (about 2 MB) — hourly westbound traffic on I-94, Minneapolis–St. Paul, 2012–2018 (UCI, CC BY 4.0). It has gaps (missing hours), which the notebook handles.
- Pretrained model: torchvision's `resnet18` with `ResNet18_Weights.DEFAULT` (ImageNet). It downloads automatically (about 45 MB). Model downloads happen on Google's computers, not on your laptop or phone data plan.

Details on all datasets: [data README](../../data/README.md).

## How it's graded

- **Completion (most of the grade):** every `# TODO` cell runs (Parts 1–4 are all required), and every required ✍️ question has a thoughtful answer in your own words. Sections marked *Optional* are not graded. The AI-use acknowledgment statement is part of completion.
- **Exit ticket:** 3 short questions you answer alone, without AI (AI-Free), in the last 10 minutes of lab.
- **AI-use acknowledgment:** labs are AI-Assisted. Fill in the last cell with the course template: *"I acknowledge the use of [tool and version] to [specific use]. Prompts I used included [paste or summarize]. I checked the output by [how I verified it]. I am responsible for this work."* — or *"I did not use AI tools for this assignment."*
- **Due:** Sunday 11:59 pm (Arizona time) of this week, on Brightspace. Late work: see the syllabus late-work table (two grace days per semester, then −10% per day, up to 3 days).

## Troubleshooting

- **Feature extraction is slow:** on the free CPU runtime, 600 photos take about 1–3 minutes; wait for the cell's `[*]` to finish. To speed it up, use a T4 GPU (see above), or temporarily lower `N_PER_CLASS` in §2.4 (e.g., to 150) and re-run from there.
- **`FileNotFoundError` for a photo:** run the unzip cell at the top of Part 1 again (Colab deletes files when the session restarts).
- **Meaningless ImageNet labels in §3.2 after running §3.4:** §3.4 removed the model's last layer. Re-run the cell in §3.1 to reload the full model.
- **`CUDA out of memory` on a GPU:** lower `batch_size` in `extract_features` (e.g., to 16), or use the CPU runtime.
- **The traffic network in Part 4 takes a while:** it trains on about 12,000 hours of data; give it 10–30 seconds (up to a minute on a busy CPU).
- **Model download fails or hangs:** check your internet connection, then **Runtime → Restart session** and run again.
- **Something is badly broken:** **Runtime → Restart session and run all**.
