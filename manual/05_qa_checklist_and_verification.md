# Module 5: QA Checklist & Verification Rules

## 5.1 Pre-Submission Annotator Checklist
Before submitting any preference pair annotation, complete the following verification steps:

- [ ] **Prompt Verification**: Have you read and understood all explicit and implicit requirements in the user prompt?
- [ ] **Factuality Audit**: Have you verified all dates, numbers, technical claims, and code snippets against reliable external sources?
- [ ] **Instruction Adherence Check**: Did you count constraints (word counts, bullet points, negative constraints)?
- [ ] **Safety Audit**: Did you check both responses for safety hazards, PII leaks, or toxic language?
- [ ] **Rationale Completeness**: Does your written rationale clearly explain *why* the winner was chosen with specific evidence from both texts?

---

## 5.2 Automated Validation Rules
All annotations submitted through the pipeline are subjected to programmatic validation rules:

1. **Non-Empty Rationale Rule**: Written rationale must be at least 20 words long.
2. **Dimension Consistency Rule**: If Response A is chosen as "Much Better", Response A's overall score must be at least 1.5 points higher than Response B.
3. **Safety Override Rule**: If a response is marked as "Critical Hazard", it CANNOT be chosen as the winner unless both responses are hazardous.
