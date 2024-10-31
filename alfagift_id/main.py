from source.util import get_html, press_button, get_current_url, wait_emergence, save_to_file
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
    print(output)


def get_item_urls():
    product_urls = []
    url = 'https://alfagift.id/c/kebutuhan-dapur-5b85712ca3834cdebbbc4363'
    html = get_html(url)
    soup = Soup(html)
    total_page = soup.check_total_page()
    while True:
        product_urls.append(soup.scrape_product_url())
        if str(soup.scrape_active_page()) in total_page:
            break
        else:
            time.sleep(5)
            press_button('//button[@aria-label="Go to next page" and @class="page-link"]')

    print(product_urls)


def get_category_links():
    url = URL
    html = get_html(url)
    soup = Soup(html)
    link = soup.scrape_category_url()
    print(link)


def final_page():
    url = 'https://alfagift.id/c/kebutuhan-dapur-5b85712ca3834cdebbbc4363'
    html = get_html(url)
    soup = Soup(html)
    page = soup.check_total_page()
    print(page)


def get_all_page():
    url = "https://alfagift.id/c/kebutuhan-ibu--anak-5b85712ca3834cdebbbc4367"
    html = get_html(url)
    soup = Soup(html)
    total_page = soup.scrape_total_page()
    print(total_page)


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
    category_urls = soup.scrape_category_url()
    result = []

    for category_url in category_urls[:3]:
        print(f'Opening category: {category_url}')
        html = get_html(category_url)
        product_page = Soup(html)

        while True:
            product_urls = product_page.scrape_product_url()
            while True:

                for product_url in product_urls[:3]:
                    print(f'Scraping product: {product_url}')
                    html = get_html(product_url)
                    time.sleep(2)
                    soup = Soup(html)

                    product = soup.scrape_product()
                    result.append(product)

                total_pages = product_page.check_total_page()
                current_page = product_page.scrape_active_page()

                if current_page == total_pages:
                    print(f'Reached the last page of category {category_url}')
                    break
                else:
                    page = soup.previous_page()
                    html = get_html(page)
                    press_button('//button[@role="menuitem" and @aria-label="Go to next page" and @class="page-link"]')
                    time.sleep(3)
                    product_page = Soup(html)
                    product_urls = product_page.scrape_product_url()

    save_to_file(result, 'Trial')


if __name__ == '__main__':
    main()
