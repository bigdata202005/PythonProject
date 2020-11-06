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
    data = [['하하하',23,1],['호호호',18,0],['크크크',44,1]]
    sql = "insert into pydb_test (name,age,gender) values (%s,%s,%s)"
    count = curs.executemany(sql, data)
    conn.commit()
    print(count, "저장완료!!!")
    sql = "select count(*) from pydb_test"
    curs.execute(sql)
    print("{}개의 데이터가 있습니다.".format(curs.fetchall()[0][0]))
    data = (('하하하1',23,1),('호호호2',18,0))
    sql = "insert into pydb_test (name,age,gender) values (%s,%s,%s)"
    count = curs.executemany(sql, data)
    conn.commit()
    print(count, "저장완료!!!")
    sql = "select count(*) from pydb_test"
    curs.execute(sql)
    print("{}개의 데이터가 있습니다.".format(curs.fetchall()[0][0]))

    data = (('하하하2',23,'하하하1'),('호호호2',18,'호호호1'))
    sql = "update pydb_test set name=%s, age=%s where name=%s"
    count = curs.executemany(sql, data)
    conn.commit()
    print(count, "수정완료!!!")
    sql = "select count(*) from pydb_test"
    curs.execute(sql)
    print("{}개의 데이터가 있습니다.".format(curs.fetchall()[0][0]))
    sql = "select * from pydb_test"
    curs.execute(sql)
    print('~' * 80)
    print("모두보기")
    print('~' * 80)
    for row in curs.fetchall():
        print(row)
    print('~' * 80)
except Exception as e:
    print(e)
finally:
    if conn is not None:
        conn.close()
