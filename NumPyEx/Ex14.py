import numpy as np

# 배열 모양 변경
rg = np.random.default_rng()  # 난수 발생기 객체 생성
ar = rg.random((3, 4))  # 난수로 3행 4열 배열 생성
print(ar)
print('~' * 80)

ar = np.floor(ar*100)  # floor 함수로 배열을 정수화
print(ar)
print('~' * 80)

# 배열의 모양은 다양한 명령으로 변경할 수 있습니다.
# 다음 세 명령은 모두 수정 된 배열을 반환하지만 원래 배열은 변경하지 않습니다.

ar2 = ar.ravel()  # flat을 적용하여 1차원 배열로 변경
print(ar2)
print('~' * 80)

ar3 = ar.reshape(2, 6)  # reshape를 이용하여 행열의 크기 변경
print(ar3)
print('~' * 80)

ar4 = ar.T  # 행열을 열행으로 변경
print(ar4.shape)
print(ar4)
print('~' * 80)

ar.resize((2, 6))  # 자신이 변경된다.
print(ar)
print('~' * 80)

# 모양 변경 작업에서 차원이 -1로 지정되면 다른 차원이 자동으로 계산됩니다.
ar5 = ar.reshape(3, -1)  # 행을 3으로 열을 -1로하면 열 값은 자동으로 계산
print(ar5)
print('~' * 80)

ar5 = ar.reshape(6, -1)  # 행을 6으로 열을 -1로하면 열 값은 자동으로 계산
print(ar5)
print('~' * 80)









