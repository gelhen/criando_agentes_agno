from agno.agent import Agent
from agno.tools.tavily import TavilyTools
from agno.models.groq import Groq
from dotenv import load_dotenv
load_dotenv()

# cria agente e passa lista de ferramentas
agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[TavilyTools()],
    debug_mode=False
)

# forma mais básica de chamar o agente, com print response
agent.print_response(
    """Use suas ferramentas para pesquisar a temperatura de hoje em Machadinho RS, 
    informe também a data da temperatura"""
)
