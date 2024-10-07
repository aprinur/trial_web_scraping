from bs4 import BeautifulSoup
from .display import Quotes


class Soup(BeautifulSoup):
    def __init__(self, html):
        super().__init__(html, 'html.parser')

    def scrape(self):
        quote = self.find('span', class_='text', itemprop='text').get_text()
        author = self.find('small', class_='author', itemprop='author').get_text()

        return Quotes(
            quote=quote,
            author=author
        )

