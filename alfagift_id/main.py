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
    urls = soup.scrape_url()


def get_category_links():
    url = URL
    html = get_html(url)
    soup = Soup(html)
    link = soup.scrape_links()


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


def main():
    url = URL
    html = get_html(url)
    soup = Soup(html)
    category_urls = soup.scrape_links()
    result = []

    for category_url in category_urls[:3]:
        print(f'Scraping category: {category_url}')
        html = get_html(url)
        c_page = Soup(html)
        product_urls = c_page.scrape_url()
        page_num = []
        if c_page.scrape_active_page() not in page_num:
            page_num.append(c_page.scrape_active_page())
            for link in product_urls[:3]:
                html = get_html(link)
                soup = Soup(html)
                result.append(soup.scrape_product())
                if len(page_num) == 3:
                    page_num.clear()
        else:
            press_button("li[class='/breadcrumb-item']")
            press_button(".page-link[aria-label='Go to next page']")

    save_to_file(result, 'Trial')
    # save_to_file(result, 'All_product_from_alfagift_id')


if __name__ == '__main__':
    main()


