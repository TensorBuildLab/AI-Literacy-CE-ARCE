# Week 1 — What AI Is (and Isn't)

**Slides:** [PDF](Week01_What-AI-Is-and-Isnt.pdf) · [PowerPoint](Week01_What-AI-Is-and-Isnt.pptx) · **Lab:** [Lab 01 — Python On-Ramp](../../labs/lab01-python-onramp/)

## Learning objectives
By the end of this week you can:
1. Describe three ways AI is already used in civil and architectural engineering.
2. Explain why "AI" has no single agreed definition, and use **autonomy + adaptivity** as a working lens.
3. Decide whether a system is AI, not AI, or "kind of" AI — and explain why.
4. Draw the big-picture map: AI ⊃ machine learning ⊃ deep learning ⊃ generative AI, plus the other branches of AI.
5. Explain how this course works: lecture days, lab days, homework, the project, grading, and the three AI-use labels.

## The big ideas
- AI already shows up across the life cycle of infrastructure and buildings: finding cracks in inspection photos, forecasting and controlling building energy use, and perceiving the road in self-driving vehicles.
- Definitions of AI differ (McCarthy, Russell & Norvig, the dictionary, the European Commission), but they share ideas: sensing the environment, making decisions or taking actions, pursuing goals, and some independence.
- A practical lens: **autonomy** (doing tasks without constant guidance) and **adaptivity** (improving from experience). The more of both, the more "AI-like" a system is. AI is a matter of degree — "a pinch of AI."
- Talk precisely: say "an AI method" or "an AI system," and say what it learned from and what it does.
- **Machine learning** is the part of AI where systems learn patterns from data; **deep learning** uses many-layered neural networks; **generative AI** creates new text, images, or code. AI also includes search and planning, logic and rules, optimization, and robotics.
- AI has gone through cycles of hype and disappointment. Engineers should be skeptical of both hype and dismissal.
- AI literacy for engineers = understand how it works, use it well, **verify** it, and use it responsibly. A licensed engineer stays responsible for the work, whatever tools were used.

## Key terms
| Term | Plain-language meaning |
|---|---|
| Artificial intelligence (AI) | The field of making computer systems that perform tasks we associate with intelligence, such as perceiving, deciding, and learning |
| Autonomy | Doing a task in a complex environment without constant guidance from a person |
| Adaptivity | Getting better at a task by learning from experience or data |
| Machine learning (ML) | AI methods that learn patterns from data instead of following hand-written rules |
| Deep learning (DL) | Machine learning with neural networks that have many layers |
| Generative AI (GenAI) | Deep learning models that create new content (text, images, code) |
| Search and planning | AI methods that look through possible actions to reach a goal, e.g., route finding |
| AI-use labels | This course's rules for each assignment: AI-Free, AI-Assisted, or AI-Required |

## Read / watch
- **Elements of AI, Chapter 1 "What is AI?"** — <https://www.elementsofai.com/> (free; about 1 hour). It matches this week's definitions and the autonomy/adaptivity idea.
- **Google Colab: "Welcome to Colaboratory"** — <https://colab.research.google.com/> (10 minutes). Sign in with a Google account before the lab.

## Check yourself
1. Give one example of AI in civil engineering and one in architectural engineering.
   <details><summary>Answer</summary>Examples: crack detection in bridge or pavement photos (CE); building energy forecasting or HVAC fault detection (ARCE). Many others are fine.</details>
2. What do the words *autonomy* and *adaptivity* mean?
   <details><summary>Answer</summary>Autonomy: performing tasks in complex environments without constant guidance by a user. Adaptivity: improving performance by learning from experience.</details>
3. Is a spreadsheet that adds up member weights to get total structural load AI? Why or why not?
   <details><summary>Answer</summary>No. It follows fixed formulas — it neither learns nor acts on its own.</details>
4. Why is it better to say "an AI method" than "an AI"?
   <details><summary>Answer</summary>AI is a field (like biology), not a single object. Naming the method — what it learned from and what it does — makes it possible to ask the right questions about how reliable it is.</details>
5. Put these in order from broadest to narrowest: deep learning, artificial intelligence, generative AI, machine learning.
   <details><summary>Answer</summary>Artificial intelligence ⊃ machine learning ⊃ deep learning ⊃ generative AI.</details>

## Coming up
- **Lab 01 (this week's lab day):** open Google Colab, learn just enough Python, and run a vision model and a small language model. Bring a charged laptop.
- **Next week:** zoom into machine learning, deep learning, and generative AI. Short quiz on this week at the start of class. Homework 1 is assigned.
