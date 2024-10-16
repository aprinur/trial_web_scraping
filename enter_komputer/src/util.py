from selenium import webdriver
import time
import pandas as pd
from .models import Items
import datetime


def get_html(url):
    driver = webdriver.Chrome()
    driver.get(url)
    r = driver.page_source
    time.sleep(3)
    return r


def save_into_xlsx(item: list[Items], filename):
    date = datetime.datetime.now().strftime('%d_%B_%Y')
    df = pd.DataFrame(item)
    df.to_excel(f'{filename}_{date}.xlsx', index=False)
    df.to_csv(fr'D:\Github\aprinur\Web_Scraping\enter_komputer\Pc_Ready_{date}.csv')
