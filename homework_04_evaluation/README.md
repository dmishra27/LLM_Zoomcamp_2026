# LLM Zoomcamp 2026 – Homework 4: Evaluation

## Overview

This homework focuses on **evaluating Retrieval-Augmented Generation (RAG)** retrieval systems rather than building them.

In previous homeworks, we developed:

- Keyword (lexical) search
- Semantic vector search
- Hybrid retrieval using Reciprocal Rank Fusion (RRF)

This assignment measures how effectively these retrieval methods identify the correct lesson pages using a labelled evaluation dataset.

---

## Learning Objectives

The objectives of this homework are to:

- Generate ground-truth evaluation questions using an LLM.
- Evaluate retrieval quality using standard Information Retrieval metrics.
- Compare keyword search and semantic vector search.
- Understand why ranking quality matters in Retrieval-Augmented Generation.
- Improve retrieval performance using Hybrid Search with Reciprocal Rank Fusion (RRF).

---

## Technologies Used

- Python 3.12
- OpenAI API
- Pydantic
- MinSearch
- Sentence Embeddings (all-MiniLM-L6-v2)
- ONNX Runtime
- Pandas
- Jupyter Notebook

---

## Dataset

The homework uses the official **LLM Zoomcamp lesson repository**.

- 72 lesson pages
- 295 document chunks
- 360 ground-truth evaluation questions

Ground truth questions were automatically generated using structured LLM outputs.

---

## Evaluation Metrics

Two Information Retrieval metrics are used throughout this homework.

### Hit Rate

Measures whether the expected document appears anywhere within the Top-k retrieved results.

Higher values indicate better retrieval coverage.

---

### Mean Reciprocal Rank (MRR)

Measures how highly the correct document is ranked.

Documents retrieved nearer the top contribute more to the final score.

MRR is generally considered a stronger metric than Hit Rate because ranking quality directly affects Retrieval-Augmented Generation performance.

---

## Retrieval Systems Evaluated

### Keyword Search

Traditional lexical retrieval using MinSearch.

---

### Semantic Vector Search

Dense embedding retrieval using the **all-MiniLM-L6-v2** embedding model.

---

### Hybrid Search

Combines Keyword Search and Vector Search using **Reciprocal Rank Fusion (RRF)**.

---

## Homework Questions

This notebook answers the following questions:

1. Ground-truth generation
2. Keyword Search evaluation
3. Vector Search evaluation
4. Hit Rate evaluation
5. Mean Reciprocal Rank evaluation
6. Hybrid Search optimisation

---

## Repository Structure

```
homework_04_evaluation/
│
├── Debabrata_Mishra_hw4_LLM_Zoomcamp_2026_evaluation.ipynb
├── README.md
├── INSIGHTS.md
├── evaluation_utils.py
├── rag_helper.py
└── ground-truth.csv
```

---

## Notes

The following helper files are provided by the official LLM Zoomcamp course:

- evaluation_utils.py
- rag_helper.py
- ground-truth.csv

The notebook and analysis are my own implementation of the homework.

---

## Author

**Debabrata Mishra**

MSc Data Science – University of Glasgow

LLM Zoomcamp 2026