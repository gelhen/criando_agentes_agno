from agno.agent import Agent
from agno.tools.yfinance import YFinanceTools
from agno.models.openai import OpenAIChat
from agno.db.sqlite import SqliteDb

import os
from dotenv import load_dotenv

load_dotenv()

# Setup the SQLite database para criar um storage
db = SqliteDb(db_file="tmp/data.db")

agent = Agent(
    name="analista_financeiro",
    model=OpenAIChat(id="gpt-5-nano", api_key=os.getenv("OPExNAI_API_KEY")),
    tools=[YFinanceTools()],
    instructions="Você é um analista e tem diferentes clientes. Lembre-se do histórico de consultas de cada cliente separadamente.",
    db=db, # base de dados para armazenar a sessão, resumindo, não é memória para o agente mas é local para recuperar informações passadas, aqui só um histórico de conversas
    add_history_to_context=True, # adiciona historico de conversas
    num_history_runs=3, # numero de conversas que o agente vai lembrar   
    enable_user_memories=True, # ativa o uso de memórias por usuário
    add_memories_to_context=True, # adiciona memórias ao contexto
    enable_agentic_memory=True, # ativa a memória agentica, ou seja, o agente pode decidir quando salvar uma memóriaxz
)
#Existe MamoryManager para gerenciar memórias, mas por enquanto não está exposto no Agent (pode ser acessado via agent.memory_manager
#em substituição ao us do enable_agentic_memory=True
#ideal para usar qundo se quer mais controle sobre quando salvar memórias e ter um modelo menor para isso assim economizando custo

#informando session_id e user_id por conversa o agente vai registrar id conforme passado
# quando passado diretamente pelo agente registra session_id aleatoria
#outro detalhe, o registro é pro sesseion_id, não inporta qual usuario_id está perguntando
# trocar as session para obrigar o agente a lembrar pelo usuario e não pela sessão
#Teste 1 comentar o teste 2
# agent.print_response("Olá, prefiro as respostas em formato de tabela, gosto de poucas informações.", session_id="petrobras_session_1", user_id="analista_petrobras")
# agent.print_response("Olá, prefiro as respostas em formato texto, gosto de mais detalhes.", session_id="vale_session_1", user_id="analista_vale")
#Teste 2, comentar o teste 1
agent.print_response("Qual é a cotação da Petrobras?", session_id="petrobras_session_2", user_id="analista_petrobras")
agent.print_response("Qual é a cotação da Vale?", session_id="vale_session_2", user_id="analista_vale")
