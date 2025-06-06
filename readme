# 🧠 RAG-Assist: Assistente Inteligente de RH

**Descrição:**  
O RAG-Assist é uma aplicação de IA que utiliza Retrieval-Augmented Generation (RAG) com LangChain, embeddings vetoriais e Azure OpenAI para responder perguntas sobre políticas internas de RH com base em documentos PDF reais da empresa.

---

## 🚀 Funcionalidades

- Upload de documentos PDF (ex: política de férias, benefícios, etc.)
- Indexação automática em base vetorial
- Interface Streamlit para perguntas/respostas
- Geração de respostas com LangChain + Azure OpenAI
- Exibição da fonte do conteúdo (transparência)
- CI/CD via GitHub Actions
- Deploy público (Render / Azure)

---

## 🧱 Arquitetura

```mermaid
graph TD
    A[PDF de RH] --> B[Conversão para Texto]
    B --> C[Criação de Embeddings]
    C --> D[Base Vetorial FAISS ou Chroma]
    E[Usuário via Streamlit] --> F[Input de Pergunta]
    F --> G[LangChain Retriever]
    G --> D
    D --> H[Azure OpenAI LLM]
    H --> I[Resposta gerada + fonte]

## ⚙️ Stack Tecnológica
- Camada --> Tecnologia
- Embeddings --> OpenAIEmbeddings ou HuggingFaceEmbeddings
- VetorStore --> Chroma ou FAISS
- LLM --> Azure OpenAI
- Framework --> RAG	LangChain
- Frontend --> Streamlit
- Backend --> Python
- CI/CD -->	GitHub Actions
- Deploy --> Render ou Azure App Service

## 📦 Instalação Rápida
git clone https://github.com/seu-user/rag-assist
cd rag-assist
pip install -r requirements.txt
streamlit run app.py
