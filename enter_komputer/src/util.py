from selenium import webdriver
import time
import pandas as pd
from .models import Items
import datetime


def get_html(url):
    driver = webdriver.Chrome()
    driver.get(url)
    r = driver.page_source
    return r


def save_to_file(item: list[Items], filename):
    date = datetime.datetime.now().strftime('%d_%B_%Y')
    items_dicts = [i.__dict__ for i in item]
    df = pd.DataFrame(items_dicts)
    df.to_excel(f'{filename}_{date}.xlsx', index=False)
    df.to_csv(fr'D:\Github\aprinur\Web_Scraping\enter_komputer\{filename}_{date}.csv', index=False)
