num = []
for i in range(10,10001):
    s = list(str(i))
    s = '*'.join(s)
    print(s)
    num.append(eval(s))
print(num)
print(sum(num))
