"""
Lunar(Dismal) Arithmetic 라는 어떤 연산이 있습니다. 이 연산에서 덧셈「+」은 각 자릿수를 비교해서 큰 수를 취합니다.

5 + 3 = 5
13 + 6 = 16

   169
 + 248
 ------
   269
그리고 곱셈「×」은 각 자릿수를 비교해서 작은 수를 취합니다.

5 × 3 = 3
13 × 6 = 13

      169
   × 248
   ------
     168
    144
 + 122
 --------
   12468
Lunar Arithmetic를 수행하는 계산기를 만들어봅시다.

"""
def ladd(a, b):
    c = ''
    a, b = str(a)[::-1], str(b)[::-1]
    for i in range(max(len(a), len(b))):
        c += max(a[i:i+1], b[i:i+1])
    return int(c[::-1])


cnt = 0
list1 = []
for i in "248"[::-1]:
    c = "";
    for j in "169"[::-1]:
        # print(i, j, min(i, j), sep=", ", end="===>")
        c = min(i, j) + c
    c += "0" * cnt
    cnt += 1
    list1.append(c)
print(list1)
e = 0
for i in list1:
    print(e, i, ladd(e,i))
    e = ladd(e, i)

print(e)