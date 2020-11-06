from pymongo import MongoClient

conn = None
try:
    db = {'host': 'localhost', "port": 27017}
    conn = MongoClient(**db)
    print("{} 연결성공!!!".format(conn))
    result = conn['big_data']['sample'].find_one(None, {"_id": False})
    print("~" * 80)
    print(result)
    print(result['name'])
    print(result['price'])
    print(result['year'])
    print("~" * 80)
    result = conn['big_data']['sample'].find_one(None, {"_id": True})
    print(result)
    print(result["_id"])
    print("~" * 80)
    result = conn['big_data']['sample'].find_one({'name': 'K5'}, {"_id": False})
    print(result)
    print("~" * 80)
    result = conn['big_data']['sample'].find_one({'name': 'BMW'}, {"_id": False})
    print(result)
    print("~" * 80)
except Exception as e:
    print(e)
finally:
    if conn is not None:
        conn.close()
