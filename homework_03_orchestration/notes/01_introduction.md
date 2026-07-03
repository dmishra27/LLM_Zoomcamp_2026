# Lesson 01 – Introduction

## Module

Module 3 – AI Orchestration with Kestra

---

# Lesson Objective

This lesson introduces AI orchestration and explains why AI is useful not only for generating workflows but also for making intelligent decisions within workflows.

Unlike the previous modules that focused on Retrieval-Augmented Generation (RAG) and Vector Search, this module focuses on coordinating AI capabilities into production-ready workflows using Kestra.

---

# What problem does AI orchestration solve?

Traditional workflows are deterministic.

They follow predefined steps and always produce the same output given the same input.

Example:

Customer Order

↓

Validate Order

↓

Process Payment

↓

Generate Invoice

↓

Send Email

Every execution follows exactly the same sequence.

However, many real-world business problems require decision making.

Examples include:

- Classifying customer feedback
- Detecting sentiment
- Choosing the appropriate response
- Summarising documents
- Researching information
- Selecting which external tool to use

These tasks cannot easily be expressed using fixed rules.

AI orchestration solves this problem by combining deterministic workflows with AI-powered decision-making.

---

# What is Kestra?

Kestra is an open-source workflow orchestration platform.

It allows users to build, schedule and monitor workflows that integrate:

- APIs
- Databases
- Python scripts
- Cloud services
- AI models
- AI agents
- External tools

Workflows are defined declaratively using YAML.

Kestra manages execution, dependencies, retries, scheduling, logging and observability.

---

# Why use workflows instead of standalone scripts?

Standalone scripts often become difficult to maintain as systems grow.

Typical problems include:

- Hard-coded execution order
- Poor error handling
- Limited observability
- Difficult scheduling
- Difficult retry mechanisms
- Poor scalability

Workflow orchestration platforms solve these problems by separating workflow logic from implementation details.

Benefits include:

- Repeatability
- Scheduling
- Monitoring
- Logging
- Error recovery
- Scalability
- Production readiness

---

# How can AI help with workflows?

AI can assist in two different ways.

## 1. AI generates workflows

Example:

Developer

↓

Prompt

↓

Kestra AI Copilot

↓

Generated YAML Workflow

The AI understands:

- Kestra syntax
- Plugin documentation
- Workflow schema
- Best practices

This reduces boilerplate coding.

---

## 2. AI executes inside workflows

Example:

Workflow

↓

Collect customer review

↓

AI analyses sentiment

↓

Positive?

↓

Yes / No

↓

Continue workflow

Here, AI performs intelligent decision making rather than deterministic execution.

---

# Deterministic vs Non-Deterministic Tasks

## Deterministic

Given identical inputs, the output is always identical.

Examples:

- File copy
- SQL query
- CSV parsing
- API request
- Data transformation

---

## Non-Deterministic

Output depends on reasoning performed by an LLM.

Examples:

- Summarisation
- Classification
- Translation
- Sentiment analysis
- Planning
- Tool selection

AI introduces flexibility into otherwise deterministic workflows.

---

# AI requires context

One of the most important concepts introduced in this lesson is:

> AI is only as useful as the context we provide.

Without context:

- AI guesses
- AI hallucinates
- AI produces outdated answers

With context:

- AI becomes reliable
- AI becomes grounded
- AI produces production-ready outputs

This idea is called **Context Engineering**, which is explored in the next lesson.

---

# Example shown in the lesson

Prompt:

"Create a Kestra flow that loads NYC taxi data from CSV to BigQuery."

ChatGPT generated a workflow that looked almost correct.

However, it contained important implementation errors because it lacked complete knowledge of Kestra's workflow execution model.

For example:

- Missing outputFiles property
- Incorrect assumptions about shared working directories
- Workflow would fail during execution

This illustrates that syntactically correct code may still be operationally incorrect when the model lacks sufficient context.

---

# Module Learning Objectives

By the end of Module 3, I should understand:

- AI Orchestration
- Kestra fundamentals
- Context Engineering
- AI Copilot
- Retrieval-Augmented Generation (RAG) workflows
- AI Agents
- Multi-Agent Systems
- Token usage optimisation
- Production best practices

---

# Key Takeaways

- AI can generate workflows.
- AI can execute tasks inside workflows.
- AI improves productivity by reducing boilerplate.
- Workflow orchestration combines deterministic execution with AI reasoning.
- AI reliability depends on context.
- Context Engineering is fundamental to production AI systems.

                 Traditional Workflow

                     Input
                       │
                       ▼
                  Task 1
                       │
                       ▼
                  Task 2
                       │
                       ▼
                  Task 3
                       │
                       ▼
                    Output



                 AI Orchestrated Workflow

                     Input
                       │
                       ▼
                Deterministic Task
                       │
                       ▼
                 AI Decision Task
                       │
        ┌──────────────┴──────────────┐
        ▼                             ▼
   Positive                    Negative
        │                             │
        ▼                             ▼
   Workflow A                   Workflow B

   Module 1
↓

Build RAG

Module 2
↓

Improve Retrieval

Module 3
↓

Coordinate Everything

Checklist
✔ What problem does AI orchestration solve?

Yes.

Your answer should include:

Traditional workflows are deterministic.
AI introduces intelligent decision making.
AI orchestration combines deterministic workflows with AI-powered reasoning.
AI reduces repetitive boilerplate while enabling decisions that fixed rules cannot easily make.
✔ What is Kestra?

Yes.

Your notes cover:

Open-source workflow orchestration platform.
YAML-based workflows.
Scheduling.
Monitoring.
Logging.
AI integration.
Production workflows.
✔ Why use workflows instead of standalone scripts?

Yes.

You now understand:

Scripts

↓

Hard to maintain

Hard to retry

Hard to observe

Hard to schedule

versus

Kestra

↓

Declarative workflows

↓

Logging

↓

Retries

↓

Scheduling

↓

Monitoring

↓

AI orchestration

✔ What are the module learning objectives?

Yes.

You listed:

Context Engineering
AI Copilot
RAG Workflows
AI Agents
Multi-Agent Systems
Best Practices
Production AI

Exactly what the instructor intended.

Why Kestra AI Copilot performs better than ChatGPT
Generic ChatGPT

Prompt
    │
    ▼
LLM Memory
    │
    ▼
Generated Workflow

↓

versus

Kestra AI Copilot

Prompt
    │
    ▼
Kestra Documentation (.md)

Workflow Schema

Plugin Documentation

Best Practices

Latest Version

    │
    ▼
LLM
    │
    ▼
Generated Workflow

Key insight: The AI model isn't necessarily better; it has better context. This is the core idea behind Context Engineering.
