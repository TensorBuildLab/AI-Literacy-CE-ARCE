# Final Presentation Guide

**When:** Week 16, during the final-exam period · **Length:** **10 minutes** + 3–5 minutes of questions · **Weight:** 30% of the project (60 points; see the [presentation rubric](../rubrics.md#4-final-presentation--60-points)) · **Slides:** upload a PDF to Brightspace before your session starts (Arizona time)

**Scheduling rule.** One 2-hour final-exam slot fits **up to 8 teams** (10-minute talk + 3–5 minutes of questions + changeover). With more than 8 teams, the class uses **two parallel rooms** (instructor in one, TA in the other) or **8-minute talks**. The schedule — your room, your order, and your talk length — is posted on Brightspace **by the end of Week 13**.

**Timing.** Aim to finish **between 9:00 and 10:00** (between 7:00 and 8:00 for 8-minute talks). The moderator stops you at the time limit, even mid-sentence.

**Your audience:** classmates, the instructor, and possibly guests from industry. Imagine a project manager at a CE/ARCE firm who must decide whether to trust your result. Technical enough to be honest, plain enough to follow.

---

## Suggested slide outline (≈ 11 slides, 10 minutes)

| # | Slide | Time | What it should show |
|---|---|---|---|
| 1 | **Title** | 0:15 | A title that states the question or finding; team members; track. |
| 2 | **The problem and the user** | 1:00 | A real situation (photo you may use or a simple diagram), who needs the answer, what decision it supports. |
| 3 | **Our question** | 0:30 | One sentence, measurable. What "useful" would mean. |
| 4 | **Data** | 1:15 | Source and license, size, what one row/image is, inputs and target with units. One exploratory figure. |
| 5 | **Data limits** | 0:45 | What the data does not represent. Be specific. |
| 6 | **Method and baseline** | 1:15 | A simple diagram of your pipeline. The baseline you compare against and why. How you kept the test unseen. |
| 7 | **Results** | 1:30 | Baseline vs your method on test data, in units. One clear figure. |
| 8 | **Where it fails** | 1:00 | Real failure examples, subgroup errors, or error types. |
| 9 | **Verification** | 0:45 | At least two of the five checks (Restate, Units & magnitude, Independent check, Sources, Test & document) with what each found; say that all five are in the report. |
| 10 | **Responsible AI** | 1:00 | Biggest risk, who could be affected, where it should not be used, who is accountable, what human review is needed. |
| 11 | **Takeaway and recommendation** | 0:45 | One sentence for a non-technical listener; use / use with conditions / don't use; what's next. |

Backup slides (after the last slide, not presented): extra results, model settings, the AI-use summary. Useful during questions.

**8-minute talks:** keep every row, and shorten each one by about 20% (for example, Results 1:15, Data 1:00). Do not cut Verification or Responsible AI.

This is the same outline the Week 15 lecture shows. The Lab 15 dry run uses a 5-minute version of it.

---

## Speaking

- **Every team member speaks.** Divide by section, not by sentence. Practice the switches between speakers ("Now Maria will show what the data can't tell us").
- **Talk to the audience, not to the screen.** Use the slide as a picture, not a script.
- **Say the number and what it means:** "The mean absolute error is 4.8 MPa — about 13% of a typical 28-day strength — and the baseline's is 13 MPa."
- **Time yourselves.** Rehearse at least twice after the Week 15 dry run. Finish between 9:00 and 10:00; at 10:00 the moderator stops you.

## Slides

- **One main point per slide**, with a slide title that states the finding ("The model misses most cracks on bridge decks"), not just a topic ("Results").
- **Big text:** 18 pt or larger for body text; never smaller than 14 pt. No more than about 5 bullets.
- **Every chart:** a title, axis labels with units, readable tick labels. Do not rely on color alone — use labels, line styles, or markers too.
- **Numbers, not adjectives:** "recall 0.62 on the poor class," not "pretty good."
- **Alt text** on images in your uploaded file, and credit for any photo or figure you did not make.
- Show code only if it is the point of the slide, and then no more than ~10 lines.

## Questions (3–5 minutes)

- Any member may be asked about any part. Make sure everyone understands the whole project.
- It is fine to say "We did not test that — here is how we would." It is not fine to guess.
- Expect questions like:
  - "Why is that baseline a fair comparison?"
  - "What happens if you run this on data from Phoenix instead of Minnesota?"
  - "How do you know the answer key in your test set is right?"
  - "Who signs off on a decision made with this tool?"
  - "Which part did you use AI tools for, and how did you check it?"

## Common mistakes

- Too much time on background, too little on results and limits.
- Results without a baseline ("85% accuracy" — compared with what?).
- Accuracy on imbalanced data with no recall or confusion matrix.
- Charts with no units or unreadable axes.
- Claiming the tool is "ready to use" for design, inspection, or safety decisions.
- Reading from the slides.

## Logistics checklist

- [ ] Slides uploaded to Brightspace as PDF before the session.
- [ ] The file opens on the classroom computer (bring a USB copy too).
- [ ] Any demo is a **recording or screenshots** — live demos often fail in front of an audience.
- [ ] Each member knows their slides and the sentence that introduces the next speaker.
- [ ] Timed run between 9:00 and 10:00 (or 7:00–8:00 for 8-minute talks).
