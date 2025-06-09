# 🧠 RAG-Assist: Assistente Inteligente de RH
**Description:**
The RAG-Assist is an AI app that uses Retrieval-Augmented Generation (RAG) with LangChain, embeddings vetoriais e OpenAI to answer questions about  internal HR policies based on PDF docs. 

<img width="429" alt="image" src="https://github.com/user-attachments/assets/c31de89b-f693-4025-930c-e003de722bf9" />

---

## 🚀 Functionality

- Upload HR PDF doc (vacation policy, benefits policy, etc.)
- Automatic indexation to vector db
- Streamlit Interface to questions/answers
- Answer generation with LangChain + OpenAI
- Show answer source (transparency)
- CI/CD by GitHub Actions (WIP)
- Public deployment (Azure) (WIP)

---

## ⚙️ Stack
- Embeddings --> OpenAIEmbeddings 
- VetorStore --> Chroma
- LLM --> OpenAI
- Framework --> RAG	LangChain
- Frontend --> Streamlit
- Backend --> Python
- CI/CD -->	GitHub Actions
- Deploy --> Render ou Azure App Service

---

## 📦 Install 
- git clone https://github.com/seu-user/rag-assist
- cd rag-assist
- pip install -r requirements.txt
- streamlit run app.py

---

## 🧱 Architecture (high level)

```mermaid
graph TD
    A[HR PDF] --> B[Text convertion]
    B --> C[Embeddings creation]
    C --> D[Vector DB]
    E[Streamlit User] --> F[Question]
    F --> G[LangChain Retriever]
    G --> D
    D --> H[OpenAI LLM]
    H --> I[Answer + source]


