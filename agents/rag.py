from langchain_google_genai import GoogleGenerativeAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv
import os
load_dotenv()


embeddings = GoogleGenerativeAIEmbeddings(
    google_api_key=os.getenv("API_KEY"),
    model="models/gemini-embedding-exp-03-07")

text="Hi My name is Anand"

result=embeddings.embed_query(text)

docs=[
    "Hello world",
    "Hi there",
    "Greetings planet",
    "Salutations earth"
]
result1=embeddings.embed_documents(docs)

similarity=cosine_similarity([result], result1)

print(similarity)
