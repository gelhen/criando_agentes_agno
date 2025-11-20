from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.yfinance import YFinanceTools

from dotenv import load_dotenv
load_dotenv()

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools()],
    #debug_mode=True,
    instructions="Use tabelas para mostrar a informação final. Não inclua nenhum outro texto."
)

agent.print_response("Qual é a cotação atual do Ouro, e o nome do ativo para investimento", stream=True)
