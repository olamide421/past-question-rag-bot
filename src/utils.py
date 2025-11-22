# src/utils.py
from pathlib import Path
from pypdf import PdfReader


def read_pdf_text(path: Path) -> str:
    reader = PdfReader(str(path))
    text = []
    for page in reader.pages:
        t = page.extract_text()
        if t:
            text.append(t)
    return "\n".join(text)
