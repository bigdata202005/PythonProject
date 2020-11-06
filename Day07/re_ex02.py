# 파이선 정규표현식에 사용되는 모듈
import re

# 참조
# https://greeksharifa.github.io/%EC%A0%95%EA%B7%9C%ED%91%9C%ED%98%84%EC%8B%9D(re)/2018/07/20/regex-usage-01-basic/

data = """
park 800905-1049118 800905-1049118
kim  700905-1059119 700905-1059119
"""

pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))