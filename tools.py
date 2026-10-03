from langchain_core.tools import tool


@tool
def get_dsa_topics():
    """Return important DSA topics for placement preparation."""
    
    return [
        "Arrays",
        "Strings",
        "Hashing",
        "Linked Lists",
        "Stacks",
        "Queues",
        "Binary Trees",
        "Graphs",
        "Dynamic Programming"
    ]
@tool
def get_company_topics(company: str):
    """Return preparation topics for a specific company."""

    print(f"\n🔧 TOOL CALLED: get_company_topics({company})\n")

    companies = {
        "HSBC": [
            "DSA",
            "OOP",
            "DBMS",
            "Computer Networks",
            "SQL",
            "Behavioral Questions"
        ],

        "Google": [
            "DSA",
            "Algorithms",
            "Data Structures",
            "Problem Solving",
            "Behavioral Questions"
        ]
    }

    return companies.get(
        company,
        [
            "DSA",
            "OOP",
            "DBMS",
            "Operating Systems",
            "Computer Networks"
        ]
    )