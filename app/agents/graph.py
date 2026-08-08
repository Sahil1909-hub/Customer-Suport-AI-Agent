import os

from dotenv import load_dotenv

from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.postgres import PostgresSaver

from app.agents.state import RouterState
from app.agents.router_agent import router_node
from app.agents.llm_node import llm_node


load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError(
        "DATABASE_URL is not set in .env"
    )


# --------------------------------------------------
# Build Graph
# --------------------------------------------------

builder = StateGraph(RouterState)


# Nodes
builder.add_node("router", router_node)
builder.add_node("llm", llm_node)


# Flow
builder.add_edge(START, "router")
builder.add_edge("router", "llm")
builder.add_edge("llm", END)


# --------------------------------------------------
# PostgreSQL Checkpointer
# --------------------------------------------------

checkpointer_context = PostgresSaver.from_conn_string(
    DATABASE_URL
)

checkpointer = checkpointer_context.__enter__()

# Create LangGraph checkpoint tables
checkpointer.setup()


# --------------------------------------------------
# Compile Graph
# --------------------------------------------------

graph = builder.compile(
    checkpointer=checkpointer
)