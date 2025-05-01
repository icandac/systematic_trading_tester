import pandas as pd
import numpy as np
import config.config_binance as config
from main import main_live_trading
import data_loader

def fake_data(*args, **kwargs):
    """Return a 100-row dataframe with a guaranteed long signal on the last row."""
    rng = pd.date_range("2024-01-01", periods=100, freq="h")
    # make a steadily rising price series
    prices = prices = 30_000 + np.arange(100)
    df = pd.DataFrame({"open_time": rng,
                       "open": prices,
                       "high": prices,
                       "low": prices,
                       "close": prices,
                       "volume": 1})
    from strategy.sample_str1 import generate_signals
    df = generate_signals(df)
    return df

class DummyExecutor:
    def __init__(self):          # must match TradeExecutor signature
        self.calls = []

    def place_order(self, **kwargs):
        self.calls.append(kwargs)
        return {"status": "FILLED"}

def test_one_live_cycle(monkeypatch):
    """
    Runs exactly ONE live-trading iteration with TESTNET=True
    but without real HTTP calls or sleeping.
    Args:
        monkeypatch: pytest fixture to patch methods
    """
    # --- 1) force testnet mode just in case
    monkeypatch.setattr(config, "TESTNET", True, raising=False)

    # --- 2) patch data loader + executor + sleep
    monkeypatch.setattr("main.fetch_historical_data", fake_data)
    dummy_exec = DummyExecutor()
    monkeypatch.setattr("main.TradeExecutor", lambda: dummy_exec)
    monkeypatch.setattr("main.time.sleep", lambda x: None)

    # --- 3) run one cycle
    main_live_trading(cycles=1, sleep_seconds=0)

    # --- 4) check we tried to place exactly one BUY order
    assert len(dummy_exec.calls) == 1
    order = dummy_exec.calls[0]
    assert order["side"] == "BUY"
    assert order["symbol"] == config.TRADING_SYMBOL
