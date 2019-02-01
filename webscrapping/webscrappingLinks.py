import requests
import bs4


res = requests.get('https://www.wizcounsel.com')
print(res.text)

soup = bs4.BeautifulSoup(res.text, 'lxml')

for link in soup.findAll('a', href=True):
    print(link['href'])
