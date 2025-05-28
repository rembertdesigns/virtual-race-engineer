from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
import os, glob

def ingest_pdfs(pdf_folder="data"):
    all_docs = []
    for file in glob.glob(f"{pdf_folder}/*.pdf"):
        loader = PyPDFLoader(file)
        docs = loader.load()
        all_docs.extend(docs)

    vectordb = FAISS.from_documents(all_docs, OpenAIEmbeddings())
    vectordb.save_local("vector_store")

if __name__ == "__main__":
    ingest_pdfs()
