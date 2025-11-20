from sys import flags
from agno.agent import Agent
from agno.tools.tavily import TavilyTools
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv
load_dotenv()


def celsius_to_fh(temperatura_celsius: float):
    """
    Converte uma temperatura de Celsius para Fahrenheit.

    Args:
        temperatura_celsius (float): Temperatura em graus Celsius.

    Returns:
        float: Temperatura convertida para Fahrenheit.
    """
    return (temperatura_celsius * 9/5) + 32


model = OpenAIChat(id="gpt-5-mini")
agent = Agent(
    model=model,
    tools=[
        TavilyTools(),
        celsius_to_fh
        ],
    debug_mode=True
)

agent.print_response("Use suas ferramentas para pesquisar a temperatura de hoje em Chapecó em Fahrenheit")
