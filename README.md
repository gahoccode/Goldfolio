# Goldfolio Analysis

A Streamlit-based web application for analyzing financial portfolio data with a focus on performance metrics and visualizations.

## Features

- CSV file upload functionality
- Configurable risk-free rate
- Comprehensive performance metrics:
  - Annualized returns
  - Volatility
  - Sharpe ratio
  - Maximum drawdown
- Interactive visualizations:
  - Price charts
  - Returns distribution
  - Returns over time

## Installation

1. Clone this repository
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit app:
```bash
streamlit run st.py
```

2. Using the app:
   - Upload your CSV file using the sidebar uploader
   - Select the price column from your data
   - Adjust the risk-free rate using the slider
   - View the analysis results and visualizations

3. Default behavior:
   - If no file is uploaded, the app will use the default "Gold Price.csv" data
   - The default risk-free rate is set to 3%

## Data Format

Your CSV file should contain at least one column with price data. The app will automatically detect columns and allow you to select the appropriate price column for analysis.
