# 고급 인덱싱 및 인덱스 트릭
# 배열은 정수 배열과 부울 배열로 인덱싱 할 수 있습니다.
import numpy as np
a = np.arange(12)**2
print("배열 a")
print(a)
print("~" * 80)
# 1차원 배열로 인수를 넘기면 해당 인덱스값을 1차원배열로 리턴
i = np.array([1, 1, 3, 8, 5])
print("[1, 1, 3, 8, 5] index")
print(a[i])

# 2차원 배열로 인수를 넘기면 해당 인덱스값을 2차원배열로 리턴
j = np.array([[3, 4], [9, 7]])
print("[[3, 4], [9, 7]] index")
print(a[j])
print("~" * 80)
# 팔레트를 사용하여 레이블 이미지를 컬러 이미지로 변환하여이 동작을 보여줍니다.
palette = np.array([[0, 0, 0],          # black
                    [255, 0, 0],        # red
                    [0, 255, 0],        # green
                    [0, 0, 255],        # blue
                    [255, 255, 255]])   # white
# 2차원 배열에 2차원 배열을 인수로 주면 행 인덱스가 되어 3차원 배열을 리턴 한다.
image = np.array([[0, 1, 2, 0], [0, 3, 4, 0]])
print(palette[image])


