import fitz


class PDFParser:

    def extract_text(self, pdf_path: str) -> str:

        document = fitz.open(pdf_path)

        pages = []

        for page in document:
            pages.append(page.get_text())

        return "\n".join(pages)