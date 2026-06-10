# AI Quality Gate

A small FastAPI service that exposes a customer-support chatbot powered by Google Gemini. Use it as a local API target for AI quality testing (e.g. with Promptfoo).

## Prerequisites

- Python 3.12+
- A [Google Gemini API key](https://aistudio.google.com/apikey)

## Setup

1. Clone the repository and enter the project root:

   ```bash
   cd ai-quality-gate
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root:

   ```env
   GEMINI_API_KEY=your_api_key_here
   ```

   Do not commit `.env` — it contains secrets.

## Run locally

Start the server from the **project root** (not from inside `app/`):

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

To allow access from other devices on your network:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

Interactive API docs: `http://127.0.0.1:8000/docs`

## API

### `GET /ask`

Ask the support bot a question.

**Query parameters**

| Parameter  | Type   | Required | Description        |
|------------|--------|----------|--------------------|
| `question` | string | yes      | The user's question |

**Example**

```bash
curl "http://127.0.0.1:8000/ask?question=How%20do%20I%20reset%20my%20password?"
```

**Response**

```json
{
  "question": "How do I reset my password?",
  "answer": "..."
}
```

## Project structure

```
ai-quality-gate/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI app and /ask endpoint
│   └── ai_service.py    # Gemini client and support bot logic
├── .env                 # API keys (local only, not committed)
├── requirements.txt
└── README.md
```

## Troubleshooting

**`ModuleNotFoundError: No module named 'app'`**

Run uvicorn from the project root, not from the `app/` directory:

```bash
# correct
cd ai-quality-gate
uvicorn app.main:app --reload
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

# incorrect
cd app
uvicorn app.main:app --reload
```

**Missing or invalid API key**

Ensure `GEMINI_API_KEY` is set in `.env` at the project root and restart the server.
