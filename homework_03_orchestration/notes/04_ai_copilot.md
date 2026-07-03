# Lesson 04 – AI Copilot

## Purpose

Generate Kestra workflows from natural language instead of manually writing YAML.

## Why AI Copilot works better than ChatGPT

- Access to current Kestra documentation
- Latest plugin schemas
- Valid property names
- Correct YAML syntax
- Production best practices

## Iterative Refinement

Workflow generation is conversational.

Example:

Generate workflow

↓

Add ETL label

↓

Add schedule

↓

Add Slack notification

↓

Review & Save

## The 5% Rule

AI generates approximately 95% of the workflow.

Developer completes the remaining 5%:
- secrets
- environment variables
- cloud resources
- retries
- notifications
- validation

## Key Learning

Reliable AI requires context.

AI Copilot combines LLM reasoning with current Kestra documentation to generate executable workflows.