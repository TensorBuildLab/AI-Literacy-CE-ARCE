# Lab 10 — Build a Simple Engineering Agent

**Week 10 lab day (first lab after spring break) · about 75 minutes · AI-Assisted**
**Due:** Sunday 11:59 pm (Arizona time) of this week, on Brightspace.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/TensorBuildLab/AI-Literacy-CE-ARCE/blob/main/labs/lab10-engineering-agent/Lab10_Engineering_Agent.ipynb)

Notebook: [`Lab10_Engineering_Agent.ipynb`](Lab10_Engineering_Agent.ipynb) · Lecture: [Week 10 — AI Agents](../../lectures/week10-ai-agents/) · Builds on: [Lab 08 — Inside an LLM, and RAG](../lab08-inside-llms-and-rag/)

## What you'll do

A chatbot answers. An **agent** acts: it picks a tool, runs it, reads the result, and decides what to do next. You build one from scratch in plain Python and test it like an engineer.

| Part | Time | What you do |
|---|---|---|
| 1. Tools | 15 min | Five engineering tools as Python functions with docstrings and units: a unit converter; a simply supported beam tool (M = wL²/8, δ = 5wL⁴/384EI, with w = uniform load in kN/m; you write the formulas); an OSHA excavation lookup (the Lab 08 retriever); a concrete-strength predictor (a **random forest**, many decision trees that vote, trained on `concrete_strength.csv`); and a **door-schedule query** over a small synthetic Revit-style schedule (an ARCE/BIM task). |
| 2. The agent loop | 10 min | Run the observe → think → act loop with a **rule-based brain** (plain `if` statements) so every step is visible. Then write a task that breaks it. |
| 3. An LLM brain | 12 min | Swap in a small language model that replies with JSON such as `{"tool": ..., "args": {...}}` or `{"final_answer": ...}`. A reply with no JSON at all counts as the final answer. Read its traces, including one successful OSHA lookup. |
| 4. Testing | 15 min | Run 6 test tasks with known answers through both brains and build an honest success table. **This cell takes several minutes on CPU: start it, then answer the Part 2–3 questions while it runs.** |
| 5. Guardrails | 8 min | Watch the step limit stop a stuck agent, and require **human approval** before a (pretend) concrete order is placed. |
| Exit ticket | 10 min | 3 short questions you answer alone, without AI (AI-Free), during the last 10 minutes of lab. If you must leave early, answer them on your own before you submit. |

**Expect the small model to make mistakes.** It may pick the wrong tool, mix up arguments, ignore a tool's result, or make up a number. Finding those mistakes in the trace is the point of the lab. It doesn't mean you did something wrong.

## Before the lab

- [ ] Review the Week 10 slides: agent = model + tools + memory + loop; tool calling; guardrails.
- [ ] Skim your Lab 08 notebook, Part 5 (the TF-IDF retriever). You will reuse it as a tool.
- [ ] Sign in to Google Colab with any Google account. Use the same account all semester.
- [ ] **In the first 5 minutes of lab:** open the notebook from the badge above, choose **File → Save a copy in Drive**, and run the cells down to the model-loading cell in Part 3, so the download (about 1 GB) finishes while you work on Parts 1–2. Model downloads happen on Google's computers, not on your laptop or your phone's data plan.
- [ ] Optional: switch to a GPU (**Runtime → Change runtime type → T4 GPU**). The notebook then uses the larger Qwen2.5-1.5B-Instruct model automatically, which follows the JSON format more reliably. Everything also works on the default CPU.

## Data used

- `data/concrete_strength.csv`: 1,030 lab-tested concrete mixes (Yeh 1998, UCI, CC BY 4.0). Used to train the strength-predictor tool.
- `data/osha/osha_1926_subpartP_excavations.txt`: OSHA 29 CFR 1926 Subpart P (Excavations), U.S. Government work. For learning only; use the current eCFR for real work.
- A **synthetic** 30-door schedule (3 levels × 10 doors with fire ratings), defined inside the notebook. It is made up for this lab. It is not a real building and not a code check.
- Model: `Qwen/Qwen2.5-0.5B-Instruct` on CPU (about 1 GB) or `Qwen/Qwen2.5-1.5B-Instruct` on GPU (about 3 GB), downloaded from Hugging Face with no API key.

## How it's graded

- **Completion (most of the lab grade):** every `# TODO` cell runs, every ✍️ question has a short answer, your success table has your own verdicts, and the AI-use acknowledgment is filled in. An honest table with failures earns full credit. A table edited to look better does not.
- **Exit ticket:** 3 short questions at the end, AI-Free (see the table above).
- **AI-use label: AI-Assisted.** Running the course's small model is part of the lab code. You may also ask an AI tool for explanations or debugging help. If you do, say so in the acknowledgment, using the course template: *"I acknowledge the use of [tool and version] to [specific use]. Prompts I used included [...]. I checked the output by [...]. I am responsible for this work."*
- **Due:** Sunday 11:59 pm (Arizona time) of this week, on Brightspace. Late work: see the syllabus late-work table (two grace days per semester, then −10% per day, up to 3 days).

## Troubleshooting

| Problem | Fix |
|---|---|
| The Part 4 evaluation cell runs for several minutes | Normal on CPU (6 tasks × 2 brains, up to 5 model calls per LLM task). Answer the Part 2–3 questions while it runs, or use a GPU runtime. |
| An input box appears in Part 5 and the cell waits | That is the human-approval step. Type `no` and press Enter (later, try `yes`). This also happens during "Restart session and run all": type `no`. |
| `NameError` for `TOOLS`, `run_agent`, `llm_brain`, … | Run the cells from the top in order (**Runtime → Run before**). |
| The LLM replies with plain text instead of JSON | If the reply has no JSON at all, the loop counts it as the final answer (a common convention). If it has broken JSON, `parse_reply` tries to repair it. If it can't, the loop sends back an error observation, and the step counts toward the limit. Note it in your success table. |
| Out of memory | **Runtime → Restart session**, then run from the top. Only one language model is loaded. |
| My trace differs from a classmate's | CPU vs. GPU (0.5B vs. 1.5B model) and library versions change the model's choices. Both are fine. Report what *your* agent did. |
| Before submitting: "Restart session and run all" | Allow about 15–20 minutes on CPU, and type `no` at the approval box. |

## Final project

The final project is assigned this week. **Team registration is due Sunday of Week 10**, and the **team charter is due with the proposal (Sunday of Week 11)**. If your team picks the **Assist** track, this notebook is a good starting point. Whatever you build, keep the habits from Part 4: a test set with known answers, a simple **baseline** (the simplest reasonable method, used as a yardstick), and an honest success table.
