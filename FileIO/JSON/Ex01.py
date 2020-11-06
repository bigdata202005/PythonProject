from urllib.request import Request, urlopen
from urllib.parse import urlencode
import copy


URL = "http://astro.kasi.re.kr/life/pageView/5"

DATA = {"sol_year": None, "sol_month": None}

headers = {"Content-Type": "application/x-www-form-urlencoded","Accept":"text/html"}

data = copy.copy(DATA)
data["sol_year"] = 2020
data["sol_month"] = 9

req = Request(URL, method="POST", data=urlencode(data).encode('utf-8'))
res = urlopen(req)
a = res.read().decode('utf-8')
print(a)