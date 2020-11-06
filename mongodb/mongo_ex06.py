from pymongo import MongoClient

conn = None
try:
    db = {'host': 'localhost', "port": 27017}
    conn = MongoClient(**db)
    print("{} 연결성공!!!".format(conn))
    result = conn['big_data']['sample'].update_one(filter={'name':'Avante'}, update={"$set": {'year':'2020'}})
    print("~" * 80)
    print(result)
    print(result.raw_result)
    print(result.matched_count)
    print("=" * 80)
    result = conn['big_data']['sample'].update_many(filter={'name':'Morning'}, update={"$set": {'year':'2020'}})
    print("~" * 80)
    print(result)
    print(result.raw_result)
    print(result.matched_count)
    print("=" * 80)
    result = conn['big_data']['sample'].find(None)
    for data in result:
        print(data)
except Exception as e:
    print("에러 :", e)
finally:
    if conn is not None:
        conn.close()
