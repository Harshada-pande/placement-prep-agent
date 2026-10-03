# 🤖 Placement Prep Agent

A beginner-friendly **Agentic AI project** that helps students prepare for technical interviews by using an LLM agent and custom tools.

The current version demonstrates how an AI agent can understand a student's request, decide which tool to use, execute that tool, and use the result to generate a response.

## 🚀 Project Status

**Version:** v0.1 — Basic Tool-Calling Agent

### Current capabilities

- Understands placement-preparation questions
- Uses a local LLM through Ollama
- Uses LangChain for LLM and tool integration
- Uses LangGraph's agent framework
- Provides DSA preparation topics
- Provides company-specific preparation topics
- Demonstrates agent-based tool selection

### Planned features

- Student state and memory
- Personalized study plans
- Weak-topic tracking
- Days-remaining based planning
- Resume analysis
- Mock interview mode
- RAG over placement notes
- Guardrails and human approval
- Progress tracking

---

# 🧠 What is Agentic AI?

A traditional chatbot generally follows:

```text
User → LLM → Response
```

This project demonstrates an agentic workflow:

```text
User
  ↓
Agent
  ↓
Decide which tool is needed
  ↓
Execute tool
  ↓
Observe tool result
  ↓
Generate final response
```

The important difference is that the agent can choose an action based on the user's request rather than simply generating a response.

---

# 🏗️ Architecture

```text
                    ┌──────────────┐
                    │    Student   │
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │ Placement    │
                    │ Agent        │
                    └──────┬───────┘
                           │
                 ┌─────────┴─────────┐
                 │                   │
                 ▼                   ▼
        ┌─────────────────┐  ┌──────────────────┐
        │ DSA Topics Tool │  │ Company Topics   │
        │                 │  │ Tool             │
        └────────┬────────┘  └────────┬─────────┘
                 │                    │
                 └─────────┬──────────┘
                           ▼
                    ┌──────────────┐
                    │ Final Answer │
                    └──────────────┘
```

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| LangChain | LLM and tool integration |
| LangGraph | Agent workflow |
| Ollama | Running the LLM locally |
| Llama 3.2 | Local language model |

---

# 📁 Project Structure

```text
placement-agent/
│
├── main.py
├── tools.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env.example
```

### `main.py`

Creates the local LLM, registers the tools, creates the agent, and sends a user request to it.

### `tools.py`

Contains the tools available to the agent:

- `get_dsa_topics()`
- `get_company_topics(company)`

### `requirements.txt`

Contains the Python dependencies required to run the project.

### `.gitignore`

Prevents files such as virtual environments, cache files, and secrets from being committed.

---

# ⚙️ Setup

## 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd placement-agent
```

## 2. Install Python dependencies

```bash
pip install -r requirements.txt
```

## 3. Install Ollama

Download Ollama from:

https://ollama.com/

Verify the installation:

```bash
ollama --version
```

## 4. Download the model

```bash
ollama pull llama3.2
```

Test the model:

```bash
ollama run llama3.2
```

Type a question to verify that the model works.

Exit with:

```text
/bye
```

## 5. Run the agent

```bash
python main.py
```

---

# 🧪 Example

### Input

```text
I am preparing for an HSBC technical interview. What topics should I study?
```

### Agent workflow

The agent identifies that company-specific information is needed and calls:

```text
get_company_topics("HSBC")
```

The tool returns:

```text
DSA
OOP
DBMS
Computer Networks
SQL
Behavioral Questions
```

The LLM then uses the tool result to generate the final response.

Example terminal output:

```text
🔧 TOOL CALLED: get_company_topics(HSBC)

Based on the available company information, important areas include:

1. DSA
2. OOP
3. DBMS
4. Computer Networks
5. SQL
6. Behavioral Questions
```

---

# 🔍 How the Agent Works

The agent has access to two tools.

### Tool 1 — DSA topics

```python
get_dsa_topics()
```

Returns important DSA topics such as:

- Arrays
- Strings
- Hashing
- Linked Lists
- Stacks
- Queues
- Binary Trees
- Graphs
- Dynamic Programming

### Tool 2 — Company topics

```python
get_company_topics(company)
```

Returns preparation topics based on the specified company.

For example:

```python
get_company_topics("HSBC")
```

returns topics including:

```text
DSA
OOP
DBMS
Computer Networks
SQL
Behavioral Questions
```

---

# 🎯 Learning Objectives

This project is designed to understand the fundamentals of Agentic AI:

1. What an LLM is
2. What tools are
3. How an LLM can call tools
4. How an agent chooses between tools
5. How LangChain connects models and tools
6. How LangGraph manages agent workflows
7. Why agents differ from traditional chatbots

---

# 🔮 Future Development

The project will gradually evolve into a more complete placement-preparation agent.

### Phase 1 — Basic Agent

- [x] Local LLM
- [x] Tool calling
- [x] DSA tool
- [x] Company preparation tool

### Phase 2 — Student State

- [ ] Store target company
- [ ] Store days remaining
- [ ] Track weak topics
- [ ] Track completed topics

### Phase 3 — Personalized Planning

- [ ] Generate study plans
- [ ] Prioritize weak areas
- [ ] Adapt plans based on progress

### Phase 4 — Advanced Agent

- [ ] Resume analyzer
- [ ] Mock technical interviewer
- [ ] RAG over placement notes
- [ ] Progress tracking
- [ ] Guardrails
- [ ] Human-in-the-loop approval

---

# ⚠️ Current Limitations

This is an educational prototype.

The current version:

- Uses a small predefined set of company information
- Does not retrieve live company information
- Does not permanently remember student information
- Does not analyze resumes yet
- Does not make external actions
- Does not provide guarantees about actual interview questions

---

# 👩‍💻 Learning Purpose

This project is being developed incrementally to understand **Agentic AI, LangChain, LangGraph, tool calling, state, and agent workflows** through a practical placement-preparation use case.