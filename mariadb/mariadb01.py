import pymysql

# MySQL 연동
conn = None
try:
    conn = pymysql.connect(host = 'localhost', user='jspuser', password='123456', db='mydb', charset='utf8')
    print("연결 성공 : {}".format(conn))
except Exception as e:
    print(e)
finally:
    if conn is not None:
        conn.close()
