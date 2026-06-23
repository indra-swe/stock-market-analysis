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

