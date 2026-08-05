def choose_model(message:str) -> str:

    message = message.lower()

    if "summarize" in message or "summary" in message:
        return "groq"
    
    if "analyze" in message or "complex" in message:
        return "nvidia"

    return "mistral"