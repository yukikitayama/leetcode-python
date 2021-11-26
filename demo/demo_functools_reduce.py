nums = [1, 2, 3, 4, 5]

import functools

result = functools.reduce(lambda x, y: x * y, nums)
# 1 * 2 * 3 * 4 * 5 = 6 * 20 = 120
print(f'result: {result}')

data = ['a', 'b', 'c']
result = functools.reduce(lambda x, y: x + y, data)
print(f'result: {result}')

