# 폰트 설정 방법 1
import matplotlib
import matplotlib.pyplot as plt

# matplotlib 폰트설정
import matplotlib.font_manager as fm
fm.get_fontconfig_fonts()
# font_location = '/usr/share/fonts/truetype/nanum/NanumGothicCoding.ttf'
font_location = './font/NanumGothicCoding.ttf' # For Windows
font_name = fm.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)
plt.plot([1, 2, 3, 4])
plt.ylabel('y-축값')
plt.show()