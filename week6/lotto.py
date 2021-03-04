import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.dhlottery.co.kr/gameResult.do?method=byWin')
soup = BeautifulSoup(res.text,'html.parser')

soup2 = soup.find('div', class_ = 'num win')
soup3 = soup2.find_all('span')

numberList = []

for i in soup3:
    print(type(i))
    numberList.append(i.text)

print(numberList)


bonus = soup.find('div', class_ = 'num bonus')
bonus2 = bonus.find('span')
numberList.append(bonus2)
print(bonus2.text)
numberList.append(bonus2.text)
print(numberList)
