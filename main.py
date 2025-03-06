from agents.news_agent import news_search_agent
from agents.technical_agent import technical_analyzer_agent
from agents.fundamental_agent import fundamental_analyzer_agent
from agents.financial_agent import financial_agent
from phi.playground import Playground, serve_playground_app


news_agent = news_search_agent()
tech_agent = technical_analyzer_agent()
fundamental_agent = fundamental_analyzer_agent()

# Create financial agent with the team of agents
finance_agent = financial_agent(news_agent, tech_agent, fundamental_agent)

# Setup and serve the playground application
app = Playground(agents=[news_agent, tech_agent, fundamental_agent, finance_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("main:app", reload=True)
