# Systematic Trading Tester

A small library for backtesting algorithmic trading strategies.

## Introduction

Note: to get the code structure, tree -I '*.pyc|__pycache__'

Library skeleton:

```.
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
```

## Installation

This library uses python3.11 for the current being. So, one should have 3.11 version of python to start. Then clone the repo by

```bash
git clone git@github.com:icandac/systematic_trading_tester.git
```

After that, do the following respectively to install the whole library without having issues.

Note: There is an ongoing issue with the backtester package we particularly handle which is addressed in one of the first issues and will be solved hopefully soon.

```bash
virtualenv --python=python3.11 .venv
source .venv/bin/activate
grep -v '^backtester==' requirements.txt > req-no-backtester.txt
pip install -r req-no-backtester.txt
pip install scikit-learn==1.6.1
pip install backtester==0.7 --no-deps
```

After these all, one should have successfully installed all necessary packages and ready to try the lib out already.

If one is interested in auto-push in developer mode, make

```bash
chmod +x git-auto.sh
```

then the developer can pre-commit, commit and push just with one CLI command which is

```bash
./git-auto.sh
```
.

## Usage

python main.py backtest
python main.py live (change testnet to True or False for paper or live trading)

## Tests

1. test_live_cycle to test a simple live cycle.

## Road-map:
- Also allowing manual trading execution by creating the same output like a bill of exchange, for discretionary trading
- Logging with logging/loguru/live dashboard also to output sharp, returns, and PnL with live trading
- Market status checker (bull, bear, etc.)
- Explore how to output different indicators, one number parameters, charts for strategy testing and comparison for the same historical time intervals.
- a second test strategy with kelly criterion and high-high low-low breakouts with stop-loss and many other easy to implement first strategies
- Store (live?) data to ipc files or sql db?
- websocket (live) data feeds
- asyncio to parallel process different calculations
- docker container to make it it up and running anywhere (in a cloud service?)
- alert/notification to telegram or e-mail
- Protect your main branch (optional due to the fact that I am the only developer currently and the repo can progress quickly)

## License

This code is available on GitHub under [the GNU Lesser General Public License v3.0](https://www.gnu.org/licenses/lgpl-3.0.en.html).
