# Lab 14 — AI Policy Workshop + Project Work

**Week 14 lab · 75 minutes · AI-Assisted · Team activity, individual submission**

> **What to hand in, when, and points**
> 1. **What:** your own copy of the Lab 14 notebook (`.ipynb`), with the team's policy, the scenario answers, your project plan, the exit ticket, and the AI-use acknowledgment.
> 2. **Due:** Sunday 11:59 pm (Arizona time) of this week, on Brightspace.
> 3. **Graded:** completion + exit ticket, like every graded lab (labs are 25% of the course; the lowest lab is dropped).
> 4. **Late work:** see the syllabus late-work table (two grace days per semester, then −10% per day, up to 3 days).
> 5. **Allow ~5 minutes** at the end to run all cells, download, and upload (no models to download today).

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/TensorBuildLab/AI-Literacy-CE-ARCE/blob/main/labs/lab14-policy-workshop/Lab14_Policy_Workshop.ipynb)

**Notebook:** [`Lab14_Policy_Workshop.ipynb`](Lab14_Policy_Workshop.ipynb) · **Printable template:** [`policy-template.md`](policy-template.md) · **Lecture:** [Week 14 — AI Policy, Ethics, and Professional Practice](../../lectures/week14-ai-policy-ethics/)

## What you'll do

**First half (about 40 minutes) — policy workshop.** Your project team plays the leadership of *Ocotillo Engineering Group*, a fictional 25-person engineering firm in Tucson that has no AI policy yet. You will:

1. Decide **what kind of information may go into which kind of AI tool** — a small table you fill in with Python, using the course's four data classes (**Public / Internal / Confidential (client) / Restricted (personal & security-sensitive)**) and three tool types (public AI tool / enterprise AI / local model).
2. Write a **one-page AI-use policy** with nine short sections — the same nine as the Week 14 lecture checklist: purpose and scope, approved tools, data classification, verification and review, disclosure to clients, training, accountability and responsible charge, incident reporting, and review cycle. **Each role writes two sections**, then the team reads the whole policy through.
3. **Apply your policy** to three required scenarios — an AI note-taking app recording a client site walk, an AI model-review tool that flags a roof beam, and AI-generated façade images for a client pitch — plus two optional ones: an AI-drafted specification that cites a code edition that does not exist, and drafting an **RFI** response (a request for information: a formal question from the contractor to the design team).
4. **Swap policies** with another team and find a gap.

**Second half (about 25 minutes) — final-project work session.** Work through the Week 14 project checklist in the notebook. The instructor visits each team for a short check-in. You leave with a plan for next week's 5-minute dry run (Lab 15).

**Last 10 minutes — exit ticket:** 3 short questions you answer alone, without AI (AI-Free), during the last 10 minutes of lab. If you must leave early, answer them on your own before you submit.

## Before the lab

- [ ] Look over the Week 14 lecture slides, especially "responsible charge" and the nine-part policy checklist.
- [ ] Skim the [NSPE Code of Ethics for Engineers](https://www.nspe.org/career-growth/ethics/nspe-code-ethics-engineers) and the [ASCE Code of Ethics](https://www.asce.org/career-growth/ethics/code-of-ethics) (10 minutes; the first few sections are enough).
- [ ] Sit with your **project team**.
- [ ] Have your project notebook ready to run, and your check-in feedback (Week 12 or 13) open.

## Data used

None. The firm profile and the scenarios are in the notebook. (If your team prefers to draft the policy in a shared document first, copy [`policy-template.md`](policy-template.md) — then paste your final text into each member's notebook.)

## How it's graded

- **Completion + exit ticket**, like every graded lab.
- The policy is **team work**: each member submits their own notebook, and the policy text may be identical across your team. List your teammates in the first answer cell.
- **AI-use label: AI-Assisted.** You may use an AI tool to brainstorm or check wording, but the decisions in your policy and your scenario judgments must be your team's own. Fill in the AI-use acknowledgment at the end. The **exit ticket is AI-Free** and individual.
- Model answers exist for every question, but many scenarios have more than one good answer. What counts is a clear decision with reasons tied to your policy, the codes of ethics, and responsible charge.

## Why this matters

Every firm you intern or work at will have (or soon need) rules like these. The same thinking goes into **HW5 Part C** (should a firm adopt AI tool X for task Y?), due at the end of this week, and into the **responsible-AI section** of your final project.

## Troubleshooting

- **The self-check says a value is `None`.** Replace every `None` in the table with `"yes"`, `"no"`, or `"ask"` — with the quotation marks.
- **`NameError: name 'policy' is not defined`.** Run the cells in order from the top (**Runtime → Run before**), including the setup cell and the table cell.
- **`may_i_paste` prints `None`.** Your table still has a `None` in it — fill it in and re-run the table cell.
- **Editing a text answer:** double-click the cell that says *Your answer:*, type, then press **Shift + Enter**.
- **Lost work?** Always work in **File → Save a copy in Drive**, not the original.
- **Laws and rules mentioned here change often.** Statements about regulations are "as of 2026" — check the current version before relying on them.
