# Document Verification Agent Harness

A simplified implementation of the **Reducto Agent Harness** architecture for document verification using **Python**, **Gemini**, and **Rust**.

This project extracts structured information from PDF documents, retrieves supporting evidence, verifies extracted claims, assigns confidence scores, and generates a final verification report through a multi-agent workflow.

---

# Architecture

```
                PDF Document
                     │
                     ▼
              PDF Parser
                     │
                     ▼
           Extracted Document Text
                     │
                     ▼
            Extractor Agent
                     │
                     ▼
            Evidence Agent
                     │
                     ▼
           Verification Agent
                     │
                     ▼
          Confidence Scoring
                     │
                     ▼
              Judge Agent
                     │
                     ▼
        Final Verification Report
```

---

# Features

- Multi-Agent AI Pipeline
- PDF Text Extraction
- Evidence-based Verification
- Confidence Scoring
- Explainable Results
- Modular Architecture
- JSON Outputs
- Rust Utility Module (Text Processing)

---

# Project Structure

```
document-verification-agent/

│
├── agents/
│   ├── base_agent.py
│   ├── extractor.py
│   ├── evidence.py
│   ├── verifier.py
│   ├── confidence.py
│   ├── judge.py
│   └── orchestrator.py
│
├── document_parser/
│   └── pdf_parser.py
│
├── models/
│
├── prompts/
│
├── rust_utils/
│   ├── Cargo.toml
│   ├── src/
│   └── pyproject.toml
│
├── utils/
│
├── examples/
│
├── output/
│
├── tests/
│
├── config.py
├── main.py
├── requirements.txt
└── README.md
```

---

# Agent Responsibilities

## 1. Extractor Agent

Extracts structured claims from the document.

Example:

```json
{
    "field":"Invoice Number",
    "value":"INV-2026-001"
}
```

---

## 2. Evidence Agent

Finds supporting text for every extracted claim directly from the original document.

Example:

```json
{
    "field":"Invoice Number",
    "evidence":"Invoice Number : INV-2026-001"
}
```

---

## 3. Verification Agent

Verifies whether each claim is supported by the retrieved evidence.

Example:

```json
{
    "verified":true,
    "reason":"Exact match found."
}
```

---

## 4. Confidence Agent

Assigns a confidence score for each verified claim.

Example:

```json
{
    "confidence":0.99
}
```

---

## 5. Judge Agent

Produces the final verification report summarizing the verification results.

---

# Installation

## Clone Repository

```bash
git clone <repository-url>

cd document-verification-agent
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure API Key

Create a `.env` file.

```
GEMINI_API_KEY=YOUR_API_KEY
```

---

# Running the Project

Example:

```bash
python main.py examples/sample.pdf
```

The pipeline will automatically

- Parse the PDF
- Extract claims
- Retrieve evidence
- Verify claims
- Assign confidence scores
- Generate the final report

---

# Output

The generated files are stored inside

```
output/
```

Files include:

```
output/

extracted_claims.json

evidence.json

verified_claims.json

confidence_scores.json

report.json
```

Example Report

```json
{
    "overall_status":"PASS",
    "verified_count":17,
    "failed_count":0
}
```

---

# Rust Module

The project contains a Rust utility module implemented using **PyO3**.

Implemented functions:

- normalize_text()
- hash_text()
- jaccard_similarity()

Build:

```bash
cd rust_utils

maturin develop
```

> **Note:** Building the Rust extension on Windows requires Microsoft Visual Studio Build Tools with the **Desktop development with C++** workload.

---

# Technologies Used

- Python 3.10
- Google Gemini API
- PyMuPDF
- PyO3
- Rust
- JSON

---

# Current Limitations

- Designed primarily for digital text-based PDFs.
- Scanned documents require an OCR preprocessing step.
- Rust utilities require a local Rust toolchain and Visual Studio Build Tools on Windows.

---

# Future Improvements

- OCR support for scanned documents.
- Parallel execution of independent agents.
- Retrieval-Augmented Generation (RAG) for external document validation.
- Automatic retry and error recovery.
- Web-based user interface.

---

# Inspiration

This project is inspired by the **Reducto Deep Extract – Agent Harness for Document Verification** architecture.

The implementation is a simplified educational version demonstrating how multiple specialized AI agents can collaborate to improve document extraction and verification.

---

# Author

Anjitha Sivakumar