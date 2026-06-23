import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf

# =====================================================================
# SYSTEM INITIALIZATION & GRAPHICS THEME
# =====================================================================
def initialize_workspace():
    """Creates local directory safe paths and establishes visual plotting properties."""
    os.makedirs('../outputs', exist_ok=True)
    os.makedirs('../data', exist_ok=True)
    
    # Establish a premium clean corporate layout for financial charts
    sns.set_theme(style="darkgrid")
    plt.rcParams['figure.figsize'] = (14, 7)
    plt.rcParams['axes.titlesize'] = 14
    plt.rcParams['axes.labelsize'] = 11
    print("🚀 Project workspace initialized. Financial graphing themes activated.")

# =====================================================================
# PHASE 1: TIME SERIES ENGINEERING PIPELINE
# =====================================================================
def extract_and_engineer_stock_data(ticker, start_date, end_date):
    """Streams live market data from Yahoo Finance API and engineers advanced metrics."""
    print(f"⏳ Ingesting market streams for ticker token: '{ticker}' from {start_date} to {end_date}...")
    
    # Download time series dataset via live API request
    stock_df = yf.download(ticker, start=start_date, end=end_date)
    
    if stock_df.empty:
        raise ValueError(f"CRITICAL: No market records returned for ticker '{ticker}'. Check symbol or connectivity.")
    
    # Reset index to bring Date from index vector into an explicit column
    stock_df.reset_index(inplace=True)
    stock_df['Date'] = pd.to_datetime(stock_df['Date'])
    
    print("⚙️ Engineering Time Series Financial Indicators...")
    # 1. Calculate Daily Financial Returns Velocity
    stock_df['Daily_Return'] = stock_df['Close'].pct_change()
    
    # 2. Engineer Short-Term (20-Day) and Long-Term (50-Day) Simple Moving Averages
    stock_df['SMA_20'] = stock_df['Close'].rolling(window=20).mean()
    stock_df['SMA_50'] = stock_df['Close'].rolling(window=50).mean()
    
    # 3. Calculate Bollinger Bands Volatility Channels (20-Day Window with 2 Standard Deviations)
    stock_df['Rolling_Std'] = stock_df['Close'].rolling(window=20).std()
    stock_df['Bollinger_Upper'] = stock_df['SMA_20'] + (stock_df['Rolling_Std'] * 2)
    stock_df['Bollinger_Lower'] = stock_df['SMA_20'] - (stock_df['Rolling_Std'] * 2)
    
    # Export clean standardized dataset file for downstream visualization or archival use
    output_csv_path = f"../data/{ticker.lower()}_market_metrics.csv"
    stock_df.to_csv(output_csv_path, index=False)
    print(f"✅ Time series engineering complete. Clean analytics data saved to: {output_csv_path}")
    return stock_df

# =====================================================================
# PHASE 2: FINANCIAL REPORTING GRAPHICS
# =====================================================================
def export_financial_graphics(stock_df, ticker):
    """Generates high-resolution production charts visualizing stock market vectors."""
    print(f"⏳ Generating high-resolution financial charts for '{ticker}'...")

    # --- Chart 1: Historical Closing Price vs Trend Moving Averages ---
    plt.figure()
    plt.plot(stock_df['Date'], stock_df['Close'], label='Daily Closing Price', color='#0073e6', linewidth=2)
    plt.plot(stock_df['Date'], stock_df['SMA_20'], label='20-Day SMA (Short-Term Trend)', color='#ff9900', linestyle='--')
    plt.plot(stock_df['Date'], stock_df['SMA_50'], label='50-Day SMA (Long-Term Trend)', color='#cc0000', linestyle=':')
    
    plt.title(f"Market Valuation Price Action & Rolling Moving Averages ({ticker})", fontweight='bold')
    plt.xlabel('Timeline Date')
    plt.ylabel('Asset Value (USD)')
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.savefig(f"../outputs/{ticker.lower()}_price_trends.png", dpi=300)
    plt.close()

    # --- Chart 2: Bollinger Bands Risk Channels ---
    plt.figure()
    plt.plot(stock_df['Date'], stock_df['Close'], label='Close Price', color='#2b2b2b', linewidth=1.5)
    plt.plot(stock_df['Date'], stock_df['Bollinger_Upper'], label='Upper Volatility Band', color='#2ca02c', alpha=0.7)
    plt.plot(stock_df['Date'], stock_df['Bollinger_Lower'], label='Lower Volatility Band', color='#d62728', alpha=0.7)
    
    # Fill the channel space between upper and lower bands to represent market variance fields
    plt.fill_between(stock_df['Date'], stock_df['Bollinger_Lower'], stock_df['Bollinger_Upper'], color='#e1e1e1', alpha=0.4, label='Volatility Range')
    
    plt.title(f"Bollinger Bands Volatility Expansion Profile ({ticker})", fontweight='bold')
    plt.xlabel('Timeline Date')
    plt.ylabel('Asset Value (USD)')
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.savefig(f"../outputs/{ticker.lower()}_volatility_channels.png", dpi=300)
    plt.close()

    # --- Chart 3: Historical Returns Distribution (Risk/Reward Histogram) ---
    plt.figure()
    sns.histplot(stock_df['Daily_Return'].dropna(), bins=50, kde=True, color='#6f42c1')
    plt.axvline(stock_df['Daily_Return'].mean(), color='black', linestyle='--', 
                label=f"Mean Return: {stock_df['Daily_Return'].mean():.4f}%")
    
    plt.title(f"Daily Asset Returns Frequency & Distribution Density ({ticker})", fontweight='bold')
    plt.xlabel('Percentage Daily Variation Split')
    plt.ylabel('Frequency Count Density')
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"../outputs/{ticker.lower()}_returns_distribution.png", dpi=300)
    plt.close()

    print("✅ Financial graphics exported successfully into the 'outputs/' directory.")

