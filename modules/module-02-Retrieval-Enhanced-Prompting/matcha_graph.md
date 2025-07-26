# 🧠 Context Engineering Lab · Module 2

## ✫️ Title

**From RAG to Reasoning Graph: Building SQL-Like Semantics over Unstructured Knowledge**

---

## 🧩 Why This Module Matters

Most Retrieval-Augmented Generation (RAG) systems today retrieve chunks of documents and pass them directly to LLMs. While this works for recall, it lacks **structured semantics**, **composability**, and **explainability** — all of which are hallmarks of SQL systems.

In contrast, SQL agents work well not because their prompts are better, but because the **data they're operating on is inherently structured, clean, and compact**.

> This module explores how we can reorganize unstructured data (like documents or web content) into a semantic graph structure to enable **LLM reasoning that approaches SQL-like precision**.

We use a concrete example: **Japanese matcha brand recommendation** — a real-world topic that combines cultural, sensory, and structured product data.

---

## 🌟 Goal

Transform RAG-style unstructured input into a graph-based reasoning system, enabling:

- Precise filtering (e.g., flavor: umami, grade: ceremonial)
- Composable logic (AND/OR reasoning)
- Explainable paths from query to answer
- Aesthetic and emotional activation through presentation-aware structures

---

## 🔧 Architecture Overview

```
Unstructured Documents
   │
   ▼
Chunking → Semantic Normalization Layer → Graph Construction
   │                                      │
   │                                      ▼
   └────▶ Metadata+Embedding Index (Hybrid)
                     │
                     ▼
         LangGraph Agent Reasoning
```

We replace flat chunk retrieval with a **semantic normalization layer**, turning paragraphs into SQL-like views that allow LLMs to reason compositionally across concepts.

---

## 📘 Example: Matcha Brand Knowledge (Structured Views)

### ✦ Semantic View: Ippodo

```json
{
  "brand": "Ippodo",
  "founded_on": "1717",
  "origin": "Kyoto",
  "flavor_profile": ["mellow", "umami"],
  "grade": "ceremonial",
  "positioning": {
    "context": "300+ years of heritage, purveyor to Kyoto’s tea culture",
    "values": ["preservation", "tradition", "hospitality"],
    "actions": [
      "sourcing from historic tea-growing regions",
      "emphasizing taste over branding",
      "providing detailed tea education"
    ]
  },
  "visual_presentation": {
    "design": "understated and formal",
    "imagery": "clean, traditional, minimal",
    "copy_tone": "respectful, instructional"
  },
  "user_quotes": [
    "Their store feels like a tea museum.",
    "I trust them completely for ceremonial tea."
  ]
}
```

### ✦ Semantic View: Marukyu Koyamaen

```json
{
  "brand": "Marukyu Koyamaen",
  "founded_on": "1704",
  "origin": "Uji, Kyoto",
  "flavor_profile": ["refined", "umami-rich"],
  "grade": "high-end ceremonial",
  "positioning": {
    "context": "Top-tier matcha maker supplying temples and tea schools",
    "values": ["craftsmanship", "prestige", "quality control"],
    "actions": [
      "multi-generational refinement of technique",
      "partnering with shrines and tea schools",
      "maintaining high purity standards"
    ]
  },
  "visual_presentation": {
    "design": "classic Japanese",
    "imagery": "awards, temple usage, expert reviews",
    "copy_tone": "formal, authoritative"
  },
  "user_quotes": [
    "This is the matcha used in official tea ceremonies.",
    "Their highest-end blends are museum-level."
  ]
}
```

### ✦ Semantic View: Naoki Matcha

Instead of relying on raw chunks, we extract and normalize brand information into structured semantic views like:

```json
{
  "brand": "Naoki Matcha",
  "founded_on": "2015",
  "origin": "Chiran, Kagoshima",
  "flavor_profile": ["creamy", "hazelnut", "umami"],
  "grade": "ceremonial",
  "cultivar": "Seimei",
  "positioning": {
    "context": "response to overhyped superfood marketing and lack of standards",
    "values": ["transparency", "education", "versatility"],
    "actions": [
      "partnering with small tea estates",
      "explaining blend logic and cultivars",
      "publishing accessible brewing guides"
    ]
  },
  "visual_presentation": {
    "design": "minimalist, modern",
    "imagery": "high-quality product photos",
    "copy_tone": "gentle, educational, user-centered"
  },
  "user_quotes": [
    "I have tried more than 10 brands but I always go back to Naoki Matcha.",
    "They explain so much about where it comes from and how it's made."
  ]
}
```

---

## 🧠 Semantic Normalization Strategy

The core strategy for bridging RAG with structured reasoning:

> **Convert freeform descriptions → queryable, composable, structured views**

### Types of Fields to Extract:

- Brand philosophy / founding story
- Value propositions and differentiators
- Tea origin and cultivar metadata
- Design language and emotional tone
- Website structure and content hierarchy
- Customer voice and sentiment clusters

### Why It Matters:

- Captures brand aesthetic and positioning
- Enables value-aligned recommendation
- Activates subjective resonance like “匠心” or “真诚”

---

## 🧠 User-Level Semantic Interpretation (Now Presentation-Aware)

```json
{
  "user": "weid336",
  "rag_result_sequence": ["Ippodo", "Marukyu Koyamaen", "Naoki Matcha"],
  "perceived_differences": {
    "Naoki Matcha": {
      "aesthetic_impression": "clean site, thoughtful photos, carefully written copy",
      "values_matched": ["匠心", "真诚", "注重教育"],
      "presentation_strengths": ["brand story surfaced", "layout user-centered", "emotional language present"]
    }
  },
  "final_choice": "Naoki Matcha",
  "reasoning_trace": [
    { "step": "presented via RAG", "brand": "Naoki Matcha" },
    { "step": "user explored site" },
    { "step": "detected emotional resonance" },
    { "step": "matched to personal values" },
    { "step": "emerged intent: purchase" }
  ]
}
```

---

## 🔍 From SQL to Graph Mapping

| SQL Concept | Graph Equivalent                                       |
| ----------- | ------------------------------------------------------ |
| Table       | Node Type (e.g., Brand)                                |
| Row         | Node Instance (e.g., "Naoki Matcha")                   |
| Column      | Node Property (e.g., flavor\_profile)                  |
| WHERE       | Subgraph Filter (e.g., values includes 'transparency') |
| JOIN        | Edges between nodes (e.g., brand → origin)             |

---

## 🧠 Why Graphs Help

- **Semantic compression**: only retain meaningful structure
- **Modular reasoning**: chain small steps (LangGraph!)
- **Explainability**: return not just answers but reasoning paths
- **Better alignment**: system structure ↔ user interpretation
- **Presentation-aware inputs**: aesthetics and emotion enter the context

---

## ✅ Evaluation

To highlight the value of structure, compare:

- 🔹 Raw chunk-based RAG: outputs may be factual but flat
- 🔸 Graph+View RAG: semantically and emotionally layered

Evaluate:

- Alignment to user preference
- Accuracy and traceability of reasoning
- Presentation match and trust

### 🧪 Prototype Code: Matching Views with User Intent
<pre> <code>
user_query_intent = {
    "values": ["transparency", "education"],
    "flavor_profile": ["umami"],
    "grade": "ceremonial",
    "design_pref": "modern"
}
</code> </pre>

<pre> <code>
def match_score(view, intent):
    score = 0
    if view["grade"] == intent["grade"]:
        score += 1
    if any(val in view["flavor_profile"] for val in intent["flavor_profile"]):
        score += 1
    if any(val in view["positioning"]["values"] for val in intent["values"]):
        score += 1
    if intent["design_pref"] in view["visual_presentation"]["design"]:
        score += 1
    return score

ranked = sorted(views, key=lambda v: match_score(v, user_query_intent), reverse=True)
</code> </pre>

✅ Output:
Naoki Matcha ranked first, matching on transparency, education, umami flavor, and modern design


---

## 🚀 Optional Extension

- Scaffold a working LangGraph agent using the structured views

  - Node 1: `QueryParser` — parses values and style preferences from natural query
  - Node 2: `ViewFilter` — filters brand views by values and grade
  - Node 3: `TraceExplainer` — constructs semantic reasoning trace for top recommendation
  - Flow: `START → QueryParser → ViewFilter → TraceExplainer → END`

- Scrape actual websites and build `site_structure.json`

- Extract `brand_story`, `visual_cues`, and `navigation_flows`

- Add `customer_review_sentiment_nodes`

Example user query for graph agent:

> "I want a matcha brand that’s with artisan spirit and feels honest, not too traditional."

System should traverse the views, match for `values` and `design`, and explain why Naoki is preferred based on tone, brand story, and visual style alignment.

- Scrape actual websites and build `site_structure.json`
- Extract `brand_story`, `visual_cues`, and `navigation_flows`
- Add `customer_review_sentiment_nodes`

---

## 🔺 System Challenges, and Why Consulting Structure Helps

While implementing a semantic normalization layer introduces significant technical and design complexity, it also provides an opportunity to approach system reasoning not just as software engineering, but as structured problem-solving.

Using consulting frameworks (like TOSCA, MECE decomposition, hypothesis trees, stakeholder mapping, and phased rollout logic), we can bring the same clarity and execution rigor to AI system design as we would in business transformation projects.

---

## 💬 Reflections

> This module embodies the shift from “finding text” to **building reasoning-ready, emotionally-aware views**.

A real RAG system must surface not just facts, but also what makes people **believe**, **feel**, and **choose**.

---

## 🧠 Daily Quote

"Graph is the new prompt. But views are what make prompts beautiful." — Weid336, after realizing context is architecture 🪜

