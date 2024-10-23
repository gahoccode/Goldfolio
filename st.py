import streamlit as st
import pandas as pd
import numpy as np

# Load Data
fileName = "Gold Price.csv"
Price = pd.read_csv(fileName)

# Calculate Returns
Returns = Price["Close"].pct_change().dropna()

# Calculate Metrics
Mean_Return = Returns.mean()
Std_Dev = Returns.std()
RiskFreeRate = 0.03
Sharpe_Ratio = (Mean_Return - RiskFreeRate) / Std_Dev

# Streamlit App
st.title("Gold Price Analysis")

st.header("Gold Price Data")
st.dataframe(Price.head())

st.header("Returns Analysis")

# Metrics Display
col1, col2 = st.columns(2)
col1.metric("Mean Return", f"{Mean_Return*100:.2f}%")
col2.metric("Standard Deviation", f"{Std_Dev:.2f}")

st.header("Sharpe Ratio")
st.write(f"The Sharpe ratio is **{Sharpe_Ratio:.2f}**")

# Risk Free Rate Display
st.header("Assumptions")
st.write(f"The risk-free rate is assumed to be **{RiskFreeRate*100}%**")

# Plotting Returns
st.header("Gold Returns Over Time")
st.line_chart(Returns)

# Additional Information
st.sidebar.title("Analysis Details")
st.sidebar.write(
    "This app calculates the Sharpe Ratio for gold price data, showing risk and return metrics."
)

# Running the App
# Streamlit run st.py
