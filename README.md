# 🧠 GEN-Ai — From Fundamentals to GenAI Systems

> **A hands-on learning repository tracking my progress across Python, Machine Learning, NLP, and Generative AI — from fundamentals to practical RAG applications.**

This repository has evolved beyond a simple course log. It now contains the code, notebooks, assignments, experiments, datasets, and prototypes I am building while developing my AI/ML foundation and moving toward **LLM and Generative AI engineering**.

The approach is simple:

**Learn → Implement → Experiment → Debug → Understand → Build**

---

## 🚀 Current Progress

I have moved from foundational programming and ML work into practical Generative AI concepts.

### ✅ Covered

- **Python Fundamentals**
  - Core Python programming
  - Problem-solving and scripting
  - Practical implementations

- **Machine Learning**
  - Data preprocessing and exploration
  - Model-building experiments
  - Classification/regression workflows
  - Dataset-based experimentation

- **Natural Language Processing**
  - NLP fundamentals
  - Text-processing concepts
  - Practical experimentation

- **Generative AI**
  - Document loading and processing
  - Text chunking
  - Embeddings
  - Vector search
  - RAG fundamentals
  - LLM-based response generation

### 🔥 Currently Building

A practical **RAG pipeline** that combines:

```text
Documents
    ↓
Document Loading
    ↓
Text Chunking
    ↓
Embeddings
    ↓
FAISS Vector Store
    ↓
Similarity Search
    ↓
Relevant Context
    ↓
LLM
    ↓
Generated Response
```

The current RAG implementation uses **LangChain document loaders, Sentence Transformers, FAISS, and a Groq-hosted LLM** to retrieve relevant information from a local knowledge base and generate a summarized response.

---

## 🏗️ Repository Structure

```text
GEN-Ai/
│
├── 🐍 Python Fundamentals/
│   ├── Python concepts
│   ├── Programs & exercises
│   └── Practical implementations
│
├── 🤖 Machine Learning/
│   ├── DataSets/
│   ├── ML Model Building/
│   └── Experiments & notebooks
│
├── 📝 Natural Language Processing/
│   └── NLP learning & implementations
│
├── 🧠 Generative AI/
│   ├── RAG/
│   │   ├── data/
│   │   ├── notebook/
│   │   ├── src/
│   │   ├── app.py
│   │   └── requirements.txt
│   └── README.md
│
├── 📚 Assignments/
│   └── Course assignments & practical work
│
├── 📄 LICENSE
└── 📖 README.md
```

---

## 🧠 RAG Implementation

The most developed part of the repository currently is the **RAG workspace**.

### Pipeline Components

| Component | Implementation |
|---|---|
| Document Loading | LangChain Community Loaders |
| PDF Processing | PyPDFLoader |
| Text Processing | RecursiveCharacterTextSplitter |
| Embeddings | Sentence Transformers |
| Embedding Model | `all-MiniLM-L6-v2` |
| Vector Store | FAISS |
| Retrieval | Similarity Search |
| LLM | Groq / `groq/compound-mini` |
| Configuration | Environment variables |

### Supported Input Types

The document loader is designed to process:

- PDF
- TXT
- CSV
- XLSX
- DOCX
- JSON

### Example Knowledge Base

The current RAG data includes material related to:

- Pharmacovigilance
- Adverse Drug Reactions
- Drug safety
- Signal detection
- Attention mechanisms
- Embeddings
- Research material
- APIP-related documents

This provides a practical domain for experimenting with retrieval and LLM-assisted question answering.

---

## 🔬 What I Have Learned Through Building

This repository is helping me understand the components behind modern AI applications rather than only using high-level tools.

```text
Python
  ↓
Machine Learning
  ↓
NLP
  ↓
Embeddings
  ↓
Vector Search
  ↓
RAG
  ↓
LLM Applications
  ↓
Agents & Tool Calling
  ↓
Production AI Systems
```

The current focus is around the transition from **ML/NLP fundamentals → LLM application development**.

---

## 📂 Main Learning Areas

### 🐍 Python

Fundamental programming concepts, exercises, scripts, and experiments used as the base for the later AI work.

### 🤖 Machine Learning

Hands-on notebooks, datasets, experiments, and model-building workflows.

### 📝 NLP

Exploring natural language processing concepts that form the foundation for working with text and language models.

### 🧠 Generative AI

Moving into embeddings, retrieval, RAG pipelines, LLM integration, and eventually agentic systems.

### 📝 Assignments

Course-related practical work and implementations maintained alongside the main learning material.

---

## 🎯 Current Direction

The goal is no longer just to complete individual topics.

I am working toward being able to design and build complete AI systems:

```text
Understand the fundamentals
          ↓
Implement the concepts
          ↓
Build small experiments
          ↓
Combine multiple components
          ↓
Build RAG applications
          ↓
Build AI agents
          ↓
Add tool calling & workflows
          ↓
Explore fine-tuning
          ↓
Develop production-ready AI systems
```

---

## 🛠️ Technologies Used So Far

```text
Python
├── NumPy
├── Pandas
├── Scikit-learn
├── Matplotlib
└── Jupyter

NLP / GenAI
├── LangChain
├── Sentence Transformers
├── FAISS
└── Groq

Development
├── Git
├── GitHub
└── VS Code
```

---

## 🧪 Learning Through Building

I intentionally keep experiments, notebooks, assignments, debugging work, and intermediate implementations in this repository.

Some code represents:

- a first implementation of a concept
- an experiment
- a debugging session
- a course assignment
- a prototype
- an intermediate step toward a larger AI system

The repository is therefore a record of **practical progression**, not a collection of only finished projects.

---

## 📈 Roadmap

### ✅ Foundation

- [x] Python fundamentals
- [x] Machine Learning fundamentals
- [x] NLP foundations
- [x] Generative AI fundamentals
- [x] Embeddings
- [x] Vector search
- [x] Basic RAG pipeline

### 🔄 In Progress

- [ ] Improve RAG architecture
- [ ] Better chunking and retrieval strategies
- [ ] Retrieval evaluation
- [ ] Prompt engineering
- [ ] LLM application patterns
- [ ] More practical GenAI projects

### ⏭️ Next

- [ ] Advanced RAG
- [ ] Reranking
- [ ] Hybrid retrieval
- [ ] Agents
- [ ] Tool calling
- [ ] Workflow orchestration
- [ ] Fine-tuning / PEFT
- [ ] Production deployment
- [ ] MLOps for AI applications

---

## 💡 Learning Philosophy

> **Don't just learn the API. Understand the system behind it.**

I use this repository to turn concepts into working code, investigate errors, and connect individual topics into complete systems.

**Theory → Code → Experiment → Debug → Understand → Build**

---

## 📊 Repository Status

This repository is **actively evolving**.

The earlier stages focus more on fundamentals and coursework. The newer work is increasingly focused on **LLMs, RAG, retrieval systems, and practical AI engineering**.

The structure and projects will continue to change as I move deeper into Generative AI.

---

## 🎯 Long-Term Goal

The direction of this repository is toward building a strong foundation in:

**Machine Learning → NLP → LLMs → RAG → Agents → AI Engineering**

Ultimately, I want to be able to take an AI idea from **concept → implementation → evaluation → deployment**.

---

### 🌱 Learn the fundamentals.
### 🧠 Understand the systems.
### 🚀 Build the applications.

**GEN-Ai — Learn → Build → Debug → Repeat.**
