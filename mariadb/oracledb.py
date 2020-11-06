import cx_Oracle

# 한글 지원 방법
import os

os.putenv('NLS_LANG', '.UTF8')

# 연결에 필요한 기본 정보 (유저, 비밀번호, 데이터베이스 서버 주소)
connection = cx_Oracle.connect('jspuser', '123456', 'localhost/xe')

cursor = connection.cursor()

cursor.execute("select SYSDATE, 1*2*3, 1+2+3+4+5 from dual")
for name in cursor:
    print(name)
    print(name[0])
    print(name[1])
    print(name[2])

