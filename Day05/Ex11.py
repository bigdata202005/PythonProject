print(dir(__builtins__))

print("-" * 80)
print("내장 함수")
print("-" * 80)

for m in dir(__builtins__):
    print(m)
print("-" * 80)

print("내장 모듈")
print(help('modules'))