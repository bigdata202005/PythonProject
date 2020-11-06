# 난수
import random

for i in range(10):
    print(random.random())  # 0~1사이의 난수
print('~' * 50)

for i in range(10):
    print(random.randint(0, 10))  # 0~10사이의 난수
print('~' * 50)


# 리스트를 인수로 받아 임의로 1개를 리턴하고 리스트에서 제거 해준다.
def random_pop(data):
    number = random.randint(0, len(data) - 1)
    return data.pop(number)


data = [1, 2, 3, 4, 5]
while data:
    print(random_pop(data))

print(data)

