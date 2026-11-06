# Week 11 — AI Across Civil and Architectural Engineering: The Big Picture

**Slides:** [PDF](Week11_AI-Across-CE-ARCE.pdf) · [PowerPoint](Week11_AI-Across-CE-ARCE.pptx) · **Lab:** [Lab 11 — End-to-End ML Workflow on Arizona Bridges](../../labs/lab11-bridges-end-to-end/) · **Project:** [Proposal canvas](../../project/templates/proposal-canvas.md) (due this Sunday)

## Learning objectives
By the end of this week you can:
1. Place AI applications on the life cycle of an asset: plan, design, build, operate, maintain, renew.
2. For a CE/ARCE application, name its **input data**, **AI task type**, and **output**.
3. Explain digital twins, surrogate models, and physics-informed machine learning.
4. Explain why CE/ARCE data is hard — and why accuracy misleads when failures are rare.
5. Analyze a case study and judge whether AI fits the task.

## The big ideas
- AI can help in **every phase** of an asset's life: forecasting demand (plan), surrogates and generative design (design), site-safety video and progress tracking (build), energy forecasts and HVAC or signal control (operate), crack detection and health monitoring (maintain), and ranking repairs (renew). Assets last decades — U.S. bridge design specifications use a 75-year design life — so data from one phase feeds the next.
- Six **task types** cover most engineering AI: regression (a number), classification (a category), detection (where in an image), forecasting (future values), optimization (best choice under limits), and generation (new content). Real systems often chain two, e.g., predict energy use, then optimize setpoints.
- A tour by sub-discipline, each described as input data → task → output:
  - **Structural** — health monitoring: vibration and strain sensors → anomaly detection → alerts for inspection.
  - **Geotechnical** — landslide susceptibility: slope, geology, rainfall map layers → classification → a hazard map.
  - **Transportation** — traffic forecasting: hourly counts, calendar, weather → forecasting → signal timing and work-zone plans.
  - **Water/environmental** — flood forecasting: rain and stream gauges → forecasting → warnings at low-water crossings.
  - **Construction** — site safety: camera frames → object detection → alerts to the safety manager about missing PPE (personal protective equipment: hard hats, vests).
  - **Building systems (ARCE)** — energy: geometry, schedules, weather, meter data → regression then optimization → forecasts, setpoints, fault alerts.
  - **Asset management** — bridges: inventory and inspection records → classification + optimization → a risk-ranked repair list.
- A **digital twin** is a model of one specific asset that is updated with data from it and used to make decisions about it. (No automatic data link = a digital model; data flowing in only = a digital shadow.)
- **Physics + data:** a **surrogate** is a fast ML model trained on runs of a slow physics model — great inside its training range, possibly badly wrong outside it. **Physics-informed ML** adds a penalty for breaking known physics to the cost function: J_total = J_data + λ·J_physics.
- CE/ARCE data is hard: small data, rare failures, long lifespans, safety-critical consequences, codes and liability, and messy records. In the 2024 Arizona bridge data only **41 of 3,762** rated decks (1.1%) are poor (rating ≤ 4), so a model that always says "not poor" is 98.9% accurate yet finds none of them — check **recall**. (In Week 13 we use "low = rating ≤ 5" instead, because 41 decks are too few to compare subgroups.) Poor bridges are also not spread evenly: 44 of the 99 bridges whose lowest rating is ≤ 4 are owned by tribes or the Bureau of Indian Affairs, whose bridge repairs are funded through a separate federal program (23 CFR 661) — an infrastructure-investment question.
- AI ranks, flags, and forecasts; engineers inspect, decide, and stay accountable.

## Key terms
| Term | Plain-language meaning |
|---|---|
| Asset life cycle | The phases of a bridge, building, or network: plan, design, build, operate, maintain, renew |
| Structural health monitoring (SHM) | Sensors left on a structure to track its behavior and detect possible damage |
| Anomaly detection | Learning what "normal" data looks like and flagging what doesn't fit |
| Susceptibility map | A map showing how likely a hazard, such as a landslide, is in each area |
| Object detection | Finding and drawing a box around each object of interest in an image |
| Digital twin | A digital model of a specific real asset, updated with its data and used to make decisions about it |
| Surrogate model | A fast ML model trained to imitate a slow physics simulation |
| Extrapolation | Using a model outside the range of data it was trained on — often unreliable |
| Physics-informed ML | ML whose cost function also penalizes breaking known physical laws |
| Class imbalance | One class (e.g., poor decks) is much rarer than the other |
| Recall | Of all the real positives (e.g., poor decks), the share the model found |
| Precision | Of all the model's alarms, the share that were real positives |
| National Bridge Inventory (NBI) | The Federal Highway Administration's database of U.S. highway bridges and their inspection ratings |
| PPE (personal protective equipment) | Safety gear such as hard hats, high-visibility vests, gloves, and safety glasses |
| Random forest | A model made of many decision trees that each vote; the majority vote (or average) is the prediction |
| Baseline | The simplest reasonable method to beat, such as "always predict not poor"; without one, a score means little |
| State DOT | A state department of transportation, which owns and inspects most highway bridges in its state |
| Hydrograph | A plot of a river's water level or flow over time |

## Read / watch
### Required (≈ 35 min total)
- **This week's slides 10 and 12 (geotechnical and water examples)** — in the [PDF](Week11_AI-Across-CE-ARCE.pdf) (about 5 minutes). Read them **before class**: we cover them only briefly, and the jigsaw activity builds on them.
- **Google Machine Learning Crash Course — "Accuracy, recall, precision, and related metrics"** — <https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall> (about 20 minutes). The metrics you will use in Lab 11.
- **FHWA National Bridge Inventory** — <https://www.fhwa.dot.gov/bridge/nbi.cfm> (about 10 minutes). Where our Arizona data comes from; browse the "condition" tables to see how states compare.

### Optional
- **National Academies (2024), *Foundational Research Gaps and Future Directions for Digital Twins*** — <https://nap.nationalacademies.org/catalog/26894> (free PDF; read the Summary, about 20 minutes). A careful definition of digital twins and what they need.
- **Raissi, Perdikaris & Karniadakis (2019), "Physics-informed neural networks"** — <https://doi.org/10.1016/j.jcp.2018.10.045> (skim the introduction). The paper that popularized physics-informed ML.

## Check yourself
1. A contractor wants an alert whenever a site camera sees a worker without a hard hat. Name the input data, the AI task type, and the output.
   <details><summary>Answer</summary>Input: images or video frames from site cameras (labeled with boxes around workers and hard hats for training). Task: object detection. Output: boxes around workers plus an alert to the safety manager when a hard hat is missing.</details>
2. Why might a structural health monitoring system raise false alarms on a cold morning?
   <details><summary>Answer</summary>Temperature changes a structure's stiffness and therefore its natural frequencies. If the model has not learned how "normal" changes with temperature, it may mistake a temperature effect for damage.</details>
3. What makes something a digital twin rather than just a digital model?
   <details><summary>Answer</summary>A digital twin is linked to one specific real asset, is updated with data from it (for example, sensors), and is used to make decisions about it. A digital model has no automatic data link.</details>
4. A surrogate trained on beam spans of 4–9 m predicts 166 mm of deflection for a 14 m span; the full simulation gives 250 mm. What went wrong, and why is it dangerous?
   <details><summary>Answer</summary>The surrogate was used outside its training range (extrapolation). It under-predicts deflection, which is unconservative: a design based on it could deflect much more than expected. Always check a surrogate's range and verify the final design with the full model.</details>
5. A bridge-deck model flags 50 decks as poor; 25 of them really are poor, and there are 41 poor decks in total. What are its recall and precision?
   <details><summary>Answer</summary>Recall = 25 ÷ 41 ≈ 61% (share of the real poor decks it found). Precision = 25 ÷ 50 = 50% (share of its alarms that were right).</details>

## Coming up
- **Lab 11 (this week's lab day):** an end-to-end ML project on the 8,573 Arizona bridges — frame the question, explore a map and age vs condition, build features, compare a baseline with logistic regression and a random forest, look at accuracy vs recall and feature importance, and write a short engineering memo. Use it as your project template. Lab due Sunday 11:59 pm (Arizona time) on Brightspace.
- **Due Sunday:** your team's two-page [project proposal canvas](../../project/templates/proposal-canvas.md) **and** your [team charter](../../project/templates/team-charter.md), plus Lab 11.
- **Next week:** AI tools for engineers — choosing, using, and verifying them. Short quiz on this week at the start of the lecture day.
