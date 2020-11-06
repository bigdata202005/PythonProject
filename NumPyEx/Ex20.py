import numpy as np

# 사본 및 보기
ar1 = np.arange(12).reshape(3,4)
print(ar1)
print("-" * 80)
# 얕은복사 : 주소가 복사된다. 전혀 복사하지 않는다.
ar2 = ar1
print("ar2 = ar1")
print("ar2 is ar1 :", ar2 is ar1)  # 같은객체다
print(id(ar1), id(ar2))  # 같은객체다
print("-" * 80)
print(ar1)
print("-" * 80)
print(ar2)
print("-" * 80)
print("수정 : ar1[1, 1] = 100")
ar1[1, 1] = 100
print("둘다 변경 : 결국 대입하면 배열은 1개뿐이다. 주소 복사!!!")
print(ar1)
print("-" * 80)
print(ar2)
print("=" * 80)

# view메서드는 동일한 데이터를 보는 새 배열 객체를 만듭니다.
ar3 = ar1.view()
print("ar3 is ar1 :", ar3 is ar1)
print("ar3.base is ar1 :", ar3.base is ar1)
print(ar1)
print("-" * 80)
print(ar3)
print("-" * 80)
print("수정 : ar3[0,0] = 1234")
print("둘다 변경 : 결국 대입하면 배열은 1개뿐이다. 주소 복사!!!")
ar3[0,0] = 1234
print(ar1)
print("-" * 80)
print(ar3)
print("=" * 80)

print(ar3.flags.owndata)

ar3 = ar3.reshape((2, 6))
print(ar1)  # 원본은 변경되지 않는다.
print("-" * 80)
print(ar3)
print("=" * 80)

# 배열을 분할하면보기가 반환됩니다.
ar4 = ar1[:, 1:3]   # 배열 분할 : 전체를 1,2열만
print(ar4)
print("-" * 80)
ar4[:] = 10         # 배열 매용을 모두 10으로 변경
print(ar4)
print("-" * 80)
print(ar1)          # 원본값이 변경
print("-" * 80)

ar1[:, 1:3] = 999
print(ar1)          # 원본값이 변경
print("=" * 80)

# 깊은 복사 : 내용이 복사된다. copy메서드 사용
ar1 = np.arange(12).reshape(3,4)
print("원본")
print(ar1)
print("-" * 80)
ar2 = np.copy(ar1)
print("사본")
print(ar2)
print("-" * 80)
print("값변경 : ar2[0, 0] = 999")
ar2[0, 0] = 999
# 사본만 변경 되었다!!!
print(id(ar1), id(ar2))
print("원본")
print(ar1)
print("-" * 80)
print("사본")
print(ar2)
print("-" * 80)

# 깊은 복사를 해야  실행 되더라도 메모리에 유지됩니다
a = np.arange(int(1e8))
b = a[:100].copy()
print(a)
print(b)
del a
print(b)
print("-" * 80)

a = np.arange(int(1e8))
b = a[:100]
print(a)
print(b)
del a
print(b)
print("-" * 80)

a = np.arange(int(1e8))
b = a    # 앝은복사
print(a)
print(b)
del a    # a삭제
print(b) # 사본인 b값이 유지가 된다.
print("-" * 80)
del b   # b삭제
# print(b)  # NameError

