# Systematic Trading Tester

A small library for backtesting algorithmic trading strategies.

## Installation

```bash
pip install -e .
pip install -r requirements.txt

## Usage

python main.py backtest

## Introduction
Note: to get the code structure, tree -I '*.pyc|__pycache__'
.
├── __init__.py
├── backtest
│   ├── __init__.py
│   └── backtester.py
├── config
│   ├── __init__.py
│   └── config_binance.py
├── data
│   └── __init__.py
├── data_loader.py
├── executor.py
├── main.py
├── outputs
│   ├── backtest_results_2025-04-26 00:27:31.csv
│   └── backtest_results_2025-04-26 00:31:05.csv
├── portfolio_management
│   ├── __init__.py
│   └── portolio_manager.py
├── readme.md
├── requirements.txt
├── risk
│   ├── __init__.py
│   └── sample_risk_calculator.py
├── scripts
│   ├── __init__.py
│   └── metrics.py
├── setup.py
├── strategy
│   ├── __init__.py
│   └── sample_str1.py
└── systematic_trading_tester.egg-info
    ├── PKG-INFO
    ├── SOURCES.txt
    ├── dependency_links.txt
    └── top_level.txt

## Installation

## Road-map:
- Logging with logging/loguru/live dashboard also to output sharp, returns, and PnL with live trading
- Explore how to output different indicators, one number parameters, charts for strategy testing and comparison for the same historical time intervals.
- a second test strategy with kelly criterion and high-high low-low breakouts with stop-loss and many other easy to implement first strategies
- Store (live?) data to ipc files or sql db?
- websocket (live) data feeds
- asyncio to parallel process different calculations
- docker container to make it it up and running anywhere (in a cloud service?)
- alert/notification to telegram or e-mail
- 

## Licence

