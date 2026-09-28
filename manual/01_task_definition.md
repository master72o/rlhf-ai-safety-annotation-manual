# Module 1: Task Definition & Operational Scope

## 1.1 Operational Objective
The primary objective of this annotation task is to provide high-precision, aligned human preference data to train and fine-tune Large Language Models (LLMs) via Reinforcement Learning from Human Feedback (RLHF) and Direct Preference Optimization (DPO).

Annotators evaluate paired LLM model outputs ($Response_A$ vs $Response_B$) generated from diverse user prompts to select the **Chosen Response** ($y_w$) and **Rejected Response** ($y_l$), alongside granular multi-dimensional scores.

---

## 1.2 Core Annotation Tasks

### Task Type 1: Pairwise Preference Ranking (RLHF / DPO)
- **Input**: User Prompt ($x$), Response A ($y_A$), Response B ($y_B$).
- **Output**: 
  - Overall Winner: `Response A`, `Response B`, or `TIE`.
  - Preference Strength: `Slightly Better`, `Better`, `Much Better`.
  - Dimension Ratings (1–5 scale): Helpfulness, Harmlessness, Honesty, Reasoning Depth, Formatting.
  - Detailed Rationale explaining the decision.

### Task Type 2: Safety & Hazard Grading
- **Input**: User Prompt ($x$), Single Model Response ($y$).
- **Output**:
  - Safety Classification: `Safe`, `Mild Risk`, `Unsafe`, `Critical Hazard`.
  - Hazard Category: Cyberattack, Chemical/Biological/Radiological/Nuclear (CBRN), Self-Harm, Hate Speech, PII Leak.
  - Action Required: `Pass`, `Refusal Required`, `Escalate Immediately`.

### Task Type 3: Supervised Fine-Tuning (SFT) Quality Audit
- **Input**: Prompt ($x$), Reference Answer ($y$).
- **Output**: Multi-aspect error identification (Hallucination, Instruction Following Failure, Formatting Defect, Tone Misalignment).

---

## 1.3 Quality Target & SLA
- **Target Inter-Annotator Agreement (IAA)**: Krippendorff's Alpha $\ge 0.80$, Cohen's Kappa $\ge 0.75$.
- **Gold Standard Audit Accuracy**: $\ge 95\%$ alignment with expert benchmark annotations.
- **Annotation Speed Expectation**: 8–12 complex preference pairs per hour per annotator.
