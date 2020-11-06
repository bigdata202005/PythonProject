import random

# 난수로 리스트 채우기
data = list()
for i in range(1,10):
    data.append(random.randint(0,100))

print(data)

# 리스트 중에 무작위로 1개 선택
print(random.choice(data))
print(random.choice(data))
print(random.choice(data))
print(data)
print()

# 리스트의 항목을 무작위로 섞고 싶을 때는 random.shuffle 함수를 사용하면 된다.
data2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(data2)
random.shuffle(data2)
print(data2)

# 데이터 중에서 몇개만 얻기
print(random.sample(list(range(1,45)), 6))
lotto = random.sample(list(range(1,45)), 6)
lotto.sort()
print(lotto)
print('~' * 80)

print("로또번호 자동생성")
num = int(input('몇게임?'))
for i in range(1,num+1):
    lotto = random.sample(list(range(1, 45)), 6)
    lotto.sort()
    print("{:02d}번째 게임 : {}".format(i, lotto))
print('~' * 80)

# 문제 : 위의 내용을 출력할때 숫자를 두자리로 출력하게 하시오!!! map사용
print("로또번호 자동생성")
num = int(input('몇게임?'))
for i in range(1,num+1):
    lotto = random.sample(list(range(1, 45)), 6)
    lotto.sort()
    print("{:02d}번째 게임 : {}".format(i, list(map(lambda x : "{:02d}".format(x), lotto))))
print('~' * 80)
