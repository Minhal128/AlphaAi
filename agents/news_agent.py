from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.googlesearch import GoogleSearch

def news_search_agent():
    """Google News Search Agent."""
    return Agent(
        name="News Search Agent",
        model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
        tools=[GoogleSearch()],
        description="You are a news agent that helps users find the latest news.",
        instructions=[
            "User Query: Respond with 4 of the latest news items on the given stock.\n",
            "Search Process: Retrieve 10 recent news items in English, then select the top 4 unique and relevant items.\n",
            "Output: Provide concise and clear summaries of the selected news items."
        ],
        show_tool_calls=True,
        markdown=True,
    )
