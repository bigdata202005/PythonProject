# 폰트 설정 방법 1
import matplotlib.pyplot as plt

# matplotlib 폰트설정
# plt.rc('font', family='NanumGothicCoding') # For MacOS
plt.rc('font', family='NanumGothicCoding') # For Windows
print(plt.rcParams['font.family'])
plt.plot([1, 2, 3, 4])
plt.ylabel('y-축값')
plt.show()