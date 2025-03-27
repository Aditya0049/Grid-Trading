# Grid Trading Bot

## 📌 Overview
This is a **Grid Trading Bot** designed for trading assets like **Forex (EUR/USD)** and **Commodities (Gold - XAU/USD)**. The bot follows a **grid trading strategy**, which places buy and sell orders at fixed price intervals to capture market volatility.

## 🚀 Features
- **Automatic Grid Placement**: Creates multiple buy and sell levels.
- **PnL Tracking**: Includes **unrealized losses** and a **stop-loss mechanism**.
- **Backtesting Support**: Run simulations on historical data.
- **Customizable Parameters**: Adjust **grid size, levels, position size, and stop-loss %**.

## 📁 Project Structure
```
Grid Trading/
│── main.py                      # Entry point for running the backtest
│── config.py                     # Configuration file for parameters
│── data/                         # Folder for market data (CSV files)
│   ├── EURUSD_2025.csv           # Sample dataset
│── strategy/
│   ├── grid_trading.py           # Core grid trading logic
│   ├── backtest.py               # Backtesting module
│── results/                      # Folder for backtest results & plots
│── requirements.txt              # Dependencies
│── README.md                     # Documentation
```

## 📜 Installation
1️⃣ **Clone the Repository**
```bash
git clone https://github.com/yourusername/grid-trading-bot.git
cd grid-trading-bot
```

2️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

3️⃣ **Run Backtest**
```bash
python main.py
```

## ⚙️ Configuration (config.py)
Modify `config.py` to customize:
```python
INITIAL_BALANCE = 10000  # Starting capital
GRID_SIZE = 0.002        # Grid spacing (20 pips for EUR/USD)
GRID_LEVELS = 10         # Number of grid levels
POSITION_SIZE = 1000     # Trade size per grid level
STOP_LOSS_PCT = 5        # Stop-loss percentage
```

## 📊 Example Output (Backtest)
```
Date      Price     Type                     PnL  
-------------------------------------------------
27-03-25  1.0801   Buy                      -20  
26-03-25  1.0785   Buy                      -120  
25-03-25  1.0770   Forced Sell (Stop Loss)  -500  
Final PnL: -$500 ❌
```

## 📌 Notes
- This bot is **optimized for grid trading**, which works best in **sideways markets**.
- Implement **risk management** (e.g., stop-loss, position sizing) to avoid liquidation.
- For **live trading**, integrate with a broker API (e.g., Binance, MT5, Alpaca, etc.).

## 🛠️ Future Improvements
- ✅ **Live Trading API Integration**
- ✅ **Dynamic Grid Adjustment** (based on ATR/Volatility)
- ✅ **Multi-Asset Support**

## 📝 License
This project is licensed under the **MIT License**.

---
✉️ Need help? Reach out at [your email] or open an issue on GitHub!
