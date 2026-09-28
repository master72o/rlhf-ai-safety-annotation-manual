# RLHF & AI Safety Human Annotation Manual

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![PyTest](https://img.shields.io/badge/PyTest-Passing-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)](https://pytest.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

An enterprise-grade, 25-page comprehensive Human Annotation Manual & Operational Standard Operating Procedure (SOP) for Reinforcement Learning from Human Feedback (RLHF), Direct Preference Optimization (DPO), and AI Safety Alignment.

---

## 📖 Manual Structure & Table of Contents

This manual is structured into 8 modular operational modules designed for annotation leads, human feedback specialists, and AI safety auditors:

1. [**Task Definition & Operational Scope**](./manual/01_task_definition.md) — Operational objectives, core annotation paradigms (SFT, Pairwise Preference, Safety Grading), and target quality standards.
2. [**Taxonomy & Multi-Dimensional Ontology**](./manual/02_taxonomy_and_ontology.md) — Hierarchical classification of user intents, response quality dimensions (Helpfulness, Harmlessness, Honesty, Reasoning, Style), and risk categories.
3. [**Rubric Examples & Counter-Examples**](./manual/03_rubric_examples_and_counterexamples.md) — Granular side-by-side preference examples, counter-examples, and scoring criteria across 5 quality tiers.
4. [**Edge Cases & Ambiguity Resolution Strategies**](./manual/04_edge_cases_and_ambiguity_resolution.md) — Systematic resolution rules for dual-use prompts, partial truth, offensive educational queries, and coding bugs.
5. [**Quality Assurance (QA) Checklist & Verification Rules**](./manual/05_qa_checklist_and_verification.md) — Pre-submission checklists, audit protocols, and automated validation rules.
6. [**Disagreement Resolution & Consensus Workflow**](./manual/06_disagreement_and_consensus_process.md) — Inter-annotator disagreement handling, adjudication mechanics, and confidence-weighted consensus algorithms.
7. [**Escalation Rules & Critical Hazard Protocols**](./manual/07_escalation_rules_and_hazard_handling.md) — Emergency escalation matrices for severe safety hazards (CBRN, CSAM, self-harm, cyberattacks).
8. [**Gold-Standard Benchmark Calibration Set**](./manual/08_gold_standard_calibration_set.md) — 10 curated benchmark examples with ground-truth labels, error rationales, and annotator calibration criteria.

---

## 💻 Technical Tooling & Validation

In addition to documentation, this repository provides tooling for annotation software:

- **JSON Schema Config**: [`schemas/annotation_schema.json`](./schemas/annotation_schema.json) for integration into Label Studio, Scale AI, or custom annotation UIs.
- **Gold Dataset**: [`data/gold_calibration_dataset.json`](./data/gold_calibration_dataset.json) containing reference annotations.
- **Validation Script**: `python validator.py` to programmatically verify annotator output JSON files against manual rules.

---

## 🛠️ Quickstart & Usage

```bash
# Install dependencies
pip install pytest

# Run schema validation tool on gold dataset
python validator.py --dataset data/gold_calibration_dataset.json

# Run unit tests
pytest tests/
```
