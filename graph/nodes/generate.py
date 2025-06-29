from typing import Any, Dict
from graph.chains.generations import chain
from graph.state import GraphState


def generate(state: GraphState) -> Dict[str, Any]:
    print("-- GENERATE --")
    question = state["question"]
    docs = state["docs"]
    
    generation = chain.invoke({"context": docs, "question": question})
    return {"docs": docs, "question": question, "generation": generation}