import sys

import numpy as np

# 1 차원 배열은 행으로, 2 차원은 행렬로, 3 차원은 행렬 목록으로 인쇄됩니다.
# 1차원  배열
array1 = np.arange(12)
print(array1)

# 2차원  배열
array2 = np.arange(12).reshape(3, 4)
print(array2)

# 3차원  배열
array3 = np.arange(12).reshape(2, 3, 2)
print(array3)

# 배열이 너무 커서 인쇄 할 수없는 경우 NumPy는 배열의 중앙 부분을 자동으로 건너 뛰고 모서리 만 인쇄합니다.
array4 = np.arange(10000)
print(array4)

array5 = np.arange(10000).reshape(100, 100)
print(array5)

# 이 동작을 비활성화하고 NumPy가 전체 배열을 인쇄하도록 강제하려면
# 인쇄 옵션을 변경할 수 있습니다 set_printoptions.
np.set_printoptions(threshold=sys.maxsize)
array6 = np.arange(10000).reshape(100, 100)
print(array6)


