dict1 = dict()
dict1['1'] = [1,2,3,4]
print(dict1)
dict1['2'] = [1,2,3,4]
print(dict1)
dict1['3'] = [1,2,3,4]
print(dict1)

for key in dict1.keys():
    print(key, dict1[key])