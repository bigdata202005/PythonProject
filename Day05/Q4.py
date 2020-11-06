# filter와 lambda를 사용하여 리스트 [1, -2, 3, -5, 8, -3]에서 음수를 모두 제거해 보자.
def positive(data_list):
    return_list = list()
    for i in data_list:
        if i>0:
            return_list.append(i)
    return return_list

# 일반 함수 사용
data = [1, -2, 3, -5, 8, -3]
print("원본 :", data)
print("결과 :", positive(data))


# 필터 사용
def positive2(data):
    return data > 0


print("결과 :", list(filter(positive2, data)))

# 람다식 사용
print("결과 :", list(filter(lambda x : x > 0, data)))

