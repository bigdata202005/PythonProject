import sys
# sys.argv는 명령행 인수를 받는다.
# 첫번째는 자기 자신이다.
args = sys.argv[0:]
for i in args:
    print(i)

