from langchain_groq import ChatGroq
from langchain.agents import create_agent

from tools import get_dsa_topics, get_company_topics


model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
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