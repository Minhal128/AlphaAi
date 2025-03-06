import os
from dotenv import load_dotenv
from phi.agent import Agent
from phi.model.openai import OpenAIChat

# Load environment variables
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

def financial_agent(news_search_agent, technical_analyzer_agent, fundamental_analyzer_agent):    
    return Agent(
        name="Financial Agent",
        team=[news_search_agent, technical_analyzer_agent, fundamental_analyzer_agent],
        model=OpenAIChat(id="gpt-4o", api_key=openai_api_key),  # API key pass ki
        instructions=["Create an investment report on the stock. Include:\n"
                "Company Snapshot: Key facts and overview.\n"
                "Financial Analysis: Top metrics and peer comparison.\n"
                "Technical Analysis: Key findings and insights.\n"
                "Fundamental Analysis: Strengths and concerns.\n"
                "Risks & Opportunities: Major risks and growth catalysts.\n"
                "Investment cases: Bull and bear cases.\n"
                "Price Target: 12-month forecast.\n"
                "Executive Summary: Investment recommendation."
                ],
        show_tool_calls=True,
        markdown=True
    )
