import os
print(os.environ)
for key in os.environ:
    print(key, ":", os.environ[key])

os.chdir('c:\\')   # cd 경로
print(os.getcwd()) # 현재 우치
# 시스템 명령어 실행
print(os.system('dir/w'))
print('-' * 80)
# 시스템 명령어 저장
file = os.popen("dir")
print(file.read())
print('-' * 80)

file = os.popen("ipconfig/all")
print(file.read())
print('-' * 80)


# 문제 : 자신의 컴퓨터 ip주소와 맥어드레스(물리적 주소)를 출력하는 프로그램 작성
file = os.popen("ipconfig/all")
all_lines = file.readlines()
print(str(len(all_lines)) + "줄")
for line in all_lines:
    if 'IPv4 주소' in line:
        print("IP주소 :", line.split(":")[1].strip())
    if '물리적 주소' in line:
        print("맥어드레스 : ", line.split(":")[1].strip())
