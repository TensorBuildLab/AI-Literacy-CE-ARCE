# Week 8 — Generative AI, Part 2: Prompting, Retrieval, and Images

**Slides:** [PDF](Week08_Generative-AI-2.pdf) · [PowerPoint](Week08_Generative-AI-2.pptx) · **Quiz:** Week 7 quiz at the start of the lecture day · **Lab:** [Lab 08 — Inside an LLM, and RAG](../../labs/lab08-inside-llms-and-rag/) · **Homework:** [HW4 — LLMs Under the Microscope](../../homework/hw4-llms-under-the-microscope/) (posted this week, due Sunday 11:59 pm at the end of Week 10; Week 9 is spring break)

## Learning objectives

By the end of this week, you can:

- Write a prompt as a **specification**: role, context, task, constraints, output format, examples, and a request for assumptions and steps.
- Recognize four **failure modes** — invented citations, unit slips, overconfidence, sycophancy — and how to catch them.
- Explain the **RAG** pipeline (chunk → embed → retrieve → generate with citations) and where it fails.
- Explain how **diffusion** models generate images, and why a concept image is not a design.
- **Evaluate** LLM outputs against known answers and sources, with cost, latency, and energy in mind.

## The big ideas

- **A prompt is a specification.** Like the scope of work you would give an intern: anything you leave out, the model fills with a guess — silently. Give a role, the context it can't know (project, code edition, units), one clear task, constraints, an output format you can check, examples if useful ("few-shot"), and ask it to list assumptions and show steps with units.
- **Good prompts make errors visible, not impossible.** Written steps are not proof; a model can show tidy steps and still be wrong.
- **Four failure modes to expect:** hallucinated citations (code sections, tables, papers), unit mistakes (psi vs. MPa, kN·m vs. kip·ft), overconfidence (wrong answers sound as sure as right ones), and **sycophancy** (it changes a correct answer when you push back — e.g., agreeing that 1:1 is fine for Type C soil, when 1:1 is the Type B limit).
- **Retrieval-augmented generation (RAG)** turns a closed-book exam into an open-book exam: split documents into chunks, turn each into a vector, retrieve the chunks most similar to the question (cosine similarity), and have the model answer **only from them, with citations**. For the Lab 08 question — *maximum allowable slope for an excavation in Type C soil less than 20 ft deep* — the grounded answer is **1½H:1V (34°)**, from OSHA 29 CFR 1926 Subpart P, Appendix B, Table B-1. RAG suits codes, specs, and project documents such as RFIs (requests for information), submittals, and O&M (operation and maintenance) manuals.
- **RAG fails when retrieval fails:** word-matching misses meaning ("really soft clay" finds soil definitions, not the slope table), chunks lose their headings (a "3/4:1" line that belongs to Type A soil), tables stored as images can't be searched (in the eCFR, Table B-1 is a picture), and old documents stay in the index. Always look at *what was retrieved*.
- **Multimodal models** read photos, drawings, and charts — useful for first passes, unreliable for dimensions, scales, and small text.
- **Diffusion models** generate images by starting from pure noise and removing predicted noise step by step, steered by the text prompt. A concept image has mood and massing, but no structure, code compliance, dimensions, MEP (mechanical, electrical, plumbing) space, or physics — it is a quick rough sketch, not a design.
- **Every token costs** money, time, and energy. Pasting all of Subpart P into each question uses 14,891 + 21 question tokens = 14,912 tokens; RAG with three chunks uses about 1,100. **Evaluate** like you would check a junior engineer: questions with known answers, check every source, check units and magnitude, re-ask, and record results.

## Key terms

| Term | Plain-language meaning |
|---|---|
| Prompt | Everything you send the model: instructions, context, examples, and the question |
| System message | The part of a chat prompt that sets the model's role and standing rules |
| Few-shot prompting | Including a few worked input → output examples in the prompt to show the pattern you want |
| Sycophancy | The model agreeing with the user (even when the user is wrong) instead of sticking to the evidence |
| Retrieval-augmented generation (RAG) | Looking up relevant passages in your documents first, then having the model answer from them |
| Chunk | A short passage cut from a longer document so it can be searched and pasted into a prompt |
| Index | The stored vectors for all chunks, with labels saying where each chunk came from |
| TF-IDF | A simple way to turn text into a vector: word counts, weighted up for words that are rare in the collection |
| Cosine similarity | A score from 0 to 1 (for these vectors) of how closely two vectors point the same way; used to rank chunks |
| Grounding / citation | Tying each claim in an answer to a specific source passage you can check |
| Multimodal model | A model that takes more than one kind of input, e.g., text plus images or PDFs |
| Diffusion model | An image generator that starts from noise and removes it step by step, guided by a text prompt |
| Latency | How long you wait for an answer; grows with answer length and model size |
| RFI (request for information) | A formal question from a contractor to the designer during construction |
| MEP | Mechanical, electrical, and plumbing systems of a building (and the space they need) |
| O&M manual | Operation and maintenance manual for a building system or piece of equipment |

## Read / watch

**Required (≈ 30 min total)** — HW3 is due this week, so the list is short:

- **DAIR.AI Prompt Engineering Guide — [Introduction](https://www.promptingguide.ai/introduction)** and **[Few-shot prompting](https://www.promptingguide.ai/techniques/fewshot)** (≈ 20 min). Free, vendor-neutral.
- **DAIR.AI — [Retrieval Augmented Generation (RAG)](https://www.promptingguide.ai/techniques/rag)** (≈ 10 min). A short overview of the pipeline you build in Lab 08.

**Optional:**

- **3Blue1Brown — [Transformers (Deep Learning Ch. 5)](https://www.youtube.com/watch?v=wjZofJX0v4M)** and **[Attention in transformers (Ch. 6)](https://www.youtube.com/watch?v=eMlx5fFNoYc)** (≈ 27 min each). Last week's ideas, visually; helpful for HW4.
- **Jay Alammar — [The Illustrated Stable Diffusion](https://jalammar.github.io/illustrated-stable-diffusion/)** (≈ 30 min read). How diffusion image models work, with diagrams.
- **NIST AI 600-1 — [Generative AI Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)** (2024; skim the list of risks, ≈ 20 min). How the U.S. standards agency describes GenAI risks such as "confabulation" (hallucination); useful for Weeks 13–14.

## Check yourself

1. Rewrite this prompt as a specification: *"What size duct do I need for this room?"* Name at least four parts you added.
   <details><summary>Answer</summary>Example: Role ("you are helping an ARCE student size a duct"); context (airflow in L/s or cfm (cubic feet per minute), room use, duct material, allowable friction loss or velocity limit, round vs. rectangular); task ("size one supply duct"); constraints (SI units, state assumptions, say if information is missing); format (numbered steps, then one line: "Diameter = … mm"). Any four of role, context, task, constraints, format, example, assumptions/steps.</details>

2. What are the four steps of a RAG pipeline, in order?
   <details><summary>Answer</summary>Chunk the documents → embed each chunk (turn it into a vector) → retrieve the chunks most similar to the question → generate an answer from those chunks, with citations.</details>

3. A RAG system answers "3/4:1" for the Type C soil slope question. Give one likely cause and one fix.
   <details><summary>Answer</summary>Cause: it retrieved a chunk about Type A soil whose heading was lost when the text was chunked (or only one chunk was retrieved). Fixes: keep headings/section labels with each chunk, retrieve more than one chunk, use larger or structure-aware chunks, use meaning-based (embedding) search, and always check the retrieved text. The correct answer is 1½H:1V (34°) from Table B-1.</details>

4. You ask an LLM "Are you sure?" and it changes its answer. What failure mode might this be, and what should you do instead?
   <details><summary>Answer</summary>Sycophancy — changing the answer because of social pressure, not new evidence. Instead of asking the model, check the source yourself (e.g., open the code table) or ask it to quote the exact passage it relied on.</details>

5. Give two reasons an AI-generated rendering of a building is not a design.
   <details><summary>Answer</summary>Any two: no structural system or load path; no code compliance (egress, fire, accessibility); no real dimensions or MEP (mechanical, electrical, plumbing) space; no cost or constructability check; no physics (it is pixels, not a daylight or energy model); unclear ownership/copyright.</details>

## Coming up

- **Lab day:** [Lab 08 — Inside an LLM, and RAG](../../labs/lab08-inside-llms-and-rag/): tokens, next-token probabilities, temperature, embeddings, and a mini-RAG over OSHA Subpart P.
- **Week 9:** spring break — no class. HW4 is due at the end of Week 10. The Week 8 quiz is at the start of the Week 10 lecture day.
- **Week 10:** AI agents — from answering to acting: model + tools + memory + loop. You will reuse your Lab 08 retriever as an agent tool. Final project teams form.
