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
        sub_category = card.find('strong').get_text() if '<strong>' in str(self.find('div', class_='categories product-subcategory fs-4 p-0 m-0')) else None
        brand = card.find_all('div', class_='categories product-category fs-4 p-0 m-0')[1].get_text().strip().replace('Kategori - Brand: PC Ready - ', '')
        img_urls = [i['href'] for i in
                    self.find('div', class_='row row-cols-3 row-cols-sm-3 row-cols-md-4').find_all('a')]
        table = self.find('table', class_='table ps-pcready__table-items').find('tbody')

        components_data = {
            'processor': 'None',
            'motherboard': 'None',
            'ssd': 'None',
            'vga': 'Integrated GPU',
            'ram': 'None',
            'psu': 'None',
            'fan_casing': 'None',
            'cpu_cooler': 'None',
            'network': 'None',
            'casing': 'None',
            'kb_m': 'None',
            'mousepad': 'None',
            'software': 'None'
        }

        for component in table.find_all('td', class_='fw-bold-thin'):
            component_name = component.find('span', class_='text-uppercase fw-bold fs-3').get_text()

            if component_name == 'Processor':
                components_data['processor'] = ' '.join(component.br.next_sibling.strip().split())
            if 'Motherboard' in str(component_name):
                components_data['motherboard'] = ' '.join(component.br.next_sibling.strip().split())
            if component_name == 'SSD':
                components_data['ssd'] = ' '.join(component.br.next_sibling.strip().split())
            if 'RAM' or 'PC - Desktop' in str(component_name):
                components_data['ram'] = ' '.join(component.br.next_sibling.strip().split())
            if component_name in ['radeon', 'nvidia']:
                components_data['vga'] = ' '.join(component.br.next_sibling.strip().split())
            if component_name == 'PSU':
                components_data['psu'] = ' '.join(component.br.next_sibling.strip().split())
            if component_name == 'Fan Casing 12CM Fan Case':
                components_data['fan_casing'] = ' '.join(component.br.next_sibling.strip().split())
            if component_name in ['Air Cooler / Heatsink Cooler', 'Liquid Cooler / Water Cooler']:
                components_data['cpu_cooler'] = ' '.join(component.br.next_sibling.strip().split())
            if component_name == 'Networking':
                components_data['network'] = ' '.join(component.br.next_sibling.strip().split())
            if component_name == 'Casing':
                components_data['casing'] = ' '.join(component.br.next_sibling.strip().split())
            if component_name == 'Keyboard + Mouse':
                components_data['kb_m'] = ' '.join(component.br.next_sibling.strip().split())
            if component_name == 'Mousepad':
                components_data['mousepad'] = ' '.join(component.br.next_sibling.strip().split())
            if component_name == 'Software':
                components_data['software'] = ' '.join(component.br.next_sibling.strip().split())

        # print('title', title)
        # print('normal price', normal_price)
        # print('current price', current_price)
        # print('sku', sku)
        # print('code', code)
        # print('weight', weight)
        # print('category', category)
        # print('brand', brand)
        # print('sub category', sub_category)
        # print('img url', img_urls)
        # print('processor', components_data['processor'])
        # print('mobo', components_data['motherboard'])
        # print('ssd', components_data['ssd'])
        # print('ram', components_data['ram'])
        # print('vga', components_data['vga'])
        # print('psu', components_data['psu'])
        # print('fan casing', components_data['fan_casing'])
        # print('cpu cooler', components_data['cpu_cooler'])
        # print('network', components_data['network'])
        # print('casind', components_data['casing'])
        # print('mouse', components_data['kb_m'])
        # print('mousepad', components_data['mousepad'])
        # print('software', components_data['software'])

        return Items(
            Title=title,
            Normal_price=normal_price,
            Current_price=current_price,
            Sku=sku,
            Code=code,
            Weight=weight,
            Category=category,
            Brand=brand,
            Sub_category=sub_category,
            Img_url=img_urls,
            Processor=components_data['processor'],
            Motherboard=components_data['motherboard'],
            Ssd=components_data['ssd'],
            Ram=components_data['ram'],
            Vga=components_data['vga'],
            Psu=components_data['psu'],
            Fan_casing=components_data['fan_casing'],
            Cpu_cooler=components_data['cpu_cooler'],
            Network=components_data['network'],
            Casing=components_data['casing'],
            Keyboard_mouse=components_data['kb_m'],
            Mousepad=components_data['mousepad'],
            Software=components_data['software']
        )

    def get_urls(self):
        url_list = [url.find('a', class_='ps-btn ps-btn--fullwidth')['href'] for url in self.find_all('div', class_='card-pcready__box my-5')]
        url_list = [str(url) for url in url_list]
        unique_urls = list(set(url_list))
        return unique_urls
        # return [''.join([str(c) for c in lst]) for lst in url]
        # return url
        # print(url)