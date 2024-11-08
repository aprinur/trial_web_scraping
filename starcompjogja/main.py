from source_code.util import get_html
from source_code.soup import Soup


def get_product_info():
    url = 'https://starcompjogja.com/product/intel-core-i7-13700f'
    html = get_html(url)
    soup = Soup(html)
    soup.scrape_product_info()


if __name__ == "__main__":
    get_product_info()