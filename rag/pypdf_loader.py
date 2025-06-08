import os
import pdfplumber
from langchain_core.documents import Document


docs = []

pdf_dir = "files"
for filename in os.listdir(pdf_dir):
    if filename.endswith(".pdf"):
        file_path = os.path.join(pdf_dir, filename)
        try:
            with pdfplumber.open(file_path) as pdf:
                for i, page in enumerate(pdf.pages):
                    text = page.extract_text()
                    if text:
                        docs.append(Document(page_content=text, metadata={"source": filename, "page": i}))
            print(f"Loaded: {filename}")
        except Exception as e:
            print(f"❌ Failed to load {filename}: {e}")

print(f"\n✅ Total pages loaded: {len(docs)}")
