# 🧠 RAG-Assist: Assistente Inteligente de RH
**Description:**
The RAG-Assist is an AI app that uses Retrieval-Augmented Generation (RAG) with LangChain, embeddings vetoriais e Azure OpenAI to answer questions about  internal HR policies based on PDF docs. 

---

## 🚀 Functionalities

- Upload HR PDF doc (vacation policy, benefits policy, etc.)
- Automatic indexation to vector db
- Streamlit Interface to questions/answers
- Answer generation with LangChain + OpenAI
- Show answer source (transparency)
- CI/CD by GitHub Actions (WIP)
- Public deployment (Azure) (WIP)

---

## ⚙️ Stack Tecnológica
- Layers  --> Tecnologia
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


