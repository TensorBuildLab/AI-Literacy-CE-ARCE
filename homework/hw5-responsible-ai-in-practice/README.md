# Homework 5 — Responsible AI in Practice

**Posted:** Week 12 · **Due:** end of Week 14, **Sunday 11:59 pm (Arizona time)** on Brightspace · **Individual** · **100 points** · Expected time: about 5 hours

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/TensorBuildLab/AI-Literacy-CE-ARCE/blob/main/homework/hw5-responsible-ai-in-practice/HW5_Responsible_AI_in_Practice.ipynb)

## Overview
Three tasks a first-year engineer at a firm that uses AI could face:

- **Part A — Find the errors (about 2 h).** A coworker pasted an AI-generated storm-drain calculation into the project file. It contains four planted errors. Find and fix them with the 5-check verification workflow from Lab 12.
- **Part B — Audit a vendor's model (about 1.5 h).** A vendor claims its concrete-strength model is accurate to about 3 MPa. Test whether that holds for *your* firm's fly-ash mixes, and where it fails.
- **Part C — Advise the firm (about 1 h).** Write a short memo (250–350 words): should the firm adopt an AI tool for a specific task? Use the NIST AI Risk Management Framework and engineering ethics.

Everything happens in the starter notebook (Colab link above). Written answers go in the notebook's text cells.

## Learning goals
1. Verify AI-generated engineering work using the 5 checks: **(1) Restate, (2) Units & magnitude, (3) Independent check, (4) Sources, (5) Test & document**.
2. Measure a model's performance under distribution shift and by subgroup, and explain why the *direction* of an error (conservative or unconservative) matters for safety.
3. Recommend whether and how to use an AI tool, using the NIST AI RMF functions (**Govern, Map, Measure, Manage**) and professional responsibilities (public safety, competence, responsible charge).

## AI-use labels
| Part | Label | What it means here |
|---|---|---|
| A | **AI-Free** | No AI tools: no chat assistants and no AI code completion. Python, your notes, a calculator, and the OSHA text are fine. **Before you start Part A, turn off Colab's AI suggestions** — see *Turning off AI suggestions* in the [Colab setup guide](../../resources/colab-setup.md). |
| B | **AI-Assisted** | You may ask AI for coding help or explanations. Acknowledge it. You are responsible for every number. |
| C | **AI-Assisted with acknowledgment** | You may use AI to brainstorm or edit, but the analysis and recommendation must be yours. An acknowledgment is **required**. |

**AI-use acknowledgment** (final notebook cell, covering Parts B and C), using the course template from the [AI-use guide](../../resources/ai-use-guide.md):
> I acknowledge the use of [tool and version] to [specific use]. Prompts I used included [paste or summarize]. I checked the output by [how I verified it]. I am responsible for this work.

or "I did not use AI tools for this assignment." **A missing acknowledgment costs 5 points** (of 100), as on every homework.

## Tasks

### Part A — Find the errors (AI-Free, 35 points)
Scenario: a new 18-in storm drain for a 3.5-acre asphalt parking lot in Tucson, with a 10-ft-deep trench in Type C soil inside a 30-ft construction easement. Flows are in **cfs** (cubic feet per second). The full AI-generated write-up is in the notebook.

| Task | Points |
|---|---|
| **A1. Restate** the problem: given (with units), asked, and the decision that depends on it. | 4 |
| **A2. The four errors:** for each, the step, what is wrong, which check caught it, and the correction. (Some steps are correct — "fixing" a correct step earns nothing.) | 16 |
| **A3. Independent check:** redo the calculation in Python (runoff, 18/21/24-in pipe capacity, trench top width). | 8 |
| **A4. Corrected conclusion:** is the 18-in pipe adequate, what do you recommend, and what does the trench width mean for the easement? | 4 |
| **A5. Sources and documentation:** name your sources and write a one-sentence verification note for the project file. | 3 |

### Part B — Audit a vendor's model (AI-Assisted, 35 points)
The notebook builds the vendor's model (a random forest trained on mixes **without fly ash**) from `concrete_strength.csv`. Do not change that cell.

| Task | Points |
|---|---|
| **B1.** Reproduce the vendor's claim: MAE on the vendor's own test set. | 5 |
| **B2.** Test on your fly-ash mixes: MAE, mean bias (predicted − actual), and the share over-predicted by more than 5 MPa. | 8 |
| **B3.** Subgroup analysis by test age: table (count, MAE, bias, share over 5 MPa) and a bar chart of bias. | 8 |
| **B4.** Predicted-vs-actual plot for both data sets with a 1:1 line. | 6 |
| **B5.** Audit conclusion (100–150 words): does the claim hold for your use, why does the model fail where it does, and what Manage actions do you recommend? | 8 |

### Part C — Should our firm adopt it? (AI-Assisted with acknowledgment, 25 points)
Write a **short memo (250–350 words)** to a principal of a 40-person Arizona firm. Pick one scenario:
1. A drone-photo crack-detection tool to rank which of a county's 400 bridges get a hands-on inspection first.
2. A general chat assistant that drafts stormwater calculation packages for permit submittals.
3. The vendor model from Part B, to decide formwork-stripping times.
4. An AI tool that predicts heating/cooling loads to choose building massing at concept design.

Your memo must contain (one or two sentences each is fine): a recommendation in the first two sentences; **Map** (task, users, who is affected, worst realistic failure); **Measure** (evidence and required tests); **Manage and Govern** (safeguards, accountability, documentation); the **data class** the tool would see (Public / Internal / Confidential (client) / Restricted) and whether that is allowed; **professional ethics** (public safety paramount, competence, responsible charge); hedged statements about current law or products ("as of 2026"). You may reuse ideas from your project's responsible-AI section — in your own words.

### Professionalism (5 points)
The notebook runs top to bottom, and plots have titles and axis labels with units.

## Rubric

| Component | Excellent (full) | Adequate (about half) | Missing / incorrect (0) | CLO · ABET SO |
|---|---|---|---|---|
| A1 Restate (4) | All givens with units, what is asked, and both decisions (pipe size, trench/easement) | Givens or asked incomplete | Missing | CLO7 · SO 6 |
| A2 Errors (16; 4 each) | Error located, explained, check named, correct value given | Located but explanation or correction wrong | Not found | CLO7 · SO 6 |
| A3 Independent check (8) | Correct code and numbers for runoff, three pipe sizes, and trench width; assumption stated | Minor slips (one wrong value) | Not attempted or mostly wrong | CLO7 · SO 6 |
| A4 Conclusion (4) | Correct adequacy call, a pipe size recommendation, easement consequence | Adequacy call right, rest missing | Wrong call | CLO7 · SO 6 |
| A5 Sources (3) | Two specific, checkable sources + a useful verification note | Vague sources ("the internet", "AI") | Missing | CLO7 · SO 6 |
| B1–B2 (13) | Correct metrics; bias sign interpreted as unconservative | Metrics right, interpretation missing | Wrong or missing | CLO7 · SO 6 |
| B3–B4 (14) | Correct subgroup table; clear, labeled charts | Table or charts incomplete or unlabeled | Missing | CLO7 · SO 6 |
| B5 Conclusion (8) | Uses numbers; explains shift (no fly-ash data; slow early strength gain); specific Manage actions | Generic ("needs more data") without numbers | Missing | CLO7 · SO 6 |
| C Memo (25) | Clear recommendation (3); Map (4); Measure with evidence (5); Manage/Govern safeguards, accountability, and data class (5); ethics incl. responsible charge (5); clear writing within 250–350 words (3) | Sections present but generic or unsupported | Missing sections | CLO6, CLO7 · SO 4 |
| Professionalism (5) | Runs cleanly; labeled plots | One of these missing | Both missing | — |
| AI-use acknowledgment | Present and specific (template above) | — | Missing: **−5 points** | — |

## Deliverables and submission
1. In Colab: **Runtime → Restart session and run all**; fix any errors.
2. **File → Download → Download .ipynb**.
3. Upload the `.ipynb` to the **HW5** assignment on Brightspace by **Sunday 11:59 pm (Arizona time) at the end of Week 14**.

Late work: see the syllabus late-work table (two grace days per semester, then −10% per day, up to 3 days). Academic-integrity rules follow the syllabus. Remember: Part A must be your own work without AI tools.

## Helpful references
- Lab 12 (5-check workflow) and Lab 13 (stress tests, subgroups, model cards).
- NIST, *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*, 2023: <https://www.nist.gov/itl/ai-risk-management-framework>
- NSPE Code of Ethics for Engineers: <https://www.nspe.org/career-growth/nspe-code-ethics-engineers>
- ASCE Code of Ethics: <https://www.asce.org/career-growth/ethics/code-of-ethics>
- OSHA excavation rule (29 CFR 1926 Subpart P): course file `data/osha/osha_1926_subpartP_excavations.txt`, or the official eCFR.
