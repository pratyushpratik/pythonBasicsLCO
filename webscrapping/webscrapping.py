import requests
import bs4

res = requests.get('https://www.wizcounsel.com')

print(type(res))
print(res.text)

soup = bs4.BeautifulSoup(res.text, 'lxml') #takes two parameters, 1st res.text and 2nd type of file
print(type(soup))

hi = soup.select('title')
print("hi", hi)

resMachineLearningWiki = requests.get('https://en.wikipedia.org/wiki/Machine_learning')

print(resMachineLearningWiki.text)

soupMachineLearningWiki = bs4.BeautifulSoup(resMachineLearningWiki.text, 'lxml')
print(type(soupMachineLearningWiki))

print('headline', soupMachineLearningWiki.select('.mw-headline'))

for i in soupMachineLearningWiki.select('.mw-headline'):
    print(i.text)
