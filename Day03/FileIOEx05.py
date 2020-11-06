file = open('test_euckr.txt', "r")
allLines = file.read()  # 전체를 스트링으로 읽는다.
print(type(allLines))
print(allLines, end="")
file.close()
print("*" * 80)

file = open('test_utf8.txt', "r", encoding="utf-8")
allLines = file.read()  # 전체를 스트링으로 읽는다.
print(type(allLines))
print(allLines, end="")
file.close()
print("-" * 80)

file = open('test_utf8.txt', "r", encoding="utf-8")
print(file.read(3)) # 원하는 글자만큼 읽기
print(file.read(3))
print(file.read(3))
print(file.read(3))
file.close()
print("=" * 80)



