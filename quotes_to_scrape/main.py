from source.soup import Soup  # mengimport class Soup dari modul soup didalam package source

# mengimport modul get_html dan save_to_xsls dari modul util didalam package source
from source.util import get_html, save_to_xsls


"""def get_quotes():
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
    soup = Soup(html)"""


def main():
    output = []  # penyimpanan sementara sebelum dimasukkan ke file xlsx
    max_pages = 10  # maksimal halaman
    for i in range(1, max_pages + 1):  # perulangan setiap halaman
        url = f"https://quotes.toscrape.com/page/{i}/"  # url dari halaman yang akan di scrape
        print(f'scraping url {url}')  # menampilkan url halaman yang sedang di-scrape
        soup = get_html(url)  # mengambil html halaman terkini untuk diproses di method get_html()
        quotes = soup.scrape()  # mengambil data tag dari halaman berdasarkan method scrape()
        output.extend(quotes)  # memasukkan hasil scraping ke list output

    save_to_xsls(output, 'Quotes.xlsx')  # menyimpan hasil scraping ke file xlsx


if __name__ == '__main__':  # Memastikan bahwa fungsi main() hanya dijalankan jika file dieksekusi langsung
    main()  # menjalankan fungsi main
