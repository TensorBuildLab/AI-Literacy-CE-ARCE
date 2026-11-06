# CE/ARCE 2XX · AI Literacy for Civil and Architectural Engineering

**University of Arizona · Department of Civil & Architectural Engineering & Mechanics · 3 units**
Instructor: Dr. Liang Zhang · liangzhang1@arizona.edu · Civil Engineering 220F

Welcome! This is the home of the course. Every slide deck, lab notebook, homework assignment, project guide, and dataset is here. Submissions, quizzes, and grades are on **[Brightspace (D2L)](https://d2l.arizona.edu)**.

> **What this course is:** AI literacy for engineers — how AI works, how to use it well, how to **verify** it, and how to use it responsibly — with hands-on Python labs on real civil and architectural engineering data. **No programming experience needed.**

## Start here
1. Read the **[syllabus](syllabus/README.md)** ([Word version](syllabus/AI-Literacy-CE-ARCE_Syllabus.docx) · [PDF](syllabus/AI-Literacy-CE-ARCE_Syllabus.pdf)).
2. Set up **Google Colab** before the first lab: **[Colab setup guide](resources/colab-setup.md)**.
3. Read the **[AI-use guide](resources/ai-use-guide.md)** — every assignment is labeled AI-Free, AI-Assisted, or AI-Required.
4. Keep the **[Python cheat sheet](resources/python-cheatsheet.md)** and the **[glossary](resources/glossary.md)** open during labs.
5. Bookmark this page. Each week: slides → lab → homework, all linked below.

## How a week works
| Lecture day (75 min) | Lab day (75 min) | Between classes |
|---|---|---|
| Short quiz on last week · lecture with CE/ARCE examples · activities | Guided Colab notebook (bring a laptop) · **exit ticket**: 3 short questions you answer alone, without AI, in the last 10 minutes | Short reading · finish the lab (due Sunday) · homework (about every two weeks) · project (from Week 10) |

## Schedule — what is due, when
Click the **lecture** title for slides, readings, and self-check questions. Click the **lab** name, then the **Open in Colab** button. Everything in the last column is due **Sunday 11:59 pm (Arizona time)** at the end of that week unless it says otherwise. Late work: see the [syllabus late-work table](syllabus/README.md#assignments-scheduledue-dates) (two grace days per semester, then −10% per day, up to 3 days).

| Wk | Lecture day | Lab day | Due / notes |
|---|---|---|---|
| 1 | [What AI Is (and Isn't)](lectures/week01-what-is-ai/) | [Lab 01 — Python On-Ramp](labs/lab01-python-onramp/) | Lab 01 · pre-course survey (Brightspace) |
| 2 | [Zooming In: ML, Deep Learning, and Generative AI](lectures/week02-ml-dl-genai/) | [Lab 02 — Working with Data](labs/lab02-working-with-data/) | Quiz on Wk 1 (lecture day) · Lab 02 · [HW1](homework/hw1-ai-or-not/) posted |
| 3 | [How Machines Learn 1: Linear Regression and Cost](lectures/week03-how-machines-learn-1/) | [Lab 03 — Model and Cost](labs/lab03-model-and-cost/) | Quiz on Wk 2 · Lab 03 · **HW1 due** |
| 4 | [How Machines Learn 2: Gradient Descent](lectures/week04-how-machines-learn-2/) | [Lab 04 — Gradient Descent](labs/lab04-gradient-descent/) | Quiz on Wk 3 · Lab 04 · [HW2](homework/hw2-fit-measure-descend/) posted |
| 5 | [Neural Networks 1: Neurons, Layers, Training](lectures/week05-neural-networks-1/) | [Lab 05 — Your First Neural Network](labs/lab05-first-neural-network/) | Quiz on Wk 4 · Lab 05 · **HW2 due** |
| 6 | [Neural Networks 2: CNNs and Sequence Models](lectures/week06-neural-networks-2/) | [Lab 06 — Crack Detection with a CNN](labs/lab06-cnn-crack-detection/) | Quiz on Wk 5 · Lab 06 · [HW3](homework/hw3-neural-networks/) posted |
| 7 | [Generative AI 1: How LLMs Work](lectures/week07-generative-ai-1/) | **Midterm exam** (Weeks 1–6) — [study guide](exams/) | Quiz on Wk 6 (lecture day) · **midterm (lab day)** |
| 8 | [Generative AI 2: Prompting, RAG, Images](lectures/week08-generative-ai-2/) | [Lab 08 — Inside an LLM, and RAG](labs/lab08-inside-llms-and-rag/) | Quiz on Wk 7 · Lab 08 · **HW3 due** · [HW4](homework/hw4-llms-under-the-microscope/) posted · mid-semester survey |
| 9 | *Spring break* | | |
| 10 | [AI Agents](lectures/week10-ai-agents/) | [Lab 10 — Build an Engineering Agent](labs/lab10-engineering-agent/) | Quiz on Wk 8 · Lab 10 · **HW4 due** · [**Project**](project/) assigned · **team registration due** |
| 11 | [AI Across CE and ARCE](lectures/week11-ai-across-ce-arce/) | [Lab 11 — Arizona Bridges, End to End](labs/lab11-bridges-end-to-end/) | Quiz on Wk 10 · Lab 11 · **project proposal + team charter due** |
| 12 | [AI Tools for Engineers](lectures/week12-ai-tools/) | [Lab 12 — Trust but Verify](labs/lab12-trust-but-verify/) · project check-ins, wave 1 | Quiz on Wk 11 · Lab 12 · [HW5](homework/hw5-responsible-ai-in-practice/) posted · check-in form due before your check-in |
| 13 | [Responsible AI](lectures/week13-responsible-ai/) | [Lab 13 — Stress-Testing Models](labs/lab13-stress-testing-models/) · project check-ins, wave 2 | Quiz on Wk 12 · Lab 13 |
| 14 | [AI Policy, Ethics, and Professional Practice](lectures/week14-ai-policy-ethics/) | [Lab 14 — AI Policy Workshop](labs/lab14-policy-workshop/) | Quiz on Wk 13 · Lab 14 · **HW5 due** |
| 15 | [Synthesis: The Big Picture, Revisited](lectures/week15-synthesis/) | [Lab 15 — Project Dry Runs](labs/lab15-project-dry-runs/) (5-minute practice talks) | Quiz on Wk 14 · **dry-run slides due before lab** · course evaluations |
| 16 | **Final project presentations** (final exam period) | | **Final notebook, report, AI-use statement, reflection, peer evaluation** |

## Grading at a glance
| Labs (12, lowest dropped) | Homework (5, lowest dropped) | Midterm | Final project | Participation & quizzes |
|---|---|---|---|---|
| 25% | 20% | 20% | 25% | 10% |

## What's in this repository
| Folder | Contents |
|---|---|
| [`syllabus/`](syllabus/) | Syllabus (web, Word, PDF) |
| [`lectures/`](lectures/) | One folder per week: slides (PDF + PowerPoint), objectives, key terms, readings, self-check questions |
| [`labs/`](labs/) | One folder per lab: Colab notebook + instructions |
| [`homework/`](homework/) | Homework handouts and starter notebooks |
| [`project/`](project/) | Final project guide, ideas, templates, rubrics, starter notebook |
| [`exams/`](exams/) | Midterm study guide, practice exam, formula sheet |
| [`data/`](data/) | All course datasets with sources and licenses |
| [`resources/`](resources/) | Colab setup, Python cheat sheet, AI-use guide, glossary, all readings |

## Getting help
- **Office hours:** see the syllabus. **Email:** include "CE/ARCE 2XX" in the subject line.
- **Stuck in a lab?** Read the error's last line, check the lab's *Troubleshooting* section, ask a neighbor, then ask us.
- **Not sure if an AI use is allowed?** Ask before you submit.

## Credits and licenses
Datasets are used under their original licenses (CC BY 4.0 or U.S. public domain); see [`data/README.md`](data/README.md). Open-source models used in labs (e.g., OpenAI CLIP, Qwen2.5, ResNet-18, MiniLM) are downloaded from their official sources at run time under their own licenses.
