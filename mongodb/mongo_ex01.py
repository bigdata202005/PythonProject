from pymongo import MongoClient
conn = None
try:
    host = "localhost"
    port = "27017"
    conn = MongoClient(host, int(port))
    print("{} 연결성공!!!".format(conn))
except Exception as e:
    print(e)
finally:
    if conn is not None:
        conn.close()
