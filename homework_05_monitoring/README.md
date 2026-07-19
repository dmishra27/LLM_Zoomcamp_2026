# LLM Zoomcamp 2026 – Homework 5: Monitoring

## Overview

This project implements the Monitoring module from **DataTalksClub LLM Zoomcamp 2026**.

Unlike the previous modules that focused on Retrieval-Augmented Generation (RAG) development and offline evaluation, this module introduces **production monitoring and observability** for LLM-powered applications.

The goal is to understand how a RAG application behaves once real users begin interacting with it by collecting runtime metrics, storing conversations, capturing user feedback, and visualising system performance through monitoring dashboards.

---

# Problem Statement

Offline evaluation provides useful benchmarks, but it cannot fully capture how an AI application performs in production.

Once deployed, important operational questions arise:

- How many requests are being processed?
- How much does each LLM call cost?
- How long do responses take?
- Which conversations receive negative feedback?
- How can poor responses be identified and investigated?

This project addresses these challenges by building a monitoring pipeline for a Retrieval-Augmented Generation application.

---

# Learning Objectives

The objectives of this homework are to:

- Build an interactive Streamlit chat application
- Capture traces and runtime metrics
- Monitor OpenAI token usage and cost
- Store conversations in PostgreSQL
- Collect user feedback
- Build monitoring dashboards
- Explore production observability for LLM applications

---

# Current Status

> **Project Status:** 🚧 In Progress

This repository is being developed incrementally while following the LLM Zoomcamp Monitoring module.

The README and findings document will be updated as additional components are implemented.

---

# Planned Components

The completed project is expected to include:

- Streamlit Chat Application
- RAG Assistant
- Runtime Metrics Collection
- PostgreSQL Conversation Storage
- Streamlit Dashboard
- Grafana Dashboard
- User Feedback Collection
- LLM-as-a-Judge Evaluation
- Synthetic Data Generation
- Docker Compose Deployment

---

# Technologies

The project is expected to use:

- Python 3.12
- Streamlit
- OpenAI API
- PostgreSQL
- Docker
- Docker Compose
- Grafana

Additional libraries will be added as the implementation progresses.

---

# Repository Structure

```
homework_05_monitoring/
│
├── README.md
└── FINDINGS.md
```

Additional source code, configuration files, dashboards, and screenshots will be added as development progresses.

---

# Documentation

This homework contains two complementary documents.

| File | Purpose |
|------|---------|
| README.md | Project overview, setup, architecture and implementation summary |
| FINDINGS.md | Experimental observations, homework answers, lessons learned and reflections |

---

# References

- DataTalksClub LLM Zoomcamp 2026
- Module 5 – Monitoring

---

# Author

**Debabrata Mishra**

MSc Data Science – University of Glasgow

LLM Zoomcamp 2026