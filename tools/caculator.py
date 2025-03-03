from .base import BaseTool
import re


class CalculatorTool(BaseTool):
    """Evaluates a mathematical expression provided as a string.

    - Input: {"input_data": A mathematical expression as a text string that must not be none.}
            ex: {"input_data": "2 + 2"}
    - Output: The calculated result as a number.
    """

    def __calculate(self, expression: str) -> float:
        cleaned_input = re.sub(r"[^\d.+\-*/() ]", "", expression)
        try:
            return eval(cleaned_input, {"__builtins__": None}, {})
        except (ValueError, SyntaxError, TypeError, ZeroDivisionError):
            return "Error: Invalid expression."

    def execute(self, input_data: str) -> str:
        return str(self.__calculate(input_data))
