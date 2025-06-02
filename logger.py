def log_request(request_id: str, question: str, response: str):
    print(f"[Request ID: {request_id}]")
    print(f"User Question: {question}")
    print(f"LLM Response: {response}")
