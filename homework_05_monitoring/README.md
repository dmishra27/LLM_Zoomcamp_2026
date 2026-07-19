# LLM Zoomcamp 2026 – Homework 5: Monitoring with OpenTelemetry

## Overview

This project implements the **Monitoring** module from **DataTalksClub LLM Zoomcamp 2026**.

Building on the Retrieval-Augmented Generation (RAG) application developed in previous homeworks, this project introduces **observability** using **OpenTelemetry (OTel)**. The RAG pipeline is instrumented with distributed tracing to monitor execution flow, measure latency, and record LLM token usage.

Instead of using a production observability backend such as Jaeger or Grafana Tempo, this homework implements a **custom SQLite span exporter** to understand how OpenTelemetry works internally. The captured traces are stored in a SQLite database and analysed using SQL and Pandas.

---

# Project Objectives

The objectives of this homework are to:

- Instrument an existing RAG application using OpenTelemetry.
- Create nested spans representing different stages of the RAG pipeline.
- Capture execution timing and token usage.
- Export trace data into SQLite.
- Analyse trace data using SQL and Pandas.
- Understand the foundations of production observability for AI systems.

---

# Implemented Components

The completed implementation includes:

- OpenTelemetry instrumentation
- Custom `SQLiteSpanExporter`
- SQLite trace database (`traces.db`)
- Nested spans:
  - `rag`
  - `search`
  - `llm`
- Input and output token monitoring
- SQL-based trace analysis
- Pandas-based token analysis
- Performance measurement of RAG execution

---

# Architecture

```
                    User Query
                         │
                         ▼
                  RAG Pipeline
                         │
        ┌────────────────┼────────────────┐
        ▼                ▼                ▼
      rag             search            llm
                                           │
                                           ▼
                                OpenTelemetry Spans
                                           │
                                           ▼
                               SQLiteSpanExporter
                                           │
                                           ▼
                                     traces.db
                                           │
                                           ▼
                           SQL / Pandas Trace Analysis
```

---

# Technologies

- Python 3.12
- OpenAI API
- OpenTelemetry
- SQLite
- Pandas
- uv

---

# Repository Structure

```
homework_05_monitoring/
│
├── analyse_traces.py
├── FINDINGS.md
├── README.md
├── ingest.py
├── rag_helper.py
├── starter.py
└── Makefile
```

> Local development files such as `.env`, `traces.db`, `__pycache__/`, and virtual environments are excluded from version control using `.gitignore`.

---

# Key Results

The monitoring implementation produced the following observations:

- Three nested spans were successfully captured:
  - `rag`
  - `search`
  - `llm`
- Average LLM latency was significantly higher than retrieval latency.
- Input token counts remained identical across repeated executions of the same query, indicating deterministic retrieval.
- Trace data was successfully exported into SQLite for downstream analysis.

---

# Documentation

This project contains two complementary documents.

| File | Description |
|------|-------------|
| **README.md** | Project overview, architecture, implementation summary and setup |
| **FINDINGS.md** | Technical implementation details, homework answers, debugging notes, observations, and key learnings |

---

# Learning Outcomes

This homework introduced several important observability concepts:

- Distributed tracing using OpenTelemetry
- Span hierarchy and execution flow
- Runtime latency measurement
- Token usage monitoring
- Custom trace exporters
- Trace analysis using SQL and Pandas

These concepts form the basis of production monitoring for modern LLM-powered applications.

---

# Relationship to Previous Homeworks

This homework completes the first stage of the LLM Zoomcamp learning journey.

| Homework | Focus |
|----------|-------|
| Homework 1 | Retrieval |
| Homework 2 | Retrieval-Augmented Generation (RAG) |
| Homework 3 | Evaluation |
| Homework 4 | Agentic AI |
| Homework 5 | Monitoring and Observability |

Together, these projects demonstrate the lifecycle of a production-ready LLM application—from retrieving knowledge and generating grounded responses to evaluating quality, orchestrating autonomous workflows, and monitoring runtime behaviour.

---

# References

- DataTalksClub – LLM Zoomcamp 2026
- Module 5 – Monitoring
- OpenTelemetry Documentation

---

# Author

**Debabrata Mishra**

ACM SIGIR July 2024 Paper "Neural Passage Quality Estimation for Static Pruning" Co-author 

LLM Zoomcamp 2026