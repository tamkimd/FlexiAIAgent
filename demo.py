from agents.agent import Agent
from llms.ollama import Ollama
from tools import WebSearchTool, CalculatorTool, TimeQueryTool
from settings import Settings
from dotenv import load_dotenv

load_dotenv()

settings = Settings(model_name="gemma2:latest")

tools = {
    "get_time": TimeQueryTool(),
    "calculator": CalculatorTool(),
}

llm = Ollama(model_name=settings.model_name)

# please add serper_api_key to the settings
# if you want to use the web search tool
if settings.serper_api_key:
    tools["web_search"] = WebSearchTool(settings.serper_api_key)

user_input = "What is the price of the Mac Mini M4 base version, and what is 80% of it?"
agent = Agent(llm=llm, tools=tools)
response = agent.perform_agent_task(user_input)
print("The answer is:")
print(response)
