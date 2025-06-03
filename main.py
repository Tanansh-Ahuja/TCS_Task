from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from openai import OpenAI
from dotenv import load_dotenv
import os
import uuid

load_dotenv()
app = FastAPI()
templates = Jinja2Templates(directory="template")

client = OpenAI(api_key=os.getenv("GROQ_API_KEY"), base_url="https://api.groq.com/openai/v1")

@app.get("/ask", response_class=HTMLResponse)
async def ask_question(request: Request, question: str):
    unique_id = str(uuid.uuid4())

    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "user", "content": question}
            ]
        )
        answer = response.choices[0].message.content
    except Exception as e:
        answer = f"Error: {e}"

    # Log with UUID
    print(f"[{unique_id}] Question: {question}")
    print(f"[{unique_id}] Answer: {answer}")

    return templates.TemplateResponse("response.html", {
        "request": request,
        "question": question,
        "answer": answer
    })
