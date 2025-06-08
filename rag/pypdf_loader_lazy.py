import os
import pdfplumber
from langchain_core.documents import Document
from typing import Generator

def lazy_pdf_loader(pdf_dir: str) -> Generator[Document, None, None]:
    for filename in os.listdir(pdf_dir):
        if filename.endswith(".pdf"):
            file_path = os.path.join(pdf_dir, filename)
            try:
                with pdfplumber.open(file_path) as pdf:
                    for i, page in enumerate(pdf.pages):
                        text = page.extract_text()
                        if text:
                            yield Document(page_content=text, metadata={"source": filename, "page": i})
                print(f"✅ Loaded lazily: {filename}")
            except Exception as e:
                print(f"❌ Failed to load {filename}: {e}")

# Usage
docs = list(lazy_pdf_loader("files"))
print(f"\n✅ Total pages lazily loaded: {len(docs)}")
