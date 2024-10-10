from bs4 import BeautifulSoup
import requests
import pandas
import datetime

# getting url requests
url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_Indonesia'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

# selecting the first table
table = soup.find_all('table', class_='wikitable sortable')[0]

# getting table head
table_head = [head.text.strip() for head in table.find_all('th')]
df = pandas.DataFrame(columns=table_head)

# getting table content
rows = table.find_all('tr')
for row in rows[1:]:
    row_data = row.find_all('td')
    item = [cell.text.strip() for cell in row_data]
    # print(item)
    length = len(df)
    df.loc[length + 1] = item

print(df)

today = datetime.datetime.now().strftime('%d-%B-%Y')
df.to_excel(f'List_of_largest_companies_in_Indonesia_{today}.xlsx', index=False)