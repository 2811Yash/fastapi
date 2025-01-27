from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langserve import add_routes
import uvicorn
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
load_dotenv()

os.environ['GOOGLE_API_KEY']=os.getenv("GOOGLE_API_KEY")
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

# Allow CORS for frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app=FastAPI(
    title="Langchain Server",
    version="1.0",
    decsription="A simple API Server"

)
prompt1=ChatPromptTemplate.from_template("explain {topic} technically answer the questions which are from a technical background only and answer in 100 words only ")


add_routes(
    app,
    prompt1|llm,
    path="/essay/invoke"
)

