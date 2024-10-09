from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_Indonesia'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

table = soup.find_all('th', class_='headerSort')
print(table)