from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="RAG Service")

class Question(BaseModel):
    question: str

@app.post("/query")
def query_rag(q: Question):
    # Simulated RAG response (safe for sandbox)
    return {
        "question": q.question,
        "answer": (
            "SME loan approval typically involves an initial risk assessment, "
            "credit scoring, compliance checks, and final approval by a credit committee."
        ),
        "source": "internal-policy-documents (simulated)"
    }
