from bs4 import BeautifulSoup
from .util import click_button


class Soup(BeautifulSoup):
    def __init__(self, html):
        super().__init__(html, 'html.parser', multi_valued_attributes=None)

    def scrape_product_info(self):
        """ Method to scrape product information"""
        article = self.find('main', class_='col-lg-6')
        title = article.find('h4').get_text()
        if article.find('div', class_='rating-wrap my-3').i['class'] == 'dot':
            sku = None
        else:
            sku = article.find('div', class_='rating-wrap my-3').find('i').get_text()
        stock = article.find('span', class_='label-rating text-success').text

        print(stock)