from dataclasses import dataclass


@dataclass
class Items:
    Title: str
    Normal_price: str
    Current_price: str
    Sku: int
    Code: str
    Weight: str
    Category: str
    Brand: str
    Sub_category: str
    Img_url: list
    Processor: str
    Motherboard: str
    Ssd: str
    Ram: str
    Vga: str
    Psu: str
    Fan_casing: str
    Cpu_cooler: str
    Network: str
    Casing: str
    Keyboard_mouse: str
    Mousepad: str
    Software: str
