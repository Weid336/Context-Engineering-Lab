# 🧠 Context Engineering Lab · Module 01

## Context Graph Construction

### 📌 Overview

This module explores how to construct context graphs from structured reasoning processes. We focus on converting structured inputs—especially those inspired by consulting frameworks—into machine-operable graphs that enable explainability, reasoning traceability, and modular prompting for LLM systems.

---

## 💼 Case Study: Strategic Positioning of a Matcha Tea Brand

### 🧭 Client Question

> "How can we position our matcha brand as the most trusted Japanese option for US wellness consumers?"

This case demonstrates how a context graph can be derived from a structured consulting-style breakdown of a strategic question.

---

## 🧱 Step 1: Structured Reasoning (Consulting Framework)

We first apply a strategic decomposition framework (inspired by TOSCA / MECE) to identify core drivers behind the client question.

### 🎯 Goal

Establish **trust** among **US wellness consumers** for a **Japanese matcha brand**.

### 🧩 Hypothesized Drivers of Trust

| Category                     | Key Factors                                                               |
| ---------------------------- | ------------------------------------------------------------------------- |
| **Product Authenticity**     | Region of origin (e.g. Uji), ceremonial grade, production method          |
| **Cultural Legitimacy**      | Brand narrative, references to Japanese tea ceremony, preparation ritual  |
| **Wellness Benefits**        | Antioxidants, calm energy, low caffeine, adaptogenic marketing claims     |
| **Social Proof & Aesthetic** | Influencer prep rituals, TikTok visuals, packaging and lifestyle branding |

---

## 🧠 Step 2: Extract Context Graph Nodes

From the structured thinking, we extract context units as **nodes** labeled by type:

```json
[
  { "id": "n1", "type": "goal", "text": "Establish brand trust among US wellness consumers" },
  { "id": "n2", "type": "hypothesis", "text": "Trust in matcha is driven by authenticity and cultural alignment" },
  { "id": "n3", "type": "fact", "text": "Matcha from Uji region in Japan is widely considered highest quality" },
  { "id": "n4", "type": "fact", "text": "US consumers respond positively to ritualistic tea preparation on TikTok" },
  { "id": "n5", "type": "observation", "text": "Ceremonial grade is used both for quality signal and as marketing buzzword" },
  { "id": "n6", "type": "hypothesis", "text": "Visual storytelling about origin and ritual builds perceived trust" },
  { "id": "n7", "type": "action", "text": "Use origin labels (e.g. Uji), matcha ceremony references, and influencer rituals" },
  { "id": "n8", "type": "observation", "text": "Consumers conflate ceremonial quality with aesthetics, not process purity" },
  { "id": "n9", "type": "observation", "text": "Users need visual explanation to understand Uji origin significance" }
]
```

---

## 🔗 Step 3: Construct Graph Edges (Relations)

We define semantic relations between nodes:

```json
[
  { "source": "n2", "target": "n1", "relation": "supports" },
  { "source": "n3", "target": "n2", "relation": "evidences" },
  { "source": "n4", "target": "n6", "relation": "supports" },
  { "source": "n6", "target": "n2", "relation": "supports" },
  { "source": "n5", "target": "n6", "relation": "complicates" },
  { "source": "n8", "target": "n5", "relation": "clarifies" },
  { "source": "n7", "target": "n1", "relation": "answers" },
  { "source": "n9", "target": "n3", "relation": "refines" },
  { "source": "n9", "target": "n6", "relation": "supports" }
]
```

---

## 🧩 Why Use a Context Graph Instead of Just a Framework?

While traditional frameworks like TOSCA or MECE are excellent for human understanding and presentation, they remain largely static and linear. A context graph retains that structure but transforms it into a dynamic, modular, and machine-navigable format.

### 🔍 Capability Comparison

| Feature                     | Consulting Framework (TOSCA/MECE) | Context Graph               |
| --------------------------- | --------------------------------- | --------------------------- |
| Human-readable logic        | ✅ Yes                             | ✅ Yes                       |
| Machine-traversable         | ❌ No                              | ✅ Yes                       |
| Modular LLM input           | ❌ Manual work                     | ✅ Each node is addressable  |
| Multi-hop reasoning         | ❌ One-level trees                 | ✅ Cross-layer logic tracing |
| Explainable decision chains | ⚠️ Requires manual mapping        | ✅ Built-in traceability     |
| Evolvable memory            | ❌ Static docs                     | ✅ Incrementally expandable  |
| Retrieval integration       | ❌ Not applicable                  | ✅ Enables RAG workflows     |

---

### 🧪 Example: Structured Prompt Built from Context Graph

#### 🔧 Breakdown by Node Role

```text
Write promotional copy for a Japanese matcha brand.

Objective (from node n1):
- Build trust among wellness-focused US consumers.

Strategic Hypothesis (from node n2):
- Trust is built through authenticity and cultural connection.

Supporting Evidence (from nodes n3, n4, n6):
- Uji matcha is renowned for quality.
- TikTok users engage with ritualistic matcha preparation.
- Visual storytelling enhances the perception of authenticity.

Tone:
- Calm, health-oriented, culturally respectful.
```

#### 🧠 Graph-Layer Contribution

| Prompt Line          | Derived From | Node Type  |
| -------------------- | ------------ | ---------- |
| Build trust…         | n1           | Goal       |
| Trust is built…      | n2           | Hypothesis |
| Uji matcha…          | n3           | Fact       |
| TikTok ritual…       | n4           | Fact       |
| Visual storytelling… | n6           | Hypothesis |

---

### 🧪 LangChain Dynamic Prompt Template

You can use the graph to auto-populate prompt sections using `jinja2` or `LangChain`'s dynamic templates:

```python
from langchain.prompts import PromptTemplate

prompt_template = PromptTemplate(
    input_variables=["goal", "hypothesis", "evidence"],
    template="""
Write promotional copy for a Japanese matcha brand.

Objective:
{{ goal }}

Strategic Hypothesis:
{{ hypothesis }}

Supporting Evidence:
{% for item in evidence %}- {{ item }}
{% endfor %}

Tone:
Calm, health-oriented, culturally respectful.
"""
)

filled_prompt = prompt_template.format(
    goal=graph["n1"],
    hypothesis=graph["n2"],
    evidence=[graph["n3"], graph["n4"], graph["n6"]]
)
```

---

### 🧪 Example: Cross-Layer Logic Tracing

> A strategy review agent is tasked with validating whether the brand’s current messaging strategy is adequately supported by factual grounding.

The agent traces: `n7 → n1 → n2 ← n6 ← {n3, n4}` If one node breaks (e.g. n3 is no longer valid), the traceability allows a clear impact path.

---

### 🧪 Example: Incrementally Expandable Memory

> New user feedback: “Most users don't understand the significance of Uji unless explained visually.”

→ Add node `n9`, link to `n3` (refines) and `n6` (supports) → This enriches the graph and updates the prompt template accordingly, enabling adaptive messaging.

---

### 📊 Side-by-Side Prompt Output Comparison

| Approach           | Output                                                                                                    | Critique                                        |
| ------------------ | --------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| Naive Prompt       | “Discover the power of Japanese matcha — calming, traditional, full of antioxidants.”                     | Generic, no Uji, no TikTok, not traceable       |
| Graph-Based Prompt | “Sourced from Uji, loved by TikTok for its calming ritual, our matcha connects you to mindful tradition.” | Structured, traceable to `n1`, `n3`, `n4`, `n6` |

---

### 🧠 Summary

> "We extend consulting frameworks into context graphs to preserve the **clarity of human reasoning**, while enabling **machine operability**. Graphs allow each element of strategy to become a modular, retrievable, and traceable context unit. This supports dynamic LLM workflows such as planning, retrieval-augmented prompting, and agent orchestration — all while staying grounded in first-principles reasoning."

---
