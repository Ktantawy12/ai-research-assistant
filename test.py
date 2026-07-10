from src.graph.graph import graph

result = graph.invoke(
    {
        "question": "What is Retrieval-Augmented Generation?"
    }
)

print(result["answer"])