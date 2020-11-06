# python 삼항 연산자
while True:
    a = int(input("정수입력 (0은 종료) : "))
    if a == 0:
        break;
    print("짝수" if a % 2 == 0 else "홀수")  # if를 이용한 3항 연산
    print(a % 2 == 0 and "짝수" or "홀수")   # and와 or를 이용한 3항 연산

print("안녕!!!")
