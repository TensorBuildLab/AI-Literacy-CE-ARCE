# Week 6 — Neural Networks, Part 2: Seeing and Remembering — CNNs and Sequence Models

**Slides:** [PDF](Week06_Neural-Networks-2.pdf) · [PowerPoint](Week06_Neural-Networks-2.pptx) · **Lab:** [Lab 06 — Crack Detection with a CNN](../../labs/lab06-cnn-crack-detection/) · **Homework:** [HW3 — Neural Networks on Engineering Data](../../homework/hw3-neural-networks/) (out this week, due end of Week 8)

## Learning objectives
By the end of this week you can:
1. Explain why a network's architecture is a set of built-in assumptions about the data.
2. Describe how convolution, pooling, and stacked layers let a convolutional neural network (CNN) find cracks in photos.
3. Explain transfer learning and why it suits small engineering datasets.
4. Turn a time series into training examples with a sliding window, and say what a recurrent network (RNN or LSTM) adds.
5. Choose a suitable architecture — MLP, CNN, RNN/LSTM, or transformer — for a CE/ARCE task.

## The big ideas
- **Architecture = built-in assumptions.** All networks train the same way (loss + backpropagation + gradient descent); what differs is the wiring. An MLP assumes nothing about the order of its inputs; a CNN assumes nearby pixels belong together; a recurrent network assumes order matters; a transformer lets anything relate to anything. Good assumptions mean less data is needed — like choosing the right structural system.
- **Images are grids of numbers.** A 227 × 227 color photo is 3 grids (red, green, blue) = 154,587 numbers, each a brightness from 0 to 255. Feeding them all to one MLP layer of 1,000 neurons would take about 155 million weights.
- **Convolution** slides a small filter (e.g., 3 × 3 weights) across the image; at each position it multiplies and adds, producing a **feature map** that shows where a pattern appears. An edge filter lights up both edges of a crack and barely responds to intact concrete (except at pores). The sign of the output tells the direction of the change (with the Lab 06 Sobel filter, negative = bright → dark from left to right); the size tells the edge strength. The same filter is reused everywhere (**weight sharing**), so a 3 × 3 color filter has only 27 weights + 1 bias. In a CNN, the filter weights are **learned**.
- **Pooling** (e.g., 2 × 2 max pooling) shrinks each feature map by keeping the strongest value in each block. A **CNN stack** repeats convolution + ReLU + pooling, then flattens the maps into a small MLP that outputs, for example, P(crack). Layers learn a ladder: **edges → textures → parts** (real ResNet-18 first-layer filters are edge and color-blob detectors).
- **Transfer learning:** reuse a network pretrained on millions of photos (ResNet-18 was trained on ImageNet, about 1.28 million photos in 1,000 categories, and has about 11.7 million weights). Remove its 1,000-category output layer, freeze the remaining 11.2 million weights, use it to turn each photo into 512 features, and train only a small classifier head (logistic regression: 512 weights + 1 bias) on your few hundred or thousand photos. That is exactly Lab 06 (600 photos on a CPU; all 1,200 on a GPU).
- **Vision in CE/ARCE:** crack and spall detection, post-disaster damage assessment from aerial images, construction-site safety (hard hats and vests), land use and impervious area from satellites, pavement condition surveys. Tasks are **classification** (one label per photo), **object detection** (boxes), or **segmentation** (a label per pixel). A model trained on one campus's walls may fail on sunlit, stained Arizona bridge decks: test on local data first.
- **Reading a confusion matrix.** A classifier's test results fall into four boxes: true positives (TP, cracks caught), false negatives (FN, cracks missed), false positives (FP, false alarms), and true negatives (TN). **Accuracy** = (TP + TN) / all. **Precision** = TP / (TP + FP): of the photos flagged "crack", how many really are. **Recall** = TP / (TP + FN): of the real cracks, how many were caught. For safety screening, **recall matters most** — a missed crack can hide damage, while a false alarm costs a second look. Lowering the decision threshold (e.g., flag when P(crack) > 0.3 instead of 0.5) raises recall but adds false alarms.
- **Sequences:** in time series the order carries information. I-94 traffic shows two weekday rush hours (about 6,500 vehicles/h at the peaks) and a single weekend hump. A **sliding window** turns a series into training rows (e.g., the past 24 hours → the next hour); always test on later dates than you train on, and beat a simple **baseline** (the simplest sensible forecast) such as "same hour last week." A **recurrent network (RNN)** reads one step at a time and carries a **hidden state** (memory); an **LSTM** adds gates that decide what to keep and forget. Uses: traffic, building load, and river-flow forecasting.
- **Attention** lets each element of a sequence score every other element and mix in the most relevant ones ("The truck crossed the bridge because **it** was open" — *it* = the bridge). **Transformers** stack attention layers and small MLPs; they power large language models (Week 7). The slide's example uses two-way attention ("it" also looks ahead to "open"), as in BERT-style encoders; ChatGPT-style models only look back at earlier words.

| Architecture | Data it suits | Built-in idea | CE/ARCE example |
|---|---|---|---|
| MLP | Tables of numbers | Every input can combine with every other | Heating load from building geometry; concrete strength from a mix |
| CNN | Images, grids, maps | Local patterns, same filter everywhere | Crack detection; hard hats on site; land use from satellites |
| RNN / LSTM | Time series, sequences | Read in order, carry a memory | Next-hour traffic; tomorrow's building load; river flow |
| Transformer | Text, long sequences (also images) | Attention: anything can relate to anything | Searching specs and codes; engineering assistants |

## Key terms
| Term | Plain-language meaning |
|---|---|
| Architecture | How a network's neurons are wired — which encodes assumptions about the data |
| Pixel | One cell of an image grid; a brightness from 0 (black) to 255 (white) per color channel |
| Convolution | Sliding a small grid of weights (a filter) over an image, multiplying and adding at each position |
| Filter (kernel) | The small grid of weights used in convolution, e.g., 3 × 3 |
| Feature map | The output of one filter: a map of where its pattern appears |
| Weight sharing | Reusing the same filter weights at every position in the image |
| Pooling | Shrinking a feature map, e.g., keeping the maximum of each 2 × 2 block |
| CNN | Convolutional neural network: stacked convolution and pooling layers plus a small classifier |
| Transfer learning | Reusing a network pretrained on a large dataset and training only a small new part |
| Pretrained / frozen | Already trained on another task / not updated during your training |
| Classification / detection / segmentation | One label per image / boxes around objects / a label for every pixel |
| Confusion matrix | A 2 × 2 table counting true positives, false negatives, false positives, and true negatives on a test set |
| Precision | TP / (TP + FP): of the items the model flagged, the share that really are positive (how trustworthy an alarm is) |
| Recall | TP / (TP + FN): of the real positives, the share the model caught (how few cracks are missed) |
| Baseline | The simplest sensible model or rule, e.g., "same hour last week"; a new model must beat it |
| Time series | Measurements in time order, e.g., hourly traffic volume |
| Sliding window | Using the last k values as inputs to predict the next value, then shifting by one step |
| RNN / LSTM | Recurrent network that reads a sequence step by step with a memory; LSTM adds gates for longer memory |
| Attention / transformer | Each element weighs every other element; transformers are stacks of attention layers |

## Read / watch
**Required (≈ 40 min total)**
- **CNN Explainer (Georgia Tech Polo Club)** — <https://poloclub.github.io/cnn-explainer/> (interactive, about 15 minutes). Click through a small CNN and watch filters, ReLU, and pooling at work. Best preparation for Lab 06.
- **3Blue1Brown: "But what is a convolution?"** — <https://www.youtube.com/watch?v=KuXjwB4LzSA> (video, about 23 minutes). Convolution explained with pictures; the image-processing section (blurring and edge detection) matches this week.

**Optional**
- **Hugging Face Computer Vision Course, Unit 2 (Convolutional neural networks)** — <https://huggingface.co/learn/computer-vision-course> (deeper; about 1 hour for the CNN and transfer-learning pages).
- **Christopher Olah: "Understanding LSTM Networks"** — <https://colah.github.io/posts/2015-08-Understanding-LSTMs/> (about 20 minutes; read the first half for the "network with memory" idea — skip the equations if you like).

## Check yourself
1. The Sobel vertical-edge filter from Lab 06 has rows [−1, 0, 1], [−2, 0, 2], [−1, 0, 1]. It sits on a patch whose rows are all [9, 9, 1]. What value does it produce, and what does a large negative value mean?
   <details><summary>Answer</summary>Rows: (−9 + 0 + 1) = −8, 2 × (−9 + 0 + 1) = −16, and −8; total −32. A large negative value means brightness drops from left to right — a bright-to-dark edge, like the left edge of a dark crack. The sign tells the direction of the change; the size tells the edge strength.</details>
2. Why does a CNN need far fewer weights than an MLP for the same 227 × 227 photo?
   <details><summary>Answer</summary>Weight sharing: a CNN reuses the same small filter (e.g., 3 × 3 × 3 = 27 weights + 1 bias) at every position, while an MLP needs one weight per pixel value per neuron — about 155 million for one layer of 1,000 neurons.</details>
3. Explain transfer learning as used in Lab 06, and why it works with only a few hundred photos.
   <details><summary>Answer</summary>We take ResNet-18, pretrained on about 1.28 million ImageNet photos, remove its last layer, and keep its remaining 11.2 million weights frozen. Each crack photo goes through it and comes out as 512 features describing edges and textures. Only a small logistic-regression head (513 parameters) is trained. It works with little data because the general visual features were already learned from millions of images.</details>
4. You have three years of hourly building electricity data. How would you set up training examples to forecast the next hour, and how should you split train and test data?
   <details><summary>Answer</summary>Use a sliding window: each row has, for example, the previous 24 hourly loads (plus weather and time of day) as inputs and the next hour's load as the target. Split by time — train on earlier months, test on later ones — so the model never sees the future. Compare with a baseline such as "same hour last week."</details>
5. Match each task to an architecture: (a) spalling in drone photos, (b) tomorrow's hourly chiller load, (c) heating load from 8 building-geometry numbers, (d) answering questions about a long specification.
   <details><summary>Answer</summary>(a) CNN; (b) sequence model — RNN/LSTM or transformer (or an MLP on sliding windows); (c) MLP (or even a simpler model); (d) transformer (a large language model, ideally with retrieval — Week 8).</details>
6. A drone survey of a bridge deck has 50 photos that really show cracks. The model flags 40 photos as "crack", and 30 of those are real cracks. What are the precision and recall? Which number should worry the bridge owner, and why?
   <details><summary>Answer</summary>TP = 30, FP = 40 − 30 = 10, FN = 50 − 30 = 20. Precision = 30/40 = 75%; recall = 30/50 = 60%. Recall is the worry: 20 real cracks were missed, and a missed crack can hide damage, while a false alarm only costs an inspector a second look. Lowering the threshold would catch more cracks at the cost of more false alarms.</details>

## Coming up
- **Lab 06 (this week's lab day):** view crack photos as numbers, apply hand-made edge filters, then transfer learning with ResNet-18 features + a logistic-regression head; confusion matrix, accuracy, precision, and recall, and the mistakes; then a short **required** part: next-hour I-94 traffic forecasting with a sliding window. Model downloads happen on Google's computers, not on your laptop or phone data plan. The lab ends with an **exit ticket**: 3 short questions you answer alone, without AI (AI-Free), during the last 10 minutes of lab. **Due:** Sunday 11:59 pm (Arizona time) of this week, on Brightspace.
- **HW3 — Neural Networks on Engineering Data** is posted: Part A (forward pass and parameter count by hand) is AI-Free; the other parts are AI-Assisted. **Due end of Week 8, Sunday 11:59 pm** on Brightspace.
- **Next week:** Generative AI, Part 1 — how large language models work (lecture day). **The lab day is the midterm exam** on Weeks 1–6 (closed book, formula sheet provided, calculator allowed) — see the [practice midterm](../../exams/). The quiz on this week is given at the start of the Week 7 lecture day — good practice for the midterm.
