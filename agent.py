from langchain_ollama import ChatOllama
from langchain.agents import create_agent

from tools import get_dsa_topics, get_company_topics


model = ChatOllama(
    model="llama3.2"
)

tools = [
    get_dsa_topics,
    get_company_topics
]

agent = create_agent(
    model=model,
    tools=tools
)


def ask_agent(question):
    response = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": question
                }
            ]
        }
    )

    return response["messages"][-1].content
