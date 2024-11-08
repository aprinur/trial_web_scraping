from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


def get_item(url):
    return driver.get(url)


def click_button(url, args):
    driver.get(url)
    driver.find_element(By.CLASS_NAME, args).click()