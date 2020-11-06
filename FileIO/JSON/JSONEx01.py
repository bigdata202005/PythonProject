import json
# json파일 처리는 json모듈을 이용!!!
student_data = {
    "FirstName": "Gildong",
    "LastName": "Hong",
    "Age": 20,
    "University": "Yonsei University",
    "Courses": [
        {
            "Major": "Statistics",
            "Classes": ["Probability",
                        "Generalized Linear Model",
                        "Categorical Data Analysis"]
        },
        {
            "Minor": "ComputerScience",
            "Classes": ["Data Structure",
                        "Programming",
                        "Algorithms"]
        }
    ]
}
print(type(student_data))
print(student_data)
print("-" * 80)

# json.dumps()를 사용해서 JSON 포맷 데이터를 메모리에 만들기
# 이때 만약 json.dumps()가 아니라 json.dump() 처럼 's'를 빼먹으면 TypeError가 발생하므로 주의하세요.
print(type(json.dumps(student_data)))
print(json.dumps(student_data))
print("-" * 80)
# 들여쓰기
str_json2 = json.dumps(student_data, indent=4)
print(type(str_json2))
print(str_json2)
print("-" * 80)
# 정렬
str_json3 = json.dumps(student_data, indent=4, sort_keys=True)
print(type(str_json3))
print(str_json3)
print("-" * 80)

# with open(): json.dump() 를 사용해서 JSON 포맷 데이터를 디스크에 쓰기
with open("student_file.json", "w") as json_file:
    json.dump(student_data, json_file)

# 디스크에 있는 JSON 포맷 데이터를 json.load()를 사용하여 Python 객체로 읽어오기 (역직렬화, 디코딩 하기)
# 이때 json.loads() 처럼 's'를 붙이면 TypeError: the JSON object must be str, not 'TextIOWrapper'가 발생합니다.
# (json.loads()가 아니라 json.load() 를 사용해야 함)
with open("student_file.json", "r") as st_json:
    st_python1 = json.load(st_json)
print(type(st_python1))
print(st_python1)
print("-" * 80)

# 메모리에 있는 JSON 포맷 데이터를 json.loads()로 Python 객체로 읽기 (역직렬화, 디코딩하기)
# 이때 만약 json.loads() 대신에 's'를 빼고 json.load()를 사용하면
# AttributeError: 'str' object has no attribute 'read' 가 발생하니 주의하기 바랍니다.

str_python2 = json.loads(str_json3)
print(type(str_python2))
print(str_python2)
print("-" * 80)


