import pymysql

# MySQL 연동
conn = None
try:
    db = {'host': 'localhost',
          'port':3306,
          'user': 'jspuser',
          'password': '123456',
          # 'db': 'mydb',
          'database': 'mydb',
          'charset': 'utf8'
          }
    conn = pymysql.connect(**db)
    print("연결 성공 : {}".format(conn))

except Exception as e:
    print(e)
finally:
    if conn is not None:
        conn.close()
