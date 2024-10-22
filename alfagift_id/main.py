from source.util import get_html, press_button
from source.soup import Soup
import time
from source.__init__ import URL


def get_item():
    url = 'https://alfagift.id/p/filma-minyak-goreng-pouch-2-l-15798'
    html = get_html(url)
    soup = Soup(html)
    output = []
    time.sleep(3)
    soup.scrape_item()


def get_item_urls():
    url = 'https://alfagift.id/c/kebutuhan-dapur-5b85712ca3834cdebbbc4363'
    html = get_html(url)
    soup = Soup(html)
    urls = soup.scrape_url()


def get_category_links():
    url = URL
    html = get_html(url)
    soup = Soup(html)
    link = soup.scrape_links()


def main():
    url = URL
    html = get_html(url)
    soup = Soup(html)
    category_urls = soup.scrape_links()
    result = []
    for url in category_urls:
        html = get_html(url)
        soup = Soup(html)
        product_urls = soup.scrape_url()
        for link in product_urls:
            html = get_html(link)
            soup = Soup(html)
            for item in soup:
                product = soup.scrape_item()
                press_button('button[aria-label="Go to next page"]')
                result.append(product)



if __name__ == '__main__':
    main()