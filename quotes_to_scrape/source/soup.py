from bs4 import BeautifulSoup
from .display import Quotes


class Soup(BeautifulSoup):
    def __init__(self, html):
        super().__init__(html, 'html.parser')
        self.url = None

    def scrape(self):
        quotes = self.find_all('div', class_='quote')
        output = []
        for quote_tag in quotes:
            quote = quote_tag.find('span', class_='text').get_text()
            author = quote_tag.find('small', class_='author', itemprop='author').get_text()
            output.append({'quote': quote,
                           'author': author})
        return output

    @staticmethod
    def url_list(url, rep):
        all_url = []
        for i in range(1, rep + 1):
            page_url = url.format(i=i)
            i += 1
            all_url.append(page_url)
        return all_url
