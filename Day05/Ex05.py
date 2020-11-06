# glob
# 가끔 파일을 읽고 쓰는 기능이 있는 프로그램을 만들다 보면
# 특정 디렉터리에 있는 파일 이름 모두를 알아야 할 때가 있다. 이럴 때 사용하는 모듈이 바로 glob이다.
import glob
import os
print("현재 디렉토리 :", os.getcwd())
print('-' * 80)
print("파일목록")
for file in glob.glob(os.getcwd()+"\\*"):
    print(file)
print('-' * 80)

for file in glob.glob("D:\\*"):
    print(file)


# tempfile
# 파일을 임시로 만들어서 사용할 때 유용한 모듈이 바로 tempfile이다.
# tempfile.mkstemp()는 중복되지 않는 임시 파일의 이름을 무작위로 만들어서 돌려준다.
print("임시파일 만들기")
import tempfile
filename = tempfile.mkdtemp()
print(filename, type(filename))

