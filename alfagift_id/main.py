from source.util import get_html, press_button, save_to_file
from source.soup import Soup
import time
from source.__init__ import URL


def get_item():
    url = 'https://alfagift.id/p/disney-lotso-tempat-minum--811091'
    html = get_html(url)
    soup = Soup(html)
    output = []
    time.sleep(3)
    soup.scrape_product()


def get_item_urls():
    url = 'https://alfagift.id/c/kebutuhan-dapur-5b85712ca3834cdebbbc4363'
    html = get_html(url)
    soup = Soup(html)
    urls = soup.scrape_product_url()


def get_category_links():
    url = URL
    html = get_html(url)
    soup = Soup(html)
    link = soup.scrape_category_url()
    print(link)


def get_page_number():
    url = 'https://alfagift.id/c/kebutuhan-dapur-5b85712ca3834cdebbbc4363'
    html = get_html(url)
    soup = Soup(html)
    page = soup.scrape_active_page()


def get_all_page():
    url = "https://alfagift.id/c/kebutuhan-ibu--anak-5b85712ca3834cdebbbc4367"
    html = get_html(url)
    soup = Soup(html)
    total_page = soup.scrape_total_page()


def previous_page():
    url = 'https://alfagift.id/p/disney-lotso-tempat-minum--811091'
    html = get_html(url)
    soup = Soup(html)
    page = soup.previous_page()
    print(page)


def active_page():
    url = "https://alfagift.id/c/kebutuhan-ibu--anak-5b85712ca3834cdebbbc4367"
    html = get_html(url)
    soup = Soup(html)
    active = soup.scrape_active_page()
    print(active)


def main():
    url = URL
    html = get_html(url)
    soup = Soup(html)
    category_urls = soup.scrape_category_url()  # scrape urls of category in main page
    result = []
    all_url_product = []
    for category_url in category_urls[:3]:
        print(f'Category = {category_url}')
        html = get_html(category_url)
        soup = Soup(html)
        product_urls = soup.scrape_product_url()
        all_url_product.append(product_urls)
        if product_urls not in all_url_product:
            press_button('button[aria-label="Go to next page"]')
        for product_url in product_urls[:3]:
            html = get_html(product_url)
            soup = Soup(html)
            product = soup.scrape_product()
            result.append(product)
    save_to_file(result, 'Trial')


if __name__ == '__main__':
    main()
