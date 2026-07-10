from src.rag.chain import ask


def rag_agent(state):

    answer, documents = ask(state["question"])

    return {
        "answer": answer,
        "documents": documents,
    }