from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()


def retrieve_answer(question):
    embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))
    vectordb = Chroma(persist_directory="db", embedding_function=embeddings)
    retriever = vectordb.as_retriever(search_kwargs={"k":1})

    qa = RetrievalQA.from_chain_type(
        llm=OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY")),
        retriever=retriever
    )

    result = qa({"query": question})
    docs = retriever.get_relevant_documents(question)
    sources = [doc.metadata.get("source","without dirrect reference") for doc in docs]

    return result['result'], sources