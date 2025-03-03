from ollama import chat, ChatResponse
from .base import BaseLLM


class Ollama(BaseLLM):
    def __init__(self, model_name: str):
        self.model_name = model_name

    def call(self, messages: list[dict[str, str]]) -> str:
        response: ChatResponse = chat(model=self.model_name, messages=messages)
        return response["message"]["content"]
