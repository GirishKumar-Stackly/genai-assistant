# GenAI Assistant

A practical 20-day GenAI engineering project covering engineering foundations, prompting, embeddings, RAG, API development, evaluation, guardrails, voice, and release readiness.

## Project Structure

```text
genai-assistant/
│
├── app/
│   ├── main.py
│   ├── api/
│   ├── core/
│   │   └── config.py
│   ├── db/
│   ├── rag/
│   ├── safety/
│   └── voice/
│
├── evals/
├── scripts/
├── tests/
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Prerequisites

Make sure the following are installed:

* Python 3.x
* Git
* VS Code or another code editor

## 1. Clone the Repository

```bash
git clone <repository-url>
cd genai-assistant
```

Replace `<repository-url>` with the actual repository URL.

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

After activation, the terminal should show:

```text
(.venv)
```

## 3. Install Dependencies

Upgrade pip:

```bash
python -m pip install --upgrade pip
```

Install project dependencies:

```bash
pip install -r requirements.txt
```

## 4. Configure Environment Variables

Create a local `.env` file from `.env.example`.

Do not commit `.env` to Git because it may contain secrets.

Example:

```env
LLM_API_KEY=your-api-key
MODEL_NAME=your-model-name
```

The application loads these values through:

```text
app/core/config.py
```

The configuration module raises a clear error if a required environment variable is missing.

## 5. Run the Smoke Check

From the project root, run:

```bash
python -m app.main
```

Expected output:

```text
{'status': 'ok', 'model': 'your-model-name', 'api_key_loaded': True}
```

The smoke check confirms that:

* The application package can be imported.
* Configuration is loaded successfully.
* The required model name is available.
* The API key is available without printing the actual secret.

## 6. Run Tests

Run the test suite using:

```bash
pytest
```

As the project grows, additional unit, integration, API, retrieval, evaluation, and guardrail tests will be added.

## Security Notes

* Never commit `.env`.
* Never hard-code API keys in source code.
* Never print or expose the actual API key.
* Use `.env.example` only for placeholder configuration values.
* Do not commit local databases, generated audio, Python cache files, or virtual environments.

## Current Status

### Day 1 — Repository Foundation

* [x] Repository structure created
* [x] Python virtual environment created
* [x] Dependency file created
* [x] `.gitignore` configured
* [x] `.env.example` created
* [x] Safe configuration module created
* [x] Application skeleton created
* [x] Smoke check implemented
* [x] Smoke check verified successfully
* [x] README setup instructions documented

Further functionality will be implemented according to the 20-day practical delivery roadmap.
