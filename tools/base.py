from abc import ABC, abstractmethod


class BaseTool(ABC):
    """The docstring of the tool class should describe the tool's purpose and input/output format.
    it will automatically added to the agent's initial prompt."""

    @abstractmethod
    def execute(self, *args, **kwargs) -> str:
        pass
