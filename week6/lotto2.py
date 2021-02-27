import requests
from bs4 import BeautifulSoup

for no in range(1,11):
    params = {
        'drwNo' : no,
        'drwNoList' : no
    }
    res = requests.post('https://www.dhlottery.co.kr/gameResult.do?method=byWin',params)
    soup = BeautifulSoup(res.text,'html.parser')

    soup2 = soup.find('div', class_ = 'num win')
    soup3 = soup2.find_all('span')
    numberList = []

    for i in soup3:
        numberList.append(i.text)


    bonus = soup.find('div', class_ = 'num bonus')
    bonus2 = bonus.find('span')
    numberList.append(bonus2.text)
    print(numberList)