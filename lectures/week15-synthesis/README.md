# Week 15 — Synthesis: The Big Picture, Revisited

**Slides:** [PDF](Week15_Synthesis.pdf) · [PowerPoint](Week15_Synthesis.pptx) · **Lab:** [Lab 15 — Project Dry Runs](../../labs/lab15-project-dry-runs/) · **Homework:** none — focus on your [final project](../../project/)

## Learning objectives

By the end of this week, you can:

1. Trace how the course's ideas connect, from data to responsibility.
2. State ten core ideas about AI, each with an engineering example.
3. Describe how to use AI with judgment in internships and early career.
4. Evaluate claims about emerging AI trends with healthy skepticism.
5. Plan a final presentation that covers every rubric element.

## The big ideas

- **One chain links the course:** data → model → cost → optimization → architectures → generation → agents → applications → responsibility. Your final project touches every link.
- **One recipe trains almost everything.** Pick a model, define a cost that measures how wrong it is, and reduce the cost with gradient descent (or a faster gradient-based method — software often uses one). It works for a straight line (Week 3), a neural network (Week 5), a CNN (Week 6), and an LLM (Week 7). Agents (Week 10) are different: they wrap a trained LLM in a loop with tools.
- **Always compare to a baseline, on unseen data.** On our concrete dataset (206 held-out mixes), always guessing the average strength is off by about 13 MPa; linear regression on all eight inputs, about 7.7 MPa; a small neural network, about 4 MPa. Without the baseline and the test set you cannot tell whether learning worked.
- **Ten ideas to remember:** (1) name the method; (2) data is a design material; (3) model + cost + optimizer; (4) test on unseen data against a baseline; (5) architecture = built-in assumptions; (6) LLMs predict plausible text, not verified facts; (7) good prompts and retrieval reduce but don't remove errors; (8) agents act, so limit them; (9) trust, but verify; (10) people stay responsible.
- **Use AI with judgment at work.** Before relying on an AI tool, ask four questions: Is this data allowed in this tool? Can I verify the answer on my own? What happens if it is wrong? Who needs to know AI was used? Then use it, verify it, and own it.
- **Licensure still tests you.** The FE and PE exams test your own knowledge, and as a PE you answer for every tool you used. Engineers who can use AI *and* check it by hand will be trusted with more.
- **Meet trends with evidence.** Multimodal agents, AI in BIM, foundation models for science (for example, ECMWF has run a machine-learning weather forecast model operationally since 2025), and construction robots are real but uneven. Ask: tested on what data, against what baseline, and who is accountable when it fails?
- **Final presentations:** a 10-minute team talk plus 3–5 minutes of questions in finals week. Follow the presentation guide's outline (problem, data and limits, method and baseline, results and failures, **verification**, responsible AI, takeaway). A 2-hour final slot fits at most 8 teams. With more teams, the class uses two parallel rooms (instructor and TA) or 8-minute talks; the schedule is on Brightspace. Due at the same time: the final notebook, a report of at most 6 pages, an AI-use statement, and an individual reflection and peer evaluation.

## Key terms

| Term | Plain-language meaning |
|---|---|
| Baseline | The simplest reasonable prediction (for example, always guess the average); a model must beat it to be useful |
| Held-out (test) data | Data the model never saw during training, used to estimate how it will do on new cases |
| Foundation model | A large model trained on broad data that can be adapted to many tasks (for example, an LLM or a weather model) |
| Multimodal model | A model that works with more than one kind of input, such as text and images together |
| BIM | Building Information Modeling: a digital 3-D model of a building with data about its parts |
| FE exam / EIT | Fundamentals of Engineering exam; passing it (plus education) leads to the Engineer in Training designation |
| PE license | Professional Engineer license; lets you seal engineering work and makes you responsible for it |
| Hype | Claims about a technology that go beyond the evidence |
| AI-use statement | A short, specific note saying which AI tools you used, for what, and how you checked their output |
| Dry run | A practice talk. In Lab 15 each team gives a 5-minute version of its final talk and gets feedback |
| RFI | Request for information: a contractor's written question to the design team during construction |

## Read / watch

**Required (≈ 40 min total)**

- **Final presentation guide** and the **presentation rubric** in the [project folder](../../project/) — about 15 minutes. Bring questions to the lab day.
- **Elements of AI** (University of Helsinki and MinnaLearn), <https://www.elementsofai.com/> — read the text of Chapter 6, "Implications" (about 25 minutes; the exercises are optional). It is a good wrap-up for this course.

**Optional (after the course)**

- **Google Machine Learning Crash Course**, <https://developers.google.com/machine-learning/crash-course> — free; the regression, classification, and fairness modules review Weeks 3–4 and 13 (about 1–2 hours).
- **Hugging Face Learn**, <https://huggingface.co/learn> — free courses on LLMs and agents if you want to go deeper into Weeks 7–10 (self-paced, several hours).
- **3Blue1Brown — Neural networks** (YouTube series), <https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi> — visual explanations of gradient descent, backpropagation, and transformers (each video 10–30 minutes).
- [Kaggle Learn](https://www.kaggle.com/learn) (short hands-on Python, pandas, and ML lessons) and [fast.ai Practical Deep Learning](https://course.fast.ai/) (for those who want to build models seriously).

## Check yourself

1. Put these in the order of the course chain: agents, cost, data, generation, model, optimization.
   <details><summary>Answer</summary>Data → model → cost → optimization → (architectures) → generation → agents. Then applications and responsibility wrap around all of them.</details>

2. A crack classifier scores 97% accuracy, but only 3% of the test images show cracks. Why is 97% not impressive, and what should you check?
   <details><summary>Answer</summary>A "model" that always says "no crack" also scores 97%. Compare against that baseline and check recall (the share of real cracks found) on the cracked class — missing cracks is the costly error.</details>

3. Which model in this course did NOT learn by gradient descent on a cost function, and how did it work instead?
   <details><summary>Answer</summary>The Week 10 agent did no new training: it wrapped an already-trained LLM in a loop with tools. (Random forests from Lab 11 also learn differently — by splitting the data — not by gradient descent.)</details>

4. Give the four questions to ask before relying on an AI tool at work.
   <details><summary>Answer</summary>(1) Is this data allowed in this tool? (2) Can I verify the answer on my own? (3) What happens if it is wrong? (4) Who needs to know AI was used? If all four are handled: use it, verify it, own it.</details>

5. A vendor says its AI "fully automates structural design with 100% accuracy." Name two questions you would ask.
   <details><summary>Answer</summary>Any two of: Tested on what data, and is it like our projects? Compared to what baseline? What are its known failure modes? What can it change without human approval? Who checks the output, and who is accountable when it is wrong? "100% accurate" and "fully automates" are signs of hype.</details>

## Coming up

- **Lab day — Lab 15:** each team gives a 5-minute practice talk (dry run) and gets structured feedback from classmates and the instructor. The dry run is 5% of the project grade; it is not one of the graded labs. If you must miss it for an excused reason, reschedule with the instructor within one week.
- **Course evaluations:** please complete the university course survey before its deadline. Specific comments help most.
- **Week 16 (finals week):** final project presentations — 10 minutes plus 3–5 minutes of questions (8-minute talks if the section uses that option; check the schedule on Brightspace). Due at the same time: the final notebook, the report (≤ 6 pages) with the AI-use statement, and your individual reflection and peer evaluation. See the [project guide](../../project/) for the official rubric.
