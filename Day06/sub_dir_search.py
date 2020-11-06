import os


def search(dirname):
    # os.listdir(경로) : 파일 목록을 리스트로 반환
    file_list = os.listdir(dirname)
    # print(type(file_list))
    for file in file_list:
        file_name = os.path.join(dirname, file)
        # print(file_name, os.path.isdir(file_name) and "디렉토리" or "파일")
        if os.path.isdir(file_name):
            search(file_name)  # 현재 파일이 디렉토리면 다시 검색한다.
        else:
            ext = os.path.splitext(file_name)[-1]
            if ext == '.py':
                print("파이선 파일 :", file_name)


if __name__ == "__main__":
    search("D:\\BigData\\PythonProject")
