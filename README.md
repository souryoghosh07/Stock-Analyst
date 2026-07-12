# LLM-Powered Stock Trend Analyst

**NOT A FINANCIAL GUIDE >>> THIS IS PURELY FOR EDUCATIONAL PURPOSES. THE CREATORS ARE NOT RESPONSIBLE FOR FINANCIAL GAN/LOSS INCURRED BY THE USER. FOR FINANCIAL ADVICE, CONTACT AN EXPERT. **

A lightweight, local, full-stack web application that dynamically fetches financial market data and orchestrates an Anthropic Large Language Model (Claude) to generate data-driven trajectory reports and recommend buying, selling or holding by assessing market trends. 

##  Overview
Built to explore the intersection of financial systems and generative AI, this project demonstrates how to safely implement Large Language Models in fintech tooling. It utilises advanced prompt engineering to enforce strict guardrails, empowering the LLM to act as an expert in finance and trading to generate more accurate analyses of structural trajectories, momentum shifts, and foundational metrics.

## Tech Stack
* **Frontend:** HTML5, CSS3, Vanilla JavaScript, Plotly (Single Page App)
* **Backend:** Python, FastAPI, Uvicorn
* **Data Integration:** `yfinance` (Yahoo Finance API)
* **AI Integration:** Anthropic Python SDK (Claude 4.5 Haiku)

##  Features
* **Live Market Data:** Dynamically pulls the last 20 days of closing prices, moving averages, and trailing P/E ratios, as well as generating a candlestick plot of the past 3 months.
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
Create a local .env in the root directory and add your Anthropic API key:
```
ANTHROPIC_API_KEY=your_actual_key_here
```

**Run the local backend server:**
```bash
python main.py
```
