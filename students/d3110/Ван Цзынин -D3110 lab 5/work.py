import requests
from bs4 import BeautifulSoup
url = 'https://movie.douban.com/subject/1300374/'
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36' }
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
data = soup.find('div', id='info').find_all('span', class_='pl')
data_dict = {}
for item in data:
    key = item.get_text().replace(':', '')
    value = item.next_sibling.next_sibling.get_text()
    data_dict[key] = value
f = open('greenmile.txt', 'w', encoding='utf-8')
f.write(str(data_dict))
f.close()