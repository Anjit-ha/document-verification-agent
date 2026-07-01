from document_parser.pdf_parser import PDFParser


def test_parser():

    parser = PDFParser()

    text = parser.extract_text("examples/sample.pdf")

    assert len(text) > 0