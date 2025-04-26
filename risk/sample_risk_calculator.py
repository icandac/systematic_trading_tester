import config.config_binance as config

class RiskManager:
    """
    Basic risk manager that checks position sizing and potential drawdown.
    """
    def __init__(self):
        self.max_position_size = config.MAX_POSITION_SIZE

    def check_position_size(self, proposed_size: float) -> float:
        """
        Ensure the proposed size doesn't exceed the maximum allowed position size.
        """
        if proposed_size > self.max_position_size:
            return self.max_position_size
        return proposed_size

    def check_risk(self, current_price: float, signal: int) -> bool:
        """
        Additional checks before placing a trade. 
        For example, max drawdown, partial offsets, etc. 
        Here, we just do a trivial pass-through.
        """
        # If more advanced logic is needed, implement here
        return True
