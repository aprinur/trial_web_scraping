from dataclasses import dataclass  # Mengimpor decorator dataclass dari modul dataclasses


@dataclass
class Quotes:  # Membuat class Quotes untuk menyimpan data quote dan author
    quote: str  # Atribut untuk menyimpan teks quote
    author: str  # Atribut untuk menyimpan nama penulis (author)
