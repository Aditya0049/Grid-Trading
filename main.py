# main.py

import pandas as pd
from strategy.backtest import Backtest

# Load Data
df = pd.read_csv("data/EUR_USD_data.csv")
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)  # Correct date format
df["Price"] = df["Price"].astype(float)  # Convert to numeric
df = df.sort_values("Date").reset_index(drop=True)

# Run Backtest
backtest = Backtest(df)
backtest.run()
