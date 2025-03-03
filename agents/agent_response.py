import re
import json
import logging
from pydantic import BaseModel, Field, model_validator
from typing import Optional, Any, ClassVar

logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


class AgentResponse(BaseModel):
    question: Optional[str] = Field(None, description="The input question.")
    thought: Optional[str] = Field(
        None, description="The agent's step-by-step thinking."
    )
    action: Optional[str] = Field(None, description="The action taken by the agent.")
    action_input: Optional[dict[str, Any]] = Field(
        None, description="The input for the action as a dictionary."
    )
    observation: Optional[str] = Field(None, description="The result of the action.")
    final_answer: Optional[str] = Field(
        None, description="The complete answer to the question."
    )
    raw_response: str = Field(..., description="The raw response from the agent.")

    patterns: ClassVar[dict[str, re.Pattern]] = {
        "question": re.compile(r"Question:\s*(.+)", re.DOTALL),
        "thought": re.compile(r"Thought:\s*(.+?)\s*(?=Action:)", re.DOTALL),
        "action": re.compile(r"Action:\s*([a-zA-Z_]+)", re.DOTALL),
        "action_input": re.compile(r"Action Input:\s*(None|{.*})", re.DOTALL),
        "observation": re.compile(r"Observation:\s*(.+)", re.DOTALL),
        "final_answer": re.compile(r"Final Answer:\s*(.+)", re.DOTALL),
    }

    @model_validator(mode="before")
    @classmethod
    def parse_response(cls, data: Any) -> Any:
        raw_response = data.get("raw_response")
        if not raw_response:
            return data

        for field, pattern in cls.patterns.items():
            match = pattern.search(raw_response)
            if not match:
                continue

            value = match.group(1).strip() if match.group(1) else None

            if field == "action_input" and value and value != "None":
                try:
                    data[field] = json.loads(value)
                except json.JSONDecodeError:
                    logger.warning(f"Invalid JSON in action_input: {value}")
                    data[field] = None
            else:
                data[field] = value if value != "None" else None

        return data
