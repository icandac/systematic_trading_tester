import time

import config.config_binance as config
from backtest.backtester import run_backtest
from data_loader import fetch_historical_data
from executor import TradeExecutor
from strategy.sample_str1 import generate_signals


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


def main_live_trading():
    executor = TradeExecutor()

    while True:
        # 1. Fetch the latest data (e.g., last 100 candles)
        df = fetch_historical_data(
            symbol=config.TRADING_SYMBOL, interval=config.TIMEFRAME, limit=1000
        )

        # 2. Generate signals
        df = generate_signals(df)

        # 3. Check the latest signal (last row)
        latest_signal = df["signal"].iloc[-1]

        # For demonstration, place a market order if signal != 0
        if latest_signal == 1:
            executor.place_order(
                symbol=config.TRADING_SYMBOL, side="BUY", quantity=0.001
            )
        elif latest_signal == -1:
            executor.place_order(
                symbol=config.TRADING_SYMBOL, side="SELL", quantity=0.001
            )

        # Sleep until next iteration.
        # Adjust to your timeframe or use websockets.
        time.sleep(60)


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
