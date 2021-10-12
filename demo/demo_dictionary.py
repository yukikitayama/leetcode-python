dic = {'a': 1, 'b': 2, 'c': 3}
print(dic)
del dic['a']
print(dic)
print()

import collections
dic = collections.defaultdict()
dic['a'] = 1
dic['b'] = 2
dic['c'] = 3
print(dic)
del dic['a']
print(dic)
print()

count = collections.Counter('abc')
print(count)
del count['a']
print(count)
print()