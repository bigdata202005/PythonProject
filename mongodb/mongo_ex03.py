from pymongo import MongoClient

conn = None
try:
    db = {'host': 'localhost', "port": 27017}
    conn = MongoClient(**db)
    print("{} 연결성공!!!".format(conn))
    data = {"name": "K5", "price": "5000", "year": "2015"}
    # 1개 저장
    result = conn['big_data']['sample'].insert_one(data).inserted_id
    print(result)
    # 여러개 저장
    data = [
        {"name": "Avante", "price": "3000", "year": "2014"},
        {"name": "Morning", "price": "1500", "year": "2020"}
    ]
    result = conn['big_data']['sample'].insert_many(data).inserted_ids
    print(result)
except Exception as e:
    print(e)
finally:
    if conn is not None:
        conn.close()
