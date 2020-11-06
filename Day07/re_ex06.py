import re
# | : 또는
p = re.compile('Crow|Servo')
m = p.match('CrowHello')
m1 = p.match('HelloServoCrow')
print(m)
print(m1)
print()

m = p.search('CrowHello')
m1 = p.search('HelloServoCrow')
print(m.group())
print(m1.group())
print()

m = p.findall('CrowHello')
m1 = p.findall('HelloServoCrow')
print(m)
print(m1)
print()
print("~" * 80)

# ^ : 시작
print(re.search('^Life', 'Life is too short'))
print(re.search('^Life', 'My Life'))
print("~" * 80)

# $ : 종료
print(re.search('com$', 'www.naver.com'))
print(re.search('kr$', 'www.naver.co.kr'))
print("~" * 80)


# 회사 사번 = com_number
com_number = ['20170203 1', '20180101 23', '20190217 1', '20190217 2', '20190217 3']
for result in com_number:
    result_2018 = re.search('^2018', result)
    result_2019 = re.search('^2019', result)
    if bool(result_2019) == True:
        print('2019년 입사자')
    elif bool(result_2018):
        print('2018년 입사자')
    else:
        print('2017년 입사자')
print("~" * 80)

# ftp 로 시작하는 웹 사이트 주소
web_site = ['www.naver.com', 'www.lycos.co.kr', 'http://www.daum.net', 'ftp://10.184.70.11:8080', 'ftp://10.2.2.3:8080']
for result in web_site:
    ftp_bool = re.search('^ftp', result)
    www_bool = re.search('^www', result)
    com_bool = re.search('com$', result)
    if bool(ftp_bool) == True:
        print('파일 전송 프로토콜')
    elif bool(www_bool) == True :
        print('web site')
    else:
        print('com으로 끝나는 site ')
print("~" * 80)

# 문자열 입력시 접두어 r
addr = "c:\data\type\node"  # \t를 탭으로 인식 \n은 줄바꿈
print(addr)
addr = "c:\\data\\type\\node"
print(addr)
addr = r"c:\data\type\node"  # \를 문자 \로 인식
print(addr)
print("~" * 80)

p = re.compile(r'\bclass\b')  # \b는 단어
print(p.search('no class at all'))

p = re.compile(r'\Bdong\B') # \B는 단어가 아닌것
print(p.search('shindongwook'))

p = re.compile(r'\BNorth Korea\B')
print(p.search('Noth Korea 북미회담을 개최하였다.'))

