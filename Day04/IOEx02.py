# 사용자 입력과 출력
print("life" "is" "too short")  # 큰따옴표(")로 둘러싸인 문자열은 + 연산과 동일하다
print("life"+"is"+"too short")
print("life", "is", "too short")  # ,(콤마)로 구분하면 공백이 삽입된다.
# 구분자 기본값은 공백이고 마지막 문자의 기본값은 줄바꿈문자
print("life", "is", "too short", sep="-", end="\n\n\n")  # 구분자와 마지막 문자 지정 가능
print("몇줄이 삽입 될었을까요?")

# 한 줄에 결괏값 출력하기
print("나의 이름은")
print("한사람")
print("입니다.")
print("*" * 60)
print("나의 이름은", end=' ')
print("한사람", end=' ')
print("입니다.")
print("*" * 60)

