from src.util import get_html
from src.soup import Soup


def get_item():
    url = 'https://www.enterkomputer.com/pc-ready/detail/185916/EK-Office-Fizzword-Red-X'
    html = get_html(url)
    soup = Soup(html)
    soup.scrape()


if __name__ == '__main__':
    get_item()