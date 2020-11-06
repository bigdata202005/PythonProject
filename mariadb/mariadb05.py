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
    create table if not exists pydb_test(
      idx int primary key auto_increment,
      name varchar(200) not null,
      age int default 0,   
      gender int default 0
      )   
    """
    curs.execute(sql)
    conn.commit()
    print("테이블 작성완료!!!")

    curs.execute("show tables")
    data = curs.fetchall()
    print(data)

    for row in data:
        print(row[0])


except Exception as e:
    print(e)
finally:
    if conn is not None:
        conn.close()
