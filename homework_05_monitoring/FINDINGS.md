# Homework 5 – Monitoring with OpenTelemetry
## Findings and Key Learnings

**Course:** LLM Zoomcamp 2026  
**Homework:** 05 – Monitoring  
**Repository:** llm-zoomcamp-code/homework_05_monitoring

---

# Objective

The objective of this homework was to instrument the Retrieval-Augmented Generation (RAG) application developed in previous homeworks using **OpenTelemetry (OTel)**.

Rather than improving retrieval quality or agent behaviour, this homework focused on answering an equally important production question:

> **What is happening inside my RAG system while it is running?**

The implementation demonstrated how tracing can be added to an existing application with minimal modifications while exposing valuable runtime metrics such as latency, token usage and execution flow.

---

# Implementation Summary

The monitoring solution was implemented using:

- OpenTelemetry SDK
- TracerProvider
- SimpleSpanProcessor
- Custom SQLiteSpanExporter
- SQLite database as the trace backend

The tracing pipeline was:

```
Application
      │
      ▼
Tracer
      │
      ▼
Span Processor
      │
      ▼
SQLite Exporter
      │
      ▼
traces.db
```

Unlike production systems that send traces to Jaeger, Grafana Tempo or an OTel Collector, this homework intentionally implemented a custom exporter to understand the internal mechanics of OpenTelemetry.

---

# Instrumentation

Three logical spans were created.

## 1. rag span

The highest level span.

It measures the total execution time of the complete RAG pipeline.

```
User Query
      │
      ▼
RAG
```

---

## 2. search span

Measures only retrieval.

```
User Query
      │
      ▼
Search
```

This excludes prompt generation and LLM inference.

---

## 3. llm span

Measures only the interaction with the language model.

It also records:

- input tokens
- output tokens

using

```python
span.set_attribute("input_tokens", usage.input_tokens)
span.set_attribute("output_tokens", usage.output_tokens)
```

---

# SQLite Exporter

Instead of printing spans to the console, a custom exporter was implemented.

Each completed span was written into SQLite.

Schema:

```sql
CREATE TABLE spans(
    name TEXT,
    start_time INTEGER,
    end_time INTEGER,
    input_tokens INTEGER,
    output_tokens INTEGER,
    cost REAL
)
```

This effectively converts runtime telemetry into structured trace data that can later be queried using SQL or analysed with Pandas for performance analysis and debugging.

---

# Debugging Experience

One of the most valuable aspects of this homework was debugging the monitoring pipeline.

Initially:

```
traces.db
```

was created successfully but contained

```
0 spans
```

The root cause was an indentation mistake.

The following methods

- export()
- shutdown()
- force_flush()

were accidentally defined outside the SQLiteSpanExporter class.

Consequently, OpenTelemetry had no exporter implementation to invoke.

Correcting the class structure immediately resolved the issue.

This reinforced an important lesson:

> In observability systems, successful initialization does not necessarily imply successful instrumentation.

---

# Homework Results

## Question 1

Number of spans created

Result:

```
3
```

Spans:

- rag
- search
- llm

---

## Question 2

Input tokens

Observed:

```
7111
```

Closest answer:

```
7000
```

---

## Question 3

LLM latency

Measured:

Approximately

```
4.6 seconds
```

Answer:

```
Over 2000 ms
```

---

## Question 4

SQLite exporter

Successfully implemented.

Database now stores

- span names
- timestamps
- token counts

---

## Question 5

SQL query:

```sql
SELECT
name,
SUM(end_time-start_time)
FROM spans
WHERE name!='rag'
GROUP BY name;
```

Results

```
llm
≈ 4.6 s

search
≈ 7 ms
```

Conclusion:

```
LLM dominates total runtime.
```

---

## Question 6

Repeated the same query four times.

Observed input tokens:

```
7111
7111
7111
7111
```

Standard deviation

```
0
```

Conclusion

```
Input tokens are identical.
```

This indicates deterministic retrieval.

---

# SQL Analysis

SQLite transformed raw traces into queryable performance data.

Example questions that become trivial:

Average LLM latency

```sql
SELECT AVG(end_time-start_time)
FROM spans
WHERE name='llm';
```

Most expensive span

```sql
SELECT *
FROM spans
ORDER BY end_time-start_time DESC;
```

Token usage

```sql
SELECT
AVG(input_tokens),
AVG(output_tokens)
FROM spans;
```

This demonstrates why observability data is typically stored separately from application logs.

---

# Key Learnings

## 1. Monitoring is different from logging

Logging answers

```
What happened?
```

Tracing answers

```
Where did it happen?

How long did it take?

Which operation caused the delay?
```

---

## 2. Nested spans describe execution flow

```
rag
├── search
└── llm
```

This hierarchy immediately reveals where execution time is spent.

---

## 3. LLM inference dominates latency

Retrieval took only a few milliseconds.

Model inference required several seconds.

Therefore optimisation efforts should focus primarily on

- prompt construction
- model choice
- response caching
- batching

rather than retrieval speed.

---

## 4. Token monitoring is essential

Every token represents

- latency
- API cost
- context size

Monitoring token usage enables

- prompt optimisation
- cost estimation
- budget control

---

## 5. Stable retrieval creates predictable prompts

Running the same query four times produced identical input token counts.

This demonstrates that

- retrieval is deterministic
- indexing is stable
- prompt construction is reproducible

This stability is important for debugging, evaluation and benchmarking.

---

## 6. OpenTelemetry separates instrumentation from storage

Instrumentation generates spans.

Exporters determine where those spans go.

Examples

```
Console

SQLite

Jaeger

Grafana Tempo

OTel Collector

Cloud monitoring services
```

Only the exporter changes.

Instrumentation remains identical.

---

# Connecting Homework 1–5

One of the strengths of this course is that each homework builds directly upon the previous one rather than introducing isolated concepts.

## Homework 1 – Retrieval

Focus

```
Find the right information.
```

Built

- indexing
- search
- retrieval

Question answered

> Which documents should the model read?

---

## Homework 2 – RAG

Focus

```
Use retrieved information to generate answers.
```

Built

- prompt construction
- LLM integration

Question answered

> How can retrieved knowledge improve generation?

---

## Homework 3 – Evaluation

Focus

```
Measure answer quality.
```

Introduced

- evaluation metrics
- correctness assessment
- comparison of responses

Question answered

> Is the system producing good answers?

---

## Homework 4 – Agents

Focus

```
Allow the model to reason and use tools.
```

Introduced

- function calling
- iterative reasoning
- agent loops

Question answered

> What should the model do next?

---

## Homework 5 – Monitoring

Focus

```
Observe everything while it runs.
```

Introduced

- tracing
- telemetry
- latency measurement
- token monitoring

Question answered

> What is happening inside the system?

---

# Overall Learning Journey

Viewed together, the first five homeworks represent the major components of a production-grade AI application.

```
Homework 1
Retrieve knowledge
        │
        ▼
Homework 2
Generate grounded responses
        │
        ▼
Homework 3
Evaluate answer quality
        │
        ▼
Homework 4
Enable autonomous reasoning and tool use
        │
        ▼
Homework 5
Monitor, measure and understand the complete system
```

Each stage addresses a different engineering concern:

- **Retrieval** ensures relevant context is available.
- **RAG** grounds model responses in external knowledge.
- **Evaluation** provides confidence in answer quality.
- **Agents** extend the system with reasoning and tool usage.
- **Monitoring** delivers visibility into runtime behaviour, performance and operational cost.

Together these form the foundation of an end-to-end, production-ready LLM application. A system that retrieves information, generates reliable responses, evaluates quality, performs autonomous actions, and exposes detailed telemetry is significantly easier to optimise, debug, scale and maintain.

---

# Final Reflection

This homework demonstrated that building an AI application does not end once the model produces the correct answer. In production, understanding **how** the application behaves is just as important as **what** it returns.

By manually instrumenting the RAG pipeline with OpenTelemetry, exporting traces to SQLite, and analysing latency and token usage, I gained practical experience with observability concepts that underpin modern AI systems. Although this exercise used a lightweight SQLite exporter, the same principles extend directly to enterprise observability platforms such as Jaeger, Grafana Tempo, and cloud-native monitoring solutions.

Across the five homeworks, the course progressed from retrieval and generation to evaluation, autonomous agents and finally monitoring, illustrating the complete lifecycle of a modern LLM application. This progression highlights that successful AI engineering requires not only accurate models, but also robust retrieval, systematic evaluation, intelligent orchestration and comprehensive observability to deliver reliable, scalable and maintainable production systems.

This progression reflects the evolution from building an LLM application that simply works to engineering one that is observable, measurable, maintainable, and ultimately suitable for production deployment.