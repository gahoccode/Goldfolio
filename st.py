import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Goldfolio Analysis", layout="wide")

# Load Data (following app.py structure)
fileName = "Gold Price.csv"
# Read CSV with proper thousands separator
Price = pd.read_csv(fileName, thousands=',')
Price['Year'] = pd.to_datetime(Price['Year'], format='%Y')

# Sidebar Configuration
st.sidebar.title("Analysis Configuration")

# Risk Free Rate Input
RiskFreeRate = st.sidebar.slider(
    "Risk-Free Rate (%)", 
    min_value=0.0, 
    max_value=10.0, 
    value=3.0,
    step=0.1
) / 100

# Calculate Returns and Metrics (following app.py structure)
Returns = Price["Close"].pct_change().dropna()
Mean_Return = Returns.mean()
Std_Dev = Returns.std()
Sharpe_Ratio = (Mean_Return - RiskFreeRate) / Std_Dev

# Calculate VaR and CVaR (95% confidence level)
confidence_level = 0.95
VaR = np.percentile(Returns, (1 - confidence_level) * 100)
CVaR = Returns[Returns <= VaR].mean()

# Main App
st.title("Gold Price Analysis Dashboard")

# Data Overview
st.header("Data Overview")
# Format the display of numeric columns
display_df = Price.copy()
numeric_cols = ['Open', 'Close', 'Average Price', 'High', 'Low']
for col in numeric_cols:
    display_df[col] = display_df[col].map('${:,.0f}'.format)
st.dataframe(display_df)

# Key Metrics (matching app.py output)
st.header("Performance Metrics")

# First row of metrics
col1, col2, col3 = st.columns(3)
col1.metric("Mean Return", f"{Mean_Return*100:.2f}%")
col2.metric("Standard Deviation", f"{Std_Dev:.2f}")
col3.metric("Sharpe Ratio", f"{Sharpe_Ratio:.2f}")

# Risk metrics row
st.subheader("Risk Metrics (95% Confidence Level)")
st.markdown("""
Value at Risk (VaR) and Conditional Value at Risk (CVaR) are calculated at a 95% confidence level:
- **VaR (95%)**: The maximum loss expected over a given period at 95% confidence level
- **CVaR (95%)**: The average loss in the worst 5% of cases (also known as Expected Shortfall)
""")

risk_col1, risk_col2, risk_col3 = st.columns(3)
risk_col1.metric("Value at Risk (95%)", f"{-VaR*100:.2f}%")
risk_col2.metric("Conditional VaR (95%)", f"{-CVaR*100:.2f}%")
risk_col3.metric(
    "Confidence Level",
    f"{confidence_level*100:.0f}%",
    help="VaR and CVaR are calculated at 95% confidence level"
)

# Risk Free Rate Display
st.header("Assumptions")
st.write(f"The risk-free rate is set to **{RiskFreeRate*100}%**")

# Visualizations
st.header("Price Analysis")
tab1, tab2 = st.tabs(["Price Trend", "Returns Analysis"])

with tab1:
    # Create closing price chart
    fig = px.line(Price, x='Year', y='Close', 
                  title='Gold Closing Price Evolution',
                  labels={'Close': 'Price (USD)', 'Year': 'Year'})
    fig.update_traces(line_color='gold', line_width=2)
    fig.update_layout(template='plotly_white', hovermode='x unified')
    # Format y-axis labels with dollar sign and commas
    fig.update_layout(yaxis=dict(tickprefix="$", tickformat=","))
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    # Returns Analysis
    col1, col2 = st.columns(2)
    
    with col1:
        # Returns over time
        fig_returns = px.line(x=Price['Year'][1:], y=Returns,
                            title='Returns Over Time',
                            labels={'x': 'Year', 'y': 'Returns'})
        fig_returns.update_traces(line_color='gold')
        fig_returns.update_layout(showlegend=False)
        # Format y-axis as percentage
        fig_returns.update_layout(yaxis=dict(tickformat=".1%"))
        st.plotly_chart(fig_returns, use_container_width=True)
    
    with col2:
        # Returns distribution
        fig_dist = px.histogram(Returns, nbins=20,
                              title='Returns Distribution',
                              labels={'value': 'Returns', 'count': 'Frequency'})
        fig_dist.update_traces(marker_color='gold')
        fig_dist.update_layout(showlegend=False)
        # Format x-axis as percentage
        fig_dist.update_layout(xaxis=dict(tickformat=".1%"))
        st.plotly_chart(fig_dist, use_container_width=True)

# Additional Information
st.sidebar.markdown("---")
st.sidebar.markdown("""
### Data Timeframe
Analysis covers gold closing prices from 2000 to 2024

### Analysis Details
This dashboard visualizes:
- Mean return and volatility
- Sharpe ratio
- Value at Risk (VaR)
- Conditional Value at Risk (CVaR)
- Price trends
- Returns analysis

### Risk Metrics Info
- VaR: Maximum expected loss at 95% confidence
- CVaR: Average loss beyond VaR threshold
""")
