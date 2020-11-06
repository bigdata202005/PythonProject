import sys

# 파이참에서 텍스트파일  만들때 탭이 공백으로 자동으로 변환된다.
# 탭이 있는 문서를 만들려면 다른 프로그램에서 텍스트 파일을 만들어서 포함해야 한다.

# print("인수 개수 :", len(sys.argv))
if len(sys.argv) == 3:
    src = sys.argv[1]  # 원본파일명
    dst = sys.argv[2]  # 사본파일명
    # print(src, dst)
    src_file = open(src, 'r', encoding='utf-8')  # 읽기용 파일 열기
    dst_file = open(dst, 'w')  # 쓰기용 파일 열기
    tab_data = src_file.read()  # 전체 내용 읽기
    # 탭을 공백 4개로 변환 : replace함수 사용
    space_data = tab_data.replace("\t", " "*4)
    # 저장
    dst_file.write(space_data)
    print(tab_data)
    print('~' * 80)
    print(space_data)
    print('~' * 80)
    # 파일 닫기
    src_file.close()
    dst_file.close()
    print("{}파일의 내용을 {}파일로 변환완료!!!!".format(src, dst))
else:
    print('실행 형식 : python tabto4.py 원본파일 사본파일')
    print('실행 예 : python tabto4.py src.txt dst.txt')
    src = 'tabto4.py\tb\tc'
    print(src)
    print(src.replace("\t", '%'*10))