# Final Project — Apply AI to a Real CE/ARCE Problem

**CE/ARCE 2XX · AI Literacy for Civil and Architectural Engineering** · Weeks 10–16 · **25% of your course grade (200 project points)**

> **What to hand in, when, and points** (all times are Arizona time, on Brightspace)
> 1. **Team registration** — Sunday of Week 10, 11:59 pm · required, 0 points
> 2. **Proposal canvas + team charter** — Sunday of Week 11, 11:59 pm · 20 points
> 3. **Check-in form + notebook link** — before your check-in lab starts (Week 12 lab = wave A, Week 13 lab = wave B) · 20 points
> 4. **Dry-run slides** — before the Week 15 lab starts; feedback forms in the lab · 10 points
> 5. **Week 16:** slides before your presentation session · presentation 60 points · notebook + report + AI-use statement 70 points · reflection + peer evaluation 20 points (deadline posted on Brightspace)

**Quick links:** [Project ideas](project-ideas.md) · [Rubrics](rubrics.md) · [Starter notebook](Project_Starter_Notebook.ipynb) ([open in Colab](https://colab.research.google.com/github/TensorBuildLab/AI-Literacy-CE-ARCE/blob/main/project/Project_Starter_Notebook.ipynb)) · [NBI decode helper](tools/nbi_decode.py) · Templates: [team charter](templates/team-charter.md) · [proposal canvas](templates/proposal-canvas.md) · [check-in](templates/check-in.md) · [report](templates/report-template.md) · [presentation](templates/presentation-guide.md) · [AI-use statement](templates/ai-use-statement.md) · [peer evaluation](templates/peer-evaluation.md)

---

## 1. Why this project?

All semester you have used AI one lab at a time. The project puts the pieces together. Your team picks a real civil or architectural engineering question, applies an AI method (or tests an AI tool), and then does what engineers always do: **checks the result, explains its limits, and says who is responsible for it.**

You do **not** need to build something impressive. A small, honest, well-checked project is better than a flashy one that nobody can verify. A model that turns out *worse* than a simple baseline can still earn full marks — if you show it clearly and explain why.

**Course learning outcomes (CLOs) you practice.** Every team works on:
- **CLO6** — select and critically evaluate an AI method or tool for an engineering task;
- **CLO7** — verify AI outputs, recognize limits (data shift, bias, uncertainty), and use AI responsibly;
- **CLO8** — work as a team and explain your approach, results, and limits to technical and non-technical audiences.

Your track adds one or two more:

| Track | Also practices |
|---|---|
| Predict | **CLO2** — how a machine learns from data (model, cost, train/test evaluation); **CLO3** if you use a neural network |
| See | **CLO3** — neural networks for images (CNNs, transfer learning) |
| Assist | **CLO4** — generative AI, prompting, and retrieval; **CLO5** if you build an agent |
| Evaluate | **CLO4** when you test a generative-AI tool (most Evaluate projects); otherwise the CLO of the method you test |

The project is also where the course measures ABET student outcomes 3 (communication) and 5 (teamwork). The [rubrics](rubrics.md#how-the-rubrics-map-to-course-and-abet-outcomes) show which rubric rows measure which outcome.

---

## 2. Teams

- **Size:** 3–4 students. Teams of 2 or 5 only with the instructor's written approval (for example, an odd class size).
- **Team registration:** by **Sunday of Week 10, 11:59 pm**. Choose your own team or ask to be placed. Register the team on Brightspace.
- **Team charter:** fill in the [team charter](templates/team-charter.md) together at your first meeting. Submit it **with the proposal (Sunday of Week 11)**. It is graded as part of the proposal's "Plan, roles, and team charter" row. It records roles, meeting times, how you will communicate and make decisions, and what you will do if someone stops contributing.
- **Suggested roles** (in a team of 3, one person takes two roles; everyone still writes code and text):
  - *Coordinator* — keeps the schedule, runs meetings, submits files.
  - *Data lead* — finds, cleans, and documents the data and its limits.
  - *Modeling lead* — builds the baseline and the main method.
  - *Verification & responsible-AI lead* — runs the five verification checks and leads the risk analysis.
- **Everyone must understand the whole project.** In the Week 16 questions, any member may be asked about any part.
- **If teamwork breaks down:** follow your charter first. If that does not fix it, tell the instructor **early** (not in Week 16).
- **If one person does much less work:** if peer evaluations and team records show that one person did much less work than the others, the instructor may lower that person's grade on the team milestones. The exact rule:
  - It happens only if **at least two teammates** rate that member's share of the work **below 60% of an equal share** (below 15% in a team of 4, below 20% in a team of 3), **and** the check-in record ("Contributions so far") agrees.
  - That member's points on the team milestones (proposal, check-in, team part of the dry run, presentation, notebook + report) are multiplied by a factor **between 0.5 and 1.0**, chosen by the instructor from the evidence.
  - The student is told first and can respond before grades are final.

---

## 3. Choose a track

Every project belongs to one of four tracks. Pick the one that fits your question — not the one that sounds hardest. The [project ideas](project-ideas.md) page has 22 concrete starting points and a short list of key terms.

### Predict — machine learning on tabular or time-series data
Train a model to predict an engineering quantity from data: linear or logistic regression, a **random forest** (many decision trees that vote — Lab 11), or a small neural network.
*Example:* predict 28-day concrete strength (MPa) from mix proportions; forecast next-hour traffic volume (vehicles/h).

**A strong Predict project:**
- predicts a clearly defined target **with units**, for a named user and decision;
- compares against a simple **baseline** (predict the average, "same hour last week," or a one-feature formula);
- splits data so the test set is truly unseen (time-based split for time series; no copies of the same mix or bridge in both sets);
- reports errors in engineering units (MAE in MPa, not just R²) and looks at *where* the model is wrong (subgroups, extremes);
- says honestly where the model should **not** be used (outside the training range, other climates or regions).

### See — computer vision
Classify, detect, or measure something in images.
*Example:* crack / no-crack classification with **transfer learning** (reusing a network trained on millions of other photos, as in Lab 06); pavement-damage types from road photos.

**A strong See project:**
- uses transfer learning or another method that fits a laptop or free Colab;
- reports accuracy **and** a confusion matrix, with recall for the class that matters (missing a crack is worse than a false alarm);
- shows and discusses the model's mistakes (real images, not just numbers);
- tests robustness (blur, brightness, shadows, images from a different source) as in Lab 13;
- respects privacy (no identifiable faces or license plates) and image licenses.

### Assist — a generative-AI tool for an engineering workflow
Build a small LLM-based helper: a **retrieval-augmented generation (RAG)** assistant (the model answers from documents your code finds first — Lab 08), a tool-using agent (Lab 10), a summarizer, or a tool that pulls structured facts out of text.
*Example:* an OSHA excavation-rules assistant that answers with citations.

**A strong Assist project:**
- names a real workflow and user ("a site superintendent checking trench sloping");
- builds a **test set** of at least 20 questions or tasks with known correct answers *before* tuning the tool;
- compares against a baseline (the LLM with no retrieval or tools, or a plain keyword search);
- scores correctness, citation accuracy, and whether the tool refuses or flags questions it cannot answer;
- keeps a human in the loop for anything consequential and explains how users should check outputs.

### Evaluate — a systematic test of an existing AI tool
Design a fair experiment that measures how well an AI tool does an engineering task.
*Example:* how often do LLMs get beam-moment, Manning's-equation, and heat-loss calculations right, and does a structured prompt help?

**A strong Evaluate project:**
- builds a test set (at least 30 items) whose correct answers you can prove (Python, hand calculation, or a public code text);
- defines the scoring rule *before* collecting answers (for example, "correct = within 2% and correct units");
- compares conditions (two tools, two prompt styles, with/without retrieval) — one condition is the baseline;
- has two teammates score a sample independently and reports how often they agree;
- records tool names, versions, settings, and dates (tools change fast), classifies the types of errors, and ends with a practical recommendation.

---

## 4. Required elements (every track)

Your proposal, notebook, report, and presentation must all cover these. The rubrics grade each one.

| Element | What it means | Where you practiced it |
|---|---|---|
| **Problem statement and users** | The question, who would use the answer, and what decision it supports. | Lab 11 engineering memo |
| **Data and its limits** | Source, license, size, what one row/image/document is, units, and what the data does *not* represent (region, years, building types, missing values, bias). | Labs 02, 11 |
| **Method** | What you did and why it fits the problem. Enough detail that another team could repeat it. | Labs 04–06, 08, 10 |
| **A baseline** | The simplest reasonable approach that your method must beat or be compared with (the average, a rule of thumb, a formula, the tool with no help). Without a baseline, a number like "MAE = 5 MPa" means nothing. | Labs 06, 11 |
| **Evaluation with appropriate metrics** | Metrics that fit the task and how serious a mistake would be: MAE/RMSE in units, recall for rare failures, correctness rate for an assistant. Reported on unseen test data. | Labs 04, 11, 12 |
| **Verification** | The course's five checks applied to your own results: **Restate, Units & magnitude, Independent check, Sources, Test & document.** | Lab 12 |
| **Responsible-AI analysis** | Risks, bias, failure modes, and **who is accountable** if someone relies on your result. Use the NIST AI RMF ideas (Govern, Map, Measure, Manage) and a short model card. | Labs 13, 14 |
| **AI-use statement** | Which AI tools you used, for what, what you checked, and confirmation that you are responsible for every line. | [Template](templates/ai-use-statement.md) |

**The five verification checks** (from Week 12):

1. **Restate** — say the problem and the result in your own words. Does the result answer the question you asked?
2. **Units & magnitude** — are the units right, and is the size plausible? (A 28-day strength of 400 MPa is not.)
3. **Independent check** — compare with a hand calculation, a different method, or a known case.
4. **Sources** — does every dataset, formula, and citation exist and say what you claim?
5. **Test & document** — write tests (`assert`) for your code, record what you checked, and keep the notebook re-runnable.

---

## 5. Milestones and weights

The project is **25% of your course grade**. Inside the project, the milestones are weighted as follows. Each rubric is scored in points (2 points per 1% of project weight; 200 points total). All deadlines are **Arizona time**.

| Milestone | When | Weight (of project) | Points | Who |
|---|---|---|---|---|
| Team formation (registration) | Sunday of Week 10, 11:59 pm | – | – | Team |
| Proposal (project canvas, 2 pages) + team charter | Sunday of Week 11, 11:59 pm | 10% | 20 | Team |
| Progress check-in (data + baseline running) | Week 12 lab (wave A) or Week 13 lab (wave B) | 10% | 20 | Team |
| Dry run + peer feedback | Week 15 lab | 5% | 10 | Team + individual |
| Final presentation | Week 16 (final-exam period) | 30% | 60 | Team |
| Final notebook + report (≤ 6 pages) | Week 16 | 35% | 70 | Team |
| Individual reflection + peer evaluation | Week 16 | 10% | 20 | Individual |
| **Total** | | **100%** | **200** | |

### Week-by-week

| Week | What happens | What you hand in |
|---|---|---|
| **10** | Project assigned. Read this guide and the ideas list. Form a team. | Team registration (Sunday of Week 10) |
| **11** | Lab 11 (Arizona bridges) is a full worked example of the project workflow — use it as a model. The instructor posts the **check-in wave list** (A or B). | [Proposal canvas](templates/proposal-canvas.md) (2 pages, PDF) + [team charter](templates/team-charter.md) (Sunday of Week 11) |
| **12** | Proposal feedback returned (wave A teams first, by the Week 12 lecture day). Load your data and build the baseline. **Wave A check-ins** in the last 25 minutes of the Week 12 lab. | Wave A: [check-in form](templates/check-in.md) + notebook link, before the Week 12 lab starts |
| **13** | **Wave B check-ins** during the Week 13 lab. The **Week 16 presentation schedule** is posted. | Wave B: check-in form + notebook link, before the Week 13 lab starts |
| **14** | Lab 14: policy workshop, then a project work session with instructor check-ins. | – |
| **15** | Lab 15: 5-minute **dry run** (a practice talk) with structured peer feedback ([Lab 15 page](../labs/lab15-project-dry-runs/)). | Draft slides (PDF) before the Week 15 lab starts; peer-feedback forms in the lab |
| **16** | Final presentations: 10 minutes + 3–5 minutes of questions. | Slides before your session; notebook, report, AI-use statement (team); reflection + peer evaluation (individual) |

**Check-in waves.** Each check-in is a ~5-minute conversation with the instructor or TA at your laptop. Half the teams check in during the last 25 minutes of the Week 12 lab (wave A); the rest during the Week 13 lab (wave B). The wave list is posted by Sunday of Week 11. Two teams may swap waves if both agree — tell the instructor. The requirement is the same in both waves: **your data loads and your baseline runs.**

**Presentation schedule.** One 2-hour final-exam slot fits **up to 8 teams** at 10 minutes + 3–5 minutes of questions + changeover. With more than 8 teams, the class uses **two parallel rooms** (instructor + TA) or **8-minute talks**. The schedule (room, order, and talk length) is posted on Brightspace **by the end of Week 13**, so you can plan around work and other exams.

---

## 6. Deliverables

| Deliverable | Format | Due (Arizona time) | Notes |
|---|---|---|---|
| Team registration | Brightspace form | Sunday of Week 10, 11:59 pm | Names of all members. |
| Team charter | PDF or Markdown | Sunday of Week 11, 11:59 pm (with the proposal) | Graded inside the proposal rubric. |
| Proposal canvas | PDF, ≤ 2 pages | Sunday of Week 11, 11:59 pm | Use the [canvas template](templates/proposal-canvas.md). |
| Check-in form | PDF or Markdown + a link to your notebook | Before your check-in lab starts (Week 12 or 13) | Use the [check-in template](templates/check-in.md). Data loads and baseline runs. |
| Dry-run slides | Draft slides (PDF) | Before the Week 15 lab starts | Graded on readiness, not polish. |
| Peer-feedback forms | Paper or Brightspace form | In the Week 15 lab | Each student completes forms for the two teams they are assigned in Lab 15. |
| **Final slides** | PDF (and .pptx/Google Slides link if you like) | Before your Week 16 session starts | See the [presentation guide](templates/presentation-guide.md). |
| **Final notebook** | `.ipynb` | Week 16 deadline on Brightspace | Start from the [starter notebook](Project_Starter_Notebook.ipynb). Must run top-to-bottom with **Runtime → Restart session and run all** in Colab, ideally in under 10 minutes on a CPU. |
| **Cached outputs** (if your method is slow) | CSV files | With the notebook | Any model or AI tool that is slow to run (LLM answers, image features, a long training run): save its outputs to CSV and have the notebook **load them if the file exists** (the starter notebook shows how). **Graders run your notebook from the cached outputs** — they do not regenerate them. |
| **Final report** | PDF, ≤ 6 pages | Week 16 deadline | Use the [report template](templates/report-template.md). References and the AI-use statement do not count toward the 6 pages. |
| **AI-use statement** | PDF or Markdown | Week 16 deadline | Use the [template](templates/ai-use-statement.md). One per team; signed by every member. |
| **Individual reflection** | PDF, about 1 page | Week 16 deadline | Prompts in the [peer evaluation form](templates/peer-evaluation.md#part-b--individual-reflection). |
| **Peer evaluation** | Brightspace form or PDF | Week 16 deadline | Confidential — only the instructor sees it. |

**File names:** `Team<number>_<deliverable>.<ext>`, for example `Team07_Report.pdf`, `Team07_Notebook.ipynb`, `Team07_llm_outputs.csv`. Individual files: `<LastName>_<FirstName>_Reflection.pdf`.

---

## 7. Policies

### AI use: the project is **AI-Assisted**
- You **may** use AI tools to brainstorm, explain concepts, debug code, draft text, and suggest analyses.
- You **must** submit an [AI-use statement](templates/ai-use-statement.md) describing what you used and what you checked. Each use is written in the course's one acknowledgment form: *"I acknowledge the use of [tool and version] to [specific use]. Prompts I used included [paste or summarize]. I checked the output by [how I verified it]. I am responsible for this work."* Keep a simple running log (date, tool, what for) from day one — it makes the statement easy.
- **You are responsible for every line** of code and text you submit, and every number in your report. "The AI wrote it" is never an explanation for an error.
- Every team member must be able to explain any AI-generated code in your notebook. If nobody on the team understands a block, rewrite it or remove it.
- In the **Assist** and **Evaluate** tracks, testing an AI model is part of the method: that part is **AI-Required**. Record the prompts, settings, dates, and outputs you analyze.
- Use tools the university has approved for course work when you can (the approved list changes; check the current UA guidance). No one should have to pay for a tool to do this project. If you use a paid tool you already have, say so and make sure your main results can be reproduced with free tools.
- The Lab 15 peer-feedback forms, the individual reflection, and the peer evaluation are **AI-Free** — your own words.

### Data you **may** use
- Any dataset in the course [`data/`](../data/) folder (CC BY 4.0 or U.S. Government public domain — give credit as in [`data/README.md`](../data/README.md)).
- Public datasets with a clear license that allows academic use (CC BY, public domain, open data). Record the provider, URL, license, and download date.
- Data your team collects yourselves *with permission*: for example, your own photos of campus concrete or pavement (no people, faces, or license plates), or measurements you take.
- Synthetic data you generate from engineering formulas — label it clearly as synthetic.
- Public code and regulation text you can link to (for example, OSHA rules on the eCFR).

### Data you **may not** use
The course uses one data-classification scheme: **Public / Internal / Confidential (client) / Restricted (personal & security-sensitive)**. Projects use **Public** data only.
- **No Confidential (client) data** — nothing from your internship, a family business, or a firm you know. This includes drawings, calculations, geotechnical reports, bids, and project photos, even if someone says "it's fine." Real firms have contracts that forbid it.
- **No Restricted data:** nothing about identifiable people (names, faces, license plates, occupant schedules, location traces) and no security-sensitive details of infrastructure.
- No data obtained by breaking a website's terms of service, logging in with someone else's account, or getting around a paywall.
- No copyrighted standards pasted in bulk into your repo, notebook, or a public AI tool (ACI, ASCE, ASTM, and similar standards are copyrighted). Short quotes with citation are fine.
- If you are unsure, **ask before you use it.**

### Late work and missed sessions
- **Project milestones:** no grace days; −10% per day late; not accepted after 3 days (see the syllabus late-work table).
- **Missed in-lab events** (your check-in, the Week 15 dry run): if your absence is excused, reschedule with the instructor within one week; otherwise those points are lost.
- **Final presentation:** it happens in your scheduled slot. In an emergency, contact the instructor as soon as you can.

### Other rules
- **Credit your sources.** Cite datasets, papers, code you adapted (including from the course labs), and tools.
- **Safety framing:** your project is a learning exercise, not a design tool. Say so in your report, and never present a model as safe to use for real design, inspection, or safety decisions.

---

## 8. FAQ

<details><summary><b>Can we use a dataset that is not in the course data folder?</b></summary>

Yes, if it is public, clearly licensed for academic use, and small enough to work with in free Colab. Put the provider, URL, license, and download date in your proposal. The [ideas page](project-ideas.md) lists external datasets we have checked. Course datasets are the safest choice — they are already cleaned and documented. For raw National Bridge Inventory files from other states or years, use the [NBI decode helper](tools/nbi_decode.py).
</details>

<details><summary><b>Our model is worse than the baseline. Did we fail?</b></summary>

No. A clear, honest negative result with a good baseline, sound evaluation, and a thoughtful explanation can earn full marks. Hiding a bad result, or changing settings until it disappears, is what loses points.
</details>

<details><summary><b>Can we use ChatGPT (or another AI) to write our code?</b></summary>

Yes — the project is AI-Assisted. Read the code before you run it, test it with `assert` statements, and record the use in your AI-use statement. Every teammate must be able to explain it.
</details>

<details><summary><b>Do we need a GPU or paid tools?</b></summary>

No. Every idea on the ideas page fits the free Colab CPU runtime (a free T4 GPU helps for vision and LLM projects but is optional). Keep models small, subsample data if training is slow, and cache slow outputs to CSV. Model downloads happen on Google's computers, not on your laptop or phone data plan.
</details>

<details><summary><b>Running our LLM test takes 40 minutes. What do we do?</b></summary>

Run it once, save the outputs to a CSV (model, settings, date, prompt, answer), and have the notebook load the CSV if it exists — the starter notebook's section 6.7 does exactly this. Submit the CSV with your notebook. Graders run your notebook from the cached outputs.
</details>

<details><summary><b>Can I use data from my internship?</b></summary>

No. Do not use Confidential (client) or employer data, even with a manager's verbal OK. Use a public dataset that resembles it instead.
</details>

<details><summary><b>Can we change our project after the proposal?</b></summary>

Small changes are normal — describe them at your check-in. A completely new topic after Week 12 needs the instructor's approval, because you still need data and a running baseline by your check-in.
</details>

<details><summary><b>Can we reuse code from the labs?</b></summary>

Yes, and you should. Lab 11 is a complete example of the project workflow. Say which lab the code came from and what you changed.
</details>

<details><summary><b>Does every team member have to present?</b></summary>

Yes. Every member speaks during the presentation, and every member should be ready to answer questions about any part of the project.
</details>

<details><summary><b>How long should the report be?</b></summary>

At most 6 pages, including figures and tables; references and the AI-use statement do not count. Shorter is fine if it covers every required element. Graders stop reading at page 6.
</details>

<details><summary><b>When will we know our presentation time?</b></summary>

The schedule is posted on Brightspace by the end of Week 13, including whether your room uses 10-minute or 8-minute talks.
</details>
