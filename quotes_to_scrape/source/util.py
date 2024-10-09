import requests  # Mengimpor library requests untuk melakukan HTTP request
import pandas as pd  # Mengimpor library pandas untuk memproses data dan menyimpan ke Excel
from .display import Quotes  # Mengimpor class Quotes dari modul display
from .soup import Soup  # Mengimpor class Soup dari modul soup


def get_html(url):  # Fungsi untuk mengambil konten HTML dari URL
    respons = requests.get(url)  # Melakukan HTTP GET request ke URL
    return Soup(respons.text)  # Mengembalikan instance Soup dengan konten HTML dari respons


def save_to_xsls(quotes: list[Quotes], filename: str):  # Fungsi untuk menyimpan hasil scraping ke file Excel
    df = pd.DataFrame(quotes)  # Membuat DataFrame dari list quotes
    df.to_excel(filename)  # Menyimpan DataFrame ke file Excel dengan nama yang diberikan

