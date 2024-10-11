from bs4 import BeautifulSoup
from .models import Items


class Soup(BeautifulSoup):
    def __init__(self, html):
        super().__init__(html, 'html.parser')

    def scrape(self):
        title = self.find('div', class_='title').find('h1').get_text()
        price_tag = self.find('h4', class_='ps-product__price')
        normal_price = price_tag.find('del', class_='ps-product__price--old').get_text().replace('Harga Normal ', '')
        current_price = price_tag.find('span').get_text()
        card = self.find('div', class_='card-body align-self-center py-0')
        sku = card.find('b').get_text()
        code = card.find('b', id='code-EK 6807D23').get_text()
        weight = card.find('div', class_='product-weight fs-4 p-0 m-0').find('b').get_text()
        category = card.find('a', class_='fw-bold').get_text()
        sub_category = card.find('strong').get_text()
        brand = card.find_all('strong')[1].get_text().replace('PC Ready - ', '')
        img_url = self.find('img', class_='img-fluid lazy').get_attribute_list('src')
        components = self.find('table', class_='table ps-pcready__table-items').find('tbody')


        return Items(
            title=title
        )
