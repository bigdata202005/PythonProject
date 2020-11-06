# 문제
# score.txt 파일을 읽어서  각각의 줄을 파싱하여
# 합계와 평균까지 구하고 평균은 소수이하 2자리까지
# score_result.txt로 저장하시오!!!

file1 = open('score.txt', "r", encoding='utf-8')
file2 = open('score_result.txt', "w", encoding='utf-8')
for line in file1.readlines():  # 모든줄 반복
    line = line.rstrip("\n")    # 줄뒤의 엔터 지우기
    line_list = line.split("\t") # 탭을 기준으로 리스트로 변환
    # print(line_list, end="")  # 출력
    # 각각의 변수로 나눔
    name = line_list[0].strip() 
    n1 = int(line_list[1].strip())
    n2 = int(line_list[2].strip())
    n3 = int(line_list[3].strip())
    n4 = int(line_list[4].strip())
    # 합계
    tot = n1 + n2 + n3 + n4
    # 평균
    avg = tot / 4
    # print("{:6s}{:6d}{:6d}{:6d}{:6d}{:6d}{:8.2f}".format(name, n1, n2, n3, n4, tot, avg))  # 출력
    file2.write("{:6s}{:6d}{:6d}{:6d}{:6d}{:6d}{:8.2f}\n".format(name, n1, n2, n3, n4, tot, avg)) ## 저장
print("저장완료!!!")
file1.close()
file2.close()
