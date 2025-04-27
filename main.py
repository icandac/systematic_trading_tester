import time

import config.config_binance as config
from backtest.backtester import run_backtest
from strategy.sample_str1 import generate_signals

from .data_loader import fetch_historical_data
from .executor import TradeExecutor


def main_backtest():
    # 1. Fetch data
    df = fetch_historical_data(
        symbol=config.TRADING_SYMBOL, interval=config.TIMEFRAME, limit=200
    )

    # 2. Generate signals
    df = generate_signals(df)

    # 3. Run backtest
    results_df = run_backtest(df)
    time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    # print(results_df.tail(10))
    results_df.to_csv(f"./outputs/backtest_results_{time_now}.csv", index=False)


def main_live_trading(cycles: int | None = None, sleep_seconds: int = 60):
    """
    Run live (or testnet) trading.
    Args:
        cycles: int | None
            If None, run forever.
            If int, run for N cycles.
        sleep_seconds: int
    """
    executor = TradeExecutor()
    i = 0

    while True:
        # 1. Fetch the latest data (e.g., last 100 candles)
        df = fetch_historical_data(
            symbol=config.TRADING_SYMBOL, interval=config.TIMEFRAME, limit=1000
        )

        # 2. Generate signals
        df = generate_signals(df)
        latest_signal = df["signal"].iloc[-1]

        # Execute
        if latest_signal == 1:
            executor.place_order(
                symbol=config.TRADING_SYMBOL, side="BUY", quantity=0.001
            )
        elif latest_signal == -1:
            executor.place_order(
                symbol=config.TRADING_SYMBOL, side="SELL", quantity=0.001
            )

        # 4. Exit early in tests
        i += 1
        if cycles is not None and i >= cycles:
            break

        time.sleep(sleep_seconds)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "mode", choices=["backtest", "live"], help="Run backtest or live trading"
    )
    args = parser.parse_args()

    if args.mode == "backtest":
        main_backtest()
    else:
        main_live_trading()
