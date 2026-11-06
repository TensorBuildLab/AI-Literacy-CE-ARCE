# Week 14 — AI Policy, Ethics, and Professional Practice

**Slides:** [PDF](Week14_AI-Policy-Ethics.pdf) · [PowerPoint](Week14_AI-Policy-Ethics.pptx) · **Lab:** [Lab 14 — AI Policy Workshop](../../labs/lab14-policy-workshop/) · **Homework:** [HW5 — Responsible AI in Practice](../../homework/hw5-responsible-ai-in-practice/) (due Sunday 11:59 pm, Arizona time, at the end of this week)

> Policy changes fast. The facts in this lecture were checked in November 2026. Before you rely on any date or rule, check the current version of the source.

**Before the lecture day:** read the three appendix slides (A1–A3) at the end of the slide deck. They cover intellectual property, the data-classification table, and the course's AI-use labels. The lecture only summarizes them, and Lab 14 starts from the data table.

## Learning objectives

By the end of this week, you can:

1. Explain why AI needs rules, and name the layers: laws, state board rules, standards, society codes of ethics, and organization policies.
2. Describe the EU AI Act's risk tiers and explain why AI used in critical infrastructure is high-risk.
3. Contrast the EU and U.S. approaches to AI regulation, and name NIST AI RMF, ISO/IEC 42001, and ISO/IEC 23894.
4. Tell society codes of ethics (NSPE, ASCE) apart from the state board rules that govern your license, and apply both to AI use and sealing.
5. Spot intellectual-property and data risks, and outline the nine parts of a firm's AI-use policy.

## The big ideas

- **Rules come in layers.**
  - *Laws* are set by governments and are mandatory.
  - *State board rules* govern your license. In Arizona that is the Board of Technical Registration, under A.R.S. Title 32, Chapter 1, and its Rules of Professional Conduct, A.A.C. R4-30-301. Only the state board can discipline a license.
  - *Standards and frameworks* are voluntary unless a contract or law requires them.
  - *Society codes of ethics* (NSPE, ASCE) govern membership and give guidance. A society can censure or expel a member, and NSPE's Board of Ethical Review publishes advisory opinions, but a society cannot take away your license.
  - *Organization policies* come from your firm, client, or university.
  - *Your judgment* covers the cases no rule covers yet.
- **The EU AI Act regulates by risk.** Regulation (EU) 2024/1689 entered into force on 1 August 2024.
  - A few uses are banned.
  - *High-risk* uses must meet strict requirements: risk management, data governance, documentation and logs, information for users, human oversight, accuracy and robustness.
  - Chatbots and AI-generated content have transparency duties. Most AI has no new duties.
  - AI used as a **safety component** in managing road traffic or the supply of water, gas, heating, or electricity is listed as high-risk. The *intended use* decides the tier, not the algorithm.
  - Duties phase in over several years, and a 2026 amendment moved the high-risk dates later. Check the current timeline.
- **The U.S. has no single AI law (as of 2026).** Sector regulators (such as the FTC, FDA, and NHTSA) apply existing law. States are passing their own AI laws, and federal executive-branch policy shifted in 2025. Negligence, contract, privacy, and licensing law apply whether or not AI was involved.
- **Standards turn intentions into a system.**
  - NIST AI RMF 1.0 (2023): Govern, Map, Measure, Manage.
  - ISO/IEC 42001:2023: an AI management system that a firm can be certified against.
  - ISO/IEC 23894:2023: guidance on AI risk management.
- **The codes and the board rules already cover AI.**
  - NSPE's canons: hold paramount public safety, practice only within your competence, be truthful, act as a faithful agent for clients, avoid deception.
  - The ASCE Code (2020): "first and foremost, protect the health, safety, and welfare of the public," and seal only work prepared or reviewed by you or under your responsible charge.
  - Arizona's binding rule, R4-30-301 item 16, is similar: a registrant may not seal documents that were not prepared by the registrant or a bona fide employee.
  - ASCE Policy Statement 573 (2024) and NSPE Position Statement 03-1774 (adopted 2023, revised February 2026) both call AI a tool and say licensed engineers stay responsible.
  - **The seal stays human.** The licensed engineer is responsible for sealed work, whatever tools were used. Treat AI output like a draft from a fast, confident assistant who is sometimes wrong.
- **Ownership and data matter.**
  - The U.S. Copyright Office (2025) says material generated wholly by AI is not protected by copyright; human contributions can be.
  - Whether training AI on copyrighted work is fair use is still being decided in court.
  - The course uses one data-classification scheme everywhere: **Public / Internal / Confidential (client) / Restricted (personal and security-sensitive)**. Each class has its own rules about which AI tools may see it.
- **A firm AI-use policy has nine parts:** purpose and scope, approved tools, data classification, verification and review, disclosure, training, accountability, incident reporting, and a review cycle.
- **Shop-drawing review is part of the EOR's professional service.** The engineer of record (EOR) reviews shop drawings for general conformance with the design and returns an action stamp. In the 1981 Hyatt Regency walkway collapse, a design change made during the shop-drawing process doubled the load on a connection; 114 people died. A common middle ground in practice: AI may *check*; a responsible engineer decides.

## Key terms

| Term | Plain-language meaning |
|---|---|
| EU AI Act | The European Union's broad AI law (Regulation (EU) 2024/1689), which sets duties by level of risk |
| Risk-based regulation | Stricter rules for uses that can cause more harm; light or no rules for low-risk uses |
| High-risk AI | Under the EU AI Act, uses listed in the law (such as safety components of critical infrastructure) that must meet strict requirements |
| Safety component | A part of a system whose failure could endanger people's health or safety, or property |
| Critical infrastructure | Systems society depends on: roads and traffic, water, gas, heating, electricity, digital networks |
| NIST AI RMF | A free, voluntary U.S. framework for managing AI risk: Govern, Map, Measure, Manage |
| ISO/IEC 42001 | An international standard for an AI management system; organizations can be certified to it |
| State board rules | The licensing law and rules of your state's engineering board (in Arizona, the Board of Technical Registration; A.A.C. R4-30-301). Breaking them can cost you your license |
| Code of ethics | A professional society's written duties (NSPE, ASCE). It governs membership. Your license is governed by your state board's rules, which cover many of the same duties |
| Responsible charge | Direct control and personal supervision of engineering work by a licensed engineer |
| Seal (stamp) | A licensed engineer's mark on documents, meaning "I prepared or supervised this, and I am responsible for it" |
| Engineer of record (EOR) | The licensed engineer responsible for a project's design, whose seal is on the design documents |
| Shop drawings | Detailed drawings from a fabricator or contractor showing how a component will be built and installed. The EOR reviews them for general conformance with the design; the EOR does not approve or seal them |
| Action stamp | The EOR's response on a reviewed submittal, typically: No exceptions taken · Make corrections noted · Revise and resubmit · Rejected |
| Delegated design | Part of the design (for example, some steel connections or precast elements) that a specialty engineer designs and seals; the EOR still reviews it |
| Data classification | Sorting information by sensitivity — Public, Internal, Confidential (client), Restricted (personal and security-sensitive) — to decide which tools may use it |
| AI-use policy | An organization's rules for which AI tools may be used, with what data, how output is checked, and who is accountable |

## Read / watch

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

## Check yourself

1. Under the EU AI Act, why might an AI system that controls chlorine dosing at a water-treatment plant be high-risk, while an AI that summarizes the plant's meeting notes is not?
   <details><summary>Answer</summary>The Act classifies AI by its intended use. AI used as a safety component in the supply of water is listed as high-risk (Annex III, critical infrastructure), because its failure could endanger public health. Summarizing meeting notes cannot directly harm anyone, so it is minimal risk with no new duties.</details>

2. Name the four functions of the NIST AI Risk Management Framework, and say whether using it is legally required in the U.S.
   <details><summary>Answer</summary>Govern, Map, Measure, Manage. It is voluntary, unless a contract, client, or regulator requires it.</details>

3. An Arizona PE uses an AI tool to draft a retaining-wall calculation, skims it, and seals the drawings. Which duties are at stake? Which body can act against the engineer's license?
   <details><summary>Answer</summary>The duties at stake: holding public safety paramount, practicing only within competence (you must be able to check the work), and sealing only work prepared or reviewed under your responsible charge. NSPE and ASCE state these duties for their members. Arizona's Board of Technical Registration enforces similar rules (A.A.C. R4-30-301) and is the body that can discipline the license. Skimming is not reviewing. The engineer, not the AI vendor, is professionally responsible.</details>

4. Is an image made entirely by an AI image generator from a one-line prompt protected by U.S. copyright? What could change that?
   <details><summary>Answer</summary>Probably not. The U.S. Copyright Office (2025) says material generated wholly by AI is not protected, and prompts alone are usually not enough. Human creative contributions — selecting, arranging, or modifying the material — can be protected. Decisions are made case by case.</details>

5. List the nine parts of a firm AI-use policy. Then classify a client's geotechnical report using the course's data-classification scheme.
   <details><summary>Answer</summary>The nine parts: purpose and scope; approved tools; data classification; verification and review; disclosure; training; accountability; incident reporting; review cycle. The geotechnical report is <b>Confidential (client)</b> data. It never goes into a public chatbot, and it goes into other tools only if the firm approves and the client contract allows.</details>

## Coming up

- **Lab day — Lab 14:** teams write a one-page AI-use policy for a small CE/ARCE firm from a nine-part template and test it on five scenarios. The second half is a final-project work session. Lab 14 is due Sunday 11:59 pm (Arizona time).
- **Sunday 11:59 pm (Arizona time):** HW5 is due.
- **Next week (Week 15):** synthesis — how the whole course connects, AI in your career, and final-presentation logistics. A quiz on this week opens the Week 15 lecture day.
