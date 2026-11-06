# Final Report Template

**Due:** Week 16, by the deadline posted on Brightspace (Arizona time) · **Weight:** the report and notebook together are 35% of the project (70 points; see the [notebook + report rubric](../rubrics.md#5-final-notebook-and-report--70-points)) · **AI-Assisted** (with a separate [AI-use statement](ai-use-statement.md)) · **Late work:** no grace days for project milestones; −10% per day late, not accepted after 3 days

**Format:** PDF, **at most 6 pages** including figures and tables. References and the AI-use statement do not count toward the 6 pages. 11-pt font or larger, single spacing, 1-inch (2.5 cm) margins. Graders stop reading at page 6.

**Audience:** an engineer at a firm or agency who knows engineering but not machine learning. Plain language, short sentences, every term defined the first time, every quantity with units.

The page budgets below are suggestions that add up to about 6 pages. The section structure mirrors the [starter notebook](../Project_Starter_Notebook.ipynb), so you can move text and figures straight across.

---

## Title block (top of page 1)
- A title that states the finding or question ("A crack classifier trained on campus photos misses one in three bridge-deck cracks").
- Team number, members, track, date.

## Summary (≈ 120 words)
Write this last. In five sentences: the problem and user; the data; the method and baseline; the main result in numbers with units; the most important limitation. A busy reader should be able to stop here and still know what you found and how far to trust it.

## 1. Problem and users (≈ ½ page)
- The engineering problem and why it matters (cost, safety, time, energy).
- The exact question you answered.
- Who would use the answer and what decision it supports. What do they do today without AI?
- What a useful result would look like (your success criterion from the proposal).

## 2. Data and its limits (≈ ¾ page)
- **Data card:** provider, URL, license, download date, size, what one row/image/document is, inputs and target with units. A small table works well.
- **Cleaning:** what you changed and why (missing values, unit conversions, removed rows). Numbers before and after.
- **Exploration:** one or two figures that show something important (target distribution, a key relationship, class imbalance). Every figure: title, axis labels with units, a caption that says what to notice.
- **Limits:** what the data does *not* represent — region, climate, years, building types, label quality, imbalance, missing groups. Be specific.
- For Assist/Evaluate: how you built the test set and the answer key, and who checked the key.

## 3. Method (≈ ¾ page)
- What you did, in enough detail that another team could repeat it: features, model or tool, key settings, prompts (or a pointer to the notebook). If you cached slow outputs (LLM answers, image features), say where the CSV files are.
- **Why** this method fits the problem and your data size.
- How you split data or organized the test (time-based split, group split by mix or shape, practice vs test questions). Explain how you kept the test truly unseen.
- What you tried that did not work (briefly — this is useful information).

## 4. Baseline and evaluation (≈ 1 page)
- The baseline and why it is a fair comparison.
- Metrics and why they fit the task and how serious a mistake would be (MAE in MPa; recall for the "poor" or "crack" class; correctness rate within 2%; citation accuracy).
- **A results table:** baseline vs your method(s), on test data, with units.
- One key figure (predicted vs actual, confusion matrix, error by subgroup, accuracy by prompt style).
- **Where it fails:** subgroups, extremes, example mistakes. Show at least two real failure cases.

## 5. Verification (≈ ½ page)
Report how you checked your own results with the course's five checks. A table works well:

| Check | What we did | What we found |
|---|---|---|
| **Restate** | | |
| **Units & magnitude** | | |
| **Independent check** | | |
| **Sources** | | |
| **Test & document** | | |

Say honestly if a check found a problem and what you changed.

## 6. Responsible-AI analysis (≈ ¾ page)
- **Risks and failure modes:** what happens if someone relies on a wrong output? Which errors are most costly (a missed crack vs a false alarm)?
- **Bias and representativeness:** whose infrastructure, buildings, or situations are missing or under-represented? Did error differ by subgroup?
- **Distribution shift:** where would the model or tool stop working (other regions, climates, sensors, code editions)?
- **Accountability:** who is responsible for decisions made with this tool? (In practice, the licensed engineer in responsible charge — never the tool.) What human review is required?
- **Other concerns** that apply: privacy, security (prompt injection, data leakage), copyright and licensing, environmental cost.
- **Model card / tool card (short):** intended use, uses it is not meant for, data, performance, known limits. You may put the full card in your notebook and summarize it here.
- Optional: organize this section with the NIST AI RMF functions — Govern, Map, Measure, Manage.

## 7. Conclusions and recommendations (≈ ½ page)
- Answer your question directly, with numbers.
- A recommendation for the user: use it / use it only with conditions / do not use it — and why.
- What you would do next with more time or data.

## References (not counted)
Datasets (with license), papers, course labs you adapted code from, software libraries, and AI tools. Any consistent citation style.

## Team contributions (not counted; ≤ ⅓ page)
One or two lines per member on what they did, and any changes to the roles or plan in your team charter (when and why). This section is graded in the "Team plan executed" rubric row, together with your charter and check-in record, and should match your peer evaluations and AI-use statement.

---

### Before you submit
- [ ] ≤ 6 pages (references and AI-use statement excluded); 11-pt font or larger.
- [ ] Every number in the report matches the final notebook run.
- [ ] Every figure has a title, axis labels with units, and a caption.
- [ ] The baseline result is in the results table.
- [ ] All five verification checks are reported.
- [ ] Limits and accountability are stated plainly.
- [ ] Sources and licenses are cited.
- [ ] Spell-checked and read aloud once by someone who did not write that section.
