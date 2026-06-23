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

