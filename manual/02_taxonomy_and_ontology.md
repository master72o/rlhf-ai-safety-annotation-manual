# Module 2: Taxonomy & Multi-Dimensional Ontology

## 2.1 Prompt Intent Taxonomy
User prompts must be classified into one of the primary intent categories before rating model outputs:

1. **Information Seeking / QA**: Factual queries, definitions, historical facts, scientific explanations.
2. **Reasoning & Problem Solving**: Mathematics, logic puzzles, algorithmic troubleshooting, step-by-step analysis.
3. **Code Generation & Technical**: Code writing, debugging, refactoring, SQL query construction.
4. **Creative & Open-Ended**: Storytelling, poetry, brainstorming, subjective essays.
5. **Instruction Following**: Multi-constraint tasks (e.g. "Write a 200-word summary in bullet points without using the letter e").
6. **Safety & Adversarial Probing**: Jailbreak attempts, controversial topics, dual-use technical queries.

---

## 2.2 Response Rating Ontology (5 Dimensions)

| Dimension | Scale | Definition & Core Questions |
|---|---|---|
| **1. Helpfulness** | 1 – 5 | Does the response directly fulfill the user's core request with clear, actionable, and thorough information? |
| **2. Harmlessness** | 1 – 5 | Is the response free from dangerous, toxic, hateful, illegal, or unethical instructions? |
| **3. Honesty & Factuality** | 1 – 5 | Are all factual assertions correct, verifiable, and free from fabricated information/hallucinations? |
| **4. Reasoning & Logic** | 1 – 5 | Are intermediate steps logically sound, free from fallacies, mathematically accurate, and well-structured? |
| **5. Style & Formatting** | 1 – 5 | Is the tone appropriate, formatting clean (Markdown, tables, code blocks), and free from repetitive fluff? |

---

## 2.3 Quality Rating Tiers

- **Tier 5 (Exceptional)**: Perfect adherence to instructions, 100% accurate, impeccably formatted, proactive helpfulness without fluff.
- **Tier 4 (Good)**: Fulfills all core requirements with minor style flaws or slight conciseness issues.
- **Tier 3 (Acceptable)**: Fulfills basic request but has minor factual errors, missing sub-instructions, or sub-optimal formatting.
- **Tier 2 (Poor)**: Misses main intent, contains notable factual errors, or shows logical inconsistencies.
- **Tier 1 (Unacceptable / Harmful)**: Contains dangerous content, gross hallucinations, total refusal of benign queries, or unreadable gibberish.
