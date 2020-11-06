# 문제
# chunja2.txt 파일을 읽어서  각각의 줄을 파싱하여
# 다음과 같이 변경하여 chunja3.txt로 저장하시오!!!
# 1. 天地玄黃(천지현황) : 하늘은 위에 있어 그 빛이 검고 땅은 아래 있어서 그 빛이 누르다.
file = open('chunja2.txt', "r",  encoding='utf-8')
file2 = open('chunja3.txt', "w",  encoding='utf-8')
chunja_list = file.readlines()
file.close()
print(str(len(chunja_list)) + "줄 읽음")
for line in chunja_list:
    line_list = line.split("|")
    # print(line_list)
    # print(line_list[0] + ". " + line_list[1] + "(" + line_list[2] + ") : " + line_list[4], end="")
    file2.write(line_list[0] + ". " + line_list[1] + "(" + line_list[2] + ") : " + line_list[4])
print("저장완료!!!")
file.close()
file2.close()
