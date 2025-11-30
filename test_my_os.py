from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.os import AgentOS

from dotenv import load_dotenv
load_dotenv()

# reasoning_effort define o nível de profundidade do raciocínio do modelo (ex: "low", "high").
assistant = Agent(
    name="Assistant",
    model=OpenAIChat(id="gpt-5-nano", reasoning_effort="low"),
    instructions=["You are a helpful AI assistant."],
    markdown=True,
)

agent_os = AgentOS(
    id="my-first-os",
    description="My first AgentOS",
    agents=[assistant],
)
# uma vez instanciado o agente, jogamos na variavel app
app = agent_os.get_app()

if __name__ == "__main__":
    # O método serve do AgentOS inicia o servidor web para o app,
    #  permitindo acessar a aplicação na porta especificada (padrão 7777).
    # app= nome do arquivo, que á o arquivo que tem o app
    agent_os.serve(app="test_my_os:app", reload=True)