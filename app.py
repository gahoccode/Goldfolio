import pandas as pd
import numpy as np

fileName = "Gold Price.csv"
Price = pd.read_csv(fileName)
# print(Price.head())
Returns = Price["Close"].pct_change().dropna()  # Calculate returns
# print(Returns.head())
Mean_Return = Returns.mean()  # Calculate mean return
Std_Dev = Returns.std()  # Calculate standard deviation
RiskFreeRate = 0.03
Sharpe_Ratio = (Mean_Return - RiskFreeRate) / Std_Dev  # Calculate Sharpe Ratio
print(f"The Sharpe ratio is {Sharpe_Ratio}")
print(f"The standard deviation is {(Std_Dev):.2f}")
print(f"The mean return is {(Mean_Return*100):.2f}%")
print(f"The risk free rate is assumed to {(RiskFreeRate*100)}%")
