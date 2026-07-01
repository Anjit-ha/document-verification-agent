import argparse
import json

from document_parser.pdf_parser import PDFParser
from agents.orchestrator import AgentHarness


def main():
    parser = argparse.ArgumentParser(
        description="Document Verification Agent Harness"
    )

    parser.add_argument(
        "pdf",
        help="Path to PDF document"
    )

    args = parser.parse_args()

    pdf_parser = PDFParser()

    text = pdf_parser.extract_text(args.pdf)

    harness = AgentHarness()

    report = harness.run(text)

    print(json.dumps(report, indent=4))


if __name__ == "__main__":
    main()