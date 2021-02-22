# writedata.py
f = open('C:\Windows\System32\drivers\etc\hosts', 'a',encoding='utf-8')
a = ('192.168.0.1    www.naver.com')
f.write(a)
f.close()