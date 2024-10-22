from dataclasses import dataclass


@dataclass
class Items:
    tittle: str
    brand: str
    original_price: str
    discount: str
    current_price: str
    description: list
