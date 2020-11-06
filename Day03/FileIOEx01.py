# 파일 쓰기
file = open('Test.txt', "w")  # 쓰기모드로 열기 : 없으면 만들고 있으면 겹쳐쓰기
# 사용하기
for i in range(1, 11):
    file.write("{:02d}Line.\n".format(i))
# 닫기
file.close()

# 파일 쓰기
file = open('Test.txt', "w")  # 쓰기모드로 열기
# 사용하기
for i in range(1, 11):
    file.write("{:02d}Line.\n".format(i))
# 닫기
file.close()


# 파일 쓰기
file = open('Test2.txt', "a")  # 추가 모드로 열기 : 없으면 만들고 있으면 추가
# 사용하기
for i in range(1, 11):
    file.write("{:02d}Line.\n".format(i))
# 닫기
file.close()



