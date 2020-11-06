import os


# 하위 디렉터리 검색을 쉽게 해주는 os.walk
# os.walk를 사용하면 위에서 작성한 코드를 보다 간편하게 만들 수 있다.
# os.walk는 시작 디렉터리부터 시작하여 그 하위 모든 디렉터리를 차례대로 방문하게 해주는 함수이다.
def search(dirname):
    for (path, dir, files) in os.walk(dirname):
        for filename in files:
            ext = os.path.splitext(filename)[-1]
            if ext == '.jpg':
                print("%s/%s" % (path, filename))


if __name__ == "__main__":
    # search("D:\\BigData\\PythonProject")
    search("D:\\")
