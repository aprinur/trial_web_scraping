from selenium import webdriver
import time


def get_html(url):
    driver = webdriver.Chrome()
    driver.get(url)
    r = driver.page_source
    time.sleep(5)
    return r
