# 파일 읽기
file = open('Test.txt', "r")  # 읽기모드로 열기 : 없으면 에러 있으면 열기
# file3 = open('Test3.txt', "r")  # FileNotFoundError: [Errno 2] No such file or directory: 'Test3.txt'
print(file.readline())  # 1줄읽기
print(file.readlines()) # 모두 읽기 -- 리스트
file.close()
print("~ " * 40)

file = open('Test.txt', "r")
while True:
    line = file.readline()
    print(line, end='')
    if not line:
        break
file.close()
print("~ " * 40)

file = open('Test.txt', "r")
lines = file.readlines()
for line in lines:
    print(line, end='')
file.close()
print("~ " * 40)

file = open('Test.txt', "r")
allLines = file.read()  # 전체를 스트링으로 읽는다.
print(type(allLines))
print(allLines)
file.close()

# 자동 닫기
with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python")