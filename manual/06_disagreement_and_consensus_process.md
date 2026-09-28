# Module 6: Disagreement Resolution & Consensus Workflow

## 6.1 Inter-Annotator Disagreement Triggers
An item is flagged for Adjudication when:
1. Two annotators choose **opposite winners** ($Response_A$ vs $Response_B$).
2. The overall rating difference across annotators exceeds **1.5 points** on a 5-point scale.
3. One annotator flags a response as "Unsafe" while another marks it as "Safe".

---

## 6.2 Adjudication Workflow

```
[Annotator 1] ───┐
                 ├───> [ 프로그램 Conflict Detector ] ───> [ Flagged for Adjudication ]
[Annotator 2] ───┘                                                   │
                                                                     ▼
                                                      [ Senior SME Adjudicator Review ]
                                                                     │
                                                                     ▼
                                                      [ Final Consensus Ground Truth ]
```

1. **Tier 1 Audit**: Automated detection flags items with low agreement.
2. **Tier 2 Lead Review**: A Senior AI Annotator/SME reviews the rationale of both annotators without knowing their identities.
3. **Consensus Resolution**: SME writes the final authoritative rating and rationale, which is logged into the Gold Calibration Set.
