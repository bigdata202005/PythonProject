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
    sql = """
      insert into pydb_test (name,age,gender) values ('한사람',33,1),
      ('두사람',23,0),('세사람',43,1),('네사람',53,0),('오사람',63,1),
      ('육사람',35,0),('칠사람',36,1),('팔사람',37,0)
    """
    curs.execute(sql)
    conn.commit()
    print("데이터 저장 완료!!!")
except Exception as e:
    print(e)
finally:
    if conn is not None:
        conn.close()
