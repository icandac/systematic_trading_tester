from dataclasses import dataclass
from enum import Enum

class Side(str, Enum):
    BUY  = "BUY"
    SELL = "SELL"

class OrderType(str, Enum):
    MARKET = "MARKET"
    LIMIT  = "LIMIT"

@dataclass
class Order:
    symbol:   str
    side:     Side
    qty:      float
    order_type: OrderType = OrderType.MARKET
    price:    float | None = None          # needed only for LIMIT
    tag:      str = "manual"               # free text – strategy name, ticket ID …
