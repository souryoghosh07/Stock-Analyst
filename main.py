# main.py

import os
import yfinance as yf
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from anthropic import Anthropic

# Load environment variables from .env file
load_dotenv()

# Verify API key is present
if not os.environ.get("ANTHROPIC_API_KEY"):
    raise RuntimeError("ANTHROPIC_API_KEY missing from environment or .env file.")

app = FastAPI(title="LLM Stock Analyst Backend")

# Enable CORS so your local HTML file can communicate with the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TickerRequest(BaseModel):
    ticker: str

@app.post("/api/analyze")
async def analyze_stock(request: TickerRequest):
    symbol = request.ticker.strip().upper()
    if not symbol:
        raise HTTPException(status_code=400, detail="Ticker symbol cannot be empty.")
    
    try:
        # 1. Fetch data from Yahoo Finance
        stock = yf.Ticker(symbol)
        
        # Get historical price data (past 3 months)
        hist = stock.history(period="3mo")
        if hist.empty:
            raise HTTPException(status_code=404, detail=f"No data found for ticker: {symbol}")
            
        # Extract recent prices to show trend trajectory
        closing_prices = hist['Close'].tolist()
        recent_closes = [round(price, 2) for price in closing_prices[-20:]]  # Last 20 trading days
        
        # Extract foundational metrics safely
        info = stock.info
        metrics = {
            "Current Price": info.get("currentPrice") or info.get("regularMarketPrice"),
            "50-Day Moving Average": info.get("fiftyDayAverage"),
            "200-Day Moving Average": info.get("twoHundredDayAverage"),
            "Trailing P/E": info.get("trailingPE"),
            "Forward P/E": info.get("forwardPE"),
            "Profit Margin": info.get("profitMargins"),
            "Debt to Equity Ratio": info.get("debtToEquity"),
            "Trailing EPS": info.get("trailingEps")
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error gathering stock data: {str(e)}")

    try:
        # 2. Construct the prompt for Claude
        metrics_summary = "\n".join([f"- {k}: {v}" for k, v in metrics.items() if v is not None])
        
        system_instruction = (
            "You are an expert institutional financial analyst. Your task is to provide a neutral, "
            "data-driven trend analysis paragraph based on the provided metrics and price trajectories. "
            "CRITICAL RULE: Do not recommend buying, selling, or holding. Do not use advisory words like "
            "'undervalued', 'overvalued', 'buy', or 'sell'. "
            "Focus entirely on structural trajectories, momentum shifts, and operational margins. "
            "Output your analysis in one or two, well-structured paragraphs."
        )
        
        user_content = (
            f"Analyze the recent financial trends for ticker symbol: {symbol}\n\n"
            f"Key Fundamental Metrics:\n{metrics_summary}\n\n"
            f"Closing Prices (Last 20 trading days chronological order):\n{recent_closes}"
        )

        # 3. Initialize Anthropic client and generate analysis
        client = Anthropic()
        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=400,
            temperature=0,
            system=system_instruction,
            messages=[
                {"role": "user", "content": user_content}
            ]
        )
        
        analysis_text = response.content[0].text
        
        return {
            "ticker": symbol,
            "company_name": info.get("longName", symbol),
            "current_price": metrics["Current Price"],
            "analysis": analysis_text
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating LLM analysis: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)