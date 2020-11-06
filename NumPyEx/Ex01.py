import numpy as np

"""
Numpy란?
Numpy는 다차원 배열을 쉽게 처리하고 효율적으로 사용할 수 있도록지원하는 파이썬의 패키지입니다. 
NumPy는 데이터 구조 외에도 수치 계산을 위해 효율적으로 구현된 기능을 제공합니다. 
데이터 분석을 할때, Pandas와 함께 자주 사용하는 도구로 등장합니다.

왜 Numpy를 사용할까
데이터란 이미지, 오디오, 텍스트, 숫자 등 다양한 형태와 크기로 존재합니다. 
사람은 이런 데이터들을 가지고 이해하지만 컴퓨터는 0 또는 1만 이해합니다. 
여기서 핵심은 데이터를 숫자의 배열로 볼 수 있습니다. 
실제로 데이터 분석을 수행하기 위한 전제 조건은 컴퓨터가 이해할 수 있도록 
데이터를 숫자 형식으로 변환하는 것입니다. 
여기서 효율적으로 배열을 저장 및 조작할 수 있어야 하는데 이러한 요구사항으로 
Numpy 패키지가 나오게 됩니다. 파이썬의 내장 기능인 리스트 또한 Numpy 배열과 동일한 기능을 
제공할 수 있기 때문에 왜 Numpy를 사용해야 하는지 의문이 듭니다. 
배열의 크기가 작으면 문제가 되지 않지만 Numpy 배열은 데이터의 크기가 커질수록 
저장 및 가공을 하는데 효율성을 보장합니다. 
이러한 장점으로 파이썬의 Numpy 패키지는 Data Science에 핵심적인 도구로 인식이 되고 있습니다.

pip install numpy

"""


def view_array(a):
    print("=" * 80)
    print(a)
    print("~" * 80)
    print("shape :", a.shape)  # 배열의 크기를 나타내는 정수의 튜플입니다.
    print("ndim :", a.ndim)  # 배열의 차원
    print("dtype.name :", a.dtype.name)  # 배열 요소 타입
    print("itemsize :", a.itemsize)  # 배열의 각 요소 크기 (바이트)
    print("size :", a.size)  # 배열의 총 요소 수
    print("~" * 80)


a = np.arange(20)
view_array(a)
b = np.arange(15).reshape(3, 5)
view_array(b)
# 2차원 배열에 접근 : ,로 첨자 구분
print(b[1, 3])
