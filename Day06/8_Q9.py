"""
Q9 평균값 구하기
다음과 같이 총 10줄로 이루어진 sample.txt 파일이 있다.
sample.txt 파일의 숫자 값을 모두 읽어 총합과 평균 값을 구한 후 평균 값을
result.txt 파일에 쓰는 프로그램을 작성하시오.

70
60
55
75
95
90
80
80
85
100
"""
src_file = open("sample.txt", "r", encoding="utf-8")
all_lines = src_file.readlines();
print(all_lines)
src_file.close()
int_list = list(map(lambda x : int(x), all_lines))
print(int_list)
dst_file = open("result.txt", "w", encoding="utf-8")
dst_file.write("합계 : {}".format(sum(int_list)))
dst_file.write("\n")
dst_file.write("평균 : {}".format(sum(int_list)/len(int_list)))
dst_file.write("\n")

