# Deep Extract-Inspired Document Verification Agent Harness

A multi-agent document verification framework inspired by the concepts of Deep Extract agent harness architectures. The system automatically extracts structured information from PDF documents, retrieves supporting evidence, verifies extracted fields, assigns confidence scores, and iteratively refines failed claims until a quality threshold is reached.

The framework is designed to work with multiple document types such as invoices, resumes, bank statements, contracts, utility bills, medical reports, passports, research papers, and other structured or semi-structured PDF documents.

---

## Features

- Multi-agent architecture
- Planner-driven extraction workflow
- Generic document support
- Evidence retrieval for every extracted field
- Automated field verification
- Confidence scoring with Rust acceleration
- Iterative refinement of failed claims
- JSON-based structured outputs
- Modular and extensible design

---

## Architecture

```text
                PDF Document
                     │
                     ▼
              PDF Parser
                     │
                     ▼
              Planner Agent
                     │
                     ▼
            Extraction Plan
                     │
                     ▼
            Extractor Agent
                     │
                     ▼
            Evidence Agent
                     │
                     ▼
            Verifier Agent
                     │
                     ▼
          Confidence Agent
             (Rust Assisted)
                     │
                     ▼
           Quality Assessment
             │             │
             │             ▼
             │      Feedback Agent
             │             │
             │             ▼
             │    Re-Extraction Loop
             │
             ▼
            Judge Agent
                     │
                     ▼
              Final Verification Report
```

---

## Project Structure

```
document-verification-agent/
│
├── agents/
│   ├── base_agent.py
│   ├── planner.py
│   ├── extractor.py
│   ├── evidence.py
│   ├── verifier.py
│   ├── confidence.py
│   ├── feedback.py
│   ├── judge.py
│   └── orchestrator.py
│
├── prompts/
│
├── rust_utils/
│   ├── Cargo.toml
│   └── src/
│       └── lib.rs
│
├── document_parser/
│
├── utils/
│
├── output/
│
├── config.py
├── main.py
├── requirements.txt
└── README.md
```

---

## Agent Responsibilities

### Planner Agent

- Understands document structure
- Identifies document type
- Creates an extraction plan
- Divides documents into logical sections

---

### Extractor Agent

- Extracts structured information
- Follows the planner's extraction strategy
- Supports refinement-based re-extraction

---

### Evidence Agent

- Retrieves supporting evidence from the original document
- Associates evidence with extracted claims

---

### Verifier Agent

- Compares extracted values against document evidence
- Determines whether each claim is verified
- Provides verification reasoning

---

### Confidence Agent

- Assigns confidence scores
- Uses Rust-based similarity functions
- Combines deterministic similarity with verification results

---

### Feedback Agent

- Analyses failed verification results
- Generates refinement instructions
- Guides targeted re-extraction

---

### Judge Agent

- Produces the final verification summary
- Reports verification statistics
- Generates the final quality assessment

---

## Rust Integration

Rust is integrated through PyO3 and Maturin to accelerate deterministic operations.

Current Rust utilities include:

- Text normalization
- Text hashing
- Jaccard similarity
- Exact matching
- Contains matching
- Duplicate line detection
- Word counting

These utilities are used to improve confidence estimation and document preprocessing.

---

## Iterative Verification Workflow

```
PDF
 │
 ▼
Planner
 │
 ▼
Extractor
 │
 ▼
Evidence
 │
 ▼
Verifier
 │
 ▼
Confidence
 │
 ├──────── PASS ───────► Judge
 │
 └──────── FAIL
            │
            ▼
       Feedback
            │
            ▼
   Re-Extraction
            │
            └────────► Verify Again
```

The workflow repeats until all claims satisfy the confidence threshold or the maximum refinement iterations are reached.

---

## Installation

Clone the repository

```bash
git clone <repository-url>
cd document-verification-agent
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

Windows

```bash
.venv\Scripts\activate
```

Linux

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Configure API

Create a `.env` file

```
GEMINI_API_KEY=YOUR_API_KEY
```

---

## Build Rust Extension

```bash
cd rust_utils
maturin develop
cd ..
```

---

## Run

```bash
python main.py examples/sample.pdf
```

---

## Example Output

```json
{
    "overall_status": "PASSED",
    "summary": "All extracted claims successfully verified.",
    "verified_count": 18,
    "failed_count": 0,
    "quality_score": 1.0,
    "recommendation": "No further refinement required."
}
```

---

## Technologies Used

- Python
- Rust
- PyO3
- Maturin
- Google Gemini API
- PyMuPDF
- JSON
- Multi-Agent Architecture

---

## Future Improvements

- Parallel execution of extraction tasks
- Local LLM support
- OCR integration
- Multi-language document support
- Advanced business-rule validation
- Table-aware extraction
- Layout-aware document understanding

---

## Disclaimer

This project is an independent implementation inspired by publicly described concepts of iterative document extraction and verification. It is not affiliated with, endorsed by, or derived from any proprietary implementation.
