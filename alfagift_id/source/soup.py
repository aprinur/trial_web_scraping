from bs4 import BeautifulSoup
from .model import Items
from .__init__ import URL


class Soup(BeautifulSoup):
    def __init__(self, html):
        super().__init__(html, 'html.parser')

    def scrape_product(self):
        """Method to scrape information from the product"""
        table = self.find('div', class_='col-sm-12 col-md-12 col-lg-5 col-12')
        tittle = (table.find('p', class_='text-xlg fw7 d-none d-sm-none d-md-none d-lg-block')
                  .get_text().strip().capitalize())
        brand = table.find('a', class_='text-sm fw7 text-secondary text-decoration-none ml-2').get_text()

        original_price = None
        if table.find('del', class_='text-neutral-60 text-sm'):
            original_price = table.find('del', class_='text-neutral-60 text-sm').get_text().strip()
        elif table.find('p', class_='text-xlg fw7 text-primary mb-1'):
            original_price = table.find('p', class_='text-xlg fw7 text-primary mb-1').get_text().strip()
        elif table.find('div', class_='alert alert-danger text-sm border-0 rounded-md'):
            original_price = (table.find('div',
                                         class_='alert alert-danger text-sm border-0 rounded-md')
                              .get_text().strip())

        discount = table.find('span', class_='badge badge-disc mr-1').get_text() if (
            table.find('span', class_='badge badge-disc mr-1')) else 'None'

        current_price = None
        if table.find('p', class_='text-xlg fw7 text-primary mb-1'):
            current_price = table.find('p', class_='text-xlg fw7 text-primary mb-1').get_text().strip()
        elif table.find('div', class_='alert alert-danger text-sm border-0 rounded-md'):
            current_price = (table.find('div',
                                        class_='alert alert-danger text-sm border-0 rounded-md')
                             .get_text().strip())
        image_url = []
        urls = [img.get_attribute_list('src') for img in self.find_all('img',
                                                                       class_='img-fluid margin-auto')]
        urls = [item for sublist in urls for item in sublist]
        for url in urls:
            if url not in image_url:
                image_url.append(url)

        description = [d.get_text() for d in self.find('div', class_='description-box').find_all('li')]

        return Items(
            Tittle=tittle,
            Brand=brand,
            Original_price=original_price,
            Discount=discount,
            Current_price=current_price,
            Image_url=image_url,
            Description=description
        )

    def scrape_product_url(self):
        """Method to scrape product urls after choose category"""
        urls = [url.get_attribute_list('href') for url in
                self.find('div', class_='row list-product').find_all('a',
                                                                     class_='text-decoration-none')]
        urls = [' '.join([str(c).replace('/p', f'{URL}p', 1) for c in lst])
                for lst in urls]
        # print(urls)
        return urls

    def scrape_category_url(self):
        """Method to scrape urls of category from main page"""
        links = [link.find('a').get_attribute_list('href') for link in
                 self.find_all('div', class_='list-group-item list-lv1')]
        links = [' '.join([str(c).replace('/c', f'{URL}c', ) for c in lst]) for lst in links]
        return links

    def scrape_active_page(self):
        """ Method to scrape active page"""
        return ''.join(self.find('button', attrs={'aria-checked': 'true'}).get_attribute_list('aria-posinset'))

    def check_final_page(self):
        """ Method to check final page"""
        return self.find('span', attrs={'aria-disabled': 'true'})

    def previous_page(self):
        """ Method to return to page after select category"""
        page = [url.find('a').get_attribute_list('href') for url in self.find_all('li', class_='breadcrumb-item')]
        return page

