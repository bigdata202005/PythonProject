data = """
park 800905-1049118 800905-1049118
kim  700905-1059119 800905-1049118
"""
print("원본")
print(data)
print('-' * 80)

print("결과")
result = []  # 완료된 결돠를 저장할 리스트
for line in data.split("\n"): # 엔터로 구분해서 반복
    word_result = []  # 변경 결과 저장할 리스트
    for word in line.split(" "): # 공백으로 구분
        # 구분 문자가가 14자리이면서 앞의 6자리가 숫자 뒤의 7자리가 숫자라면
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            # 뒤의 7자리를 *로 변경 : 앞의 6자리만 취하고 뒤에는 -*******를 붙인다.
            word = word[:6] + "-*******"
        word_result.append(word)  # 추가

    result.append(" ".join(word_result)) # 추가

print("\n".join(result)) # 리스트의 요소들을 줄바꿈 문자로 연결
print('-' * 80)
