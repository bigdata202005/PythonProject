from flask import Flask, render_template
import pymysql

app = Flask(__name__)


@app.route('/')
def hello_world():
    rows = select_all()
    return render_template('db_test.html', title="데이터베이스 연동", data=rows)


@app.route('/dict')
def hello_world2():
    rows = select_all()
    data_list = []
    for row in rows:
        person = dict()
        person['idx'] = row[0]
        person['name'] = row[1]
        person['age'] = row[2]
        person['gender'] = '남자' if row[3]==1 else '여자'
        data_list.append(person)
    # print(data_list)
    return render_template('db_test2.html', title="데이터베이스 연동", data=data_list)


# DB에서 데이터 받기
def select_all():
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
        print(type(rows), rows)
        return rows
    except Exception as e:
        print(e)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    app.run()  # 서버 실행
