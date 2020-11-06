import sys

# print("인수 개수 :", len(sys.argv))
if len(sys.argv)>1:
    option = sys.argv[1]
    # print("명령 :", option)

    if option == '-a':
        memo = sys.argv[2]
        # print("메모 :", memo)
        # 저장 처리
        file = open('memo.txt', 'a')
        # 이렇게하면 공백으로 구분된 뒤의 내용은 저장이 되지 않는다.
        # file.write(memo)
        for i in range(2, len(sys.argv)):
            file.write(sys.argv[i])
            file.write(' ')
        file.write('\n')
        file.close()
    elif option == '-v':
        file = open('memo.txt', 'r')
        print(file.read())
        file.close()
else:
    print('실행 형식 : python memo_dao.py 옵션 [내용]')
    print('저장 예 : python memo_dao.py -a 저장내용')
    print('보기 예 : python memo_dao.py -v')

