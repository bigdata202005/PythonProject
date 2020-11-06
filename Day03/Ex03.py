# Bitwise연산자 : & (AND), | (OR), ^ (XOR), ~ (Complement), <<, >> (Shift)
a = 3
b = 5
# 3 =   0011
# 5 =   0101
# and   0001 ==> 1
# or    0111 ==> 7
# xor   0110 ==> 6
print("{} & {} =  {}".format(a, b, a & b))
print("{} | {} =  {}".format(a, b, a | b))
print("{} ^ {} =  {}".format(a, b, a ^ b))
c = a + (~b+1)
print(c) # -2 : 뺄셈은 2의 보수를 더해서 한다!!!! ~은 1의보수, 1의보수+1 = 2의보수

print("{} << {} =  {}".format(a, 2, a << 2))
print("{} >> {} =  {}".format(b, 1, b >> 1))
print("{} >> {} =  {}".format(b, 2, b >> 2))

print(a == b)
print(a != b)
print(2**3)
d = 2
d **= 3
print(d)  # 8
d *= 2 + 3
print(d)  # 40
