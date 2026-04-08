<div align="center">
  <img src="assets/banner.png" alt="Stock Agent Banner" width="100%">
</div>

# Stock Agent
> **An intelligent, multi-agent stock market analysis and trading tool.**

Stock Agent leverages the power of GenAI to intelligently track, analyze, and generate insights for various stocks. Utilizing modern agent-based patterns, it plans, researches, codes, and executes data analysis routines on stock prices autonomously.

## 🚀 Features
* **Automated Data Processing**: Uses autonomous agents to gather and format real-time market data.
* **GenAI-Powered Decisions**: Employs an intelligent orchestrator pattern for plan execution and code generation.
* **Resilient Error Handling**: Built-in self-correction and reviewer agents to ensure high-quality insights.
* **Seamless Git Integration**: Automatically generates pull requests via GitHub tokens for robust CI/CD code workflows.

## 📦 Project Structure

```
├── stock_agent/        # Core agent logic and routing
├── tests/              # Pytest battery for ensuring reliability
├── docs/               # System architecture and design documentation
└── README.md           # You are here
```

## 🛠️ Quick Start

### 1. Requirements
* Python 3.11+
* `uv` or `pip` for dependency management
* OpenRouter and NewsAPI credentials

### 2. Setup
Clone the repository and install the required dependencies:
```bash
git clone https://github.com/srikanth086/stock_agent.git
cd stock_agent

# Create a virtual environment with uv
uv venv
source .venv/bin/activate

# Install dependencies
uv pip install -e .
```

### 3. Usage
Run the agent using the provided CLI interface:
```bash
python -m stock_agent.main "fetch AAPL data and chart the momentum strategy"
```

## 🔐 Credentials
This project makes use of OpenRouter (to access LLMs like Qwen) and NewsAPI (for fetching stock news). Ensure you have these environment variables set:
```bash
export OPENROUTER_API_KEY="your_openrouter_api_key_here"
export NEWS_API_KEY="your_news_api_key_here"
```
For GitHub deployment features, remember to set the `GITHUB_TOKEN` environment variable.

## 🤝 Contributing
Contributions, issues, and feature requests are welcome!
Feel free to check [issues page](#) to contribute.

## 📜 License
This project is licensed under the MIT License.
