import requests
import pandas as pd
from .display import Quotes
from .soup import Soup


def get_html(url):
    respons = requests.get(url)
    return Soup(respons.text)


def save_to_xsls(quotes: list[Quotes], filename: str):
    df = pd.DataFrame(quotes)
    df.to_excel(filename)


