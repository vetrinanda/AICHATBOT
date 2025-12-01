from langchain_google_genai import GoogleGenerativeAIEmbeddings, GoogleGenerativeAI
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_classic.chains import RetrievalQA
import os
load_dotenv()

loader=TextLoader('input.txt')
documents=loader.load()

text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
docs=text_splitter.split_documents(documents)

embeddings = GoogleGenerativeAIEmbeddings(
    google_api_key=os.getenv("API_KEY"),
    model="models/gemini-embedding-exp-03-07")


vectorstore=FAISS.from_documents(docs, embeddings)

retriever=vectorstore.as_retriever()


model=GoogleGenerativeAI(
    google_api_key=os.getenv("API_KEY"),
    model="gemini-2.5-flash"
)


chain=RetrievalQA.from_chain_type(
    llm=model,
    retriever=retriever
)

query="Explain the key concepts discussed about AI?"
response=chain.invoke(query)

print("Response:")
print(response["result"])