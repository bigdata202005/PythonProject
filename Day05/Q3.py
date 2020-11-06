# Q3
# 다음 결과를 예측해 보자.
#
# 하나.
# >>> all([1, 2, abs(-3)-3])
# 둘.
# >>> chr(ord('a')) == 'a'

print([1, 2, abs(-3)-3])
print(all([1, 2, abs(-3)-3]))  # False
print(chr(ord('a')))
print(chr(ord('a')) == 'a')  # True
