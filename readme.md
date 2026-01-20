# 🧭 What to Expect

This repository is a 12-week intensive build log. It documents my journey from raw API calls to building autonomous systems that can reason, use tools, and process private data.

Here is how the repository will evolve:

## 🛠️ 1. The Foundations

- **Raw Mechanics**: Understanding tokens, cost optimization, and streaming responses.
- **Tool Use**: Implementing Function Calling so the LLM can actually do things—like calculate math, check weather, or search the web—rather than just talk.

## 🧠 2. Context & Retrieval (RAG)

- **Memory**: Moving beyond short-term chats to Vector Databases (Qdrant).
- **Knowledge**: Building pipelines that let the AI "read" PDFs, Docs, and text to answer questions based on specific data, not just general training.
- **Reasoning**: Using LangGraph to create "ReAct" loops where the AI thinks, acts, and observes until a task is complete.

## 🚀 3. Production & Reliability

- **Advanced Search**: Using Rerankers and Query Rewriting to make retrieval more accurate.
- **System Design**: Moving tasks to the background (Async), handling errors gracefully, and tracking costs.
- **Deployment**: Packaging everything into Docker so it runs anywhere, not just on my machine.

---

**Note**: This is a learning-by-doing repo. Each project is built to be modular, readable, and focused on solving one specific problem in the AI stack. Feedback are welcome as I refine these systems!