# setup.py
from setuptools import find_packages, setup

setup(
    name="systematic_trading_tester",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # e.g. "numpy>=1.25,<2.0",
        #      "pandas>=2.0,<3.0",
    ],
)
