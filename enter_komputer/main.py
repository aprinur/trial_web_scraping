from src.util import get_html, save_into_xlsx
from src.soup import Soup


def get_item():
    url = 'https://www.enterkomputer.com/pc-ready/detail/185916/EK-Office-Fizzword-Red-X'
    html = get_html(url)
    soup = Soup(html)
    soup.scrape()


def get_url():
    url = 'https://www.enterkomputer.com/pc-ready'
    html = get_html(url)
    soup = Soup(html)
    soup.get_urls()


def main():
    url = 'https://www.enterkomputer.com/pc-ready'
    html = get_html(url)
    soup = Soup(html)
    urls = soup.get_urls()
    output = []
    for url in urls[1:6]:
        html = get_html(url)
        soup = Soup(html)
        items = soup.scrape()
        output.append(items)
    save_into_xlsx(output, 'Pc_ready')


if __name__ == '__main__':
    main()