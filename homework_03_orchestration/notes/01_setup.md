# Lesson 03 – Setting up Kestra

---

# Objective

Install and configure Kestra locally so that AI workflows can be developed and executed.

---

# Environment

Operating System

- Windows 11

Editor

- Visual Studio Code

Shell

- PowerShell

Repository

- LLM_Zoomcamp_2026

Docker

```powershell
docker --version
docker compose version
docker ps
```

---

# Project Structure

```text
LLM_Zoomcamp_2026

├── homework_03_orchestration
├── kestra
│   ├── flows
│   └── data
```

---

# Kestra Installation

(To be completed during the lesson)

- Download Docker Compose file
- Configure environment variables
- Start Docker containers

Commands:

```powershell
docker compose up -d
```

---

# AI Provider

Model Provider

- Google Gemini

Authentication

- Gemini API Key

Storage

- Environment Variable / Kestra Secret

(Never commit API keys.)

---

# Importing Flows

Imported:

- 1_chat_without_rag.yaml
- 2_chat_with_rag.yaml
- 4_simple_agent.yaml

---

# Verification

Checklist

- [ ] Docker running
- [ ] Kestra UI opens
- [ ] AI Copilot available
- [ ] Gemini configured
- [ ] Example flows imported
- [ ] Example flow executes successfully

---

# Screenshots

- kestra_home.png
- imported_flows.png
- first_execution.png

---

# Lessons Learned

(To be completed after setup.)
