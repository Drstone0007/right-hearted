def run(text: str, model: str = "hermes3:8b") -> str:
    from langchain_ollama import ChatOllama
    llm = ChatOllama(model=model, temperature=0.5)
    return llm.invoke(f"Summarize this text in 3 bullet points:\n\n{text}").content
