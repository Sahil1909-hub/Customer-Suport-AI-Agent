from typing import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages



class RouterState(TypedDict):

    messages: Annotated[list, add_messages]

    model: str

    