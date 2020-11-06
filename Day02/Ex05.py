# 맵 : {Key1:Value1, Key2:Value2, Key3:Value3, ...}
dic = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(dic)

# 키/값 형태로 사용 가능
a = {1: 'hi'}
print(a)
a = {'a': [1, 2, 3]}
print(a)

#  디셔너리에 쌍을 추가/ 삭제
a[2] = [4, 5, 6]  # 추가
a['name'] = "한사람"  # 추가
a['age'] = 22  # 추가
print(a)
# del 디셔너리[키] : 삭제
del a[2]
del a['age']
print(a)

p = {"김연아": "피겨스케이팅", "류현진": "야구", "박지성": "축구", "귀도": "파이썬"}
print(p)

# 딕셔너리에서 Key 사용해 Value 얻기
print(p["귀도"])
print(p["박지성"])
print(p["류현진"])

# 딕셔너리 만들 때 주의할 사항 : 키는 중복을 허용하지 않는다.
dic1 = {1: '하나', 2: '둘', 3: '셋'}
print(dic1)
dic1[1] = '한놈'  # 동일한 키를 사용하면 수정이 된다.
dic1[2] = '두식이'
print(dic1)

# 키값만 리스트로 만들기
print(dic1.keys())
print(type(dic1.keys()))
print(list(dic1.keys()))
print(type(list(dic1.keys())))

for key in dic1.keys():
    print(str(key) + " : " + dic1[key])

# 값만
print(dic1.values())
print(type(dic1.values()))
print(list(dic1.values()))
print(type(list(dic1.values())))

# Key, Value 쌍 얻기(items)
print(dic1.items())
print(type(dic1.items()))
print(list(dic1.items()))
print(type(list(dic1.items())))
print(list(dic1.items())[1][1])

# Key: Value 쌍 모두 지우기(clear)
dic1.clear()
print(dic1)

dic1['name'] = '한사람'
dic1['age'] = 22
dic1['gender'] = '여자'
# 키를 통한 값얻기
print("이름 : " + dic1['name'])
print("이름 : " + dic1.get('name'))

# 해당 Key가 딕셔너리 안에 있는지 조사하기(in)
print(dic1)
# print("없는 키 : " + dic1.get('nickname')) # 에러 : TypeError: can only concatenate str (not "NoneType") to str
print('name' in dic1)
print('nickname' in dic1)

dic1 = {'name': '한사람', 'age': 33}
dic2 = {'name': '두사람', 'age': 22, 'nickname': '최고관리자'}
# 위의 사전 자료형에서 별명이 있는지를 판단하여 있으면 찍고 없으면 "별명없다"를 출력하시오
# 어제 배운 삼항 연산자 2개를 이용하여 해결하시오

print(dic1['nickname'] if 'nickname' in dic1 else '별명없다')
print(dic2['nickname'] if 'nickname' in dic2 else '별명없다')

print('nickname' in dic1 and dic1['nickname'] or '별명없다')
print('nickname' in dic2 and dic2['nickname'] or '별명없다')



