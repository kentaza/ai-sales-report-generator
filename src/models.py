from dataclasses import dataclass


@dataclass
class SalesRecord:
    date: str
    region: str
    product: str
    units_sold: int
    unit_price: float
