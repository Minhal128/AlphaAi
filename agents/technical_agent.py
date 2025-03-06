from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools


def technical_analyzer_agent():
    return Agent(
        name="Technical Analyzer Agent",
        model=OpenAIChat(id="gpt-4o"),
        description=("You are a technical analysis agent that helps users analyze stock prices and trends."),
        tools=[YFinanceTools(stock_price=True, technical_indicators=True, historical_prices=True)],
        instructions=["Perform technical analysis on the stock. Include:\n"
                "Moving Averages (1 Year): 50-day & 200-day, with crossovers.\n"
                "Support & Resistance: 3 levels each, with significance.\n"
                "Volume Analysis (3 Months): Trends and anomalies.\n"
                "RSI & MACD: Compute and interpret signals.\n"
                "Fibonacci Levels: Calculate and analyze.\n"
                "Chart Patterns (6 Months): Identify 3 key patterns.\n"
                "Sector Comparison: Contrast with sector averages."
                ],
        show_tool_calls=True,
        markdown=True,
    )
