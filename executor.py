import time
from binance.client import Client
import config.config_binance as config
from risk.sample_risk_calculator import RiskManager

class TradeExecutor:
    """
    Responsible for sending orders to Binance (market, limit, stop, etc.).
    """
    def __init__(self):
        self.client = Client(config.API_KEY, config.API_SECRET, testnet=config.TESTNET)
        self.rm = RiskManager()
        self.manual_override = False

    def place_order(self, symbol: str, side: str, quantity: float, order_type="MARKET"):
        """
        Places a market order. 
        side can be "BUY" or "SELL".
        Args:
            symbol (str): Trading pair symbol (e.g., "BTCUSDT").
            side (str): "BUY" or "SELL".
            quantity (float): Quantity to buy/sell.
            order_type (str): Type of order ("MARKET", "LIMIT", etc.).
        Returns:
            dict: Order response from Binance API.
        """
        if self.manual_override:
            print("[Manual Override] Order blocked by user.")
            return None
        
        # Check risk once more
        if not self.rm.check_risk(0.0, 1 if side == "BUY" else -1):
            print("Order blocked by risk manager.")
            return None
        
        try:
            # Convert quantity if needed to correct step size
            order = self.client.create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity
            )
            print(f"Placed {side} {order_type} order for {quantity} of {symbol}.")
            return order
        except Exception as e:
            print("Error placing order:", e)
            return None

    def set_manual_override(self, override: bool):
        """
        Enable or disable manual override. When True, all new orders are blocked.
        Args:
            override (bool): True to enable manual override, False to disable.
        """
        self.manual_override = override
