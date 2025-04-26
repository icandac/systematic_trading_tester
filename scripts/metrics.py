import pandas as pd
import numpy as np

def calculate_returns(df: pd.DataFrame, column="close"):
    """
    Calculate log returns or simple returns on 'column'.
    """
    df["returns"] = df[column].pct_change().fillna(0)
    return df

def calculate_sharpe_ratio(returns, risk_free_rate=0.00):
    """
    Calculate Sharpe Ratio = (mean(returns) - risk_free_rate) / std(returns)
    """
    excess_returns = returns - risk_free_rate
    if np.std(excess_returns) == 0:
        return 0
    return np.mean(excess_returns) / np.std(excess_returns)
