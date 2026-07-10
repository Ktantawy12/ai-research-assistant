
CITATION_KEYWORDS = [
    "cite",
    "citation",
    "apa",
    "mla",
    "ieee",
    "bibtex",
    "doi",
    "reference",
    "references",
    "author",
]
def router(state):

    question = state["question"].lower()

    if any(word in question for word in CITATION_KEYWORDS):
        state["route"] = "citation"
    else:
        state["route"] = "rag"

    print(f"Selected route: {state['route']}")

    return state