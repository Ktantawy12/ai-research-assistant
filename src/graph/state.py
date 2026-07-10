from typing import TypedDict


class ResearchState(TypedDict):
    question: str
    answer: str
    documents: list
    route: str