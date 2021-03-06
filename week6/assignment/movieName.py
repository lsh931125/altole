import requests
from bs4 import BeautifulSoup

res = requests.get('https://movie.naver.com/movie/running/current.nhn#')
movieSite = BeautifulSoup(res.text,'html.parser')
# print(movieSite)
movieList = movieSite.find('ul', class_ = "lst_detail_t1")
# print(type(movieList))
# print(movieList)

#
#
# movie = movieList.find('')
movie = []
for i in movieList.find_all('dt',class_ = 'tit'):
    movie.append(i.a.text)
    # print(i.a.text)
    # for f in i.find_all('a'):
    #     print(f.text)
    #     movie.append(f.text)
print(movie)