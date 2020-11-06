import numpy as np


def line(count=30):
    print("~" * count)


# 기본 작업
# 배열의 산술 연산자는 요소별로 적용됩니다 .
# 새 배열이 생성되고 결과로 채워집니다.
a = np.array([20, 30, 40, 50])
print("원본")
print("a :", a)
b = np.arange(1, 5)
print("b :", b)
line()

print("배열 + 정수")
c = a + 3
print("a :", a)
print("c :", c)
line()

print("배열 + 배열")
c = a + b
print("a :", a)
print("b :", b)
print("c :", c)
line()

print("배열 - 정수")
c = a - 3
print("a :", a)
print("c :", c)
line()

print("배열 - 배열")
c = a - b
print("a :", a)
print("b :", b)
print("c :", c)
line()

print("배열 * 정수")
c = a * 3
print("a :", a)
print("c :", c)
line()

print("배열 * 배열")
c = a * b
print("a :", a)
print("b :", b)
print("c :", c)
line()

# 행렬 곱은 @연산자 (python> = 3.5) 또는 dot함수를 사용하여 수행 할 수 있습니다 .
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
print(matrix1, end='\n\n')
print(matrix2, end='\n\n')
matrix3 = matrix1 @ matrix2
matrix4 = matrix1.dot(matrix2)
print(matrix3, end='\n\n')
print(matrix4, end='\n\n')
line()

print("배열 // 정수")
c = a // 3
print("a :", a)
print("c :", c)
line()

print("배열 // 배열")
c = a // b
print("a :", a)
print("b :", b)
print("c :", c)
line()

print(b**2)
line()
print(np.sin(b))
print(10 * np.sin(b))
line()


