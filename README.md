# CodeLens AI 🔍🤖

CodeLens AI is an intelligent code analysis, review, and documentation assistant. Built with Python, LangChain/RAG capabilities, and modern LLM integrations, it provides automated code reviews, bug detection, complexity evaluation, quality scoring, and interactive Q&A over your codebase.

---

## ✨ Features

- 🛠️ **Automated Code Review:** Scans source code to identify bugs, anti-patterns, and security vulnerabilities.
- 📊 **Quality & Complexity Analysis:** Calculates quality scores and measures cyclomatic/structural code complexity.
- 🧠 **Context-Aware Chat (RAG):** Ask questions about your codebase powered by Retrieval-Augmented Generation.
- 📄 **PDF Report Generation:** Export detailed code health and review reports into clean PDF documents.
- ⚡ **Multi-Language Support:** Detects programming languages and parses ASTs for accurate insights.

---

## 📁 Repository Structure

```text
CodeLens AI/
├── app.py                      # Main application entry point / UI
├── main.py                     # Core operational script
├── requirements.txt            # Project dependencies
├── config/                     # System settings & prompt templates
│   ├── settings.py
│   └── prompts.py
├── backend/
│   ├── chat/                   # Memory and chat conversation services
│   ├── llm/                    # Groq client, chains, and output parsers
│   ├── parser/                 # AST parsing & language detection
│   ├── rag/                    # Vector stores, embeddings, & retriever setup
│   ├── report/                 # PDF report generation
│   ├── reviewer/               # Bug detection, complexity, and quality logic
│   └── services/               # Orchestration services (review, RAG, quality)
└── test_pdf.py                 # Test suite for report generation