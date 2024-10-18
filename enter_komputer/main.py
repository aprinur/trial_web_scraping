from src.util import get_html, save_to_file
from src.soup import Soup
import time


def get_item():
    url = 'https://www.enterkomputer.com/pc-ready/detail/191361/EK-Gaming-BattleStar-306-12G-AYW'
    html = get_html(url)
    soup = Soup(html)
    results = []
    result = soup.scrape()
    results.append(result)
    save_to_file(results, 'Trial')


def get_url():
    url = 'https://www.enterkomputer.com/pc-ready'
    html = get_html(url)
    soup = Soup(html)
    result = []
    same_url = []
    urls = soup.get_urls()
    for i in urls:
        if i not in result:
            result.append(i)
        else:
            same_url.append(i)
    print('result', len(result))
    print('same url', len(same_url))


def main():
    url = 'https://www.enterkomputer.com/pc-ready'
    html = get_html(url)
    soup = Soup(html)
    urls = soup.get_urls()
    output = []
    for url in urls:
        print(url)
        html = get_html(url)
        soup = Soup(html)
        items = soup.scrape()
        output.append(items)

    save_to_file(output, 'Pc_ready_91_page')


if __name__ == '__main__':
    main()