# GenAI Assistant

A practical 20-day GenAI engineering project covering engineering foundations, prompting, embeddings, RAG, API development, evaluation, guardrails, voice, and release readiness.

The project is being developed incrementally according to the 20-day practical GenAI engineering roadmap.

---

## Project Structure

```text
genai-assistant/
│
├── app/
│   ├── main.py
│   ├── api/
│   ├── core/
│   │   ├── config.py
│   │   ├── llm_client.py
│   │   ├── prompts_v1.py
│   │   └── prompts_v2.py
│   ├── db/
│   ├── rag/
│   │   ├── loader.py
│   │   ├── chunker.py
│   │   └── chunk_pipeline.py
│   ├── safety/
│   └── voice/
│
├── data/
│   ├── documents/
│   └── chunks/
│
├── evals/
│   ├── prompt_cases.json
│   ├── results.json
│   └── chunk_quality_review.md
│
├── scripts/
│   └── run_prompt_tests.py
│
├── tests/
│   ├── test_document_api.py
│   ├── test_document_repository.py
│   ├── test_document_service.py
│   ├── test_document_loader.py
│   ├── test_chunker.py
│   ├── test_chunk_pipeline.py
│   ├── test_llm_client.py
│   └── test_output_validator.py
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

# Prerequisites

Make sure the following are installed:

* Python 3.x
* Git
* VS Code or another code editor

---

# 1. Clone the Repository

```bash
git clone <repository-url>
cd genai-assistant
```

Replace `<repository-url>` with the actual repository URL.

---

# 2. Create a Virtual Environment

## Windows

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

---

# 3. Install Dependencies

Upgrade pip:

```bash
python -m pip install --upgrade pip
```

Install project dependencies:

```bash
pip install -r requirements.txt
```

---

# 4. Configure Environment Variables

Create a local `.env` file from `.env.example`.

Do not commit `.env` to Git because it contains secrets.

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

---

# 5. Run the Smoke Check

From the project root:

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

---

# 6. Run Tests

Run the complete test suite:

```bash
python -m pytest -v
```

The test suite currently covers:

* Document API
* Document repository
* Document service
* Document loading
* Text cleaning
* Chunking
* Chunk pipeline
* LLM client
* Structured output validation

---

# Security Notes

* Never commit `.env`.
* Never hard-code API keys in source code.
* Never print or expose the actual API key.
* Use `.env.example` only for placeholder configuration values.
* Do not commit local databases.
* Do not commit generated audio files.
* Do not commit Python cache files.
* Do not commit virtual environments.
* API keys must be stored only in environment variables.

---

# Development Progress

## Day 01 — Project Setup and Repository Foundation

### Goal

Create a clean and reproducible project foundation that can be cloned, configured, and executed by another developer.

### Completed Tasks

* [x] Repository structure created
* [x] Git repository initialized
* [x] Python virtual environment created
* [x] `requirements.txt` created
* [x] `.gitignore` configured
* [x] `.env.example` created
* [x] Safe configuration module created
* [x] Application skeleton created
* [x] Smoke-check command implemented
* [x] Smoke check verified successfully
* [x] README setup instructions documented

### Day 01 Evidence

The project can be configured using the documented setup instructions and the smoke check successfully verifies the application configuration.

---

# Day 02 — JSON Validation, SQL Event Logging, and Engineering Tests

### Goal

Build the first working document-processing utility with validation, SQL persistence, event logging, and automated tests.

### Completed Tasks

* [x] Document input model created
* [x] Required document fields defined
* [x] JSON input validation implemented
* [x] Document loading workflow implemented
* [x] SQLite database implemented
* [x] Documents table implemented
* [x] Processing events table implemented
* [x] Started/completed/failed processing events implemented
* [x] Error handling implemented
* [x] Pytest test cases created
* [x] Document API tests created
* [x] Repository tests created
* [x] Service tests created

### Day 02 Evidence

The document workflow supports successful and failed processing and the associated automated tests verify the expected behavior.

---

# Day 03 — Prompt Playground for Core Business Tasks

### Goal

Create a reusable LLM prompt playground for summarization, information extraction, and document classification.

### Completed Tasks

* [x] Shared LLM client wrapper created
* [x] Provider-specific LLM code isolated in the client
* [x] LLM response model created
* [x] Model name captured
* [x] Request latency measured
* [x] Summarization prompt created
* [x] Information extraction prompt created
* [x] Classification prompt created
* [x] Structured JSON output requirements added
* [x] Prompt templates separated from application logic
* [x] Sample prompt inputs created
* [x] LLM client tests created

### Prompt Tasks

The project currently supports three core prompt tasks:

1. **Summarization**
2. **Information Extraction**
3. **Classification**

---

# Day 04 — Structured Outputs, Prompt Test Harness, and Version Logging

### Goal

Turn the prompt playground into a measurable and testable component with structured output validation, fixed test cases, prompt versions, and measurable failures.

### Completed Tasks

* [x] Pydantic output models created
* [x] Summary output validation implemented
* [x] Extraction output validation implemented
* [x] Classification output validation implemented
* [x] JSON parsing validation implemented
* [x] Validation failures separated from LLM failures
* [x] 10-case prompt evaluation dataset created
* [x] Prompt test runner implemented
* [x] Machine-readable results generated
* [x] Prompt versions V1 and V2 created
* [x] V1 and V2 tested against the same fixed dataset
* [x] Prompt version recorded
* [x] Model version recorded
* [x] Latency recorded
* [x] Failure category recorded

## Prompt Version Comparison

| Metric          |         V1 |         V2 |
| --------------- | ---------: | ---------: |
| Pass Rate       |        30% |       100% |
| Average Latency | 3652.68 ms | 1950.82 ms |
| Passed Cases    |       3/10 |      10/10 |
| Failed Cases    |       7/10 |       0/10 |

### Decision

**Preferred Prompt Version: V2**

### Reason

V2 produced valid structured JSON for all 10 fixed test cases and reduced average latency compared with V1.

V1 experienced multiple JSON parsing failures, while V2 successfully passed validation for all summary, extraction, and classification cases.

Therefore, V2 was selected as the preferred prompt version based on the fixed evaluation dataset.

### Day 04 Evidence

The prompt evaluation runner can execute the complete fixed dataset and generate machine-readable results containing:

* Case ID
* Task
* Prompt version
* Model
* Latency
* Validation result
* Failure category

---

# Day 05 — Document Preprocessing and Chunking

### Goal

Create a reliable preprocessing pipeline that loads documents, cleans their text, splits them into configurable chunks, and attaches traceable metadata.

---

## Document Dataset

The current approved sample document set contains:

```text
data/documents/

├── fastapi.md
├── genai.md
├── machine_learning.md
├── python.md
└── sql.md
```

Current sample document count:

```text
5 documents
```

The roadmap target is 30–50 approved documents. The preprocessing pipeline is implemented and currently verified using the 5-document sample dataset.

---

## Completed Tasks

### 1. Document Loading

* [x] Markdown document loading implemented
* [x] Plain text processing supported
* [x] Document folder loading implemented
* [x] Stable document IDs generated
* [x] Source file information preserved

### 2. Text Cleaning

* [x] Whitespace normalization implemented
* [x] Empty lines removed
* [x] Empty sections handled
* [x] Meaningful Markdown headings preserved

### 3. Configurable Chunking

* [x] Chunking function implemented
* [x] Configurable chunk size implemented
* [x] Configurable overlap implemented
* [x] Empty input handling implemented
* [x] Invalid chunk size validation implemented
* [x] Overlap validation implemented
* [x] Chunk overlap behavior tested

### 4. Chunk Metadata

Every generated chunk contains traceable metadata including:

* `chunk_id`
* `document_id`
* `title`
* `source_path`
* `updated_at`
* `chunk_index`
* `text`

### 5. Chunk Dataset

Generated chunks are stored in:

```text
data/chunks/chunks.jsonl
```

The current pipeline generates:

```text
Documents : 5
Chunks    : 6
```

### 6. Chunk Quality Review

A chunk-quality review file has been created:

```text
evals/chunk_quality_review.md
```

The review checks for:

* Empty chunks
* Incorrect chunk boundaries
* Heading/content separation
* Excessive duplicated overlap
* Traceability to the source document

---

# Day 05 Commands

## Load Documents

```bash
python -c "from pathlib import Path; from app.rag.loader import load_documents; docs=load_documents(Path('data/documents')); print('Documents:', len(docs)); [print(d['filename']) for d in docs]"
```

Example output:

```text
Documents: 5
fastapi.md
genai.md
machine_learning.md
python.md
sql.md
```

## Generate Chunks

```bash
python -m app.rag.chunk_pipeline
```

Example output:

```text
============================================================
CHUNK PIPELINE
============================================================
Documents : 5
Chunks    : 6
Output    : D:\python\genai-assistant\data\chunks\chunks.jsonl
```

## Run Chunker Tests

```bash
python -m pytest tests/test_chunker.py -v
```

Expected:

```text
6 passed
```

## Run Chunk Pipeline Tests

```bash
python -m pytest tests/test_chunk_pipeline.py -v
```

Expected:

```text
6 passed
```

## Run Complete Test Suite

```bash
python -m pytest -v
```

Current result:

```text
37 passed
```

---

# Day 05 Test Coverage

The Day 05 implementation is covered by automated tests for:

* Document loading
* Supported file handling
* Text cleaning
* Heading preservation
* Chunk generation
* Chunk size limits
* Chunk overlap
* Empty text handling
* Invalid chunk size
* Invalid overlap
* Required metadata
* Source document traceability
* Sequential chunk indexes
* Empty chunk prevention

---

# Current Project Status

| Day       | Topic                                  | Status     |
| --------- | -------------------------------------- | ---------- |
| Day 01    | Project Setup & Repository Foundation  | ✅ Complete |
| Day 02    | JSON Validation, SQL & Tests           | ✅ Complete |
| Day 03    | Prompt Playground                      | ✅ Complete |
| Day 04    | Structured Outputs & Prompt Evaluation | ✅ Complete |
| Day 05    | Document Preprocessing & Chunking      | ✅ Complete |
| Day 06    | Vector Indexing & Semantic Search      | ⏳ Next     |
| Day 07    | Retrieval Evaluation                   | ⏳ Upcoming |
| Day 08    | RAG Pipeline                           | ⏳ Upcoming |
| Day 09    | RAG API                                | ⏳ Upcoming |
| Day 10    | ...                                    | ⏳ Upcoming |
| Day 11–20 | ...                                    | ⏳ Upcoming |

> Days 06–20 will be documented here incrementally as each day's implementation is completed.

---

# Current Test Status

The complete automated test suite currently contains:

```text
37 tests
37 passed
0 failed
```

Run all tests with:

```bash
python -m pytest -v
```

---

# Next Step

The next development milestone is:

## Day 06 — Build Vector Indexing and Semantic Search

Planned areas:

* Generate document embeddings
* Store embeddings
* Build a vector index
* Implement semantic search
* Implement top-k retrieval
* Add metadata filtering
* Add similarity score thresholds
* Create retrieval evaluation cases
* Generate retrieval result reports
