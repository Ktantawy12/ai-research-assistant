from langgraph.graph import StateGraph, END

from src.graph.state import ResearchState
from src.agents.router import router
from src.agents.rag_agent import rag_agent
from src.agents.citation_agent import citation_agent


builder = StateGraph(ResearchState)


builder.add_node("router", router)
builder.add_node("rag", rag_agent)
builder.add_node("citation", citation_agent)


builder.set_entry_point("router")


builder.add_conditional_edges(
    "router",
    lambda state: state["route"],
    {
        "rag": "rag",
        "citation": "citation",
    },
)


builder.add_edge("rag", END)
builder.add_edge("citation", END)

graph = builder.compile()