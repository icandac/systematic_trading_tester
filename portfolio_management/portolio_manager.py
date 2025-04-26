import pandas as pd

class PortfolioManager:
    """
    Simple portfolio manager that tracks position, average cost, PnL.
    """
    def __init__(self):
        self.position_size = 0.0
        self.entry_price = 0.0

    def update_position(self, signal: int, price: float, quantity: float):
        """
        Update the portfolio based on the new trade signal.
        """
        if signal == 1:
            # Assume "buy" or "go long"
            if self.position_size == 0:
                self.position_size = quantity
                self.entry_price = price
            else:
                # If you already have a position, you might do partial add, etc.
                # This is an example: Weighted Average Price
                total_cost = self.entry_price * self.position_size + price * quantity
                self.position_size += quantity
                self.entry_price = total_cost / self.position_size
        
        elif signal == -1:
            # For simplicity, assume "sell/close" entire position if we have any
            if self.position_size > 0:
                # Real PnL calculation
                realized_pnl = (price - self.entry_price) * self.position_size
                print(f"PnL from closing position: {realized_pnl:.2f}")
                # Reset
                self.position_size = 0.0
                self.entry_price = 0.0
        else:
            # No change
            pass

    def get_unrealized_pnl(self, current_price: float):
        """
        Calculate unrealized PnL based on current price.
        """
        if self.position_size > 0:
            return (current_price - self.entry_price) * self.position_size
        return 0.0
