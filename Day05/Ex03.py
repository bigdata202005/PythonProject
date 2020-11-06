# pickle
# pickle은 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈이다.
# 다음 예는 pickle 모듈의 dump 함수를 사용하여 딕셔너리 객체인 data를 그대로 파일에 저장하는
# 방법을 보여 준다.
import pickle
file1 = open('pickle_test.txt', 'wb')
data1 = {1 : 'python',2:'java', 3:'jsp'}
print("data1 :", data1)
pickle.dump(data1, file1)
file1.close()

file2 = open('pickle_test.txt', 'rb')
data2 = pickle.load(file2)
print("data2 :", data2)
file2.close()
