import pymysql

# MySQL 연동
conn = None
try:
    db = {'host': 'localhost',
          'port': 3306,
          'user': 'jspuser',
          'password': '123456',
          'database': 'mydb',
          'charset': 'utf8'
          }
    conn = pymysql.connect(**db)
    curs = conn.cursor()
    sql = "select * from pydb_test"
    curs.execute(sql)
    rows = curs.fetchall()
    print(len(rows), "개가 있습니다.")
    for row in rows:
        # print(row)
        print("{:02d}. {}({}세,{})".format(row[0], row[1], row[2], "남자" if row[3] else "여자"))
    print("데이터 읽기 완료!!!")
except Exception as e:
    print(e)
finally:
    if conn is not None:
        conn.close()
