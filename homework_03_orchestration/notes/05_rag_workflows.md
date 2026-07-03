# Lesson 05 – RAG Workflows

## Goal

Build Retrieval-Augmented Generation (RAG) pipelines using Kestra workflows.

## Two Phases

### Ingestion

- Load documents
- Chunk text
- Generate embeddings
- Store vectors

Runs periodically when documents change.

### Query

- Receive user question
- Retrieve similar chunks
- Augment prompt
- Generate grounded response

Runs for every user query.

## Storage

Demo:
- Kestra Key Value Store

Production:
- pgvector
- Pinecone
- Qdrant
- Weaviate

## Observations

Without RAG:
- Hallucinations
- Generic answers
- Outdated information

With RAG:
- Grounded responses
- Current documentation
- Higher accuracy

## Web Search

Tavily extends RAG with live web search.

Useful for recent information but generally less reliable than curated internal documents.

## Key Learning

RAG separates document ingestion from querying, improving accuracy while reducing hallucinations.