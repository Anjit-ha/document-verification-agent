from document_parser.pdf_parser import PDFParser
from agents.extractor import ExtractorAgent


def test_pipeline():

    parser = PDFParser()

    text = parser.extract_text("examples/sample.pdf")

    extractor = ExtractorAgent()

    claims = extractor.run(text)

    assert isinstance(claims, list)