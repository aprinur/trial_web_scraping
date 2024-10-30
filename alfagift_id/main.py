from source.util import get_html, press_button, get_current_url, wait_emergence
from source.soup import Soup
import time
from source.__init__ import URL
import pandas
import datetime


def save_to_file(product, filename):
    date = datetime.datetime.now().strftime('%d_%B_%Y')
    df = pandas.DataFrame(product)
    df.to_excel(f'{filename}_{date}.xlsx', index=False)
    df.to_csv(fr'D:\Github\aprinur\Web_Scraping\alfagift_id\{filename}_{date}.csv', index=False)


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
    while True:
        product_urls.append(soup.scrape_product_url())
        press_button('//button[@aria-label="Go to next page" and @class="page-link"]')
        if soup.check_final_page():
            break
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
    # 1. Open main URL
    url = URL
    html = get_html(url)
    soup = Soup(html)

    # 2. Scrape category URLs from the main page
    category_urls = soup.scrape_category_url()
    result = []

    # 3. Loop through each category URL
    for category_url in category_urls:
        print(f'Opening category: {category_url}')
        html = get_html(category_url)
        product_page = Soup(html)

        # 4. Start scraping product URLs from the category page
        while True:
            # 5. Scrape product URLs on the current page
            product_urls = product_page.scrape_product_url()

            for product_url in product_urls[:3]:
                print(f'Scraping product: {product_url}')
                html = get_html(product_url)
                time.sleep(2)
                soup = Soup(html)

                # 6. Scrape product information and store in result
                product = soup.scrape_product()
                result.append(product)

            # 7. Check if we are on the last page of the product page
            total_pages = product_page.check_total_page()
            current_page = product_page.scrape_active_page()

            if current_page == total_pages:
                print(f'Reached the last page of category {category_url}')
                break
            else:
                # 8. Move to the next page in the category if it's not the last page
                soup.previous_page()
                # wait_emergence('d-flex justify-content-center mt-4 mb-5')
                press_button('/html/body/div[1]/div/div/div[2]/div[1]/div/div[2]/div[2]/div[3]/div/ul/li[9]/button')
                time.sleep(3)  # Wait to load the next page
                html = get_html(get_current_url())
                product_page = Soup(html)  # Refresh Soup object with new page content

    # 9. Save scraped data to file after all categories are processed
    save_to_file(result, 'Trial')


if __name__ == '__main__':
    main()
