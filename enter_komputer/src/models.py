from dataclasses import dataclass


@dataclass
class Items:
    title: str
    normal_price: int
    current_price: int
    sku: int
    code: str
    weight: str
    category: str
    brand: str
    sub_category: str
    img_url: str
    component: dict
