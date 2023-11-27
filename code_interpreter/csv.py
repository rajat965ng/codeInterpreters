from langchain.agents import AgentType
from langchain.chat_models import ChatOpenAI
from langchain_experimental.agents.agent_toolkits import (
    create_csv_agent,
)


def main():
    ## Data Sample:
    ## https://www.kaggle.com/datasets/pardeep19singh/icc-mens-world-cup-2023/
    csv_agent_executor = create_csv_agent(
        llm=ChatOpenAI(temperature=0),
        path=[
            "data/worldcup/2k23/output/matches.csv",
            "data/worldcup/2k23/output/deliveries.csv",
            "data/worldcup/2k23/output/points_table.csv",
        ],
        verbose=True,
        agent_type=AgentType.OPENAI_FUNCTIONS,
    )

    csv_agent_executor.run(
        "How many times India has won the matches and in which year against who?"
    )


def run():
    main()
