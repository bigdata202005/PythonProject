import json

import matplotlib.pyplot as plt
lotto = None
with open("lotto.json", 'r', encoding="utf-8-sig") as json_file:
    lotto = json.load(json_file)
total_count = 0
if lotto is not None:
    total_count = len(lotto)
print("전체개수 :", total_count)
# ------------------------------------------------------
lotto_list = list()
for key in lotto.keys():
    for l in lotto[key]:
        lotto_list.append(l)
print(lotto_list)
y_array = []
for i in range(1, 46):
    print(i, ":", lotto_list.count(i))
    y_array.append(lotto_list.count(i))

plt.bar(range(1, 46), y_array)
plt.show()

plt.barh( range(1, 46), y_array)
plt.show()

plt.hist(lotto_list)
plt.show()
