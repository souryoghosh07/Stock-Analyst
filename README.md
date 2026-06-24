# LLM-Powered Stock Trend Analyst

A lightweight, local, full-stack web application that dynamically fetches financial market data and orchestrates an Anthropic Large Language Model (Claude) to generate strictly data-driven trajectory reports. 

##  Overview
Built to explore the intersection of financial systems and generative AI, this project demonstrates how to safely implement Large Language Models in fintech tooling. It utilizes advanced prompt engineering to enforce strict guardrails, preventing the LLM from giving explicit financial advice (like "buy" or "sell"), forcing it instead to act as an objective institutional analyst evaluating structural trajectories, momentum shifts, and foundational metrics.

## Tech Stack
* **Frontend:** HTML5, CSS3, Vanilla JavaScript (Single Page App)
* **Backend:** Python, FastAPI, Uvicorn
* **Data Integration:** `yfinance` (Yahoo Finance API)
* **AI Integration:** Anthropic Python SDK (Claude 4.5 Haiku)

##  Features
* **Live Market Data:** Dynamically pulls the last 20 days of closing prices, moving averages, and trailing P/E ratios.
* **LLM Orchestration:** Compiles raw financial metrics into a structured system prompt.
* **Secure Architecture:** The LLM API key is handled strictly on the backend via environment variables, keeping it out of the browser and network payload.
* **Clean UI:** Responsive, modern dashboard with asynchronous loading states and seamless view transitions.

##  Local Installation & Setup

**1. Clone the repository:**
```bash
git clone [https://github.com/souryoghosh07/Stock-Analyst.git](https://github.com/souryoghosh07/Stock-Analyst.git)
cd Stock-Analyst
```

**2. Install Dependencies:**
```bash
pip install -r requirements.txt
```

**3. Configure your API Key:**
*Create a local .env in the root directory and add your Anthropic API key:
```
ANTHROPIC_API_KEY=your_actual_key_here
```

**Run the local backend server:**
```bash
python main.py
```
