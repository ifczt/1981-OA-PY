import json
from urllib import request

url = 'http://api.k780.com/?app=finance.rate&scur=USD&tcur=CNY&appkey=10003&sign=b59bc3ef6191eb9f747dd4e83c99f2a4'
r= request.urlopen(url)
print(json.loads(r.read())['result']['rate'])