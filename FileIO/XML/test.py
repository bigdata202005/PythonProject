import collections

print('Regular dictionary:')
d = {}
d['e'] = 'E'
d['c'] = 'C'
d['d'] = 'D'
d['a'] = 'A'
d['b'] = 'B'

print(d)
for k, v in d.items():
    print(k, v)

d = collections.OrderedDict()
print('\nOrderedDict:')
d['e'] = 'E'
d['c'] = 'C'
d['d'] = 'D'
d['a'] = 'A'
d['b'] = 'B'
print(d)
for k, v in d.items():
    print(k, v)


