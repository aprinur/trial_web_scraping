from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import pandas
import datetime

driver = webdriver.Chrome()


def press_button(tag):
    try:
        next_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, tag)))
        driver.execute_script("arguments[0].click();", next_button)
        return True
    except Exception as e:
        print(f'Error pressing button: {e}')
        return False


def get_html(url):
    driver.get(url)
    time.sleep(2)
    return driver.page_source


def get_current_url():
    return driver.page_source


def save_to_file(product, filename):
    date = datetime.datetime.now().strftime('%d_%B_%Y')
    df = pandas.DataFrame(product)
    df.to_excel(f'{filename}_{date}.xlsx', index=False)
    df.to_csv(fr'D:\Github\aprinur\Web_Scraping\alfagift_id\{filename}_{date}.csv', index=False)


def wait_emergence(class_name):
    return WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, f"{class_name}")))


"""
press_button(".page-link[aria-label='Go to next page']")


'.'                            = indicates a css class selector
'page-link'                    = refers to an element that has the class='page-link'
'[]'                           = to target elements with specific attributes
'aria-label='Go to next page'' = an attribute selector that finds elements where the 
                                 aria-label attribute exactly matches 'Go to next page'

.page-link[aria-label='Go to next page'] this is a compound selector combining both a 
class and an attribute, it selects an element that both has the class="page-link" and 
has an aria-label attribute with the value 'Go to next page'                               
"""
