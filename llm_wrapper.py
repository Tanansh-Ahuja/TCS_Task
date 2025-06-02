import requests

def query_llm(question: str) -> str:
    response = requests.post("http://localhost:11434/api/generate", json={
        "model": "mistral",
        "prompt": question
    })
    print(response)
    #return response.json()["response"]
