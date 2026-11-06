# Week 7 — Generative AI, Part 1: How Large Language Models Work

**Slides:** [PDF](Week07_Generative-AI-1.pdf) · [PowerPoint](Week07_Generative-AI-1.pptx) · **Quiz:** Week 6 quiz at the start of this week's lecture day · **Lab:** no lab this week — the lab-day slot is the **midterm exam** (Weeks 1–6); study guide, practice exam, and formula sheet are in [`exams/`](../../exams/) · **Homework:** [HW3 — Neural Networks on Engineering Data](../../homework/hw3-neural-networks/) is due at the end of Week 8

## Learning objectives

By the end of this week, you can:

- Explain language modeling as **next-token prediction**, and how repeating it generates text.
- Describe **tokens** and **embeddings**, and why "superplasticizer" becomes four tokens.
- Explain in plain words what **attention** does and what a **transformer block** contains.
- Describe the training stages — **pretraining, instruction tuning, preference tuning (RLHF)** — and the role of scale.
- Explain how **temperature** and the **context window** shape output, and why LLMs **hallucinate**.

## The big ideas

- A large language model (LLM) does one thing: given the text so far, it gives a **probability to every possible next token**. Writing an answer means repeating *predict → pick → append* until it stops. Underneath, it is a classifier with ~150,000 classes.
- Text is first cut into **tokens** by a tokenizer. Common words are one token (" concrete"); rare technical words are built from pieces (" superplasticizer" → `super | pl | astic | izer`); the Qwen tokenizer splits numbers one digit per token. Prices, speed, and context limits are counted in tokens (≈ ¾ of an English word each).
- Each token becomes an **embedding** — a vector of numbers (896 per token in Qwen2.5-0.5B). Tokens used in similar ways end up with nearby vectors.
- **Attention** lets each token look back at earlier tokens, weigh how relevant each one is, and blend in their information (e.g., "it" in "The beam rests on the column because it…" pulls from "beam" and "column"). A **transformer** stacks many blocks of attention + a feed-forward network (24 blocks in Qwen2.5-0.5B).
- Training uses the same recipe as Week 3: a **cost** (cross-entropy: how surprised the model was by the true next token) minimized by **gradient descent** — on trillions of tokens (pretraining), then on example answers (instruction tuning) and human preferences (RLHF). Pretraining is **self-supervised**: the next word in the text is the label, so nobody has to label the data by hand.
- **Scale** matters: parameters, training tokens, and compute grow together. Our lab model has 494 million parameters; GPT-3 (2020) has 175 billion. Many current commercial models no longer publish their size (as of 2026).
- **Softmax** turns scores into probabilities that add up to 1 (the many-class cousin of Week 4's sigmoid). **Temperature** reshapes those probabilities: low T is focused and repeatable, high T takes chances. It changes randomness, **not** truth. The **context window** is everything the model can see at once (32,768 tokens for Qwen2.5-0.5B).
- LLMs **hallucinate** because they generate plausible text and nothing in the process checks facts. In engineering this looks like invented code sections, unit slips (4000 psi is ≈ 27.6 MPa, not 4000 MPa), backwards physics, and arithmetic drift. Use LLMs for drafts and ideas; verify anything that goes into a decision.

## Key terms

| Term | Plain-language meaning |
|---|---|
| Language model | A model that gives a probability to each possible next piece of text |
| Large language model (LLM) | A language model with billions of parameters trained on huge amounts of text |
| Token | A piece of text (word, word part, digit, or symbol) that the model reads and writes |
| Tokenizer | The tool that cuts text into tokens and turns them into ID numbers |
| Next-token prediction | Guessing which token comes next — the single task an LLM is trained on |
| Embedding | A vector (list of numbers) that represents a token; similar meanings → nearby vectors |
| Attention | A step where each token scores the earlier tokens and blends in information from the relevant ones |
| Transformer | The network design behind LLMs: stacked blocks of attention + feed-forward layers |
| Parameter | A number inside the model (a weight) that training adjusts |
| Pretraining | The big first training stage: next-token prediction on trillions of tokens of text |
| Self-supervised learning | Learning where the labels come from the data itself — in pretraining, the next word is the label |
| Instruction tuning | Training on prompts paired with good answers so the model follows instructions |
| Preference tuning (RLHF) | Tuning the model toward answers people rated higher (reinforcement learning from human feedback) |
| Logit | The model's raw score for a token, before it is turned into a probability |
| Softmax | The function that turns a list of scores into probabilities that add up to 1 (the many-class version of the sigmoid) |
| RFI (request for information) | A formal question from a contractor to the designer during construction |
| Temperature (T) | A setting that sharpens (T < 1) or flattens (T > 1) the next-token probabilities |
| Context window | The maximum number of tokens the model can consider at once (prompt + documents + answer) |
| Hallucination | Fluent, confident output that is false or not supported by any source |

## Read / watch

**Required (≈ 8 min total)** — it is midterm week and HW3 is open, so only one short item is required:

- **3Blue1Brown — [Large Language Models explained briefly](https://www.youtube.com/watch?v=LPZh9BOjkQs)** (≈ 8 min). The whole lecture in one short video.

**Optional** (good for HW4, or for the week after the exam):

- **3Blue1Brown — [Transformers, the tech behind LLMs (Deep Learning Ch. 5)](https://www.youtube.com/watch?v=wjZofJX0v4M)** and **[Attention in transformers (Ch. 6)](https://www.youtube.com/watch?v=eMlx5fFNoYc)** (≈ 27 min each). Visual intuition for embeddings, attention, and temperature.
- **Jay Alammar — [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)** (≈ 30 min read). Step-by-step diagrams; skim the matrix parts if they get heavy.
- **[Transformer Explainer](https://poloclub.github.io/transformer-explainer/)** (interactive, 10–15 min). Runs a small GPT-2 in your browser: type a prompt and watch the next-token probabilities change with temperature.

## Check yourself

1. In one sentence, what does an LLM compute at each step of generating text?
   <details><summary>Answer</summary>A probability for every token in its vocabulary as the next token, given the text so far; one token is then picked, appended, and the process repeats.</details>

2. Why might an LLM make mistakes on "4000 psi × 0.006895"?
   <details><summary>Answer</summary>It does not calculate; it predicts likely text. Its tokenizer also splits numbers into digits (4 | 0 | 0 | 0), so it never handles 4000 as one quantity. Multi-digit arithmetic can drift. (The right answer is ≈ 27.6 MPa — check with a calculator or code.)</details>

3. What is the difference between an embedding and a token?
   <details><summary>Answer</summary>A token is a piece of text (with an ID number). An embedding is the vector of numbers the model uses to represent that token; embeddings are learned so that tokens used in similar ways have nearby vectors.</details>

4. You set temperature to 0 (always the top token). Is the answer now guaranteed to be correct? Explain.
   <details><summary>Answer</summary>No. Temperature 0 makes the output repeatable, not true. If the most likely continuation is wrong, the model will give the same wrong answer every time.</details>

5. Name the three training stages of a chat assistant and what each one adds.
   <details><summary>Answer</summary>Pretraining (next-token prediction on huge text → a base model that continues text); instruction tuning (prompt–answer examples → follows instructions and chats); preference tuning / RLHF (human rankings → answers people prefer, which can also make it agreeable or overconfident).</details>

## Coming up

- **Lab day this week: midterm exam** on Weeks 1–6 — 75 min, closed book, AI-Free, formula sheet provided, calculator allowed. Study guide and practice exam in [`exams/`](../../exams/).
- **Week 8:** using generative AI well — prompting as specification, failure modes, retrieval-augmented generation (RAG), image generation, and evaluating outputs. Lab 08 builds a mini-RAG over the OSHA excavation rules. HW4 is posted. The Week 7 quiz (this lecture) is at the start of the Week 8 lecture day.
