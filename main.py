from fastapi import FastAPI, Request
from pydantic import BaseModel
import uuid
from llm_wrapper import query_llm
from logger import log_request

app = FastAPI()

class QueryInput(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(input: QueryInput, request: Request):
    request_id = str(uuid.uuid4())
    question = input.question
    response = query_llm(question)
    
    log_request(request_id, question, response)
    
    return {"id": request_id, "answer": response}
