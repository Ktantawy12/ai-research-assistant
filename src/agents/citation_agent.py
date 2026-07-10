def citation_agent(state):

    question = state["question"]

    answer = (
        "Citation tool is not connected yet.\n\n"
        f"Question received:\n\n{question}"
    )

    return {
        "answer": answer,
        "documents": [],
    }