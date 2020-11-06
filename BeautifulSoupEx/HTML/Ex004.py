import urllib.request
from bs4 import BeautifulSoup

if __name__ == "__main__":
    url = "https://astro.kasi.re.kr/life/pageView/5"
    year = input("년도")
    query = "?sol_year="+year
    month = input("월")
    query += "&sol_month="+month

    req = urllib.request.Request(url  + query);
    data = urllib.request.urlopen(req).read()
    bs = BeautifulSoup(data, 'html.parser')
    print(bs.prettify())
