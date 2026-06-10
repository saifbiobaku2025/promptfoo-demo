from fastapi import FastAPI
from app.ai_service import ask_support_bot

app = FastAPI()

@app.get("/ask")
def ask(question: str):

    answer = ask_support_bot(question)

    return {
        "question": question,
        "answer": answer
    }