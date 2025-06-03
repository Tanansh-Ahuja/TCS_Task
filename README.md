# 🚀 FastAPI + Groq LLM (Task 1)

This project is a basic **FastAPI** application that lets you ask general knowledge questions via an API. The backend sends your question to the **Groq API**, gets a response from an LLM (LLaMA3 8B), and displays it on a simple HTML page. All API requests are logged with a UUID.

---

## ❗ Initial Attempt: Hosting LLM Locally with Ollama

### 🔧 Steps:

1. Installed Ollama from [https://ollama.com](https://ollama.com)
2. Pulled a small model like `mistral` or `qwen:0.5b`
3. Tried running it using `ollama run mistral`

### ⚠️ Errors Faced:

* Models were **too large (5GB+)** for smooth performance on 16GB RAM
* Errors like:

  ```
  wsarecv: An existing connection was forcibly closed by the remote host
  ```

  suggested the antivirus/firewall or system memory couldn't handle the load.
* Some models failed to load with:

  ```
  Exit code: 18446744072635812000
  ```

---

## 🔄 Why I Switched to Groq API

Due to system limitations and unstable behavior with local models, I switched to using **Groq's hosted LLM API**. This offered:

* Reliable performance
* Easy integration via OpenAI-compatible SDK
* Free tier access for development

---

## ✅ What This Code Does

1. You send a question to `/ask?question=...`
2. FastAPI uses Groq's LLaMA3 to generate a response
3. The response is rendered in a basic HTML template
4. Each request is logged in the terminal with:

   * A **unique UUID**
   * The **user's question**
   * The **LLM's response**

---

## 📁 Tech Stack

* **FastAPI**: Web framework
* **Groq API**: Hosted LLM provider
* **Jinja2**: HTML rendering
* **OpenAI SDK**: For calling Groq
* **UUID**: To track and log each request
* **Python Dotenv**: For managing secrets

---

## ▶️ How to Run This Project

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install fastapi uvicorn jinja2 openai python-dotenv
```

### 3. Create `.env` File

In the root folder, add a `.env` file:

```
GROQ_API_KEY=your_actual_groq_api_key_here
```

> 🔑 You can get the Groq API key from [https://console.groq.com](https://console.groq.com)

### 4. Run the Server

```bash
uvicorn main:app --reload
```

### 5. Ask a Question

Open browser and visit:

```
http://127.0.0.1:8000/ask?question=What is the capital of Japan?
```

---

## 📸 Sample Screenshot

*(Optional)*
Add a screenshot showing the question and LLM response rendered on the HTML page.

---

## 🧐 Example Terminal Output

```
[dd1493d2-ccf2-4b90-a591-bb9e94ff8ea7] Question: What is the capital of France?
[dd1493d2-ccf2-4b90-a591-bb9e94ff8ea7] Answer: The capital of France is Paris.
```

---

## 📌 To-Do (Optional)

* Add a front-end form for input
* Convert to POST request
* Handle rate limits and error responses better
