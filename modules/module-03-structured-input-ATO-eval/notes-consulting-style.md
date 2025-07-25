
## 🧠 Instructional Design Commentary: Consulting-style Prompting

This prompt architecture follows a consulting-style reasoning framework:

| Principle       | Implementation                                                                |
| --------------- | ----------------------------------------------------------------------------- |
| **Complete**    | Covers 5 signal categories: behavioral, device, network, temporal, historical |
| **Conclusive**  | Requires `Likely`, `Unlikely`, or `Ambiguous` output                          |
| **Explainable** | Justification must cite observed signals                                      |
| **Structured**  | JSON format supports auditability and integration                             |
| **Composable**  | Input blocks are modular and can be omitted or dynamically filled             |

This reflects the **CCE** mindset: *Complete, Conclusive, Explainable* — a consulting-derived discipline adapted to prompt design.

This prompt isn't just about guiding the LLM's internal reasoning — it's about controlling the **external presentation of the decision**. By enforcing a JSON schema aligned with consulting-style output (e.g. executive summaries, key signal breakdowns, actionable next steps), we ensure that:

- The model’s output is immediately actionable
- Its reasoning trace is auditable
- Its tone matches high-stakes security reporting environments

This mirrors how consulting teams deliver assessments: structured, justified, and outcome-oriented.


---

## 📊 Prompt Evaluation Plan

- **Human Evaluation**: Security analysts score LLM outputs on relevance, grounding, clarity
- **LLM-as-Judge**: GPT-4 compares outputs across prompt versions (e.g. flat vs modular)
- **Grounding Score**: % of signals mentioned in output that map back to inputs
- **Output Structure Check**: JSON validity, key completeness, formatting accuracy
- **Scenario A/B Testing**: Run multiple variants with different signal strengths

---

## 🔁 Next Steps

- Add prompt variants (v1: flat input, v2: partial context, v3: full + instruction)
- Generate sample outputs for each variant
- Build evaluation dashboard or scoring script

---

## 🔗 Related Modules
- [Module 01: Context Graph Construction](#)
- [Module 02: Retrieval-Enhanced Prompting](#)
- [Module 04: Agent Routing Based on Structured Context](#)

---
