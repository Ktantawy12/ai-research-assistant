from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.loaders.pdf_loader import load_documents


def split_documents():
    documents = load_documents()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
        separators=["\n\n", "\n", " ", ""],
    )

    chunks = text_splitter.split_documents(documents)

    return chunks


if __name__ == "__main__":
    chunks = split_documents()

    print(f"Created {len(chunks)} chunks.\n")

    print(chunks[0].page_content)