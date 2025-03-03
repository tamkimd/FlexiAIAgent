from abc import ABC, abstractmethod


class BaseLLM(ABC):
    @abstractmethod
    def call(self, *args, **kwargs):
        pass
