from pymongo import MongoClient

conn = None
try:
    db = {'host': 'localhost', "port": 27017}
    conn = MongoClient(**db)
    print("{} 연결성공!!!".format(conn))
    result = conn['big_data']['sample'].delete_one({'name': 'Avante'})
    print("~" * 80)
    print(result)
    print(result.raw_result)
    print(result.deleted_count)
    print("=" * 80)
    result = conn['big_data']['sample'].delete_many({'name': 'Morning'})
    print("~" * 80)
    print(result)
    print(result.raw_result)
    print(result.deleted_count)
    print("=" * 80)

except Exception as e:
    print("에러 :", e)
finally:
    if conn is not None:
        conn.close()
