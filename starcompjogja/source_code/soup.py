from bs4 import BeautifulSoup
from .util import click_button


class Soup(BeautifulSoup):
    def __init__(self, html):
        super().__init__(html, 'html.parser')

    def scrape_product_info(self):
        """ Method to scrape product information"""
        article = self.find('article', class_='ps-lg-3')
        title = article.get_text()
        print(title)