from fastapi import FastAPI
import requests

app = FastAPI(title="GenAI API Gateway")

@app.get("/ask")
def ask(question: str):
    r = requests.post("http://rag-service/query", json={"question": question})
    return r.json()
