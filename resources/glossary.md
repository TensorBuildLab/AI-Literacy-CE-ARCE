# Course Glossary

Every key term from the weekly lecture pages, in alphabetical order. The week link shows where the term is introduced — open it for examples and self-check questions.

| Term | Plain-language meaning | Week |
|---|---|---|
| **Abrams' law** | The 1918 finding that concrete strength falls roughly exponentially as the w/c ratio rises | [W3](../lectures/week03-how-machines-learn-1/) |
| **Action stamp** | The EOR's response on a reviewed submittal, typically: No exceptions taken · Make corrections noted · Revise and resubmit · Rejected | [W14](../lectures/week14-ai-policy-ethics/) |
| **Activation function** | The "bend" applied to a neuron's weighted sum (ReLU, sigmoid, tanh) | [W5](../lectures/week05-neural-networks-1/) |
| **Adaptivity** | Getting better at a task by learning from experience or data | [W1](../lectures/week01-what-is-ai/) |
| **Adversarial example** | An input changed slightly and deliberately to make a model fail | [W13](../lectures/week13-responsible-ai/) |
| **Agent loop** | Repeat *observe → think → act → observe* until done or a limit is reached | [W10](../lectures/week10-ai-agents/) |
| **AI agent** | A system that uses a model to choose actions toward a goal, takes them through tools, and uses the results to decide what to do next | [W10](../lectures/week10-ai-agents/) |
| **AI-use acknowledgment** | A short statement of which AI tool you used, for what, and how you verified the result | [W12](../lectures/week12-ai-tools/) |
| **AI-use labels** | This course's rules for each assignment: AI-Free, AI-Assisted, or AI-Required | [W1](../lectures/week01-what-is-ai/) |
| **AI-use policy** | An organization's rules for which AI tools may be used, with what data, how output is checked, and who is accountable | [W14](../lectures/week14-ai-policy-ethics/) |
| **AI-use statement** | A short, specific note saying which AI tools you used, for what, and how you checked their output | [W15](../lectures/week15-synthesis/) |
| **Anomaly detection** | Flagging examples that do not look like normal behavior | [W2](../lectures/week02-ml-dl-genai/) |
| **Architecture** | How a network's neurons are wired — which encodes assumptions about the data | [W6](../lectures/week06-neural-networks-2/) |
| **Artificial intelligence (AI)** | The field of making computer systems that perform tasks we associate with intelligence, such as perceiving, deciding, and learning | [W1](../lectures/week01-what-is-ai/) |
| **`assert`** | A Python statement that stops the program with an error if a condition is false — the simplest test | [W12](../lectures/week12-ai-tools/) |
| **Asset life cycle** | The phases of a bridge, building, or network: plan, design, build, operate, maintain, renew | [W11](../lectures/week11-ai-across-ce-arce/) |
| **Attention** | A step where each token scores the earlier tokens and blends in information from the relevant ones | [W7](../lectures/week07-generative-ai-1/) |
| **Attention / transformer** | Each element weighs every other element; transformers are stacks of attention layers | [W6](../lectures/week06-neural-networks-2/) |
| **Automation bias** | Over-trusting an automated tool and not looking for what it missed | [W13](../lectures/week13-responsible-ai/) |
| **Autonomy** | Doing a task in a complex environment without constant guidance from a person | [W1](../lectures/week01-what-is-ai/) |
| **Backpropagation** | Computing every weight's slope ∂J/∂w by passing the error backward with the chain rule | [W5](../lectures/week05-neural-networks-1/) |
| **Baseline** | The simplest reference model a real model must beat — here, always predicting the average strength of the training mixes | [W4](../lectures/week04-how-machines-learn-2/) |
| **Batch** | A small group of examples used for one gradient-descent update | [W5](../lectures/week05-neural-networks-1/) |
| **Bias (in data or models)** | Systematic error — consistently worse for some places, groups, or asset types | [W13](../lectures/week13-responsible-ai/) |
| **BIM** | Building Information Modeling: a digital 3-D model of a building with data about its parts | [W15](../lectures/week15-synthesis/) |
| **BIM (building information model)** | A 3-D model of a building whose objects carry data such as type, size, and fire rating | [W10](../lectures/week10-ai-agents/) |
| **Calibration** | Whether predicted probabilities match how often things actually happen | [W13](../lectures/week13-responsible-ai/) |
| **Chunk** | A short passage cut from a longer document so it can be searched and pasted into a prompt | [W8](../lectures/week08-generative-ai-2/) |
| **Classification** | Supervised learning that predicts a category (crack / no crack) | [W2](../lectures/week02-ml-dl-genai/) |
| **Classification / detection / segmentation** | One label per image / boxes around objects / a label for every pixel | [W6](../lectures/week06-neural-networks-2/) |
| **Class imbalance** | One class (e.g., poor decks) is much rarer than the other | [W11](../lectures/week11-ai-across-ce-arce/) |
| **Clustering** | Grouping similar examples without being told the groups | [W2](../lectures/week02-ml-dl-genai/) |
| **CNN** | Convolutional neural network: stacked convolution and pooling layers plus a small classifier | [W6](../lectures/week06-neural-networks-2/) |
| **Code of ethics** | A professional society's written duties (NSPE, ASCE). It governs membership. Your license is governed by your state board's rules, which cover many of the same duties | [W14](../lectures/week14-ai-policy-ethics/) |
| **Coding assistant** | An AI tool that writes, explains, or debugs code, usually inside an editor or notebook | [W12](../lectures/week12-ai-tools/) |
| **Confusion matrix** | A 2 × 2 table counting true positives, false negatives, false positives, and true negatives on a test set | [W6](../lectures/week06-neural-networks-2/) |
| **Context window** | The maximum number of tokens the model can consider at once (prompt + documents + answer) | [W7](../lectures/week07-generative-ai-1/) |
| **Convergence** | When the cost stops going down noticeably | [W4](../lectures/week04-how-machines-learn-2/) |
| **Convolution** | Sliding a small grid of weights (a filter) over an image, multiplying and adding at each position | [W6](../lectures/week06-neural-networks-2/) |
| **Cosine similarity** | A score from 0 to 1 (for these vectors) of how closely two vectors point the same way; used to rank chunks | [W8](../lectures/week08-generative-ai-2/) |
| **Cost bowl / contour map** | Plots of J over the parameters; the lowest point is the best fit | [W3](../lectures/week03-how-machines-learn-1/) |
| **Cost function J(w, b)** | One number that scores how badly a model fits: here, half the average squared error | [W3](../lectures/week03-how-machines-learn-1/) |
| **Critical infrastructure** | Systems society depends on: roads and traffic, water, gas, heating, electricity, digital networks | [W14](../lectures/week14-ai-policy-ethics/) |
| **Data classification** | Sorting data into levels that decide which tools may see it. This course uses Public / Internal / Confidential (client) / Restricted (personal & security-sensitive) | [W12](../lectures/week12-ai-tools/) |
| **Deep learning** | Machine learning with many-layered neural networks that learn their own features | [W2](../lectures/week02-ml-dl-genai/) |
| **Deep learning (DL)** | Machine learning with neural networks that have many layers | [W1](../lectures/week01-what-is-ai/) |
| **Delegated design** | Part of the design (for example, some steel connections or precast elements) that a specialty engineer designs and seals; the EOR still reviews it | [W14](../lectures/week14-ai-policy-ethics/) |
| **Diffusion model** | An image generator that starts from noise and removes it step by step, guided by a text prompt | [W8](../lectures/week08-generative-ai-2/) |
| **Digital twin** | A digital model of a specific real asset, updated with its data and used to make decisions about it | [W11](../lectures/week11-ai-across-ce-arce/) |
| **Distribution shift** | The data a model meets in use differ from the data it learned from, so its test score no longer applies | [W13](../lectures/week13-responsible-ai/) |
| **Domain tool** | AI features built into engineering software (BIM, CAD, structural or energy analysis) | [W12](../lectures/week12-ai-tools/) |
| **Dry run** | A practice talk. In Lab 15 each team gives a 5-minute version of its final talk and gets feedback | [W15](../lectures/week15-synthesis/) |
| **Early stopping** | Stopping training when the validation error stops improving | [W5](../lectures/week05-neural-networks-1/) |
| **Embedding** | A vector (list of numbers) that represents a token; similar meanings → nearby vectors | [W7](../lectures/week07-generative-ai-1/) |
| **Engineer of record (EOR)** | The licensed engineer responsible for a project's design, whose seal is on the design documents | [W14](../lectures/week14-ai-policy-ethics/) |
| **Epoch** | One full pass through all the training examples | [W5](../lectures/week05-neural-networks-1/) |
| **Error / residual** | Prediction minus truth, ŷ − y | [W3](../lectures/week03-how-machines-learn-1/) |
| **EU AI Act** | The European Union's broad AI law (Regulation (EU) 2024/1689), which sets duties by level of risk | [W14](../lectures/week14-ai-policy-ethics/) |
| **Example** | One row of data — here, one concrete mix tested at one age | [W2](../lectures/week02-ml-dl-genai/) |
| **Extrapolation** | Using a model outside the range of data it was trained on — often unreliable | [W11](../lectures/week11-ai-across-ce-arce/) |
| **Feature map** | The output of one filter: a map of where its pattern appears | [W6](../lectures/week06-neural-networks-2/) |
| **Feature scaling / standardization** | Rescaling each feature to mean 0 and standard deviation 1 | [W4](../lectures/week04-how-machines-learn-2/) |
| **Feature (X)** | An input column the model uses, e.g., cement content or age | [W2](../lectures/week02-ml-dl-genai/) |
| **FE exam / EIT** | Fundamentals of Engineering exam; passing it (plus education) leads to the Engineer in Training designation | [W15](../lectures/week15-synthesis/) |
| **Few-shot prompting** | Including a few worked input → output examples in the prompt to show the pattern you want | [W8](../lectures/week08-generative-ai-2/) |
| **Filter (kernel)** | The small grid of weights used in convolution, e.g., 3 × 3 | [W6](../lectures/week06-neural-networks-2/) |
| **Forward pass** | Running inputs through the network, layer by layer, to get a prediction | [W5](../lectures/week05-neural-networks-1/) |
| **Foundation model** | A large model pretrained on broad data and adapted to many tasks | [W2](../lectures/week02-ml-dl-genai/) |
| **Generative AI** | Models that create new content: text, images, code, designs | [W2](../lectures/week02-ml-dl-genai/) |
| **Generative AI (GenAI)** | Deep learning models that create new content (text, images, code) | [W1](../lectures/week01-what-is-ai/) |
| **Gradient descent** | Repeatedly stepping the parameters downhill on the cost surface | [W4](../lectures/week04-how-machines-learn-2/) |
| **Gradient / partial derivative (∂J/∂w)** | The slope of the cost in one parameter's direction | [W4](../lectures/week04-how-machines-learn-2/) |
| **Grounding / citation** | Tying each claim in an answer to a specific source passage you can check | [W8](../lectures/week08-generative-ai-2/) |
| **Hallucinated citation** | A reference an AI invents, or a real reference that does not say what the AI claims | [W12](../lectures/week12-ai-tools/) |
| **Hallucination** | Fluent, confident output that is false or not supported by any source | [W7](../lectures/week07-generative-ai-1/) |
| **Held-out (test) data** | Data the model never saw during training, used to estimate how it will do on new cases | [W15](../lectures/week15-synthesis/) |
| **High-risk AI** | Under the EU AI Act, uses listed in the law (such as safety components of critical infrastructure) that must meet strict requirements | [W14](../lectures/week14-ai-policy-ethics/) |
| **Human in the loop** | A person must approve consequential actions before they happen | [W10](../lectures/week10-ai-agents/) |
| **Hydrograph** | A plot of a river's water level or flow over time | [W11](../lectures/week11-ai-across-ce-arce/) |
| **Hype** | Claims about a technology that go beyond the evidence | [W15](../lectures/week15-synthesis/) |
| **Hyperparameter** | A setting you choose before training (learning rate, layers, neurons, epochs) | [W5](../lectures/week05-neural-networks-1/) |
| **Independent check** | A second way to get the answer that does not depend on the first (hand calc, Python, another method) | [W12](../lectures/week12-ai-tools/) |
| **Index** | The stored vectors for all chunks, with labels saying where each chunk came from | [W8](../lectures/week08-generative-ai-2/) |
| **Instruction tuning** | Training on prompts paired with good answers so the model follows instructions | [W7](../lectures/week07-generative-ai-1/) |
| **ISO/IEC 42001** | An international standard for an AI management system; organizations can be certified to it | [W14](../lectures/week14-ai-policy-ethics/) |
| **Iteration** | One step of gradient descent | [W4](../lectures/week04-how-machines-learn-2/) |
| **JSON** | A simple text format of `"key": value` pairs that programs can read, used for tool requests | [W10](../lectures/week10-ai-agents/) |
| **k-fold cross-validation** | Split the data into k parts; train on k − 1 and test on the remaining one, k times; average the results | [W13](../lectures/week13-responsible-ai/) |
| **Language model** | A model that gives a probability to each possible next piece of text | [W7](../lectures/week07-generative-ai-1/) |
| **Large language model (LLM)** | A language model with billions of parameters trained on huge amounts of text | [W7](../lectures/week07-generative-ai-1/) |
| **Latency** | How long you wait for an answer; grows with answer length and model size | [W8](../lectures/week08-generative-ai-2/) |
| **Layer (input, hidden, output)** | A group of neurons that all take the same inputs; hidden layers sit between input and output | [W5](../lectures/week05-neural-networks-1/) |
| **Learning curve** | A plot of cost vs iteration, used to check that training works | [W4](../lectures/week04-how-machines-learn-2/) |
| **Learning rate (α)** | How big each gradient-descent step is | [W4](../lectures/week04-how-machines-learn-2/) |
| **Least privilege** | Giving an agent only the permissions and tools its task needs | [W10](../lectures/week10-ai-agents/) |
| **Least squares** | Choosing the line with the lowest sum of squared errors (what `numpy.polyfit` does) | [W3](../lectures/week03-how-machines-learn-1/) |
| **Linear regression** | Fitting a straight line (or flat surface) to predict a number | [W3](../lectures/week03-how-machines-learn-1/) |
| **Local / open model** | A model whose weights you can download and run on your own computer, so data stays local | [W12](../lectures/week12-ai-tools/) |
| **Logistic regression** | A classification model: weighted sum → sigmoid → probability → threshold | [W4](../lectures/week04-how-machines-learn-2/) |
| **Logit** | The model's raw score for a token, before it is turned into a probability | [W7](../lectures/week07-generative-ai-1/) |
| **Loss** | The error measure training tries to reduce (the cost J from Weeks 3–4) | [W5](../lectures/week05-neural-networks-1/) |
| **Low deck (this week)** | A bridge deck rated 5 or lower on the 0–9 scale; Lab 11's "poor" is 4 or lower | [W13](../lectures/week13-responsible-ai/) |
| **m** | The number of examples in the dataset | [W3](../lectures/week03-how-machines-learn-1/) |
| **Machine learning (ML)** | AI methods that learn patterns from data instead of following hand-written rules | [W1](../lectures/week01-what-is-ai/) |
| **MAE** | Mean absolute error: the average size of a miss, in the target's units | [W3](../lectures/week03-how-machines-learn-1/) |
| **Memory** | What the agent keeps track of: the goal, steps so far, and tool results (short-term, in the context window) plus files or databases (long-term) | [W10](../lectures/week10-ai-agents/) |
| **MEP** | Mechanical, electrical, and plumbing systems of a building (and the space they need) | [W8](../lectures/week08-generative-ai-2/) |
| **Model** | A function that turns inputs into a prediction, ŷ = f(x); in ML its numbers (parameters) are learned from data | [W2](../lectures/week02-ml-dl-genai/) |
| **Model card** | A short document that travels with a model: intended use, data, performance, limits, owner | [W13](../lectures/week13-responsible-ai/) |
| **Multi-agent system** | Several agents with different roles (e.g., coordinator, specialists, reviewer) working on one job | [W10](../lectures/week10-ai-agents/) |
| **Multilayer perceptron (MLP)** | A fully connected network: every neuron uses all outputs of the previous layer | [W5](../lectures/week05-neural-networks-1/) |
| **Multimodal model** | A model that takes more than one kind of input, e.g., text plus images or PDFs | [W8](../lectures/week08-generative-ai-2/) |
| **National Bridge Inventory (NBI)** | The Federal Highway Administration's database of U.S. highway bridges and their inspection ratings | [W11](../lectures/week11-ai-across-ce-arce/) |
| **NDA** | Non-disclosure agreement: a contract that limits who may see a client's information | [W12](../lectures/week12-ai-tools/) |
| **Neuron** | A weighted sum of inputs plus a bias, passed through an activation function | [W5](../lectures/week05-neural-networks-1/) |
| **Next-token prediction** | Guessing which token comes next — the single task an LLM is trained on | [W7](../lectures/week07-generative-ai-1/) |
| **NIST AI RMF** | The U.S. NIST AI Risk Management Framework (AI RMF 1.0, Jan 2023): Govern, Map, Measure, Manage | [W13](../lectures/week13-responsible-ai/) |
| **Object detection** | Finding and drawing a box around each object of interest in an image | [W11](../lectures/week11-ai-across-ce-arce/) |
| **O&M manual** | Operation and maintenance manual for a building system or piece of equipment | [W8](../lectures/week08-generative-ai-2/) |
| **Order of magnitude** | The rough size of a number (1, 10, 100…); unit slips usually change it by 10× or more | [W12](../lectures/week12-ai-tools/) |
| **Overfitting** | A model that memorizes training noise; low training error, high test error | [W4](../lectures/week04-how-machines-learn-2/) |
| **Parameter** | A number inside the model (a weight) that training adjusts | [W7](../lectures/week07-generative-ai-1/) |
| **Parameters** | All the weights and biases the network learns | [W5](../lectures/week05-neural-networks-1/) |
| **Parameters (w, b)** | The numbers inside the model that learning adjusts: weight (slope) and bias (intercept) | [W3](../lectures/week03-how-machines-learn-1/) |
| **PE license** | Professional Engineer license; lets you seal engineering work and makes you responsible for it | [W15](../lectures/week15-synthesis/) |
| **Permutation feature importance** | How much a model's score drops when one input column is shuffled | [W13](../lectures/week13-responsible-ai/) |
| **Physics-informed ML** | ML whose cost function also penalizes breaking known physical laws | [W11](../lectures/week11-ai-across-ce-arce/) |
| **Pixel** | One cell of an image grid; a brightness from 0 (black) to 255 (white) per color channel | [W6](../lectures/week06-neural-networks-2/) |
| **Planning** | Breaking a goal into steps before acting, and re-planning when a step fails | [W10](../lectures/week10-ai-agents/) |
| **Pooling** | Shrinking a feature map, e.g., keeping the maximum of each 2 × 2 block | [W6](../lectures/week06-neural-networks-2/) |
| **PPE (personal protective equipment)** | Safety gear such as hard hats, high-visibility vests, gloves, and safety glasses | [W11](../lectures/week11-ai-across-ce-arce/) |
| **Precision** | TP / (TP + FP): of the items the model flagged, the share that really are positive (how trustworthy an alarm is) | [W6](../lectures/week06-neural-networks-2/) |
| **Preference tuning (RLHF)** | Tuning the model toward answers people rated higher (reinforcement learning from human feedback) | [W7](../lectures/week07-generative-ai-1/) |
| **Pretrained / frozen** | Already trained on another task / not updated during your training | [W6](../lectures/week06-neural-networks-2/) |
| **Pretraining** | The big first training stage: next-token prediction on trillions of tokens of text | [W7](../lectures/week07-generative-ai-1/) |
| **Prompt** | Everything you send the model: instructions, context, examples, and the question | [W8](../lectures/week08-generative-ai-2/) |
| **Prompt injection** | Text in a document, web page, or email that tries to give the agent new instructions | [W10](../lectures/week10-ai-agents/) |
| **Quantity takeoff** | Measuring quantities (volumes, areas, counts) from drawings or a model for a cost estimate | [W10](../lectures/week10-ai-agents/) |
| **R²** | Coefficient of determination: the share of the variation in y the model explains (1 = perfect, 0 = no better than the average) | [W3](../lectures/week03-how-machines-learn-1/) |
| **Random forest** | A model made of many decision trees that each vote; the majority vote (or average) is the prediction | [W11](../lectures/week11-ai-across-ce-arce/) |
| **ReAct** | A pattern where the model alternates thoughts, actions (tool calls), and observations | [W10](../lectures/week10-ai-agents/) |
| **Recall** | TP / (TP + FN): of the real positives, the share the model caught (how few cracks are missed) | [W6](../lectures/week06-neural-networks-2/) |
| **Recall / false alarm rate** | Share of true positives the model catches / share of true negatives it wrongly flags | [W13](../lectures/week13-responsible-ai/) |
| **Regression** | Supervised learning that predicts a number (MPa, kWh/m²) | [W2](../lectures/week02-ml-dl-genai/) |
| **Reinforcement learning** | Learning a strategy by acting and receiving rewards or penalties | [W2](../lectures/week02-ml-dl-genai/) |
| **ReLU** | Rectified linear unit: max(0, z) — negatives become 0, positives pass through | [W5](../lectures/week05-neural-networks-1/) |
| **Representativeness** | How well the training data matches the situations where the model will be used | [W2](../lectures/week02-ml-dl-genai/) |
| **Research/search assistant** | An AI tool that searches the web or papers and answers with citations you must open and check | [W12](../lectures/week12-ai-tools/) |
| **Responsible charge** | Direct control and personal supervision of engineering work by a licensed engineer | [W14](../lectures/week14-ai-policy-ethics/) |
| **Retrieval-augmented generation (RAG)** | Looking up relevant passages in your documents first, then having the model answer from them | [W8](../lectures/week08-generative-ai-2/) |
| **RFI** | Request for information: a contractor's written question to the design team during construction | [W15](../lectures/week15-synthesis/) |
| **RFI (request for information)** | A formal question from a contractor to the designer during construction | [W7](../lectures/week07-generative-ai-1/) |
| **Risk-based regulation** | Stricter rules for uses that can cause more harm; light or no rules for low-risk uses | [W14](../lectures/week14-ai-policy-ethics/) |
| **RMSE** | Root mean squared error: like MAE, in the target's units, but large misses weigh more | [W4](../lectures/week04-how-machines-learn-2/) |
| **RNN / LSTM** | Recurrent network that reads a sequence step by step with a memory; LSTM adds gates for longer memory | [W6](../lectures/week06-neural-networks-2/) |
| **Robustness / stress test** | How well a model holds up when conditions change (blur, lighting, noise); a test that changes them on purpose | [W13](../lectures/week13-responsible-ai/) |
| **ROC AUC** | A 0.5–1.0 score for how well a model ranks positives above negatives; 0.5 = random guessing | [W13](../lectures/week13-responsible-ai/) |
| **Safety component** | A part of a system whose failure could endanger people's health or safety, or property | [W14](../lectures/week14-ai-policy-ethics/) |
| **Saliency map** | An image highlighting which pixels most affected a vision model's output | [W13](../lectures/week13-responsible-ai/) |
| **scikit-learn** | The standard Python library for classic machine learning (`fit`, `predict`) | [W4](../lectures/week04-how-machines-learn-2/) |
| **Seal (stamp)** | A licensed engineer's mark on documents, meaning "I prepared or supervised this, and I am responsible for it" | [W14](../lectures/week14-ai-policy-ethics/) |
| **Search and planning** | AI methods that look through possible actions to reach a goal, e.g., route finding | [W1](../lectures/week01-what-is-ai/) |
| **Self-supervised learning** | Learning where the labels come from the data itself — e.g., the next word in a sentence; how large language models are pretrained (Week 7) | [W2](../lectures/week02-ml-dl-genai/) |
| **Shop drawings** | Detailed fabrication drawings a contractor or fabricator submits for the designer's review | [W10](../lectures/week10-ai-agents/) |
| **Shortcut learning / spurious correlation** | The model uses a cue that happens to go with the label in training data but is not the real reason | [W13](../lectures/week13-responsible-ai/) |
| **Sliding window** | Using the last k values as inputs to predict the next value, then shifting by one step | [W6](../lectures/week06-neural-networks-2/) |
| **Softmax** | The function that turns a list of scores into probabilities that add up to 1 (the many-class version of the sigmoid) | [W7](../lectures/week07-generative-ai-1/) |
| **State board rules** | The licensing law and rules of your state's engineering board (in Arizona, the Board of Technical Registration; A.A.C. R4-30-301). Breaking them can cost you your license | [W14](../lectures/week14-ai-policy-ethics/) |
| **State DOT** | A state department of transportation, which owns and inspects most highway bridges in its state | [W11](../lectures/week11-ai-across-ce-arce/) |
| **Structural health monitoring (SHM)** | Sensors left on a structure to track its behavior and detect possible damage | [W11](../lectures/week11-ai-across-ce-arce/) |
| **Subgroup analysis** | Measuring a model's errors separately for each group (e.g., material, owner, age) | [W13](../lectures/week13-responsible-ai/) |
| **Submittal** | A document a contractor sends for the designer's review, such as a concrete mix design | [W10](../lectures/week10-ai-agents/) |
| **Success rate** | Test tasks passed ÷ test tasks tried | [W10](../lectures/week10-ai-agents/) |
| **Supervised learning** | Learning from examples that include the right answers | [W2](../lectures/week02-ml-dl-genai/) |
| **Surrogate model** | A fast ML model trained to imitate a slow physics simulation | [W11](../lectures/week11-ai-across-ce-arce/) |
| **Susceptibility map** | A map showing how likely a hazard, such as a landslide, is in each area | [W11](../lectures/week11-ai-across-ce-arce/) |
| **Sycophancy** | The model agreeing with the user (even when the user is wrong) instead of sticking to the evidence | [W8](../lectures/week08-generative-ai-2/) |
| **System message** | The part of a chat prompt that sets the model's role and standing rules | [W8](../lectures/week08-generative-ai-2/) |
| **Target / label (y)** | The output we want to predict, e.g., compressive strength | [W2](../lectures/week02-ml-dl-genai/) |
| **Temperature (T)** | A setting that sharpens (T < 1) or flattens (T > 1) the next-token probabilities | [W7](../lectures/week07-generative-ai-1/) |
| **Test case (known case)** | An input whose correct output you already know, used to check code | [W12](../lectures/week12-ai-tools/) |
| **TF-IDF** | A simple way to turn text into a vector: word counts, weighted up for words that are rare in the collection | [W8](../lectures/week08-generative-ai-2/) |
| **Time series** | Measurements in time order, e.g., hourly traffic volume | [W6](../lectures/week06-neural-networks-2/) |
| **Token** | A piece of text (word, word part, digit, or symbol) that the model reads and writes | [W7](../lectures/week07-generative-ai-1/) |
| **Tokenizer** | The tool that cuts text into tokens and turns them into ID numbers | [W7](../lectures/week07-generative-ai-1/) |
| **Tool** | A function the agent can call, such as a unit converter, a beam calculator, or a document search | [W10](../lectures/week10-ai-agents/) |
| **Tool (function) calling** | The model writes a structured request naming a tool and its inputs; the surrounding program runs the tool and returns the result | [W10](../lectures/week10-ai-agents/) |
| **Training set / test set** | Data used to fit the model / data held back to estimate performance on new cases | [W4](../lectures/week04-how-machines-learn-2/) |
| **Transfer learning** | Reusing a network pretrained on a large dataset and training only a small new part | [W6](../lectures/week06-neural-networks-2/) |
| **Transformer** | The network design behind LLMs: stacked blocks of attention + feed-forward layers | [W7](../lectures/week07-generative-ai-1/) |
| **Underfitting** | A model too simple to capture the pattern; high error on training and test data | [W4](../lectures/week04-how-machines-learn-2/) |
| **Unsupervised learning** | Finding structure (groups, unusual cases) in data without answers | [W2](../lectures/week02-ml-dl-genai/) |
| **Validation set** | Part of the training data used to choose settings such as α or model size | [W4](../lectures/week04-how-machines-learn-2/) |
| **Verification** | Checking an output independently before relying on it | [W12](../lectures/week12-ai-tools/) |
| **Weight / bias** | The adjustable numbers in a neuron; weights scale inputs, the bias shifts the result | [W5](../lectures/week05-neural-networks-1/) |
| **Weight sharing** | Reusing the same filter weights at every position in the image | [W6](../lectures/week06-neural-networks-2/) |
| **x⁽ⁱ⁾, y⁽ⁱ⁾** | The input and true output of the i-th example | [W3](../lectures/week03-how-machines-learn-1/) |
| **ŷ ("y-hat")** | The model's prediction | [W3](../lectures/week03-how-machines-learn-1/) |

*198 terms. Generated from the weekly pages; edit the weekly Key terms tables, not this file.*
