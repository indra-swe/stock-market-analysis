# 📈 Market Intelligence: Advanced Time-Series Engineering & Quantitative Valuation

## 📌 Strategic Overview
This repository contains an end-to-end quantitative financial analytics framework designed to pull, process, and map real-time equity time-series parameters. Moving past static spreadsheets, the system communicates with live market data streams to engineer rolling momentum indicators, calculate localized standard-deviation volatility matrices, and output production-ready risk reports.

### 🎯 Analytical Objectives Met
* **Live Automated Ingestion:** Deployed an API stream architecture wrapped in mock user headers to ingest historical time-series sequences safely.
* **Momentum Trajectory Modeling:** Programmed dual-window simple moving averages ($SMA$) to trace mid-term and long-term structural momentum pivots.
* **Risk Variance Modeling:** Formulated standard-deviation-bounded Bollinger Bands to evaluate asset volatility expansion channels.
* **Distribution Volatility Mapping:** Constructed parametric probability distribution metrics to track systematic day-to-day capital return densities.

---
⚙️ Quantitative Financial TransformationsRaw transaction logs only capture historical closing data points. This pipeline engineers those values into mathematical market indicators:
* Simple Moving Average ($\text{SMA}_t$):
  Calculates the continuous rolling arithmetic mean across specific time bounds ($N$) to smooth erratic noise and isolate trends:
    $$\text{SMA}_t = \frac{1}{N} \sum_{i=0}^{N-1} \text{Close}_{t-i}$$
* Daily Return Velocity ($\text{R}_t$): Calculates day-to-day growth rates as a percentage variance metric across a sequential timeline:
    $$\text{R}_t = \frac{\text{Close}_t - \text{Close}_{t-1}}{\text{Close}_{t-1}}$$
* Bollinger Band Variance Boundaries: Maps pricing volatility envelopes by placing boundaries exactly $\pm 2$ standard deviations ($\sigma$) away from a 20-day rolling average:
    $$\text{Bollinger Channels} = \text{SMA}_{20} \pm \left(2 \times \sigma_{20}\right)$$
📊 Quantitative Strategic Insights
**1. Dual-SMA Intersection SignalsPlotting the short-term 20-day trend line against the broader 50-day trajectory isolates macro equity momentum shifts. When the 20-day SMA cuts clearly above the 50-day line, it represents a structural bull market breakout window.
**2. Gaussian Returns SymmetryEvaluating the daily return percentage metrics confirms a tight normal distribution peaked near a positive mean. The tails of this distribution quantify extreme outlier trading sessions, providing a raw dataset for systematic value-at-risk (VaR) profiling.
  
🚀 Environment Execution & Setup
1. Clone & Core InitializationBashgit clone [https://github.com/indra-swe/stock-market-analysis.git](https://github.com/indra-swe/stock-market-analysis.git)
  cd stock-market-analysis
  pip install -r requirements.txt
2. Trigger the Quantitative PipelineTo execute the live extraction API, compute metrics, and regenerate the high-resolution charts in your workspace:Bashpython notebooks/stock_analyzer.py
---
## 🛠 Project Workspace Architecture
```text
├── data/
│   └── aapl_market_metrics.csv       # Standardized time-series metrics engine file
├── notebooks/
│   └── stock_analyzer.py             # Functionalized engineering & math script
├── outputs/
│   ├── aapl_price_trends.png         # Chart: Moving average intersections
│   ├── aapl_volatility_channels.png  # Chart: Bollinger Band volatility vectors
│   └── aapl_returns_distribution.png # Chart: Daily return frequency density
├── dashboards/
│   └── stock_dashboard.pbix          # Premium dark financial BI workspace dashboard
└── requirements.txt                  # System software dependencies

