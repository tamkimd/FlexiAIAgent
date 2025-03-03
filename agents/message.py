from pydantic import BaseModel


class LLMMessage(BaseModel):
    role: str
    content: str
