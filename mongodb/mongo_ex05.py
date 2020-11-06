from pymongo import MongoClient

conn = None
try:
    db = {'host': 'localhost', "port": 27017}
    conn = MongoClient(**db)
    print("{} 연결성공!!!".format(conn))
    result = conn['big_data']['sample'].find(None, {"_id": False})
    print("~" * 80)
    print(result)
    print("~" * 80)
    for data in result:
        print(data)
    print("=" * 80)

    result = conn['big_data']['sample'].find({"name":"Avante"}, {"_id": False})
    print("~" * 80)
    print(result)
    print("~" * 80)
    for data in result:
        print(data)
    print("=" * 80)

    result = conn['big_data']['sample'].find({"name":"BMW"}, {"_id": False})
    print("~" * 80)
    print(result)
    print("~" * 80)
    for data in result:
        print(data)

except Exception as e:
    print(e)
finally:
    if conn is not None:
        conn.close()
