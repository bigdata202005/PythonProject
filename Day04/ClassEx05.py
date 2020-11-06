# 클래스 변수 : 자바의 static변수와 동일
class Family:
    name = "한사람"


family1 = Family()
family2 = Family()

print(family1.name)  # 한사람
print(family2.name)  # 한사람

# 자바의 static 같지만 아니다!!!  객체마다 변수가 따로 생성!!!
family2.name = "두사람"
print(family1.name)  # 한사람
print(family2.name)  # 두사람

# 클래스이름으로 접근하면 처음의 변수가 변경!!!
Family.name = "세사람"
print(family1.name)  # 세사람
print(family2.name)  # 두사람

#  클래스이름으로 접근하면 이후 생성되는 객체들의 변수 값이 변경된다.
family3 = Family()
print(family3.name)  # 세사람


