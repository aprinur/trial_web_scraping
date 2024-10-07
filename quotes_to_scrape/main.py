from source.soup import Soup
from source.util import get_html, save_to_xsls


def get_quotes():
    url = 'https://quotes.toscrape.com/page/1/'
    html = get_html(url)
    soup = Soup(html)
    quotes = soup.scrape()
    print(quotes)


def access_page():
    url = 'https://quotes.toscrape.com/page/1/'
    html = get_html(url)
    soup = Soup(html)


def main():
    output = []
    max_pages = 10
    for i in range(1, max_pages + 1):
        url = f"https://quotes.toscrape.com/page/{i}/"
        print(f'scraping url {url}')
        soup = get_html(url)
        output.append(soup.scrape())

    save_to_xsls(output, 'Quotes.xlsx')


if __name__ == '__main__':
    main()