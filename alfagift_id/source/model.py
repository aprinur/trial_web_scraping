from dataclasses import dataclass


@dataclass
class Items:
    Tittle: str
    Brand: str
    Original_price: str
    Discount: str
    Current_price: str
    Image_url: list
    Description: list
