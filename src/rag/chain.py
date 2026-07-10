from src.retrieval.retriever import retrieve_documents
from src.llm.llm import get_llm


def ask(question: str):
    """
    Answers a question using Retrieval-Augmented Generation (RAG).
    """

    # Step 1: Retrieve relevant documents
    documents = retrieve_documents(question)

    print(f"\nRetrieved {len(documents)} documents.\n")

    for i, doc in enumerate(documents, start=1):
        print(f"Document {i}")
        print("-" * 60)
        print(doc.page_content[:300])
        print("\nMetadata:", doc.metadata)
        print()

    # Step 2: Build context
    context = "\n\n".join(
        doc.page_content for doc in documents
    )

    print("\n================ CONTEXT ================\n")
    print(context)
    print("\n=========================================\n")

    # Step 3: Build prompt
    prompt = f"""
You are a helpful Research assistant.

Answer ONLY using the information provided in the context below.

If the answer is not contained in the context, reply exactly:

"I couldn't find that information in the provided documents."

Context:
{context}

Question:
{question}

Answer:
"""

    print("\n================ PROMPT ================\n")
    print(prompt)
    print("\n========================================\n")

    # Step 4: Call LLM
    llm = get_llm()

    response = llm.invoke(prompt)

    print("\n================ RESPONSE ================\n")
    print(response.content)
    print("\n==========================================\n")

    return response.content, documents


if __name__ == "__main__":
    question = "What documents are required for a personal loan?"
    answer, documents = ask(question)

    print(answer)