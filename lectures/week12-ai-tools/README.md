# Week 12 — AI Tools for Engineers: Choosing, Using, and Verifying

**Slides:** [PDF](Week12_AI-Tools-for-Engineers.pdf) · [PowerPoint](Week12_AI-Tools-for-Engineers.pptx) · **Lab:** [Lab 12 — Trust but Verify](../../labs/lab12-trust-but-verify/) · **Homework:** [HW5 — Responsible AI in Practice](../../homework/hw5-responsible-ai-in-practice/) (posted this week, due end of Week 14, Sunday 11:59 pm)

*Project:* proposal feedback is returned this week. Progress check-ins run in two waves: half the teams in the last 25 minutes of Lab 12, the rest in Lab 13. Before your check-in, have your data loading and a **baseline** model running (the simplest reasonable model a real model must beat), and upload the check-in form and your notebook link on Brightspace.

## Learning objectives

By the end of this week, you can:

1. Describe the main **categories** of AI tools and what each is good and bad at.
2. Choose a tool using **task fit, accuracy, privacy, cost, and licensing**.
3. Apply the **5-check verification workflow** to an AI answer and catch its errors.
4. Test AI-written code with known cases and `assert` before trusting it.
5. Write a clear **AI-use acknowledgment** statement.

## The big ideas

- **Learn categories, not brands.** Engineers meet eight kinds of AI tools: general chat assistants, coding assistants, research/search assistants with citations, document and spreadsheet AI, image and visual tools, domain tools inside BIM/CAD/analysis software, local and open models, and agents. Products and features change every few months (this list is as of 2026); the questions you ask about them do not.
- **Five questions before you use a tool:** Is it the right kind of tool for the task (sometimes a spreadsheet or formula is better)? How accurate is it on *your* kind of problem — test it on cases you know? What data will it see, store, or train on? What does it cost, including your time to check it? What do its terms and license allow?
- **Classify data before you paste it.** The course uses one scheme: **Public** (published codes, course datasets) can go into most tools. **Internal** work needs a university- or firm-approved tool. **Confidential (client)** data under a contract or NDA goes only where the contract and policy allow — often nowhere. **Restricted** data (personal information and security-sensitive infrastructure details): don't paste. Deleting a client's name does not make a report public.
- **Match your reliance on AI to the risk.** Where an undetected error is costly and hard to check (a final foundation design), avoid AI or require expert review. Where errors are costly but easy to check (a beam calculation), use AI and verify every result.
- **The 5-check verification workflow** — use these names in Lab 12, HW5, and your project:
  1. **Restate** — restate the problem, inputs, and assumptions. Did the AI solve *your* problem?
  2. **Units & magnitude** — check units and whether the size of the answer is reasonable.
  3. **Independent check** — a hand calculation, Python, or a different method (not the same chatbot again).
  4. **Sources** — confirm that cited codes and papers exist and actually say that.
  5. **Test & document** — test generated code with known cases, and document your AI use.
- **Worked examples.** An AI used the cantilever formula wL²/2 (w = load, kN/m) for a *simply supported* beam (6 m, 10 kN/m) and got 180 kN·m; Restate and an Independent check (statics) give wL²/8 = 45 kN·m. Another entered a 0.5 % channel slope as 0.5 in Manning's equation and got about 51 m³/s; the Units & magnitude check (velocity ≈ 32 m/s, highway speed) exposes it — the right answer is about 5.1 m³/s. And an AI quoted OSHA as allowing 1:1 slopes in Type C soil; only the Sources check catches that Table B‑1 says 1½H:1V (34°).
- **AI-written code is a draft.** Read every line, check units and imports (AI sometimes names packages that don't exist), never paste secrets, and test it with `assert` against cases worked by hand. In the lecture-only example, a rational-method function that divided by 3600 instead of 360 looked right until one known case failed. In Lab 12 (Part 4), an AI-written Manning function uses R^(3/2) instead of R^(2/3) — and still passes a test with R = 1 m, because 1 raised to any power is 1. Choose tests that a wrong function would fail.
- **Document AI use** with the course template (from the [AI-use guide](../../resources/ai-use-guide.md)): *I acknowledge the use of [tool and version] to [specific use]. Prompts I used included [paste or summarize]. I checked the output by [how I verified it].* You remain responsible for everything you submit. Template and examples: the course [AI-use guide](../../resources/ai-use-guide.md).

## Key terms

| Term | Plain-language meaning |
|---|---|
| Coding assistant | An AI tool that writes, explains, or debugs code, usually inside an editor or notebook |
| Research/search assistant | An AI tool that searches the web or papers and answers with citations you must open and check |
| Domain tool | AI features built into engineering software (BIM, CAD, structural or energy analysis) |
| Local / open model | A model whose weights you can download and run on your own computer, so data stays local |
| Data classification | Sorting data into levels that decide which tools may see it. This course uses Public / Internal / Confidential (client) / Restricted (personal & security-sensitive) |
| Baseline | The simplest reasonable model (e.g., always predict the most common class) that a real model must beat |
| NDA | Non-disclosure agreement: a contract that limits who may see a client's information |
| Verification | Checking an output independently before relying on it |
| Order of magnitude | The rough size of a number (1, 10, 100…); unit slips usually change it by 10× or more |
| Independent check | A second way to get the answer that does not depend on the first (hand calc, Python, another method) |
| `assert` | A Python statement that stops the program with an error if a condition is false — the simplest test |
| Test case (known case) | An input whose correct output you already know, used to check code |
| Hallucinated citation | A reference an AI invents, or a real reference that does not say what the AI claims |
| AI-use acknowledgment | A short statement of which AI tool you used, for what, and how you verified the result |

## Read / watch

### Required (≈ 37 min total)

- **OSHA excavation rules, 29 CFR 1926 Subpart P (eCFR)** — <https://www.ecfr.gov/current/title-29/subtitle-B/chapter-XVII/part-1926/subpart-P>. Open Appendix B and find Table B‑1 (maximum allowable slopes). 5 minutes. This is what "go to the primary source" looks like.
- **Python documentation: the `assert` statement** — <https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement>. 2 minutes; you will use `assert` in Lab 12.
- **Course AI-use guide** — [resources/ai-use-guide.md](../../resources/ai-use-guide.md). The acknowledgment template and the 5 checks. 10 minutes.
- **NIST AI 600-1, Generative AI Profile (2024)** — <https://doi.org/10.6028/NIST.AI.600-1>. Skim Section 2, its list of 12 risks of generative AI (confabulation, data privacy, information security, intellectual property, and more). About 20 minutes; it previews Week 13.

### Optional

- **U.S. Copyright Office: Copyright and Artificial Intelligence** — <https://www.copyright.gov/ai/>. Skim the overview of current U.S. guidance on AI-assisted work. About 10 minutes. Guidance changes — note the date of what you read.

## Check yourself

1. You need the maximum moment for a simply supported beam with a known formula. Is a chat assistant the best tool? What would you use instead, and why?
   <details><summary>Answer</summary>Not the best fit. A known formula is exact and auditable in a spreadsheet, Python, or by hand (M = wL²/8). A chat assistant might pick the wrong formula or slip on arithmetic, and you would have to check it anyway. Use AI for explaining or drafting, not for replacing a calculation you can do directly.</details>

2. A classmate removes the client's name from a confidential geotechnical report and pastes it into a free chatbot. What is wrong with this?
   <details><summary>Answer</summary>Removing the name does not remove the confidentiality obligation — the site address, boring locations, and project details still identify the client, and the contract or NDA, plus the firm's AI policy, decide where the data may go. Free consumer tools may store or train on inputs. Use only an approved tool the contract allows, or do it yourself.</details>

3. An AI answer for a rectangular channel gives Q = 51 m³/s for a 2 m wide channel flowing 0.8 m deep. Which check flags it, and how?
   <details><summary>Answer</summary>Units & magnitude. The velocity is V = Q/A = 51 / 1.6 ≈ 32 m/s, about highway speed — not plausible in a small concrete channel. The cause: a slope of 0.5 % entered as 0.5 instead of 0.005. With S = 0.005, Q ≈ 5.1 m³/s and V ≈ 3.2 m/s.</details>

4. Why is asking the same chatbot "Are you sure?" not an Independent check?
   <details><summary>Answer</summary>It uses the same model, the same training, and often the same faulty reasoning, so it can repeat or confidently defend the error (or flip its answer to please you). An independent check uses a different route: a hand calculation, a Python calculation, a different method, or a trusted reference.</details>

5. An AI-written function returns Manning velocity as `(1 / n) * R ** (3 / 2) * S ** 0.5`. A test with n = 0.013, R = 1 m, S = 0.001 passes (2.43 m/s). Why doesn't that prove the function is right, and what test would catch the bug?
   <details><summary>Answer</summary>Manning's equation uses R^(2/3), but 1 raised to any power is 1, so R = 1 m cannot reveal a wrong exponent. Use an R other than 1 m with a hand-calculated answer — e.g., R = 0.5 m gives V = (1/0.013) × 0.5^(2/3) × 0.001^(1/2) ≈ 1.53 m/s, while the buggy function gives ≈ 0.86 m/s — or a property test: doubling R should multiply V by 2^(2/3) ≈ 1.59. Example: <code>assert abs(f(0.013, 0.5, 0.001) - 1.532) &lt; 0.01</code>.</details>

## Coming up

- **Lab 12 — Trust but Verify (this week's lab day):** ask a small LLM eight CE/ARCE questions (beam moment, unit conversions, Manning's equation, wall heat loss Q = U·A·ΔT, w/c ratio, OSHA slope, trip generation, rational method Q = CiA), check every answer in Python with the 5 checks, catch a bug in an AI-written Manning function with `assert` (Part 4), and write an AI-use acknowledgment. The lab ends with an **exit ticket**: 3 short questions you answer alone, without AI (AI-Free), during the last 10 minutes of lab. **Due:** Sunday 11:59 pm (Arizona time) of this week, on Brightspace.
- **Project check-in, wave 1:** half the teams meet the instructor in the last 25 minutes of Lab 12 (the rest in Lab 13). Upload the check-in form and notebook link on Brightspace before your check-in.
- **HW5 — Responsible AI in Practice:** posted now, due end of Week 14 (Sunday 11:59 pm).
- **Week 13 — Responsible AI:** what can go wrong with a whole model even when its test score looks good — distribution shift, bias, uncertainty, explainability, privacy, security, environmental footprint — and the NIST AI Risk Management Framework. The Week 13 lab holds the second wave of project check-ins.
