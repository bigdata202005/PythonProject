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
    sql = "delete from pydb_test where age>=50"
    count = curs.execute(sql)
    print("{}개 삭제완료!!!".format(count))
    sql = "select * from pydb_test"
    curs.execute(sql)
    rows = curs.fetchall()
    print(len(rows), "개가 있습니다.")

    sql = "delete from pydb_test"
    count = curs.execute(sql)
    print("{}개 삭제완료!!!".format(count))
    sql = "select * from pydb_test"
    curs.execute(sql)
    rows = curs.fetchall()
    print(len(rows), "개가 있습니다.")
    conn.commit()
except Exception as e:
    print(e)
finally:
    if conn is not None:
        conn.close()
