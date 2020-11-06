"""
Q1 문자열 바꾸기
다음과 같은 문자열이 있다.
a:b:c:d
문자열의 split와 join 함수를 사용하여 위 문자열을 다음과 같이 고치시오.
a#b#c#d
"""
# 문자열 나누기(split)
# 문자열 삽입 및 연결(join)
str1 = "a:b:c:d"
print(str1)
str2 = "#".join(str1.split(":"))
print(str2)

print(str1.split(":")) # 구분자로 나눠 리스트로
print("~".join(str1)) # 모든 문자 사이에 ~ 삽입
# 이것도 가능
print(str1.replace(":","#"))
print("|^|".join(str1.split(":")))
