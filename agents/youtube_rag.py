from youtube_transcript_api import YouTubeTranscriptApi,TranscriptsDisabled
from youtube_transcript_api._errors import NoTranscriptFound
from langchain_google_genai import GoogleGenerativeAIEmbeddings, GoogleGenerativeAI,ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
import re


load_dotenv()
import os

embeddings = GoogleGenerativeAIEmbeddings(
    google_api_key=os.getenv("API_KEY"),
    model="models/gemini-embedding-exp-03-07")


model=GoogleGenerativeAI(
    google_api_key=os.getenv("API_KEY"),
    model="gemini-3-flash-preview"
)


def extract_video_information(video_input,question):
    id=re.search(r"v=([a-zA-Z0-9_-]{11})",video_input)
    if id:
        video_id=id.group(1)        
    else:
        raise ValueError("Invalid YouTube URL or ID")

    try:
        yt=YouTubeTranscriptApi()
        transcript_list=yt.fetch(video_id=video_id,languages=['en','en-IN'])
        transcript=" ".join(chunk.text for chunk in transcript_list)
    except TranscriptsDisabled:
        transcript="Transcript is disabled for this video."
    except NoTranscriptFound:
        transcript = "No transcript available for the requested languages."
            
    splitter=RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=250)
    chunks=splitter.create_documents([transcript])
    
    vector_store=FAISS.from_documents(chunks, embeddings)
    retriever=vector_store.as_retriever(search_type="similarity", search_kwargs={"k":2})
    retrived_docs=retriever.invoke(question)
    context = "\n \n".join(doc.page_content for doc in retrived_docs)

    prompt=PromptTemplate(
        template="You are a very Helpful and intelligent assistant. Answer only from the provided transcript context.IF the contxt feels insufficient just say I dont know. \n context: {context}\n\n question: {question}",
        input_variables=["context","question"]
    )

    final_prompt=prompt.invoke({"context":context,"question":question})

    answer=model.invoke(final_prompt)
    return answer





#video_input=input("Enter YouTube Video video link:")
#example = https://www.youtube.com/watch?v=Z0L6NVMjUkU

#question=input("Enter your question about the video:")

#answer=extract_video_information(video_input,question)
#print(f"Answer:{answer}")