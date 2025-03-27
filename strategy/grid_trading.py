# strategy/grid_trading.py

import pandas as pd
from config import GRID_SIZE, NUM_LEVELS, TRADE_SIZE, INITIAL_BALANCE


class GridTrading:
    def __init__(self, initial_balance, grid_size=0.002, grid_levels=10, position_size=1000):
        self.balance = initial_balance
        self.grid_size = grid_size  # 0.002 = 20 pips
        self.grid_levels = grid_levels
        self.position_size = position_size
        self.open_positions = []

    def run_strategy(self, data):
        trade_log = []
        base_price = data["Price"].iloc[0]
        grid_prices = [base_price + i * self.grid_size for i in range(-self.grid_levels, self.grid_levels + 1)]

        for index, row in data.iterrows():
            price = row["Price"]
            date = row["Date"]

            # Execute Buy Orders
            for level in grid_prices:
                if price <= level and all(pos["Price"] != level for pos in self.open_positions):
                    self.open_positions.append({"Date": date, "Price": level, "Type": "Buy"})
                    trade_log.append({"Date": date, "Price": level, "Type": "Buy", "PnL": self.balance})

            # Execute Sell Orders (Grid Exit)
            for position in self.open_positions[:]:
                if price >= position["Price"] + self.grid_size:
                    profit = (price - position["Price"]) * self.position_size
                    self.balance += profit
                    self.open_positions.remove(position)
                    trade_log.append({"Date": date, "Price": price, "Type": "Sell", "PnL": self.balance})

        final_pnl = self.balance - INITIAL_BALANCE
        return pd.DataFrame(trade_log), final_pnl
