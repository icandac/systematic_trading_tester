# manual_orders.py
import json
import pathlib
from typing import List

import yaml

from .order_types import Order, OrderType, Side

SCHEMA = {
    "required": {"symbol", "side", "qty"},  # minimal validation
    "optional": {"order_type", "price", "tag"},
}


def _validate(item: dict):
    missing = SCHEMA["required"] - item.keys()
    if missing:
        raise ValueError(f"Missing fields {missing} in manual order")
    return Order(
        symbol=item["symbol"].upper(),
        side=Side(item["side"].upper()),
        qty=float(item["qty"]),
        order_type=OrderType(item.get("order_type", "MARKET").upper()),
        price=float(item["price"]) if item.get("price") else None,
        tag=item.get("tag", "manual"),
    )


def load_orders(path: str | pathlib.Path) -> List[Order]:
    p = pathlib.Path(path)
    data = (
        yaml.safe_load(p.read_text())
        if p.suffix in {".yml", ".yaml"}
        else json.loads(p.read_text())
    )
    if isinstance(data, dict):  # allow single-order file
        data = [data]
    return [_validate(item) for item in data]
