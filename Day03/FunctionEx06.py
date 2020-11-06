# 딕셔너리를 인수로 받을 수 있을까?
def makeURL(url, **kwargs):
    urlAddr = url + "?"   # "http://localhost:8080/list?"
    for key, value in kwargs.items():
        urlAddr += key + "=" + str(value) + "&"
    urlAddr = urlAddr.rstrip("&")
    return urlAddr


dict1 = {'p': '1', 's': '10', 'b': '5'}
print(makeURL("http://localhost:8080/list?", **dict1))
print(makeURL("http://localhost:8080/list?", name='kimc',age=33,gender=True))
