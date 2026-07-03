# Lesson 02 – Context Engineering

## Core Idea

The quality of AI output depends primarily on the quality of the context provided to the model.

---

## Prompt vs Context

A prompt tells the model what to do.

Context provides the knowledge needed to perform the task correctly.

---

## Problems Without Context

- Outdated plugin syntax
- Incorrect property names
- Hallucinated features
- Outdated APIs
- Missing best practices

---

## Why Generic ChatGPT Fails

Generic LLMs rely mainly on their training data, which has a knowledge cutoff and may not include the latest software versions or organisation-specific information.

---

## Why Kestra AI Copilot Performs Better

Kestra AI Copilot automatically provides:

- Current Kestra documentation
- Workflow schema
- Plugin documentation
- Best practices
- Version-specific syntax

This enables the model to generate more accurate and production-ready workflows.

---

## Connection to Previous Modules

Module 1:
RAG retrieves relevant documents.

Module 2:
Vector search retrieves the most relevant context.

Module 3:
Context Engineering supplies the LLM with the information required to generate correct workflows.

---

## Key Takeaway

Prompt + Context → Reliable AI

Prompt without Context → Guessing and hallucinations

## Practical Experiment

Flow 1 (Without RAG)

- LLM answered using training data only.
- Response was generic and included inaccurate or fabricated features.
- Demonstrated hallucination due to lack of context.

Flow 2 (With RAG)

- Retrieved Kestra 1.1 documentation before answering.
- Response was accurate, detailed, and grounded in the retrieved context.
- Demonstrated how RAG improves reliability.

### Key Learning

LLMs do not automatically know the latest software documentation.

Reliable AI = Prompt + Retrieved Context

Without context:
Prompt → LLM Memory → Guessing

With RAG:
Prompt → Retrieve Documents → LLM → Grounded Answer