from bs4 import BeautifulSoup
from .model import Items
from .__init__ import URL


class Soup(BeautifulSoup):
    def __init__(self, html):
        super().__init__(html, 'html.parser')

    def scrape_item(self):
        """Method to scrape information from the product"""
        table = self.find('div', class_='col-sm-12 col-md-12 col-lg-5 col-12')
        tittle = table.find('p', class_='text-xlg fw7 d-none d-sm-none d-md-none d-lg-block').get_text().strip()
        brand = table.find('a', class_='text-sm fw7 text-secondary text-decoration-none ml-2').get_text()
        original_price = table.find('del', class_='text-neutral-60 text-sm').get_text()
        discount = table.find('span', class_='badge badge-disc mr-1').get_text()
        current_price = table.find('p', class_='text-xlg fw7 text-primary mb-1').get_text().strip()
        description = [d.get_text() for d in self.find('div', class_='description-box').find_all('li')]

        return Items(
            tittle=tittle,
            brand=brand,
            original_price=original_price,
            discount=discount,
            current_price=current_price,
            description=description
        )

    def scrape_url(self):
        """Method to scrape url product from product page"""
        urls = [url.get_attribute_list('href') for url in self.find('div', class_='row list-product').find_all('a', class_='text-decoration-none')]
        urls = [' '.join([str(c).replace('/p', f'{URL}p', 1) for c in lst]) for lst in urls]
        print(urls)
        # return urls

    def scrape_links(self):
        """Method to scrape url category from category page"""
        links = [link.find('a').get_attribute_list('href') for link in self.find_all('div', class_='list-group-item list-lv1')]
        links = [' '.join([str(c).replace('/c', f'{URL}c', ) for c in lst]) for lst in links]
        print(links)
