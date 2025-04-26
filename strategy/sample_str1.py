import pandas as pd
import config.config_binance as config

def moving_average_crossover_signals(df: pd.DataFrame, short_window: int, long_window: int):
    """
    For each row in df, compute short and long moving averages and generate signals:
      - 1 for buy/long
      - -1 for sell/short
      - 0 for hold/do nothing
    Args:
      df (pd.DataFrame): DataFrame containing the price data.
      short_window (int): Short moving average window.
      long_window (int): Long moving average window.
    Returns:
      pd.DataFrame: DataFrame with additional columns for short and long moving averages and signals.
    """
    df["MA_short"] = df["close"].rolling(short_window).mean()
    df["MA_long"] = df["close"].rolling(long_window).mean()
    
    df["signal"] = 0
    df.loc[df["MA_short"] > df["MA_long"], "signal"] = 1
    df.loc[df["MA_short"] < df["MA_long"], "signal"] = -1
    
    # SHIFT the signal to represent "this is what we do at next candle"
    df["signal"] = df["signal"].shift(1).fillna(0)
    
    return df

def generate_signals(df: pd.DataFrame):
    """
    Wrapper to call whichever strategies you want.
    Currently uses a simple MA crossover strategy.
    Args:
      df (pd.DataFrame): DataFrame containing the price data.
    Returns:
      pd.DataFrame: DataFrame with additional columns for signals.
    """
    short_window = config.SHORT_WINDOW
    long_window = config.LONG_WINDOW
    
    df = moving_average_crossover_signals(df, short_window, long_window)
    return df
