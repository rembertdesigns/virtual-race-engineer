from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
import os

# Load vector store
def load_vectorstore():
    return FAISS.load_local("vector_store", OpenAIEmbeddings())

# Build QA chain
def run_query(query):
    vectordb = load_vectorstore()
    llm = ChatOpenAI(model="gpt-4", temperature=0.3)
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=vectordb.as_retriever())
    return qa_chain.run(query)
