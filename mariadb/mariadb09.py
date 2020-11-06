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
    sql = "update pydb_test set age = " + str(random.randint(1,100)) \
          + " where age>=" + str(random.randint(1,100))
    count = curs.execute(sql)
    conn.commit()
    print(str(count) + "개 수정완료!!!")
except Exception as e:
    print(e)
finally:
    if conn is not None:
        conn.close()
