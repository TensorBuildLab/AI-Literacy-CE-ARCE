# Project Ideas

Twenty-two starting points across civil and architectural engineering and all four tracks. Use one as it is, combine two, or bring your own (see the end of this page). Every idea fits free Google Colab.

**How to read each idea**
- **Question** — what you are trying to find out. Make it more specific for your team.
- **Data** — course files from [`data/`](../data/) first. External datasets are public and free to download; we checked every link in November 2026, but websites change — tell the instructor if one breaks. Always read the license on the provider's page.
- **Methods** — a reasonable plan, not the only one.
- **Baseline** — the simple thing your method must beat (or be compared with).
- **Watch out for** — the mistake teams most often make with this idea.

**Difficulty:** ★ = good first project, data ready to use · ★★ = some data work or a new technique · ★★★ = harder data access or a less clear-cut answer.

**Key terms used on this page**

| Term | Plain meaning |
|---|---|
| **Baseline** | The simplest reasonable approach (predict the average, "same as last week," the tool with no help) that your method must beat or be compared with. |
| **Random forest** | Many decision trees, each trained on a slightly different sample of the data, that vote or average their answers (Lab 11). |
| **Transfer learning** | Reusing a network trained on millions of other images and training only a small new last part (Lab 06). |
| **Zero-shot** | Using a model on a task it was never trained for, just by describing the task in words (CLIP in Lab 01). |
| **RAG** | Retrieval-augmented generation: your code first finds relevant passages in documents, then the LLM answers from them (Lab 08). |
| **Recall / precision** | Recall: of the real problems, how many the model caught. Precision: of the model's alarms, how many were real. |
| **Group split / time-based split** | Ways to keep the test set truly new: keep all rows of one mix (or one bridge) on the same side; or train on earlier dates and test on later ones. |
| **Persistence** | A forecast that says "the next value equals the current one." |
| **Leakage** | Information about the answer that sneaks into the inputs, so the model looks better than it really is. |

| # | Idea | Track | Sub-discipline | Data | Difficulty |
|---|---|---|---|---|---|
| P1 | [Concrete strength from mix design](#p1-concrete-strength-from-mix-design) | Predict | Structures & materials | course | ★ |
| P2 | [Early-design energy loads](#p2-early-design-energy-loads) | Predict | Building systems (ARCE) | course | ★ |
| P3 | [Next-hour traffic forecasting](#p3-next-hour-traffic-forecasting) | Predict | Transportation | course | ★★ |
| P4 | [Household energy forecasting and unusual hours](#p4-household-energy-forecasting-and-unusual-hours) | Predict | Building operation (ARCE) | course | ★★ |
| P5 | [Bridge condition: does an Arizona model travel?](#p5-bridge-condition-does-an-arizona-model-travel) | Predict | Infrastructure asset management | course + FHWA | ★★ |
| P6 | [Low-cost air-quality sensor calibration](#p6-low-cost-air-quality-sensor-calibration) | Predict | Environmental | UCI | ★★ |
| P7 | [Will the wash run tomorrow?](#p7-will-the-wash-run-tomorrow) | Predict | Water resources | USGS + AZMet | ★★★ |
| P8 | [Which bridge decks will lose a rating point by 2024?](#p8-which-bridge-decks-will-lose-a-rating-point-by-2024) | Predict | Infrastructure asset management | course + FHWA 2019 | ★★ |
| S1 | [Crack detection beyond the course photos](#s1-crack-detection-beyond-the-course-photos) | See | Structural inspection | course + SDNET2018 | ★★ |
| S2 | [Pavement damage types](#s2-pavement-damage-types) | See | Transportation (pavements) | RDD2022 | ★★★ |
| S3 | [What is the crack model looking at?](#s3-what-is-the-crack-model-looking-at) | See | Structural inspection | course | ★★ |
| S4 | [How much of the image is crack?](#s4-how-much-of-the-image-is-crack) | See | Structural inspection | course | ★★ |
| A1 | [OSHA trench and fall-protection assistant](#a1-osha-trench-and-fall-protection-assistant) | Assist | Construction safety | course | ★★ |
| A2 | [Engineering calculator agent](#a2-engineering-calculator-agent) | Assist | Structures, water, building systems | you build | ★★ |
| A3 | [Sorting construction injury reports](#a3-sorting-construction-injury-reports) | Assist | Construction safety | OSHA | ★★★ |
| A4 | [Ask the bridge inventory](#a4-ask-the-bridge-inventory) | Assist | Infrastructure asset management | course | ★★ |
| A5 | [Plain-language energy explainer](#a5-plain-language-energy-explainer) | Assist | Building systems (ARCE) | course | ★★ |
| E1 | [Can AI do routine engineering calculations?](#e1-can-ai-do-routine-engineering-calculations) | Evaluate | General CE/ARCE | you build | ★ |
| E2 | [Citation audit: real section or made up?](#e2-citation-audit-real-section-or-made-up) | Evaluate | Codes & regulations | course | ★ |
| E3 | [OSHA soil type from a site description](#e3-osha-soil-type-from-a-site-description) | Evaluate | Geotechnical | course | ★★ |
| E4 | [Concept images vs. the design brief](#e4-concept-images-vs-the-design-brief) | Evaluate | Architecture / ARCE | you build | ★★ |
| E5 | [The wrong-premise test](#e5-the-wrong-premise-test) | Evaluate | General CE/ARCE | you build | ★ |

---

## Predict

### P1. Concrete strength from mix design
**Track:** Predict · **Sub-discipline:** Structures & materials · ★
- **Question:** How accurately can we predict compressive strength (MPa) of a concrete mix at a given age — and how far outside the tested mixes can we trust the prediction?
- **Data:** `concrete_strength.csv` (1,030 lab tests; 8 inputs in kg/m³ and days; target in MPa).
- **Methods:** multiple linear regression with engineered features (water–cement ratio, water–binder ratio where binder = cement + slag + fly ash, log of age); random forest; a small neural network (`MLPRegressor`); predicted-vs-actual plot; errors by age group.
- **Baseline:** predict the training-set average; then a one-feature w/c-ratio line (Lab 03).
- **Watch out for:** the same mix is often tested at several ages — the file has only **428 different mixes** in 1,030 rows. A random train/test split puts the same mix on both sides and makes scores look better than they are. Split **by mix** (scikit-learn `GroupShuffleSplit`). Also: these are lab specimens, not field concrete, and there is no information on curing.

### P2. Early-design energy loads
**Track:** Predict · **Sub-discipline:** Building systems (ARCE) · ★
- **Question:** Which early design choices (shape, glazing, orientation) drive annual heating and cooling loads (kWh/m²), and can a fast model stand in for an energy simulation at the concept stage?
- **Data:** `building_energy_efficiency.csv` (768 simulated buildings).
- **Methods:** linear regression, random forest, small neural network; permutation feature importance; separate models for heating and cooling; compare which features matter for each.
- **Baseline:** predict the average; then linear regression on relative compactness alone.
- **Watch out for:** there are only **12 distinct building shapes**, all with the same volume and materials, simulated for one location. A random split tests shapes the model has already seen. Hold out whole shapes (group by `relative_compactness`) to test a new design. Your model copies the simulator's assumptions — it is a *surrogate*, not a measurement.

### P3. Next-hour traffic forecasting
**Track:** Predict · **Sub-discipline:** Transportation · ★★
- **Question:** How well can we forecast next-hour traffic volume (vehicles/h) on a freeway, and does weather add anything beyond time of day and day of week?
- **Data:** `metro_traffic_volume.csv` (40,575 hours on westbound I‑94, Minnesota, 2012–2018).
- **Methods:** features for hour, day of week, holiday, temperature, rain, snow; lag features (previous hour, same hour last week); random forest or `MLPRegressor`; sliding windows (Lab 06 bonus); MAE in vehicles/h by time of day.
- **Baseline:** "same hour last week"; average volume for that hour of the week.
- **Watch out for:** split by **time** (train on earlier years, test on the last year) — a random split lets the model peek at the future. The record has gaps (missing hours), which break lag features. The `holiday` column is filled in only for the **first hour (midnight)** of each holiday — spread it to the whole day. One station in Minnesota, before 2020: snow matters there, and patterns may differ elsewhere.

### P4. Household energy forecasting and unusual hours
**Track:** Predict · **Sub-discipline:** Building operation (ARCE) · ★★
- **Question:** Can we forecast next-hour appliance energy use (Wh) in a low-energy house, and can the forecast errors flag unusual hours?
- **Data:** `house_energy_hourly.csv` (3,290 hours, January–May 2016, one house in Belgium; room temperatures and humidity, outdoor weather).
- **Methods:** time-of-day and lag features, indoor temperatures; random forest; residual-based anomaly flags (hours where the error is much larger than usual).
- **Baseline:** persistence ("next hour = this hour"); same hour yesterday.
- **Watch out for:** one house and one family — behavior drives most of the energy use, so results will not transfer to other homes. Use is very spiky (median 380 Wh, maximum 3,650 Wh), so MAE and RMSE tell different stories — report both. Energy data can reveal when people are home: discuss privacy.

### P5. Bridge condition: does an Arizona model travel?
**Track:** Predict · **Sub-discipline:** Infrastructure asset management · ★★
- **Question:** A model trained on Arizona bridges flags those likely to have low condition ratings. Does it still work in another state with a different climate and bridge stock?
- **Data:** `arizona_bridges_nbi2024.csv` plus the National Bridge Inventory file for a second state from the same source: FHWA, <https://www.fhwa.dot.gov/bridge/nbi/ascii.cfm> (U.S. Government work). Decode it with the course's [NBI decode helper](tools/nbi_decode.py), which gives the same columns as the course file.
- **Methods:** logistic regression and random forest (Lab 11); recall and precision for the low-condition class; subgroup errors by material and design type; train on Arizona → test on the other state; compare with a model trained on the other state.
- **Baseline:** always predict the majority class; a rule such as "built before 1970 = at risk."
- **Watch out for:** Lab 11 already did Arizona deck condition, so go further (substructure or culvert ratings, or the state-to-state test). Raw NBI files use numeric codes — the [decode helper](tools/nbi_decode.py) handles the common ones, but check a few rows against FHWA's *Recording and Coding Guide*. Low ratings are rare: only 41 of about 3,760 rated Arizona decks are rated 4 or below (Lab 11's "poor"), which is why Lab 13 uses "low = 5 or below" to get enough examples in each subgroup. For a forecasting version, see P8. Ratings are inspectors' judgments, and reconstruction changes the real age. This is a prioritization aid, never a safety decision.

### P6. Low-cost air-quality sensor calibration
**Track:** Predict · **Sub-discipline:** Environmental · ★★
- **Question:** Can cheap metal-oxide gas sensors, corrected with machine learning, estimate a pollutant concentration (for example CO in mg/m³ or benzene in µg/m³) measured by a reference analyzer?
- **Data:** UCI Machine Learning Repository, *Air Quality* — hourly readings from a low-cost sensor array in an Italian city, with co-located reference-analyzer values: <https://archive.ics.uci.edu/dataset/360/air+quality>.
- **Methods:** linear regression and random forest from sensor signals plus temperature and humidity; time-based split; plot error month by month to see sensor drift.
- **Baseline:** a single-sensor straight-line calibration.
- **Watch out for:** missing values are stored as **−200**, not blank — replace them before anything else or every average is wrong. Sensors drift over months, so train on early months and test on later ones. One device in one city. Check the license on the UCI page.

### P7. Will the wash run tomorrow?
**Track:** Predict · **Sub-discipline:** Water resources · ★★★
- **Question:** During the monsoon, can rainfall and recent flow predict whether a Tucson-area river or wash will be flowing tomorrow (or how high its daily flow will be)?
- **Data:** daily discharge at a USGS stream gauge near Tucson (for example on the Santa Cruz River or Rillito Creek) from USGS Water Data, <https://waterdata.usgs.gov/>, plus daily rainfall and weather from the University of Arizona's Arizona Meteorological Network (AZMet), <https://azmet.arizona.edu/>. Both are free.
- **Methods:** logistic regression or random forest using rainfall over the last 1–3 days, day of year, and yesterday's flow; recall and precision for "flow" days; event-by-event plots.
- **Baseline:** persistence ("flows tomorrow if it flowed today"); a simple rainfall-threshold rule.
- **Watch out for:** these streams are dry on most days, so flow days are rare — accuracy is misleading (Lab 11). The rain gauge may be far from the watershed. USGS reports discharge in ft³/s (1 ft³/s = 0.0283 m³/s), and recent data are provisional. USGS has been modernizing its water-data website and download tools (as of 2026), so the download steps may change — budget time for data access.

### P8. Which bridge decks will lose a rating point by 2024?
**Track:** Predict · **Sub-discipline:** Infrastructure asset management · ★★
- **Question:** Using only what was known in 2019, can we predict which Arizona bridge decks will drop by at least one condition-rating point by 2024? This is a true forecast — unlike Lab 11, which predicts a rating from the same year's data.
- **Data:** the 2019 Arizona National Bridge Inventory file from FHWA, <https://www.fhwa.dot.gov/bridge/nbi/2019/delimited/AZ19.txt> (U.S. Government work, about 3.4 MB; list of years at <https://www.fhwa.dot.gov/bridge/nbi/ascii.cfm>). Decode it with the course's [NBI decode helper](tools/nbi_decode.py) and join it to `arizona_bridges_nbi2024.csv` on `structure_id` (the helper reproduces the course file exactly from FHWA's 2024 file). In our check, **3,599 decks** have a rating in both years; **293 of them (8.1%) dropped by one point or more**, and 256 went up.
- **Methods:** inputs from 2019 only (age, material, design type, traffic, 2019 deck/superstructure/substructure ratings); target = "deck rating dropped by ≥ 1 point by 2024" (or the 2024 rating itself); class-weighted logistic regression and random forest (Lab 11); cross-validated recall and precision; results by material and owner group (Lab 13).
- **Baseline:** "no change" (predict no drop for every deck); a simple rule such as "2019 rating ≤ 6 and older than 50 years → will drop."
- **Watch out for:** **leakage** — no 2024 column may be an input (write an `assert` for it). Ratings can go *up*: only 34 of the 256 increases have a reconstruction year between 2019 and 2024, so many reflect repairs not recorded as reconstruction, or a different inspector's judgment — decide how to treat them *before* modeling. Some structures were added (360) or removed (107) between the two files. A 2019 rating may come from an inspection up to about two years earlier (most bridges are inspected every 24 months; some low-risk bridges less often). A forecast is a prioritization aid, never a reason to skip an inspection.

---

## See

### S1. Crack detection beyond the course photos
**Track:** See · **Sub-discipline:** Structural inspection · ★★
- **Question:** A crack classifier trained on our course photos scores near-perfect. Does it still work on harder images of bridge decks, walls, and pavements?
- **Data:** `concrete_cracks_sample.zip` (training) and **SDNET2018** (Utah State University; 56,000+ labeled images of cracked and uncracked concrete bridge decks, walls, and pavements; CC BY 4.0): <https://digitalcommons.usu.edu/all_datasets/48/>.
- **Methods:** ResNet-18 transfer learning (Lab 06) trained on course photos → tested on an SDNET2018 sample; then retrain with some SDNET2018 images and compare; confusion matrices; recall for cracks; results per surface type.
- **Baseline:** CLIP zero-shot (Lab 01); "always predict no crack" (shows why accuracy misleads on imbalanced data).
- **Watch out for:** the full download is large — use a few hundred images per class. SDNET2018 has far more uncracked than cracked images, and its images are a different size (resize them). The drop in accuracy *is* the finding: report it clearly instead of hiding it.

### S2. Pavement damage types
**Track:** See · **Sub-discipline:** Transportation (pavements) · ★★★
- **Question:** Can a CNN tell common pavement-distress types apart (longitudinal crack, transverse crack, alligator crack, pothole) from road photos?
- **Data:** Road Damage Dataset 2022 (RDD2022) from the RoadDamageDetector project: <https://github.com/sekilab/RoadDamageDetector>. Road photos from several countries with labeled boxes around damage. The license (stated on the page) is CC BY-SA 4.0, which requires credit and sharing derived data under the same license.
- **Methods:** crop each labeled box into a small image; transfer-learning classifier on the crops; confusion matrix; per-country results.
- **Baseline:** always predict the most common class; CLIP zero-shot with text labels.
- **Watch out for:** the labels are made for *object detection* (finding boxes), which is harder than this course needs — cropping turns it into classification. Download one country's subset only. Photos can show cars and people: do not publish identifiable faces or license plates. Classes are imbalanced.

### S3. What is the crack model looking at?
**Track:** See · **Sub-discipline:** Structural inspection · ★★
- **Question:** Does our crack classifier react to the crack itself, or to shortcuts such as dark pixels, stains, or texture?
- **Data:** `concrete_cracks_sample.zip`.
- **Methods:** the Lab 06 transfer-learning model; occlusion maps (slide a gray square over the image and record how much the crack score drops); planned edits (draw a dark pencil-like line on an uncracked image; add a shadow); the brightness and blur tests from Lab 13.
- **Baseline:** a simple edge-density classifier (count strong edge pixels from a Lab 06 edge filter and pick a threshold).
- **Watch out for:** saliency and occlusion maps *suggest* what matters; they do not prove it. Decide your test edits before looking at results, and show many examples, not just the prettiest one.

### S4. How much of the image is crack?
**Track:** See · **Sub-discipline:** Structural inspection · ★★
- **Question:** Can simple image processing estimate the fraction of an image that is crack, and does a CNN's crack probability rise with crack size?
- **Data:** `concrete_cracks_sample.zip`, plus your own labels: hand-sort 50+ crack images into "hairline / medium / wide."
- **Methods:** grayscale → threshold → clean-up (`scipy.ndimage` opening/closing) → crack-pixel fraction; compare with the CNN's probability and with your hand labels.
- **Baseline:** a single global threshold with no clean-up.
- **Watch out for:** the photos have no scale, so **pixels are not millimeters** — you cannot report crack widths in mm. Stains, joints, and shadows look like cracks. Have a second teammate label the same images and report how often you agree.

---

## Assist

### A1. OSHA trench and fall-protection assistant
**Track:** Assist · **Sub-discipline:** Construction safety · ★★
- **Question:** Can a small open LLM with retrieval answer excavation and fall-protection questions correctly — and cite the right section?
- **Data:** `osha/osha_1926_subpartP_excavations.txt` and `osha/osha_1926_subpartM_fall_protection.txt`.
- **Methods:** split the text into chunks by section; TF-IDF or sentence-embedding retrieval (Lab 08); Qwen2.5-0.5B-Instruct (or 1.5B on a GPU) prompted with the retrieved chunks and asked to cite sections; a test set of 25+ questions with answers and section numbers written *before* you tune anything.
- **Baseline:** the same LLM without retrieval; retrieval alone (show the top chunk, no LLM).
- **Watch out for:** if retrieval brings back the wrong section, the LLM will confidently use it — score retrieval and the final answer separately. Table B‑1 is a text transcription in our files. The assistant should say "not covered" for out-of-scope questions; test that. It is a study aid, never a substitute for a competent person on site.

### A2. Engineering calculator agent
**Track:** Assist · **Sub-discipline:** Structures, water, building systems · ★★
- **Question:** Does giving an LLM calculator tools make its engineering answers reliable?
- **Data:** 30+ test tasks your team writes, with answers computed in Python. Tools to build: unit converter; simply supported beam maximum moment and deflection; Manning's equation; rational method Q = CiA; wall heat loss Q = U·A·ΔT.
- **Methods:** the Lab 10 agent loop with JSON tool calls; a human-approval step and a step limit; a log of every tool call; success rate by task type.
- **Baseline:** the same LLM answering directly, with no tools.
- **Watch out for:** the model may pick the wrong tool or pass numbers in the wrong units (kN vs N, ft vs m) — put units in every tool's name or arguments. Malformed JSON is common with small models; count it as a failure. The rational method has a US form (Q in ft³/s from i in in/h and A in acres) and an SI form (Q = CiA/360 in m³/s with i in mm/h and A in hectares) — pick one and test both your tool and the agent on it.

### A3. Sorting construction injury reports
**Track:** Assist · **Sub-discipline:** Construction safety · ★★★
- **Question:** Can a model sort severe-injury narratives into event types (fall, struck-by, caught-in/between, electrical) so a safety manager can see trends quickly?
- **Data:** OSHA *Severe Injury Reports*, <https://www.osha.gov/severe-injury-reports> (downloadable; U.S. Government work). Keep construction employers (industry codes, NAICS, starting with 23). The file includes coded event categories you can use as labels — read its data dictionary.
- **Methods:** TF-IDF + logistic regression trained on the coded labels; a zero-shot LLM prompt on the same test set; an LLM-written monthly summary checked against counts you compute with pandas.
- **Baseline:** keyword rules ("fell," "ladder," "roof" → fall); the majority class.
- **Watch out for:** the federal data mainly cover states where federal OSHA has jurisdiction — Arizona runs its own state plan, so most Arizona incidents are not in it. Narratives can name employers: do not publish lists of companies, and never add personal details. Reported severe injuries are not all injuries.

### A4. Ask the bridge inventory
**Track:** Assist · **Sub-discipline:** Infrastructure asset management · ★★
- **Question:** Can an LLM agent answer plain-English questions about Arizona's bridges ("How many steel bridges built before 1960 have a deck rating of 5 or lower?") and get the numbers right?
- **Data:** `arizona_bridges_nbi2024.csv`.
- **Methods:** give the LLM the column names and meanings; it chooses from *your* safe query tools (filter, count, average by group) using JSON tool calls (Lab 10); 25+ test questions whose answers you compute yourselves with pandas.
- **Baseline:** the LLM answering without data access; a fixed menu of pre-written queries.
- **Watch out for:** **never run arbitrary code an LLM writes** — allow only your own query functions. Vague questions ("old bridges") need a definition; decide how the tool should ask. A blank condition rating means "not applicable" (for example, culverts have no deck rating), not zero. Check every number.

### A5. Plain-language energy explainer
**Track:** Assist · **Sub-discipline:** Building systems (ARCE) · ★★
- **Question:** Can an LLM turn model results into an accurate, plain-language note for a client — without inventing numbers or advice?
- **Data:** `building_energy_efficiency.csv` and a prediction model you train on it (see P2).
- **Methods:** your model predicts heating and cooling loads for two design options; the LLM writes a ~120-word comparison from a structured prompt containing only those numbers; Python checks that every number in the text matches the inputs; two teammates rate clarity and accuracy.
- **Baseline:** a fill-in-the-blank template ("Option B's predicted heating load is __ kWh/m², __% lower than Option A").
- **Watch out for:** LLMs like to add claims the model never made ("triple glazing will cut your bills by 30%") — count them. The data are simulated for one location; the note must say so. A qualified person must review the text before any client sees it.

---

## Evaluate

### E1. Can AI do routine engineering calculations?
**Track:** Evaluate · **Sub-discipline:** General CE/ARCE · ★
- **Question:** How often do LLMs get routine CE/ARCE calculations right, and which prompt style helps most?
- **Data:** 40+ problems your team writes — beam moment M = wL²/8 (w = load, kN/m), Manning's equation, wall heat loss U·A·ΔT, rational-method runoff Q = CiA, water–cement ratio, unit conversions — with answers computed in Python (as in Lab 12).
- **Methods:** compare Qwen2.5-0.5B-Instruct and 1.5B-Instruct (plus any free chatbot you can access); plain prompt vs structured prompt ("state the formula, show units, check the magnitude"); score "correct = within 2% with correct units"; classify each error (formula, arithmetic, units, misread problem).
- **Baseline:** the plain prompt with the smallest model.
- **Watch out for:** write the answer-parsing rule before testing. Use `do_sample=False` so runs repeat. Record tool versions and dates. Do not tune prompts on the test problems — keep a separate small "practice" set.

### E2. Citation audit: real section or made up?
**Track:** Evaluate · **Sub-discipline:** Codes & regulations · ★
- **Question:** When asked which OSHA section answers a question, how often do AI tools cite a section that does not exist or does not say what they claim?
- **Data:** 30+ questions about 29 CFR 1926 Subparts P and M, checked against the course `osha/` files and the current official text on the eCFR, <https://www.ecfr.gov/current/title-29/subtitle-B/chapter-XVII/part-1926>.
- **Methods:** ask each tool; check each citation: does the section exist? does it support the answer? Categories: correct, wrong section, nonexistent, too vague. Compare with a retrieval (RAG) version from Lab 08.
- **Baseline:** the plain prompt with no retrieval.
- **Watch out for:** use only regulations you can check publicly. Do not paste copyrighted standards (ACI, ASCE, ASTM) into AI tools or your repo. Have two teammates judge "supports the answer" independently and report how often they agree.

### E3. OSHA soil type from a site description
**Track:** Evaluate · **Sub-discipline:** Geotechnical · ★★
- **Question:** Given a short description of soil and site conditions, can an LLM assign the correct OSHA soil classification (Stable rock, Type A, Type B, or Type C)?
- **Data:** Appendix A of `osha/osha_1926_subpartP_excavations.txt`, plus 30+ short case descriptions your team writes, each with the correct classification and the Appendix A clause that decides it (checked by a second teammate).
- **Methods:** LLM alone vs LLM with the Appendix A text retrieved into the prompt vs a rule-based Python classifier you write from the same clauses; accuracy and a confusion matrix; which conditions cause errors.
- **Baseline:** your rule-based classifier; "always Type C" (the most conservative answer).
- **Watch out for:** include the conditions that change the answer (fissured soil, vibration from traffic, previously disturbed soil, seeping water). Your test is only as good as your answer key. In real work, soil is classified by a competent person using visual and manual tests — say so.

### E4. Concept images vs. the design brief
**Track:** Evaluate · **Sub-discipline:** Architecture / ARCE · ★★
- **Question:** Do AI image generators follow a design brief's checkable constraints (number of stories, approximate window-to-wall ratio, shading on the west façade, a stated material)?
- **Data:** images you generate — for example 20 prompts × 3 images each — with any image tool your team can use for free, plus a scoring rubric you write first.
- **Methods:** two raters score every image on every constraint (met / not met); report how often raters agree; compare plain prompts with detailed prompts; note what the images get physically wrong.
- **Baseline:** the plain prompt.
- **Watch out for:** read the tool's terms of use and image-license rules. Do not prompt for a living architect's style or a specific copyrighted building. Images are not designs — they ignore structure, codes, and cost. Free tools change and limit use: record the tool, settings, and dates.

### E5. The wrong-premise test
**Track:** Evaluate · **Sub-discipline:** General CE/ARCE · ★
- **Question:** If a question contains a wrong engineering premise, does the AI correct it or play along?
- **Data:** 30 question pairs your team writes — the same question with a neutral wording and with a wrong premise (for example, "Since a higher water–cement ratio makes concrete stronger, how much water should I add to reach 40 MPa?"). Each wrong premise must be contradicted by a source you cite.
- **Methods:** score each answer as "corrects the premise," "ignores it," or "agrees with it"; compare models; test a system prompt that tells the model to check assumptions; test reworded versions of the same premise.
- **Baseline:** the neutral question with no premise.
- **Watch out for:** fix the scoring rules before you collect answers. Small changes in wording can change results — test at least two wordings per item. This tests *agreeableness*, a known LLM failure mode; connect it to automation bias in your responsible-AI section.

---

## Bringing your own idea

Your own idea is welcome. Before the proposal, check it against these five questions:

1. **Is there data you may use?** Public, clearly licensed, no confidential client data, no personal data (see the [policies](README.md#7-policies)).
2. **Is there a baseline?** If you cannot name a simple thing to beat or compare against, the question is not ready.
3. **Can you measure success?** Name the metric and the test set now.
4. **Does it fit?** Free Colab, about five weeks, three or four people. A small, finished project is better than a big, broken one.
5. **Is there something to verify and something to worry about?** If there is no way to check results and no way for things to go wrong, it is probably not an engineering problem.

Bring the idea to the instructor in the Week 10 or 11 lab, or to office hours, before the proposal is due (Sunday of Week 11).
