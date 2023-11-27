from langchain.agents import AgentType
from langchain.chat_models import ChatOpenAI
from langchain_experimental.agents.agent_toolkits import create_python_agent
from langchain_experimental.tools import PythonREPLTool


def main():
    python_agent_executor = create_python_agent(
        llm=ChatOpenAI(temperature=0, max_tokens=1000),
        tool=PythonREPLTool(),
        verbose=True,
        agent_type=AgentType.OPENAI_FUNCTIONS,
        agent_executor_kwargs={"handle_parsing_errors": True},
    )
    python_agent_executor.run(
        "Generate and save in current working directory followed by 'data/qrcodes' 2 QRcodes that point to https://www.linkedin.com/in/rajat-nigam-877208127"
    )


def run():
    main()
