from .message import LLMMessage
from .agent_response import AgentResponse
from .prompt import REACT_PROMPT
import logging
from llms.base import BaseLLM


logger = logging.getLogger(__name__)


class Agent:
    def __init__(
        self,
        llm: BaseLLM,
        tools: dict[str, object] = None,
        system_prompt: str = REACT_PROMPT,
    ):
        self.tools = tools or {}
        tools_description = "\n".join(
            [f"- {name}: {tool.__doc__.strip()}" for name, tool in self.tools.items()]
        )
        self.REACT_PROMPT = system_prompt.format(tools_description=tools_description)
        self.messages = [LLMMessage(role="system", content=self.REACT_PROMPT)]
        self.scratchpad: list[str] = []
        self.llm = llm

    def __send_message(self, message: str) -> AgentResponse:
        full_prompt = self.REACT_PROMPT + "\n\n"
        if self.scratchpad:
            full_prompt += "Agent Scratchpad:\n" + "\n".join(self.scratchpad) + "\n\n"
        full_prompt += message
        self.messages.append(LLMMessage(role="user", content=full_prompt))

        response_message = self.llm.call(
            messages=[msg.model_dump() for msg in self.messages]
        )
        self.messages.append(LLMMessage(role="assistant", content=response_message))

        return AgentResponse(raw_response=response_message)

    def __process_action(self, agent_response: AgentResponse) -> str:
        if agent_response.action in self.tools:
            logger.info(
                f"Executing action: {agent_response.action} with input {agent_response.action_input}"
            )
            result = self.tools[agent_response.action].execute(
                **(agent_response.action_input or {})
            )
            return result
        logger.warning(f"Unknown action: {agent_response.action}")
        return "Unknown action."

    def perform_agent_task(self, user_input: str, max_turns: int = 10) -> str:
        for _ in range(max_turns):
            agent_response = self.__send_message(user_input)
            logger.info(f"Thought: {agent_response.thought}")
            if agent_response.final_answer:
                logger.info(f"Final Answer: {agent_response.final_answer}")
                return agent_response.final_answer
            if agent_response.action:
                observation = self.__process_action(agent_response)
                logger.info(f"Observation: {observation}")
                agent_response.observation = observation
                self.scratchpad.append(
                    f"Action: {agent_response.action}\nAction Input: {agent_response.action_input}\nObservation: {observation}"
                )
                user_input = f"Observation: {observation}\nContinue with:\nThought: Now I have the result.\n"
            else:
                logger.warning("Could not generate an answer.")
                return "I could not generate an answer, please try again later."
        logger.warning("Max turns reached, could not generate an answer.")
        return "I could not generate an answer, please try again later."
