import pymysql
import json


def get_connection():
    db_config = None
    connection = None
    try:
        with open('db.config') as json_file:
            db_config = json.load(json_file)
        connection = pymysql.connect(**db_config)
        if connection is None:
            db_config = {"host": "localhost", "port": 3306,
                         "user": "jspuser", "password": "123456",
                         "database": "mydb", "charset": "utf8"}
            connection = pymysql.connect(**db_config)
        # print("연결 성공 : {}".format(connection))
    except Exception as e:
        print("에러 :", e)
    return connection


if __name__ == '__main__':
    get_connection()
