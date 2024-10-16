from dataclasses import dataclass


@dataclass
class Items:
    title: str
    normal_price: str
    current_price: str
    sku: int
    code: str
    weight: str
    category: str
    brand: str
    sub_category: str
    img_url: list
    processor: str
    motherboard: str
    ssd: str
    ram: str
    vga: str
    psu: str
    fan_casing: str
    cpu_coller: str
    network: str
    casing: str
    kb_m: str
    mousepad: str
    software: str
