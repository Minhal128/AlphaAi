from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools

def fundamental_analyzer_agent():
    return Agent(
    name="Fundamental Analyzer Agent",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    description="You are a fundamental analysis agent that helps users analyze the financial health of companies.",
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    instructions=["Conduct fundamental analysis of the stock. Include:\n"
            "Financial Statements (3 Years): Review key highlights.\n"
            "Key Ratios: P/E, P/B, P/S, PEG, Debt-to-Equity, etc.\n"
            "Competitive Position: Strengths and market advantages.\n"
            "Management Effectiveness: Assess ROE and capital allocation.\n"
            "Growth Trends: Revenue and earnings trajectory.\n"
            "Growth Catalysts & Risks (2-3 Years): Identify key drivers and challenges.\n"
            "DCF Valuation: Include assumptions and insights.\n"
            "Competitor & Industry Comparison: Analyze against peers and averages."
        ],
    show_tool_calls=True,
    markdown=True,
)
