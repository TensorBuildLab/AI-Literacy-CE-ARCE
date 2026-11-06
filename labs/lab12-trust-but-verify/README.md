# Lab 12 — Trust but Verify

**Week 12 lab · about 75 minutes · AI-Assisted** · **Due:** Sunday 11:59 pm (Arizona time) of this week, on Brightspace. · Lecture: [Week 12 — AI Tools for Engineers](../../lectures/week12-ai-tools/)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/TensorBuildLab/AI-Literacy-CE-ARCE/blob/main/labs/lab12-trust-but-verify/Lab12_Trust_but_Verify.ipynb)

AI assistants give fast, confident, nicely formatted answers — and some of them are wrong. When you sign a calculation, you are responsible for it, not the tool. Today you score a small language model on nine engineering problems where you can compute the right answer, and you practice the **5-check verification workflow** from lecture:

| # | Check | Ask yourself |
|---|---|---|
| 1 | **Restate** | What is given, what is asked, in which units? Did the AI answer *that* question? |
| 2 | **Units & magnitude** | Do the units work out? Is the size of the number reasonable? |
| 3 | **Independent check** | Recompute another way: hand calculation, Python, a worked example. |
| 4 | **Sources** | Compare with the code, standard, or textbook. Does every citation exist and say that? |
| 5 | **Test & document** | Test code with known answers; record what you checked and how you used AI. |

## What you'll do
1. **Your answers first.** Write a short Python check for nine CE/ARCE problems *before* you see the AI's answers (so its numbers can't anchor you): beam moment (M = qL²/8, q = distributed load in kN/m), psi → MPa, Manning's equation (SI), wall heat gain (Q = U·A·ΔT), water–cement ratio from bags and gallons, OSHA Type C excavation slope, trip generation, the rational method (Q ≈ C·i·A, with Q in **cfs** = cubic feet per second, i in in/hr, A in acres), and a factored moment from 1.2D + 1.6L.
2. **Ask the AI.** Run `Qwen2.5-0.5B-Instruct` on the same nine problems, score it, and tabulate right/wrong by problem type. (Optional: score Colab's built-in Gemini on the same problems.)
3. Ask the model for a code citation and check it against the OSHA Subpart P text.
4. Catch a subtle bug in "AI-written" Manning's-equation code with `assert` tests (and see why a test with R = 1 m can never catch it), then fix it.
5. Write a verification log and an AI-use acknowledgment.

## Time and speed — read this
- **The model run in Part 2 takes about 10–20 minutes on Colab's free CPU** (about 2–4 minutes on a T4 GPU: **Runtime → Change runtime type → T4 GPU**). Colab can't run other cells while it works, so do Part 1 first and read Parts 3–4 while you wait.
- The answers are saved in a variable (`ai_answers`). Re-running the cell only asks the questions that are still missing, so you won't wait twice — unless you restart the session.
- Model downloads (about 1 GB) happen on Google's computers, not on your laptop or phone data plan.

## Before the lab
- [ ] Review the Week 12 lecture's verification workflow.
- [ ] Refresh: Manning's equation, the rational method, U·A·ΔT, and the 1.2D + 1.6L load combination (one line each is enough).
- [ ] Bring a charged laptop; sign in to Google so you can save a copy in Drive.

## Data used
- `osha/osha_1926_subpartP_excavations.txt` — 29 CFR 1926 Subpart P (Excavations), U.S. Government work, from the course [data folder](../../data/). For learning only; use the official eCFR text for real work.
- The language model `Qwen/Qwen2.5-0.5B-Instruct` from Hugging Face (downloaded automatically; no account or API key needed).

## How it's graded
Completion (all cells run, TODOs done, written answers present) + the **exit ticket**: 3 short questions you answer alone, without AI (AI-Free), during the last 10 minutes of lab. The rest of the lab is **AI-Assisted** — running the course's small model is part of the lab code, not outside help; if you also use another AI tool, say so in the AI-use acknowledgment in the last cell. Submit the downloaded `.ipynb` on Brightspace by **Sunday 11:59 pm (Arizona time) of this week**. Late work: see the syllabus late-work table (two grace days per semester, then −10% per day, up to 3 days).

## Troubleshooting
- **The answers take a long time:** see "Time and speed" above. If Colab disconnects, reconnect and run from the top; Part 1 takes seconds.
- **Model download is slow or fails:** run the cell again; downloads resume. If Colab runs out of memory, use **Runtime → Restart session** and run from the top.
- **Your model answers differ from a classmate's:** the model runs with `do_sample=False`, so the same prompt usually gives the same answer, but different software versions or hardware can change a word or a number. Score what *your* model said.
- **`extract_answer` read the wrong number:** expected — this small model usually ignores the `ANSWER:` instruction, so the code falls back to the last number in the text. Note it in your answer and score that problem by reading the text yourself (Check 5 applies to your checking code too).
- **`NameError: truth is not defined`:** run the worked-example cell in Part 1 before the TODO cells.
