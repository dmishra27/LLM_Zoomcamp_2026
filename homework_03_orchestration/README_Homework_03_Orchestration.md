LLM Zoomcamp 2026 – Homework 03
Workflow Orchestration with Kestra
Student: Debabrata Mishra
Repository
homework_03_orchestration/
________________________________________
1. Objective
The objective of this homework was to understand how Large Language Models can be orchestrated using Kestra workflows.
The exercise covered:
•	Standard LLM interaction 
•	Retrieval-Augmented Generation (RAG) 
•	Web Search based RAG 
•	AI Agents 
•	Tool-using Agents 
•	Multi-Agent orchestration 
•	Token monitoring 
•	Workflow execution monitoring 
________________________________________
2. Environment Setup
The following environment was used.
Component	Version
Windows 11	Local
Docker Desktop	Running
Kestra	Local Docker deployment
Gemini Model	gemini-2.5-flash
AI Provider	Google Gemini API
Browser	Chrome
GitHub	Homework repository
The Gemini API key was configured as a Kestra Secret:
GEMINI_API_KEY
The workflows were executed locally through
http://localhost:8080
________________________________________
3. Kestra Workflow Overview
The homework demonstrates progressively more capable orchestration patterns.
1_chat_without_rag

↓

2_chat_with_rag

↓

3_rag_with_websearch

↓

4_simple_agent

↓

5_web_research_agent

↓

6_multi_agent_research
The progression moves from a plain LLM toward autonomous multi-agent workflows.
________________________________________
4. Description of the Six Flows
Flow 1 — Chat without RAG
Purpose
Demonstrate an LLM responding only from its pretrained knowledge.
Observed behaviour
•	Generic response 
•	Hallucinated several Kestra 1.1 features 
•	No access to release documentation 
•	Lower factual accuracy 
This illustrates why an LLM without retrieval cannot reliably answer questions about recent software releases.
________________________________________
Flow 2 — Chat with RAG
Purpose
Ground the LLM using retrieved Kestra documentation.
Observed behaviour
The response correctly identified:
•	New Filters 
•	No-Code Dashboard Editor 
•	Multi-Agent AI Systems 
•	Fix with AI 
•	Human Task 
•	Air-Gapped Support 
•	New Plugins 
The answer became significantly more accurate because the model relied on retrieved documentation rather than memory.
________________________________________
Flow 3 — RAG with Web Search
Purpose
Retrieve live information from the web before generating the answer.
Observed behaviour
The workflow successfully used web search to obtain current Kestra information.
Advantages
•	Current information 
•	More accurate than static model knowledge 
•	Useful for fast-changing domains 
Limitations
•	Internet dependency 
•	Longer execution 
•	External API usage 
________________________________________
Flow 4 — Simple Agent
Purpose
Demonstrate prompt-controlled AI agents.
The workflow contained two agents.
Agent 1
Creates a multilingual summary.
Configurable parameters
•	short 
•	medium 
•	long 
Languages
•	English 
•	French 
•	German 
•	Spanish 
•	Portuguese 
•	Japanese 
Agent 2
Converts the output into a concise English summary.
This demonstrates sequential agent chaining.
________________________________________
Flow 5 — Web Research Agent
Purpose
Demonstrate an autonomous tool-using AI agent.
Unlike a traditional workflow, the agent decides:
•	what to search 
•	how many searches are required 
•	how to organize findings 
•	when research is complete 
The workflow also saves the research report as a Markdown document.
This represents Goal → Reasoning → Tool Usage → Final Report.
________________________________________
Flow 6 — Multi-Agent Research
Purpose
Demonstrate agent collaboration.
Architecture
Main Analyst Agent
↓
Research Agent
↓
Web Search
↓
Report Generation
The main agent delegates information gathering to a specialized research agent before synthesizing the final report.
This modular architecture is easier to extend and maintain than placing all logic inside one agent.
________________________________________
5. RAG vs Non-RAG Comparison
Without RAG
Observed
•	Generic answer 
•	Hallucinated features 
•	Used outdated knowledge 
•	Less trustworthy 
The model attempted to answer from training data alone.
________________________________________
With RAG
Observed
•	Accurate release features 
•	Context grounded 
•	Higher factual correctness 
•	Better reliability 
The retrieved Kestra documentation substantially improved response quality.
Conclusion
RAG dramatically improves factual accuracy for documentation-based question answering.
________________________________________
6. Web Search RAG Observations
Unlike static RAG, Web Search RAG can retrieve current information.
Advantages
•	Latest releases 
•	Current announcements 
•	Dynamic knowledge 
•	Better for frequently changing domains 
Trade-offs
•	Additional latency 
•	External API dependency 
•	Higher execution cost 
________________________________________
7. Simple Agent Behaviour
The simple agent demonstrated:
•	Prompt engineering 
•	Configurable output length 
•	Multilingual responses 
•	Agent chaining 
•	Token monitoring 
The second agent reused the first agent's output instead of regenerating information.
This illustrates modular workflow design.
________________________________________
8. Web Research Agent Behaviour
Unlike a deterministic workflow, the research agent autonomously:
•	selected searches 
•	gathered evidence 
•	synthesized findings 
•	produced a structured report 
The user specifies only the goal.
The agent determines the execution strategy.
________________________________________
9. Multi-Agent Workflow Pattern
The final workflow demonstrated specialization.
Instead of a single large prompt,
Main Agent
↓
Research Agent
↓
Tool
↓
Result
This separation improves
•	maintainability 
•	modularity 
•	scalability 
•	agent reuse 
This architecture is closer to production AI systems.
________________________________________
10. Token Usage Analysis
Multiple executions were performed.
Observed multilingual agent outputs:
Run	Output Tokens
Long summary	172
Long summary	195
Short summary	86
3-sentence version	73
English Brevity Agent
Typical output ranged between
44–68 tokens
Observations
•	Longer prompts increase token consumption. 
•	Shorter summaries reduce overall cost. 
•	Token monitoring is useful for production budgeting. 
•	Minor variations occur because LLM outputs are stochastic. 
________________________________________
11. Gemini API Quota Limitation
During experimentation, the following error occurred:
RESOURCE_EXHAUSTED
Reason
Google Gemini Free Tier daily request quota was exceeded.
Example message
Quota exceeded

generate_content_free_tier_requests

Model

gemini-2.5-flash
Resolution
•	Wait for quota reset 
•	Retry after suggested delay 
•	Upgrade billing if higher throughput is required 
This limitation prevented repeating one comparison run, but sufficient earlier executions were available to complete the analysis.
________________________________________
12. Troubleshooting Notes
Several issues were encountered during the homework.
Gemini quota exceeded
Cause
Free-tier request limit.
Resolution
Wait for quota reset.
________________________________________
Token count variability
Repeated executions produced slightly different token counts.
Reason
LLMs generate non-deterministic responses.
________________________________________
Flow failures
Some executions failed due to external API limitations rather than workflow logic.
________________________________________
Prompt modification
The second agent prompt was changed from
Generate exactly 1 sentence
to
Generate exactly 3 sentences
to observe token usage differences.
________________________________________
13. Conclusions
This homework demonstrated the evolution from simple LLM prompting to production-oriented AI workflow orchestration.
Key learnings include:
•	RAG improves factual accuracy by grounding responses in retrieved documents. 
•	Web Search RAG extends this capability with current information. 
•	AI Agents can autonomously plan and execute tasks based on goals rather than fixed instructions. 
•	Multi-agent systems enable modular, specialized collaboration that is more maintainable than monolithic prompts. 
•	Monitoring token usage is essential for controlling operational cost. 
•	External service limits, such as Gemini free-tier quotas, must be considered when designing production workflows. 
Overall, Kestra provides a flexible orchestration platform for integrating LLMs, retrieval systems, web search, and autonomous agents into reproducible workflows suitable for modern AI applications.
________________________________________
Repository Structure
homework_03_orchestration/
│
├── flows/
│   ├── 1_chat_without_rag.yaml
│   ├── 2_chat_with_rag.yaml
│   ├── 3_rag_with_websearch.yaml
│   ├── 4_simple_agent.yaml
│   ├── 5_web_research_agent.yaml
│   └── 6_multi_agent_research.yaml
│
├── screenshots/
│   ├── flow_list.png
│   ├── chat_without_rag.png
│   ├── chat_with_rag.png
│   ├── rag_websearch.png
│   ├── simple_agent_tokens.png
│   ├── web_research_agent.png
│   └── multi_agent_research.png
│
├── logs/
│   ├── rag_execution.txt
│   ├── web_research_execution.txt
│   └── multi_agent_execution.txt
│
├── notes/
│   └── observations.md
│
└── README.md
This report is appropriate as both your repository README.md and as the basis for a polished submission document (Word or PDF) accompanying your Homework 3 GitHub repository.

