from fastapi import FastAPI
from pydantic import BaseModel
import requests
from chatbot import get_answer
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

class Query(BaseModel):
    question: str

@app.post("/chat")
async def chat(query: Query):
    answer = get_answer(query.question)
    return {"answer": answer}

@app.post("/create-ticket")
async def create_ticket(data: dict):
    crm_url = os.getenv("CRM_API_URL")
    token = os.getenv("CRM_AUTH_TOKEN")
    res = requests.post(
        f"{crm_url}/tickets",
        headers={"Authorization": f"Bearer {token}"},
        json=data
    )
    return {"status": res.status_code, "response": res.json() if res.ok else "error"}
