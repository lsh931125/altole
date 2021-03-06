# API 요청
# API는 http 가지고 구현이 되어있음
# 가상화폐 가격정보 가지고 오고싶은 상태
# 빗썸에서는 가상화폐 가격정보를 제공하는 API가 있다.

import requests
import json

res = requests.get('https://api.bithumb.com/public/ticker/ALL_KRW')
convert_dic = json.loads(res.text)

print(convert_dic['data']['BTC']['opening_price'])


