"""
Q8 역순 저장
다음과 같은 내용의 파일 abc.txt가 있다.

AAA
BBB
CCC
DDD
EEE
이 파일의 내용을 다음과 같이 역순으로 바꾸어 저장하시오.

EEE
DDD
CCC
BBB
AAA
"""
src_file = open("abc.txt", "r", encoding="utf-8")
all_lines = src_file.readlines();
src_file.close()
print(all_lines)
all_lines.sort()
print(all_lines)
all_lines.reverse()
print(all_lines)
dst_file = open("abc_reverse.txt", "w", encoding="utf-8")
for line in all_lines:
    dst_file.write(line)
dst_file.close()
