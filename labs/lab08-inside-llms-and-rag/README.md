# Lab 08 — Inside an LLM, and RAG

**Week 8 lab day · about 75 minutes · AI-Assisted**
**Due:** Sunday 11:59 pm (Arizona time) of this week, on Brightspace.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/TensorBuildLab/AI-Literacy-CE-ARCE/blob/main/labs/lab08-inside-llms-and-rag/Lab08_Inside_LLMs_and_RAG.ipynb)

Notebook: [`Lab08_Inside_LLMs_and_RAG.ipynb`](Lab08_Inside_LLMs_and_RAG.ipynb) · Lecture: [Week 8 — Generative AI, Part 2](../../lectures/week08-generative-ai-2/) · Homework posted this week: [HW4 — LLMs Under the Microscope](../../homework/hw4-llms-under-the-microscope/)

## What you'll do

You open up a small language model (Qwen2.5-0.5B-Instruct, the same one as in Lab 01) and look at how it works inside. Then you build a small question-answering system that looks things up in OSHA excavation rules before it answers.

| Part | Time | What you do |
|---|---|---|
| 1. Tokens | 8 min | Split engineering text into tokens and count them, including the whole OSHA excavation standard. |
| 2. Next-token probabilities | 10 min | See the model's top-5 guesses for the next token after "…w L squared divided by", and check whether the top guess is right. |
| 3. Temperature | 10 min | Sample text at T = 0.2, 1.0, and 1.5 with fixed random seeds, then try a top-p cutoff. |
| 4. Embeddings | 12 min | Turn sentences into 384-number vectors (all-MiniLM-L6-v2) and compare meanings with cosine similarity. |
| 5. Mini-RAG | 25 min | Chunk OSHA Subpart P, search it with TF-IDF (and optionally with embeddings), build a prompt with numbered sources, and ask: *"What is the maximum allowable slope for an excavation in Type C soil less than 20 ft deep?"*, with and without retrieval. Check the answers against Table B-1 (1½H:1V, 34°). |
| Exit ticket | 10 min | 3 short questions you answer alone, without AI (AI-Free), during the last 10 minutes of lab. If you must leave early, answer them on your own before you submit. |

## Before the lab

- [ ] Review the Week 7 and Week 8 slides on tokens, next-token prediction, temperature, embeddings, and RAG.
- [ ] Sign in to Google Colab with any Google account. Use the same account all semester, so all your Drive copies end up in one place.
- [ ] **In the first 5 minutes of lab:** open the notebook from the badge above, choose **File → Save a copy in Drive**, and run the setup cell and the Part 2 model-loading cell. The model download (about 1 GB) then runs while you work on Part 1. (Starting it earlier in the day doesn't help, because idle Colab sessions disconnect.)

Model downloads happen on Google's computers, not on your laptop or your phone's data plan.

## Data used

- `data/osha/osha_1926_subpartP_excavations.txt`: OSHA 29 CFR 1926 Subpart P (Excavations), including Appendix A (soil classification) and Appendix B (sloping and benching). U.S. Government work. Table B-1 is an image in the eCFR, so the course file has a typed copy of it. **This file is for learning only. Use the current official text at [ecfr.gov](https://www.ecfr.gov) for real work.**
- Models (downloaded from Hugging Face, no account or API key needed): `Qwen/Qwen2.5-0.5B-Instruct` (about 1 GB) and `sentence-transformers/all-MiniLM-L6-v2` (about 90 MB).

## How it's graded

- **Completion (most of the lab grade):** every `# TODO` cell runs, every ✍️ question has a short answer, and the AI-use acknowledgment at the end is filled in. A wrong guess you explain honestly still counts. Lab grading rewards real effort, not correct model output.
- **Exit ticket:** 3 short questions at the end, AI-Free (see the table above).
- **AI-use label: AI-Assisted.** Running the course's small model is part of the lab code. You may also ask an AI tool for explanations or debugging help. If you do, say so in the acknowledgment, using the course template: *"I acknowledge the use of [tool and version] to [specific use]. Prompts I used included [...]. I checked the output by [...]. I am responsible for this work."*
- **Due:** Sunday 11:59 pm (Arizona time) of this week, on Brightspace. Late work: see the syllabus late-work table (two grace days per semester, then −10% per day, up to 3 days).

## Troubleshooting

| Problem | Fix |
|---|---|
| Model download is slow or stalls | Wait 1–2 minutes. If nothing changes, choose **Runtime → Restart session**, then run the cells again from the top. |
| `NameError: name 'tok' is not defined` (or `model`, `chunks`, …) | You skipped a cell or restarted. Run the cells from the top in order (**Runtime → Run before**). |
| Colab says it ran out of RAM | **Runtime → Restart session** and run again. The lab keeps one language model and the small embedding model loaded, and frees the embedding model after Part 5's optional cell. |
| "concrete" is 2 tokens but the text says common words are 1 | That's expected. See the note under the first cell: the space before a word is part of its token. |
| The T = 0.2 samples look like quiz questions ("____. A. … B. …") | Also expected. The raw prompt makes the small model continue it like exam text it saw in training. |
| My answers differ slightly from a classmate's | Greedy answers are repeatable on one machine, but different library versions or hardware (CPU vs. GPU) can change a word here and there. Sampled text (Part 3) depends on the seed. |
| The answer cells take 30–60 s each | That's normal on a free CPU runtime. A GPU runtime (**Runtime → Change runtime type → T4 GPU**) is faster but not required. |
| The self-check says Table B-1 was not found | Look at the two word lists printed above it. Write your search query with the document's own words ("slopes", "excavations", "feet"). |
| Before submitting: "Restart session and run all" | Allow about 10 minutes on a CPU runtime (the models load again). |

## Why this matters

RAG is how most "chat with your documents" tools work, including assistants for specifications, codes, and project files. The lab shows the weak link: **if retrieval brings back the wrong passage, the model may give a wrong answer with a citation that looks trustworthy.** Always look at the retrieved text and check numbers against the source.
