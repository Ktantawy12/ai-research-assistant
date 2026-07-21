# 📚 AI Research Assistant

An AI-powered research assistant that combines **Retrieval-Augmented Generation (RAG)** with **OpenAlex** to answer questions from local research papers and discover academic literature through natural language.

Built with **LangGraph**, **LangChain**, **OpenAI GPT-4.1 Mini**, **ChromaDB**, **MCP**, and **Streamlit**.

---

## 🚀 Live Demo

🌐 **Application:** *(Coming Soon)*

🎥 **Video Demo:** *(Coming Soon)*

---

## ✨ Features

- 📄 Answer questions from uploaded research papers using RAG
- 🔍 Perform semantic document retrieval with ChromaDB
- 🤖 Multi-agent workflow powered by LangGraph
- 📚 Search academic papers using OpenAlex
- 🌟 Discover seminal papers
- 🤝 Find related research papers
- 🕸️ Explore citation networks
- 💬 Simple Streamlit chat interface

---

## 🏗️ Architecture

```text
                    User
                      │
              Streamlit Interface
                      │
                  LangGraph
                      │
                  Router Agent
         ┌────────────┴────────────┐
         │                         │
     RAG Agent              Citation Agent
         │                         │
  Retriever + ChromaDB      Citation Tool
         │                         │
   Local Research Papers     OpenAlex MCP Server
         │                         │
         └────────────┬────────────┘
                      │
                GPT-4.1 Mini
                      │
                 Final Response
```

---

## 📁 Project Structure

```text
ai-research-assistant/
│
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
├── data/
├── chroma_db/
│
└── src/
    ├── agents/
    ├── chunking/
    ├── embeddings/
    ├── graph/
    ├── llm/
    ├── loaders/
    ├── mcp/
    ├── rag/
    ├── retrieval/
    ├── tools/
    └── vectordb/
```

---

## ⚙️ Tech Stack

### Artificial Intelligence

- OpenAI GPT-4.1 Mini
- LangChain
- LangGraph
- OpenAI Embeddings

### Retrieval

- Retrieval-Augmented Generation (RAG)
- ChromaDB
- Semantic Search

### Academic Search

- OpenAlex
- Model Context Protocol (MCP)

### Frontend

- Streamlit

### Language

- Python

---

## 🔄 Workflow

1. User asks a question.
2. The Router Agent determines the appropriate workflow.
3. If the question is about uploaded documents:
   - Retrieve relevant chunks from ChromaDB.
   - Generate an answer using GPT-4.1 Mini.
4. If the question requires academic search:
   - Query OpenAlex via MCP.
   - Format and return the results.
5. Display the response in the Streamlit interface.

---

## 📦 Installation

Clone the repository.

```bash
git clone https://github.com/Ktantawy12/ai-research-assistant.git

cd ai-research-assistant
```

Create a virtual environment.

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv .venv

source .venv/bin/activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
OPENAI_API_KEY=your_openai_api_key
```

---

## 📄 Add Your Documents

Place your research papers inside the `data/` directory.

Example:

```text
data/
├── attention_is_all_you_need.pdf
├── bert.pdf
├── random_forest.pdf
```

---

## 🧠 Build the Vector Database

```bash
python -m src.vectordb.chroma_db --rebuild
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 💡 Example Questions

### RAG

- Summarize this paper.
- What are the key contributions?
- Explain the proposed methodology.
- Compare Random Forest and XGBoost.
- What datasets were used?

### OpenAlex

- Find seminal papers about Graph Neural Networks.
- Search papers about Retrieval-Augmented Generation.
- Show the citation network of Attention Is All You Need.
- Find related papers to BERT.

---

## 📌 Future Improvements

- Upload PDFs directly through the UI
- Hybrid retrieval (semantic + keyword)
- Multi-document collections
- Conversation memory
- Streaming responses
- Source highlighting
- Docker support
- Authentication

---

## 🎯 Skills Demonstrated

- Retrieval-Augmented Generation (RAG)
- Agentic AI
- LangGraph Workflows
- MCP Integration
- Vector Databases
- Semantic Search
- Prompt Engineering
- LLM Application Development
- Python Software Engineering

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Karim Tantawy**

GitHub: https://github.com/Ktantawy12

LinkedIn: *(Add your LinkedIn profile URL)*

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
