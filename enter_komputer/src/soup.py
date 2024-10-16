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
        sku = int(card.find('b').get_text())
        code = card.find_all('b')[1].get_text()
        weight = card.find('div', class_='product-weight fs-4 p-0 m-0').find('b').get_text()
        category = card.find('a', class_='fw-bold').get_text()
        sub_category = card.find('strong').get_text()
        brand = card.find_all('strong')[1].get_text().replace('PC Ready - ', '')
        img_urls = [i['href'] for i in
                    self.find('div', class_='row row-cols-3 row-cols-sm-3 row-cols-md-4').find_all('a')]
        table = self.find('table', class_='table ps-pcready__table-items').find('tbody')

        components_data = {}

        for component in table.find_all('td', class_='fw-bold-thin'):
            components_data['processor'] = str(' '.join(component.br.next_sibling.strip().split()) if component.find('span', class_='text-uppercase fw-bold fs-3').get_text() == 'Processor' else None)
            components_data['motherboard'] = str(' '.join(component.br.next_sibling.strip().split()) if component.find('span', class_='text-uppercase fw-bold fs-3').get_text() == 'Motherboard' else None)
            components_data['ssd'] = str(' '.join(component.br.next_sibling.strip().split()) if component.find('span', class_='text-uppercase fw-bold fs-3').get_text() == 'SSD' else None)
            components_data['vga'] = str(' '.join(component.br.next_sibling.strip().split()) if component.find('span', class_='text-uppercase fw-bold fs-3').get_text() in ['radeon', 'nvidia'] else 'Integrated Gpu')
            components_data['ram'] = str(' '.join(component.br.next_sibling.strip().split()) if component.find('span', class_='text-uppercase fw-bold fs-3').get_text() == 'RAM' else None)
            components_data['psu'] = str(' '.join(component.br.next_sibling.strip().split()) if component.find('span', class_='text-uppercase fw-bold fs-3').get_text() == 'PSU' else None)
            components_data['casing'] = str(' '.join(component.br.next_sibling.strip().split()) if component.find('span', class_='text-uppercase fw-bold fs-3').get_text() == 'Casing' else None)
            components_data['fan_casing'] = str(' '.join(component.br.next_sibling.strip().split()) if component.find('span', class_='text-uppercase fw-bold fs-3').get_text() == 'Fan Casing 12CM Fan Case' else None)
            components_data['cpu_coller'] = str(' '.join(component.br.next_sibling.strip().split()) if component.find('span', class_='text-uppercase fw-bold fs-3').get_text() in ['Air Cooler / Heatsink Cooler', 'Liquid Cooler / Water Cooler'] else None)
            components_data['network'] = str(' '.join(component.br.next_sibling.strip().split()) if component.find('span', class_='text-uppercase fw-bold fs-3').get_text() == 'Networking' else None)
            components_data['software'] = str(' '.join(component.br.next_sibling.strip().split()) if component.find('span', class_='text-uppercase fw-bold fs-3').get_text() == 'Software' else None)
            components_data['kb_m'] = str(' '.join(component.br.next_sibling.strip().split()) if component.find('span', class_='text-uppercase fw-bold fs-3').get_text() == 'Keyboard + Mouse' else None)
            components_data['mousepad'] = str(' '.join(component.br.next_sibling.strip().split()) if component.find('span', class_='text-uppercase fw-bold fs-3').get_text() == 'Mousepad' else None)

        return Items(
            title=title,
            normal_price=normal_price,
            current_price=current_price,
            sku=sku,
            code=code,
            weight=weight,
            category=category,
            brand=brand,
            sub_category=sub_category,
            img_url=img_urls,
            processor=components_data['processor'],
            motherboard=components_data['motherboard'],
            ssd=components_data['ssd'],
            ram=components_data['ram'],
            vga=components_data['vga'],
            psu=components_data['psu'],
            fan_casing=components_data['fan_casing'],
            cpu_coller=components_data['cpu_coller'],
            network=components_data['network'],
            casing=components_data['casing'],
            kb_m=components_data['kb_m'],
            mousepad=components_data['mousepad'],
            software=components_data['software']
        )

    def get_urls(self):
        url = [url.find('a')['href'] for url in self.find_all('div', class_='card-pcready__box mb-5')]
        return url
