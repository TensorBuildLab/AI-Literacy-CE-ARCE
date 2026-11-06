# All Readings and Videos

Each week's reading list in one place. Required items are short (≤ 45 minutes per week); optional items go deeper. All are free.

## Week 1 — [What AI Is (and Isn't)](../lectures/week01-what-is-ai/)

- **Elements of AI, Chapter 1 "What is AI?"** — <https://www.elementsofai.com/> (free; about 1 hour). It matches this week's definitions and the autonomy/adaptivity idea.
- **Google Colab: "Welcome to Colaboratory"** — <https://colab.research.google.com/> (10 minutes). Sign in with a Google account before the lab.

## Week 2 — [Zooming In: Machine Learning, Deep Learning, and Generative AI](../lectures/week02-ml-dl-genai/)

**Required (≈ 40 min total)**
- **Elements of AI, Chapter 4, Section I: "The types of machine learning"** — <https://course.elementsofai.com/4/1> (free; about 20 minutes). Supervised, unsupervised, and reinforcement learning, matching this week's lecture.
- **Google for Developers: "Introduction to Machine Learning"** — <https://developers.google.com/machine-learning/intro-to-ml> (about 20 minutes, Google's estimate). What ML is, the types of ML, and a short note on generative AI.

**Optional**
- **3Blue1Brown: "But what is a neural network?"** — <https://www.youtube.com/watch?v=aircAruvnKk> (video, about 19 minutes). The best visual preview of what "deep" means. We build on it in Week 5.
- **Google ML Crash Course: "Introduction to Large Language Models"** — <https://developers.google.com/machine-learning/crash-course/llm> (about 45 minutes). A preview of Week 7.

## Week 3 — [How Machines Learn, Part 1](../lectures/week03-how-machines-learn-1/)

**Required (≈ 45 min total)**
- **Google ML Crash Course: "Linear regression"** — <https://developers.google.com/machine-learning/crash-course/linear-regression> (whole module about 80 minutes). Read only the first page and the **Loss** page this week (about 30 minutes); save the Gradient descent and Hyperparameters pages for Week 4. Note: they call J the "loss."
- **Elements of AI, Chapter 4, Section III: "Regression"** — <https://course.elementsofai.com/4/3> (free; about 15 minutes). A gentle, non-coding take on fitting a line.

**Optional**
- **Course data README** — [`data/README.md`](../lectures/week03-how-machines-learn-1/../../data/README.md) (5 minutes). Where the concrete data come from and what each column means.

## Week 4 — [How Machines Learn, Part 2](../lectures/week04-how-machines-learn-2/)

**Required (≈ 45 min total)**
- **Google ML Crash Course: "Linear regression" — Gradient descent and Hyperparameters pages** — <https://developers.google.com/machine-learning/crash-course/linear-regression/gradient-descent> and <https://developers.google.com/machine-learning/crash-course/linear-regression/hyperparameters> (about 30 minutes together, with interactive exercises on the learning rate).
- **Google ML Crash Course: "Datasets, generalization, and overfitting"** — <https://developers.google.com/machine-learning/crash-course/overfitting> (whole module about 105 minutes). Read only "Dividing the original dataset" for this week (about 15 minutes).

**Optional**
- The "Overfitting" page of the same Google module (about 20 minutes).
- **3Blue1Brown: "Gradient descent, how neural networks learn"** — <https://www.youtube.com/watch?v=IHZwWFHWa-w> (video, about 21 minutes). The same idea applied to a neural network — a bridge to Week 5.
- **scikit-learn user guide: "Linear Models"** — <https://scikit-learn.org/stable/modules/linear_model.html> (reference; read the first section on ordinary least squares, about 10 minutes).

## Week 5 — [Neural Networks, Part 1](../lectures/week05-neural-networks-1/)

**Required (≈ 30 min total)**
- **3Blue1Brown: "But what is a neural network?" (Deep learning, chapter 1)** — <https://www.youtube.com/watch?v=aircAruvnKk> (video, about 19 minutes). Neurons, layers, weights, and biases, clearly animated. Watch before the lab.
- **TensorFlow Playground** — <https://playground.tensorflow.org> (about 10 minutes: try the spiral data with different numbers of layers and neurons).

**Optional**
- **3Blue1Brown: "Backpropagation, intuitively" (chapter 3)** — <https://www.youtube.com/watch?v=Ilg3gGewQ5U> (video, about 13 minutes). The "passing blame backward" idea in pictures; helpful for HW3.
- **Google ML Crash Course: "Neural networks" module** — <https://developers.google.com/machine-learning/crash-course/neural-networks> (about 1 hour, with interactive exercises on nodes, hidden layers, and activation functions).

## Week 6 — [Neural Networks, Part 2](../lectures/week06-neural-networks-2/)

**Required (≈ 40 min total)**
- **CNN Explainer (Georgia Tech Polo Club)** — <https://poloclub.github.io/cnn-explainer/> (interactive, about 15 minutes). Click through a small CNN and watch filters, ReLU, and pooling at work. Best preparation for Lab 06.
- **3Blue1Brown: "But what is a convolution?"** — <https://www.youtube.com/watch?v=KuXjwB4LzSA> (video, about 23 minutes). Convolution explained with pictures; the image-processing section (blurring and edge detection) matches this week.

**Optional**
- **Hugging Face Computer Vision Course, Unit 2 (Convolutional neural networks)** — <https://huggingface.co/learn/computer-vision-course> (deeper; about 1 hour for the CNN and transfer-learning pages).
- **Christopher Olah: "Understanding LSTM Networks"** — <https://colah.github.io/posts/2015-08-Understanding-LSTMs/> (about 20 minutes; read the first half for the "network with memory" idea — skip the equations if you like).

## Week 7 — [Generative AI, Part 1](../lectures/week07-generative-ai-1/)

**Required (≈ 8 min total)** — it is midterm week and HW3 is open, so only one short item is required:

- **3Blue1Brown — [Large Language Models explained briefly](https://www.youtube.com/watch?v=LPZh9BOjkQs)** (≈ 8 min). The whole lecture in one short video.

**Optional** (good for HW4, or for the week after the exam):

- **3Blue1Brown — [Transformers, the tech behind LLMs (Deep Learning Ch. 5)](https://www.youtube.com/watch?v=wjZofJX0v4M)** and **[Attention in transformers (Ch. 6)](https://www.youtube.com/watch?v=eMlx5fFNoYc)** (≈ 27 min each). Visual intuition for embeddings, attention, and temperature.
- **Jay Alammar — [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)** (≈ 30 min read). Step-by-step diagrams; skim the matrix parts if they get heavy.
- **[Transformer Explainer](https://poloclub.github.io/transformer-explainer/)** (interactive, 10–15 min). Runs a small GPT-2 in your browser: type a prompt and watch the next-token probabilities change with temperature.

## Week 8 — [Generative AI, Part 2](../lectures/week08-generative-ai-2/)

**Required (≈ 30 min total)** — HW3 is due this week, so the list is short:

- **DAIR.AI Prompt Engineering Guide — [Introduction](https://www.promptingguide.ai/introduction)** and **[Few-shot prompting](https://www.promptingguide.ai/techniques/fewshot)** (≈ 20 min). Free, vendor-neutral.
- **DAIR.AI — [Retrieval Augmented Generation (RAG)](https://www.promptingguide.ai/techniques/rag)** (≈ 10 min). A short overview of the pipeline you build in Lab 08.

**Optional:**

- **3Blue1Brown — [Transformers (Deep Learning Ch. 5)](https://www.youtube.com/watch?v=wjZofJX0v4M)** and **[Attention in transformers (Ch. 6)](https://www.youtube.com/watch?v=eMlx5fFNoYc)** (≈ 27 min each). Last week's ideas, visually; helpful for HW4.
- **Jay Alammar — [The Illustrated Stable Diffusion](https://jalammar.github.io/illustrated-stable-diffusion/)** (≈ 30 min read). How diffusion image models work, with diagrams.
- **NIST AI 600-1 — [Generative AI Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)** (2024; skim the list of risks, ≈ 20 min). How the U.S. standards agency describes GenAI risks such as "confabulation" (hallucination); useful for Weeks 13–14.

## Week 10 — [AI Agents](../lectures/week10-ai-agents/)

### Required (≈ 35 min total)
- **"Building effective agents" (Anthropic, 2024)** — <https://www.anthropic.com/engineering/building-effective-agents> (about 20 minutes). A practical argument for starting with simple workflows and adding agent autonomy only when it is needed.
- **OWASP Top 10 for LLM Applications — Prompt Injection** — <https://genai.owasp.org/llmrisk/llm01-prompt-injection/> (about 15 minutes). Real attack patterns and defenses.

### Optional
- **Hugging Face Agents Course, Unit 1 "Introduction to Agents"** — <https://huggingface.co/learn/agents-course/unit1/introduction> (free; about 1 hour). Tools, the thought–action–observation loop, and how LLMs call tools. Good extra preparation for the lab.
- **ReAct paper (Yao et al., 2022)** — <https://arxiv.org/abs/2210.03629> (10 minutes for the abstract and Figure 1). The original "reason + act" idea.

## Week 11 — [AI Across Civil and Architectural Engineering](../lectures/week11-ai-across-ce-arce/)

### Required (≈ 35 min total)
- **This week's slides 10 and 12 (geotechnical and water examples)** — in the [PDF](../lectures/week11-ai-across-ce-arce/Week11_AI-Across-CE-ARCE.pdf) (about 5 minutes). Read them **before class**: we cover them only briefly, and the jigsaw activity builds on them.
- **Google Machine Learning Crash Course — "Accuracy, recall, precision, and related metrics"** — <https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall> (about 20 minutes). The metrics you will use in Lab 11.
- **FHWA National Bridge Inventory** — <https://www.fhwa.dot.gov/bridge/nbi.cfm> (about 10 minutes). Where our Arizona data comes from; browse the "condition" tables to see how states compare.

### Optional
- **National Academies (2024), *Foundational Research Gaps and Future Directions for Digital Twins*** — <https://nap.nationalacademies.org/catalog/26894> (free PDF; read the Summary, about 20 minutes). A careful definition of digital twins and what they need.
- **Raissi, Perdikaris & Karniadakis (2019), "Physics-informed neural networks"** — <https://doi.org/10.1016/j.jcp.2018.10.045> (skim the introduction). The paper that popularized physics-informed ML.

## Week 12 — [AI Tools for Engineers](../lectures/week12-ai-tools/)

### Required (≈ 37 min total)

- **OSHA excavation rules, 29 CFR 1926 Subpart P (eCFR)** — <https://www.ecfr.gov/current/title-29/subtitle-B/chapter-XVII/part-1926/subpart-P>. Open Appendix B and find Table B‑1 (maximum allowable slopes). 5 minutes. This is what "go to the primary source" looks like.
- **Python documentation: the `assert` statement** — <https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement>. 2 minutes; you will use `assert` in Lab 12.
- **Course AI-use guide** — [resources/ai-use-guide.md](../lectures/week12-ai-tools/../../resources/ai-use-guide.md). The acknowledgment template and the 5 checks. 10 minutes.
- **NIST AI 600-1, Generative AI Profile (2024)** — <https://doi.org/10.6028/NIST.AI.600-1>. Skim Section 2, its list of 12 risks of generative AI (confabulation, data privacy, information security, intellectual property, and more). About 20 minutes; it previews Week 13.

### Optional

- **U.S. Copyright Office: Copyright and Artificial Intelligence** — <https://www.copyright.gov/ai/>. Skim the overview of current U.S. guidance on AI-assisted work. About 10 minutes. Guidance changes — note the date of what you read.

## Week 13 — [Responsible AI](../lectures/week13-responsible-ai/)

### Required (≈ 45 min total)

- **NIST AI Risk Management Framework** — <https://www.nist.gov/itl/ai-risk-management-framework>. Overview page with links to AI RMF 1.0 and the Generative AI Profile (NIST AI 600-1, July 2024). Skim the four functions; about 20 minutes. NIST updates its guidance — check for the current version.
- **Mitchell et al., "Model Cards for Model Reporting" (2019)** — <https://arxiv.org/abs/1810.03993>. Read the list of model-card sections and one example card; about 15 minutes. You will write a model card in Lab 13.
- **scikit-learn: Permutation feature importance** — <https://scikit-learn.org/stable/modules/permutation_importance.html>. How the importance tool in Lab 13 works, including its caution about correlated features; about 10 minutes.

### Optional

- **Google Machine Learning Crash Course: Fairness** — <https://developers.google.com/machine-learning/crash-course/fairness>. Types of bias and how to evaluate for them; about 1 hour with exercises.
- **LBNL 2024 United States Data Center Energy Usage Report** — <https://eta-publications.lbl.gov/publications/2024-lbnl-data-center-energy-usage-report>. Source of the U.S. data-center electricity and water estimates; read the executive summary (15 minutes).

## Week 14 — [AI Policy, Ethics, and Professional Practice](../lectures/week14-ai-policy-ethics/)

**Required (≈ 35 min total)**

- **Appendix slides A1–A3** at the end of this week's slide deck — about 10 minutes. Read these before the lecture day.
- **EU AI Act — High-level summary** (artificialintelligenceact.eu): <https://artificialintelligenceact.eu/high-level-summary/> — about 15 minutes.
- **NSPE Code of Ethics for Engineers**: <https://www.nspe.org/career-growth/nspe-code-ethics-engineers> — read the Fundamental Canons and skim Section II (about 10 minutes).

**Optional**

- [ASCE Code of Ethics](https://www.asce.org/career-growth/ethics/code-of-ethics) and [ASCE Policy Statement 573, AI and Engineering Responsibility](https://www.asce.org/advocacy/policy-statements/ps573---artificial-intelligence-and-engineering-responsibility) — about 10 minutes together.
- Arizona Rules of Professional Conduct, A.A.C. R4-30-301 (Cornell LII copy): <https://www.law.cornell.edu/regulations/arizona/Ariz-Admin-Code-SS-R4-30-301>. Item 16 is the sealing rule. The official text is on the Arizona Board of Technical Registration website (btr.az.gov).
- NIST AI Risk Management Framework: <https://www.nist.gov/itl/ai-risk-management-framework> — skim the overview (helps with HW5 Part C).
- EU AI Act, Annex III (the eight high-risk areas): <https://artificialintelligenceact.eu/annex/3/>
- U.S. Copyright Office, Copyright and Artificial Intelligence: <https://www.copyright.gov/ai/> (Part 2 covers copyrightability).
- University of Arizona student AI guidelines: <https://artificialintelligence.arizona.edu/students/student-guidelines-principles>
- "The Hyatt Regency Disaster Revisited," STRUCTURE magazine: <https://www.structuremag.org/article/the-hyatt-regency-disaster-revisited/>

## Week 15 — [Synthesis: The Big Picture, Revisited](../lectures/week15-synthesis/)

**Required (≈ 40 min total)**

- **Final presentation guide** and the **presentation rubric** in the [project folder](../lectures/week15-synthesis/../../project/) — about 15 minutes. Bring questions to the lab day.
- **Elements of AI** (University of Helsinki and MinnaLearn), <https://www.elementsofai.com/> — read the text of Chapter 6, "Implications" (about 25 minutes; the exercises are optional). It is a good wrap-up for this course.

**Optional (after the course)**

- **Google Machine Learning Crash Course**, <https://developers.google.com/machine-learning/crash-course> — free; the regression, classification, and fairness modules review Weeks 3–4 and 13 (about 1–2 hours).
- **Hugging Face Learn**, <https://huggingface.co/learn> — free courses on LLMs and agents if you want to go deeper into Weeks 7–10 (self-paced, several hours).
- **3Blue1Brown — Neural networks** (YouTube series), <https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi> — visual explanations of gradient descent, backpropagation, and transformers (each video 10–30 minutes).
- [Kaggle Learn](https://www.kaggle.com/learn) (short hands-on Python, pandas, and ML lessons) and [fast.ai Practical Deep Learning](https://course.fast.ai/) (for those who want to build models seriously).
