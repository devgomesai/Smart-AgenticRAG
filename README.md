
<p align="center">
  <h1 align="center">🤖 Smart-AgenticRAG (using LangGraph)</h1>
  <p align="center">A dynamic Retrieval-Augmented Generation agent workflow built with LangGraph</p>
</p>

---

## 🔍 Overview

**Smart-AgenticRAG** is a modular and intelligent agent system designed using **LangGraph**.  
It implements a structured RAG pipeline with distinct phases—**retrieval**, **grading**, **web search**, and **response generation**—to ensure optimal response quality.

---

## 🚦 Workflow Stages

1. 📥 **Retrieve** documents based on the user query  
2. 📊 **Grade** relevance of retrieved documents  
3. 🌍 **Web Search** if documents aren't sufficient  
4. 🧾 **Generate** the final response based on best sources  

---

## 🛠️ Setup

### 📦 Clone the Repo

```bash
git clone https://github.com/gomesjonathan99/Smart-AgenticRAG.git
cd Smart-AgenticRAG
pip install uv
uv venv
.venv\Scripts\activate
````

### 🔐 Environment Setup

Create a `.env` file in the root directory and add:

```env
LANGCHAIN_API_KEY=your-langchain-api-key-here
OPENAI_API_KEY=your-openai-api-key-here
LANGCHAIN_PROJECT=agentic-rag
LANGCHAIN_TRACING_V2=true
TAVILY_API_KEY=your_tavily_api_key
LLM="gpt-3.5-turbo"
```

> 💡 You can get your [LangSmith API key here](https://smith.langchain.com)
> 🧠 Tavily key: [https://app.tavily.com](https://app.tavily.com)

---

### ▶️ Running the App

```bash
uv run  main.py
```

---
