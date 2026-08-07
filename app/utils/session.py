import uuid

def create_conversation_id():
    """
    Generate a unique conversation ID.
    """
    return str(uuid.uuid4())