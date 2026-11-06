# Using AI in This Course — A Practical Guide

This is a course about AI, so you will use AI tools — sometimes because you must, sometimes because it helps, and sometimes not at all. This page explains the rules and how to use AI well. The official policy is in the [syllabus](../syllabus/README.md#use-of-generative-ai-sometimes-permitted-by-assignment-label).

## The three labels
Every lab, homework part, quiz, and project milestone shows one label.

| Label | What it means | Typical examples |
|---|---|---|
| ✕ **AI-Free** | Do not use AI tools to produce what you submit. (You may use AI earlier to study the ideas.) | Quizzes, the midterm, lab exit tickets, homework parts done by hand |
| ~ **AI-Assisted** | AI help is allowed — explanations, debugging, brainstorming, feedback on your writing. Add an acknowledgment. You own every line. | All lab work (including Labs 08 and 12, where the lab's own code runs a small model), most homework, the final project |
| ✓ **AI-Required** | Using an AI model *is* the task. Follow the instructions and record prompts and outputs. | HW4 (testing an LLM's answers); the model-testing parts of Assist and Evaluate projects |

The symbol is always written next to the label's name, so the meaning never depends on color.

**Never allowed:** submitting AI output as your own without acknowledgment; using AI in place of participating in class activities; pasting exam content, other students' work, private information, or confidential data into AI tools.

## Writing the acknowledgment
Put it at the end of the notebook (every lab has a cell for it) or the end of your report:

> I acknowledge the use of **[tool and version, e.g., Gemini in Colab / ChatGPT / Copilot]** to **[specific use, e.g., explain a pandas error message and suggest a fix for my groupby code]**. Prompts I used included **[paste or summarize]**. I checked the output by **[how I verified it]**. I am responsible for this work.

If you used no AI tools, write: *"I did not use AI tools for this assignment."* This is the **only** template used in this course — every notebook, homework, and project uses it.

**What it's worth:** on homework, a missing acknowledgment on AI-Assisted or AI-Required work costs **5 points (of 100)**. In labs, the statement is part of completing the notebook. Undisclosed AI use on AI-Free work is an academic-integrity issue.

See also the UA Libraries guide [Citing generative AI](https://libguides.library.arizona.edu/students-chatgpt/citing).

## Good uses vs. poor uses (AI-Assisted work)
| ✅ Good | ❌ Poor |
|---|---|
| "Explain what this error means: `KeyError: 'strength'`" | "Write the whole lab for me" |
| "Why does a lower water–cement ratio make concrete stronger?" — then check a textbook | Copying an AI's numbers into a report without checking them |
| "Here is my paragraph; what is unclear?" | Letting AI write your reflection — reflections are about *your* thinking |
| Asking for three different ways to plot the data, then choosing one you understand | Running code you don't understand and can't explain |

A useful test: **could you explain and defend every line to your instructor without the AI?** If not, keep working.

## The 5-check verification workflow
AI tools can be fluent and wrong. Before you use an AI answer in engineering work, run these five checks (you'll practice them in Week 12 and Lab 12):

1. **Restate** — restate the problem, the inputs, and the assumptions. Did the AI answer the question you actually asked?
2. **Units & magnitude** — are the units consistent? Is the size of the answer reasonable (e.g., a beam moment of 54 kN·m, not 54,000)?
3. **Independent check** — check with a hand calculation, a quick Python script, or a different method.
4. **Sources** — if it cites a code section, standard, or paper, confirm that it exists and actually says that.
5. **Test & document** — test AI-written code on cases with known answers (`assert`), and document how you used AI.

## Staying AI-Free inside Colab
Colab can suggest code as you type (AI-powered completions). For AI-Free work (exit tickets, AI-Free homework parts), turn this off: in Colab open **Tools → Settings → AI assistance** and switch off the AI-powered inline completions (and hide generative-AI features if that option is shown). Menu names change from time to time — if you can't find the setting, ask. Ordinary auto-complete of variable names is fine.

## Privacy and confidentiality
- Free public AI tools may keep and learn from what you type. **Do not paste** personal information, other people's work, exam or quiz content, or any client/employer data.
- In internships and jobs, follow your employer's AI policy. Many firms restrict which tools may see project data.
- Most labs use **open models that run inside your own Colab session**, so your prompts go to that model rather than to a commercial chatbot service. (Optional cells that use Colab's built-in Gemini do send prompts to Google.)

## Questions?
If you're unsure whether a use is allowed, ask **before** you submit. Honest questions are always welcome; undisclosed misuse is an academic-integrity issue.
