from source.util import get_html, press_button, get_current_url, save_to_file
from source.soup import Soup
import time
from source.__init__ import URL


def get_item():
    url = 'https://alfagift.id/p/alfamart-sabun-cuci-piring-lime-650-ml-56255'
    html = get_html(url)
    soup = Soup(html)
    time.sleep(3)
    result = soup.scrape_product()
    print(result)


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
    # Open main URL
    url = URL
    html = get_html(url)
    soup = Soup(html)
    category_urls = soup.scrape_category_url()   # Scrape category urls from main page
    result = []

    # list to contain product url
    product_urls = []
    while True:
        # Loop through each category URL
        for category_url in category_urls[:3]:
            print(f'Opening category: {category_url}')
            html = get_html(category_url)
            product_page = Soup(html)
            product_urls.append(product_page.scrape_product_url())
            while True:
                press_button('//button[@role="menuitem" and @aria-label="Go to next page" and @class="page-link"]')
                time.sleep(5)
                product_page = Soup(get_current_url())
                product_urls.append(product_page.scrape_product_url())
                print(product_urls)
                # if product_page.final_page():
                #     break
                if product_page.scrape_active_page() == '2':
                    break
        # loop url in product_urls
        product_urls = [element for innerlist in product_urls for element in innerlist]
        for product_url in product_urls:
            print(product_url)
            html = get_html(product_url)
            soup = Soup(html)
            time.sleep(5)
            result.append(soup.scrape_product())

        save_to_file(result, 'Product_from_first_3_category_and_first_2_page')
        break


if __name__ == '__main__':
    main()



