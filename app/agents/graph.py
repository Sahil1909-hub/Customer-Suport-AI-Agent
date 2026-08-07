from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver

from app.agents.state import RouterState
from app.agents.router_agent import router_node
from app.agents.llm_node import llm_node


builder = StateGraph(RouterState)

# Nodes
builder.add_node("router", router_node)
builder.add_node("llm", llm_node)

# Flow
builder.add_edge(START, "router")
builder.add_edge("router", "llm")
builder.add_edge("llm", END)

# Memory
memory = InMemorySaver()

graph = builder.compile(
    checkpointer=memory
)