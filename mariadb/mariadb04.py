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
    sql = "select 1+2+3, 1*2*3, 12.3*3.14"
    curs.execute(sql)
    data = curs.fetchall()
    print(data)
    print("1+2+3 :", data[0][0], type(data[0][0]))
    print("1*2*3 :", data[0][1], type(data[0][1]))
    print("12.3*3.14 :", data[0][2], type(data[0][2]))

except Exception as e:
    print(e)
finally:
    if conn is not None:
        conn.close()
