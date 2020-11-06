import pymysql

# MySQL 연동
conn = None
try:
    db = {'host': 'localhost',
          'port':3306,
          'user': 'jspuser',
          'password': '123456',
          'database': 'mydb',
          'charset': 'utf8'
          }
    conn = pymysql.connect(**db)
    curs = conn.cursor()
    sql = "select now()"
    curs.execute(sql)
    data = curs.fetchall()
    print(data)
    print("DB 시간 :", data[0][0], type(data[0][0]))

except Exception as e:
    print(e)
finally:
    if conn is not None:
        conn.close()
