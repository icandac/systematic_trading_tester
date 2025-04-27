import pandas as pd

from portfolio_management.portolio_manager import PortfolioManager
from risk.sample_risk_calculator import RiskManager
from scripts.metrics import calculate_returns, calculate_sharpe_ratio


def run_backtest(df: pd.DataFrame):
    """
    A simple event-based backtester:
      - Step through each row in df.
      - Generate signal (already in df["signal"]).
      - Check risk & update portfolio with trades.
      - Track PnL.
    args:
        df (pd.DataFrame): DataFrame containing historical data with 'close' and 'signal' columns.
    returns:
        pd.DataFrame: DataFrame with additional columns for unrealized
                      PnL and returns.
    """
    pm = PortfolioManager()
    rm = RiskManager()

    # For collecting performance
    equity_curve = []

    for index, row in df.iterrows():
        current_signal = row["signal"]  # 1, -1, or 0
        current_price = row["close"]

        # Check if the risk manager approves
        if current_signal != 0 and rm.check_risk(current_price, current_signal):
            # Hard-coded quantity example
            quantity = rm.check_position_size(0.01)  # e.g. trade 0.01 BTC
            pm.update_position(
                signal=current_signal, price=current_price, quantity=quantity
            )

        # Evaluate unrealized PnL
        unrealized_pnl = pm.get_unrealized_pnl(current_price)
        equity_curve.append(unrealized_pnl)

    # Convert to pandas Series
    df["unrealized_pnl"] = equity_curve

    # Calculate final performance metrics
    # For simplicity, let's get returns from price only (no leveraged returns)
    df = calculate_returns(df, column="close")
    sr = calculate_sharpe_ratio(df["returns"])

    total_unrealized_pnl = df["unrealized_pnl"].iloc[-1]
    print(f"Final Unrealized PnL: {total_unrealized_pnl:.2f}")
    print(f"Sharpe Ratio (price-based): {sr:.2f}")

    return df
