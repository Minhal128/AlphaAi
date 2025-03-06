from agents.news_agent import news_search_agent
from agents.technical_agent import technical_analyzer_agent
from agents.fundamental_agent import fundamental_analyzer_agent
from agents.financial_agent import financial_agent
from phi.playground import Playground, serve_playground_app
from dotenv import load_dotenv
import os
load_dotenv()

openai_api_key = os.getenv("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")
groq_api_key = os.getenv("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")
phi_api_key = os.getenv("phi-zb_5AVvLR60clVCdEiaJL1X7SyJKDUeVhXXeyEILI64")

news_agent = news_search_agent()
tech_agent = technical_analyzer_agent()
fundamental_agent = fundamental_analyzer_agent()

# Create financial agent with the team of agents
finance_agent = financial_agent(news_agent, tech_agent, fundamental_agent)

# Setup and serve the playground application
app = Playground(agents=[news_agent, tech_agent, fundamental_agent, finance_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("main:app", reload=True)
