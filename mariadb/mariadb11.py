import pymysql
import random

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
    data = ('한사람', random.randint(1, 100), random.randint(0, 1))
    sql = "insert into pydb_test (name,age,gender) values (%s,%s,%s)"
    count = curs.execute(sql, data)
    conn.commit()
    print("저장완료!!!")
    sql = "select count(*) from pydb_test"
    curs.execute(sql)
    print("{}개의 데이터가 있습니다.".format(curs.fetchall()[0][0]))
    sql = "select * from pydb_test where age < %s"
    curs.execute(sql, [50])
    for row in curs.fetchall():
        print(row)
except Exception as e:
    print(e)
finally:
    if conn is not None:
        conn.close()
