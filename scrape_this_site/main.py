from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime

# Get requests
web_url = 'https://www.scrapethissite.com/pages/forms/?page_num=1&per_page=100'
page = requests.get(web_url)
soup = BeautifulSoup(page.text, 'html.parser')

# getting table name
table = soup.find_all('th', class_=False)
table_title = [title.text.strip() for title in table]
df = pd.DataFrame(columns=table_title)

# getting item in table in page 1 to 4 (5-1)
for i in range(1, 7):
    web_url = f'https://www.scrapethissite.com/pages/forms/?page_num={i}&per_page=100'
    print(f"scraping {web_url}")
    page = requests.get(web_url)
    soup = BeautifulSoup(page.text, 'html.parser')
    datas = soup.find_all('tr')
    for data in datas[1:]:
        row_data = data.find_all('td')
        row = [item.get_text().strip() for item in row_data]
        length = len(df)
        df.loc[length + 1] = row

# saving to external file
today = datetime.datetime.now().strftime('%d-%B-%Y')
df.to_excel(f'Hockey_{today}.xlsx')
df.to_csv(rf'D:\Github\aprinur\Web_Scraping\scrape_this_site\Hockey_{today}.csv')



