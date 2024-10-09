from source.soup import Soup
from source.util import get_html, save_to_xsls


def get_quotes():
    output = []
    max_page = 10
    for i in range(1, max_page + 1):
        url = f'https://quotes.toscrape.com/page/{i}/'
        soup = get_html(url)
        quotes = soup.scrape()
        output.append(quotes)
    save_to_xsls(output, 'Scraping_quotes.xlsx')


def access_page():
    url = 'https://quotes.toscrape.com/page/1/'
    html = get_html(url)
    soup = Soup(html)


def main():
    output = []  # penyimpanan sementara sebelum dimasukkan ke file xlsx
    max_pages = 10
    for i in range(1, max_pages + 1):
        url = f"https://quotes.toscrape.com/page/{i}/"  # url yang akan di scrape
        print(f'scraping url {url}')
        soup = get_html(url)
        quotes = soup.scrape()
        output.extend(quotes)

    save_to_xsls(output, 'Quotes.xlsx')  # memasukkan ke file xlsx


if __name__ == '__main__':
    main()
