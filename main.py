import requests as r
from bs4 import BeautifulSoup as bs
HOME_URL = 'https://prenadamedia.com/kategori/'

html = r.get(HOME_URL).content
soup = bs(html,'html.parser')
categories = soup.find_all('li', class_='product-category product first')
for category in categories:
    category_url = category.find('a')['href']
    category_text = category.find('a').text.strip().title().split('(')[0]
    print(category_url,category_text)
    category_url_page = category_url+'page/'
    category_html = r.get(category_url).content
    category_soup = bs(category_html,'html.parser')
    page_num_soup = category_soup.find_all('a', class_='page-numbers')
    try:
        last_page = page_num_soup[-2].text
    except:
        last_page = 0
