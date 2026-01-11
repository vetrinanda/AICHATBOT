from langchain_google_genai import GoogleGenerativeAIEmbeddings, GoogleGenerativeAI
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_classic.chains import RetrievalQA
import os
load_dotenv()

# from pathlib import Path

# Load `input.txt` relative to this script so the loader works regardless of CWD
# BASE_DIR = Path(__file__).parent
# INPUT_PATH = BASE_DIR / "input.txt"
# if not INPUT_PATH.exists():
#     raise FileNotFoundError(f"Required file not found: {INPUT_PATH}")

# loader = TextLoader(str(INPUT_PATH))
# documents = loader.load()

embeddings = GoogleGenerativeAIEmbeddings(
    google_api_key=os.getenv("API_KEY"),
    model="models/gemini-embedding-exp-03-07")

model=GoogleGenerativeAI(
    google_api_key=os.getenv("API_KEY"),
    model="gemini-3-flash-preview"
)


def rag_chat(documents,query):
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    if isinstance(documents, str):
        docs = text_splitter.create_documents([documents])
    else:
        docs = text_splitter.split_documents(documents)
    vectorstore=FAISS.from_documents(docs, embeddings)
    retriever=vectorstore.as_retriever()

    chain=RetrievalQA.from_chain_type(
        llm=model,
        retriever=retriever
    )
    response=chain.invoke(query)
    answer=response["result"]
    return answer




# print("Response:")
# print(response["result"])