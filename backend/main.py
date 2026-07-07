import os
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from groq import Groq
from fastapi.middleware.cors import CORSMiddleware


# Load environment variables from .env
load_dotenv()

# Get API key
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key kaha hai bhai")


# Create Groq client
client = Groq(api_key=my_api_key)


# Create FastAPI app
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# Data format coming from frontend
class TranslationRequest(BaseModel):
    text: str
    language: str


# Translation API endpoint
@app.post("/translate")
def translate(request: TranslationRequest):

    prompt = f"""
Translate the following text into {request.language}.
Only return the translated text. Do not add explanations.

Text:
{request.text}
"""

    messages = [
        {
            "role": "user",
            "content": prompt
        }
    ]

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )

    answer = response.choices[0].message.content

    return {
        "translation": answer
    }