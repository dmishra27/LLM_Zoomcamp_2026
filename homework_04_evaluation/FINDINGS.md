# Homework 4 – Findings and Insights

## Objective

The purpose of this homework was to evaluate the effectiveness of different retrieval strategies for Retrieval-Augmented Generation (RAG).

Rather than improving language models, the focus was on measuring retrieval quality using standard Information Retrieval metrics.

---

# Ground Truth Generation

Ground-truth questions were generated from the first three lesson pages using structured outputs from GPT.

Results:

- Lessons processed: **3**
- Questions per lesson: **5**
- Total generated questions: **15**
- Average input tokens: **1357**

Homework Answer:

**Q1 → 1400**

---

# Keyword Search

Keyword search retrieves documents based on lexical similarity.

Observation:

Although keyword search often retrieved relevant documents, the highest-ranked result was not always the original lesson.

For the first evaluation query:

Expected lesson:

```
01-agentic-rag/lessons/01-intro.md
```

Retrieved:

```
01-agentic-rag/lessons/03-rag.md
```

This demonstrates the limitations of exact word matching.

Homework Answer:

**Q2**

```
01-agentic-rag/lessons/03-rag.md
```

---

# Semantic Vector Search

Semantic search retrieves documents using embedding similarity.

Unlike keyword search, vector search correctly retrieved the original lesson.

Top result:

```
01-agentic-rag/lessons/01-intro.md
```

This illustrates how semantic embeddings capture meaning rather than exact wording.

Homework Answer:

**Q3**

```
01-agentic-rag/lessons/01-intro.md
```

---

# Keyword Search Performance

Metric:

Hit Rate

Computed value:

```
0.7583333333333333
```

Rounded:

```
0.76
```

Interpretation:

Approximately **76%** of evaluation questions retrieved the correct lesson within the Top-5 search results.

Homework Answer:

**Q4 → 0.76**

---

# Vector Search Performance

Metric:

Mean Reciprocal Rank (MRR)

Computed value:

```
0.5486111111111112
```

Rounded:

```
0.55
```

Interpretation:

Semantic search generally ranks the correct lesson significantly higher than keyword search.

Homework Answer:

**Q5 → 0.55**

---

# Hybrid Search

Hybrid Search combines lexical and semantic retrieval using Reciprocal Rank Fusion (RRF).

The following RRF values were evaluated:

| k | MRR |
|---:|----:|
| 1 | 0.645833 |
| 50 | **0.646759** |
| 100 | 0.646759 |
| 200 | 0.646759 |

Homework Answer:

**Q6 → 50**

---

# Key Learnings

This homework demonstrated several important Information Retrieval concepts.

## 1. Better retrieval improves RAG

A stronger retrieval system often produces better answers than simply using a larger language model.

---

## 2. Semantic search outperforms lexical search

Embedding-based retrieval successfully handled paraphrased questions that keyword search could not rank correctly.

---

## 3. Ranking matters

MRR captures ranking quality, making it a more informative metric than Hit Rate when evaluating Retrieval-Augmented Generation systems.

---

## 4. Hybrid retrieval is most robust

Combining keyword search with semantic search consistently produced the highest retrieval performance.

---

## 5. RRF is simple but highly effective

Reciprocal Rank Fusion significantly improved retrieval quality without requiring additional model training.

---

# Final Homework Answers

| Question | Answer |
|-----------|--------|
| Q1 | 1400 |
| Q2 | 01-agentic-rag/lessons/03-rag.md |
| Q3 | 01-agentic-rag/lessons/01-intro.md |
| Q4 | 0.76 |
| Q5 | 0.55 |
| Q6 | 50 |

---

# Overall Reflection

This homework reinforced the importance of retrieval evaluation in modern RAG systems.

Rather than relying solely on qualitative inspection, retrieval systems should be measured using quantitative metrics such as Hit Rate and Mean Reciprocal Rank (MRR). The experiments demonstrated that semantic search substantially improves ranking quality over keyword search, while hybrid retrieval using Reciprocal Rank Fusion offers the strongest overall performance by combining the strengths of both approaches.