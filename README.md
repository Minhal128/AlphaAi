# AlphaAi : View The Future

An AI-powered stock analysis tool that provides **fundamental, technical, and news-based analysis** for informed trading decisions. Built using **Phidata, Groq, OpenAI, YFinance, and FastAPI**.

## Features
- **News Search Agent**: Fetches the latest stock news using Google Search.
- **Technical Analyzer Agent**: Performs moving averages, RSI, MACD, Fibonacci, and chart pattern analysis.
- **Fundamental Analyzer Agent**: Analyzes financial statements, key ratios, growth trends, and company performance.
- **Financial Analyzer Agent**: Combines all insights to provide comprehensive stock recommendations.

---

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Minhal128/AlphaAi.git
cd AlphaAi
```

### 2. Set Up a Virtual Environment
```bash
python -m venv alpha
source alpha/bin/activate  # For Mac/Linux
alpha\Scripts\activate  # For Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up API Keys
Export API keys as environment variables:
```bash
export OPENAI_API_KEY='your-api-key-here'
export PHI_API_KEY='your-api-key-here'
export GROQ_API_KEY='your-api-key-here'
```

For Windows (PowerShell):
```powershell
$env:OPENAI_API_KEY="your-api-key-here"
$env:PHI_API_KEY="your-api-key-here"
$env:GROQ_API_KEY="your-api-key-here"
```

---

## Usage
### 1. Run the App
```bash
python main.py
```

### 2. Access the AI Agent Playground
After running the script, open the provided URL in your browser to interact with the AI agents.

### 3. Example Query
Ask the agent:
> "Stock analysis of Nvidia."

![Alt Text](https://imgur.com/tqlbGdE.jpg)

![Alt Text](https://imgur.com/7MM1alr.jpg)

---

## Project Structure
```
AlphaAi/
│── agents/
│   ├── news_agent.py   # News search agent
│   ├── technical_agent.py   # Technical analysis agent
│   ├── fundamental_agent.py   # Fundamental analysis agent
│   ├── financial_agent.py   # Financial AI agent
│── main.py   # Main app entry point
│── requirements.txt   # Dependencies
│── README.md   # Project documentation
```

---

## Future Enhancements
- **Sentiment Analysis** for news articles.
- **Real-time Data Fetching** from multiple stock market APIs.
- **Portfolio Management Features** for better investment tracking.

---

## Contributing
Pull requests are welcome! Feel free to contribute and improve this project.

---

## License
This project is open-source and available under the **MIT License**.

---

## Contact
If you have any questions or suggestions, please reach out on **LinkedIn** or **GitHub Discussions**.

Happy Investing! 🚀

⭐ Star me if it helps you in your Stock market analysis or Crypto Market Analysis and If using this makes you to lose your money then Follow me and wait because only GOD TEST YOU

