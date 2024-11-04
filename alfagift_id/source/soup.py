from bs4 import BeautifulSoup
from .model import Items
from .__init__ import URL


class Soup(BeautifulSoup):
    def __init__(self, html):
        super().__init__(html, 'html.parser')

    def scrape_product(self):
        """Method to scrape information from the product"""
        table = self.find('div', class_='col-sm-12 col-md-12 col-lg-5 col-12')
        tittle = table.find('p', class_='text-xl fw5 d-lg-none').get_text().strip()
        if table.find('a', class_='text-sm fw7 text-secondary text-decoration-none ml-2'):
            brand = table.find('a', class_='text-sm fw7 text-secondary text-decoration-none ml-2').get_text().capitalize()
        else:
            brand = None
        original_price = None
        if table.find('del', class_='text-neutral-60 text-sm'):
            original_price = table.find('del', class_='text-neutral-60 text-sm').get_text().strip()
        elif table.find('p', class_='text-xlg fw7 text-primary mb-1'):
            original_price = table.find('p', class_='text-xlg fw7 text-primary mb-1').get_text().strip()
        elif table.find('div', class_='alert alert-danger text-sm border-0 rounded-md'):
            original_price = (table.find('div', class_='alert alert-danger text-sm border-0 rounded-md').get_text().strip())

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

        # print(brand)
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

    def check_total_page(self):
        """ Method to check total page"""
        return str(''.join(self.find('button', class_='page-link').get_attribute_list('aria-setsize')))

    def previous_page(self):
        """ Method to return to page after select category"""
        page = ''.join([page.find_next('a')['href'] for page in self.find_all('li', class_='breadcrumb-item')[1]])
        return page.replace('/c', f'{URL}c')

    def final_page(self):
        """Method to check final page"""
        return bool(self.find('span', attrs={'aria-label': 'Go to next page', 'class': 'page-link'}))

