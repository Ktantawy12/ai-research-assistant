from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader


def load_documents():
    documents = []

    pdf_folder = Path("data/documents")

    for pdf_file in pdf_folder.glob("*.pdf"):
        loader = PyPDFLoader(str(pdf_file))
        documents.extend(loader.load())

    return documents


if __name__ == "__main__":
    docs = load_documents()

    print(f"Loaded {len(docs)} pages.\n")

    for doc in docs[:5]:
        print(doc.metadata)