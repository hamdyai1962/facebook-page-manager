from __future__ import annotations


class AIWorkflow:
    def __call__(self, message: str, context: str = "") -> str:
        base = "I am an advanced AI assistant designed for content management, OCR, and automation."
        if context:
            return f"{base}\nContext:\n{context}\n\nUser message:\n{message}"
        return f"{base}\n\nUser message:\n{message}"


agent_workflow = AIWorkflow()
