# Project Proposal Canvas

**Due:** **Sunday of Week 11, 11:59 pm (Arizona time)**, on Brightspace, together with your [team charter](team-charter.md) · **Weight:** 10% of the project (20 points, charter included; see the [proposal rubric](../rubrics.md#1-proposal--20-points)) · **Length:** at most **2 pages** as a PDF · **AI-Assisted** (add an AI-use acknowledgment at the bottom) · **Late work:** project milestones have no grace days; −10% per day late, not accepted after 3 days

Copy this file into a document, fill in every box, and delete the grey guidance text. Bullet points are fine. Aim for the word counts shown — short and specific is better than long and vague. Lab 11's engineering memo is a good model for the tone.

---

**Team number:** ____ **Members:** ______________________
**Project title:** ______________________ (a title that states the question or finding, not just a topic: "Can a crack model trained on campus photos work on bridge decks?" is better than "Crack detection")
**Track:** ☐ Predict ☐ See ☐ Assist ☐ Evaluate **Idea from the list?** ☐ Yes, # ____ ☐ Our own

---

### 1. Problem and question (≈ 60 words)
> What engineering problem are you working on, and what exact question will you answer? A good question has a measurable answer.

### 2. Users and decision (≈ 40 words)
> Who would use your result (a bridge inspector, an energy modeler at the concept stage, a site superintendent)? What decision would it help with? What do they do today without AI?

### 3. Data (≈ 80 words + a small table)
> Where does the data come from (provider, URL, license)? How many rows, images, or documents? What is one row? What are the inputs and the target, with **units**? For Assist and Evaluate: what is your test set, and how will you know the correct answers?

| Source and license | Size | One row/item is… | Inputs (units) | Target or answer key (units) |
|---|---|---|---|---|
| | | | | |

### 4. Data limits (≈ 50 words)
> What does the data *not* represent? (Region, climate, years, building types, missing values, labels that are someone's judgment, class imbalance.) Name at least two limits.

### 5. Method (≈ 60 words)
> What AI method or tool will you use, and why does it fit? (For example: random forest on tabular data; ResNet-18 transfer learning; TF-IDF retrieval + Qwen2.5-0.5B; testing two chatbots with two prompt styles.) Which lab is the closest model?

### 6. Baseline (≈ 30 words)
> What simple approach will you compare against? (Predict the average; "same hour last week"; always predict the majority class; the LLM without retrieval; the plain prompt.)

### 7. Evaluation and success (≈ 50 words)
> How will you split the data or build the test set? Which metrics, in which units? What result would count as useful — for example, "MAE below 5 MPa and better than the baseline on a mix-wise split"?

### 8. Verification plan (≈ 50 words)
> How will you apply the five checks to *your own* results? One line each is enough.

| Check | Our plan |
|---|---|
| Restate | |
| Units & magnitude | |
| Independent check | |
| Sources | |
| Test & document | |

### 9. Responsible-AI first look (≈ 60 words)
> What could go wrong if someone relied on your result? Who could be harmed or left out by the data? What is the worst failure mode? Who is accountable for decisions made with it?

### 10. Plan and roles

| Week | Goal | Lead |
|---|---|---|
| 12 | Data loaded and explored; baseline started | |
| 12 or 13 | **Check-in** (your wave): data + baseline running | |
| 14 | Main method and evaluation | |
| 15 | **Dry run;** verification and responsible-AI analysis | |
| 16 | Final presentation, notebook, report | |

### 11. Biggest project risk and backup plan (≈ 30 words)
> What is most likely to stop you (data access, training time, a test set that takes too long to write)? What will you do if it happens?

### 12. AI tools we plan to use
> Which tools, for what (for example, "Gemini in Colab for debugging; Qwen2.5-0.5B as the model under test")? Remember to keep an AI-use log from today.

---

*AI-use acknowledgment for this proposal:* "I acknowledge the use of [tool and version] to [specific use]. Prompts I used included [paste or summarize]. I checked the output by [how I verified it]. I am responsible for this work." — or "We did not use AI tools for this proposal."
