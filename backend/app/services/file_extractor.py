from __future__ import annotations

from pathlib import Path
from typing import Any

from fastapi import UploadFile
from pypdf import PdfReader
from docx import Document
from PIL import Image
import pytesseract


def _read_pdf_text(file_path: Path) -> str:
    reader = PdfReader(str(file_path))
    pages = []
    for page in reader.pages:
        text = page.extract_text() or ""
        pages.append(text)
    return "\n\n".join(pages)


def _read_docx_text(file_path: Path) -> str:
    doc = Document(str(file_path))
    paragraphs = [p.text for p in doc.paragraphs if p.text.strip()]
    return "\n".join(paragraphs)


def _read_image_text(file_path: Path) -> str:
    image = Image.open(file_path)
    text = pytesseract.image_to_string(image)
    return text.strip()


async def extract_text_from_file(file: UploadFile) -> str:
    content = await file.read()
    file_path = Path(f"/tmp/{file.filename}")
    file_path.parent.mkdir(exist_ok=True, parents=True)
    file_path.write_bytes(content)

    suffix = file_path.suffix.lower()

    try:
        if suffix == ".pdf":
            return _read_pdf_text(file_path)
        if suffix in {".doc", ".docx"}:
            return _read_docx_text(file_path)
        if suffix in {".png", ".jpg", ".jpeg", ".bmp", ".tiff", ".webp"}:
            return _read_image_text(file_path)
        if suffix in {".txt", ".md", ".csv"}:
            return content.decode("utf-8", errors="ignore")
        return "Unsupported file format for text extraction."
    except Exception as exc:  # pragma: no cover
        return f"Extraction failed: {str(exc)}"
