# strategy/backtest.py

import pandas as pd
import matplotlib.pyplot as plt
from strategy.grid_trading import GridTrading
from config import INITIAL_BALANCE

class Backtest:
    def __init__(self, data):
        self.data = data
        self.strategy = GridTrading(INITIAL_BALANCE)

    def run(self):
        # Run the strategy
        trade_log, final_pnl = self.strategy.run_strategy(self.data)

        # Save results
        trade_log.to_csv("results/trade_log.csv", index=False)
        print(f"Final PnL: ${final_pnl:.2f}")  # Display the final PnL

        self.plot_results(trade_log)

    def plot_results(self, trade_log):
        plt.figure(figsize=(10, 5))
        plt.plot(self.data["Date"], self.data["Price"], label="EUR/USD Price", color="blue")

        buy_trades = trade_log[trade_log["Type"] == "Buy"]
        sell_trades = trade_log[trade_log["Type"] == "Sell"]

        plt.scatter(buy_trades["Date"], buy_trades["Price"], color="green", label="Buys", marker="^")
        plt.scatter(sell_trades["Date"], sell_trades["Price"], color="red", label="Sells", marker="v")

        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.title(f"Grid Trading Strategy Backtest | Final PnL: ${trade_log['PnL'].iloc[-1]:.2f}")
        plt.legend()
        plt.savefig("results/performance.png")
        plt.close()  # Prevents freezing
