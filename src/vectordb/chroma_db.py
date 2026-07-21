import os
import shutil

from langchain_chroma import Chroma

from src.chunking.splitter import split_documents
from src.embeddings.embedding_model import get_embedding_model

DB_PATH = "chroma_db"


def create_vector_store():
    """
    Creates a new Chroma vector database from the document chunks.
    """

    print("Loading documents...")

    chunks = split_documents()

    print(f"Created {len(chunks)} chunks.")

    embedding_model = get_embedding_model()

    print("Generating embeddings and creating Chroma database...")

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=DB_PATH,
    )

    print("Vector database created successfully!")

    return vector_store


def load_vector_store():
    """
    Loads an existing Chroma vector database.
    """

    embedding_model = get_embedding_model()

    return Chroma(
        persist_directory=DB_PATH,
        embedding_function=embedding_model,
    )


def rebuild_vector_store():
    """
    Deletes the existing vector database and rebuilds it
    from the PDFs in the documents folder.
    """

    if os.path.exists(DB_PATH):
        print("Removing existing vector database...")
        shutil.rmtree(DB_PATH)

    return create_vector_store()


def load_or_create_vector_store():
    """
    Loads an existing vector database if it contains data.
    Otherwise, creates a new one.
    """

    if not os.path.exists(DB_PATH):
        print("Vector database not found.")
        return create_vector_store()

    vector_store = load_vector_store()

    data = vector_store.get()

    if len(data["documents"]) == 0:
        print("Existing database is empty. Rebuilding...")
        return rebuild_vector_store()

    print(f"Loaded existing vector database ({len(data['documents'])} chunks).")

    return vector_store


if __name__ == "__main__":

    # Development: always rebuild after changing PDFs
    vector_store = rebuild_vector_store()

    # Production:
    # vector_store = load_or_create_vector_store()

    data = vector_store.get()

    print(f"\nTotal indexed chunks: {len(data['documents'])}")