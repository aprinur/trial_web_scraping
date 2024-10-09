from bs4 import BeautifulSoup  # mengimport BeautifulSoup dari library bs4
from .display import Quotes  # mengimport class Quotes dari modul display


class Soup(BeautifulSoup):  # membuat class Soup yang merupakan inheritance dari BeautifulSoup
    def __init__(self, html):  # Inisialisasi class soup
        # memanggil inisialisasi superclass BeautifulSoup dengan parser HTML
        super().__init__(html, 'html.parser')

    def scrape(self):  # method untuk scraping data quote dan author dari halaman
        quotes = self.find_all('div', class_='quote')  # mengambil semua elemen div dengan class 'quote'
        output = []  # list untuk menyimpan hasil scraping
        for quote_tag in quotes:  # perulangan untuk setiap elemen quote
            # mengambil teks dari elemen span dengan class 'text'
            quote = quote_tag.find('span', class_='text').get_text()
            # mengambil teks dari elemen small dengan class 'author' dan itemprop 'author'
            author = quote_tag.find('small', class_='author', itemprop='author').get_text()
            output.append({'quote': quote, 'author': author})  # menyimpan hasil scraping ke list output
        return output  # mengembalikan list output yang berisi data quote dan author

    @staticmethod
    def url_list(url, rep):  # # Metode statis untuk membuat daftar URL berdasarkan pola halaman
        all_url = []  # List untuk menyimpan URL
        for i in range(1, rep + 1):  # Perulangan dari halaman 1 hingga rep
            page_url = url.format(i=i)  # Mengganti nilai {i} pada string URL dengan nomor halaman
            all_url.append(page_url)  # Menambahkan URL halaman ke list
        return all_url  # Mengembalikan daftar URL
