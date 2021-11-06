"""
- a ^ a ^ a = a

- NOT
  - negation of each bit, just flip each bit
  - If the current bit is 1, turn it 0
  - If the current bit is 0, turn it 1

x
seen_once: 0
seen_twice: 0

1st
seen_once ^ x = x
~seen_twice & (seen_once ^ x) = ~seen_twice & x = x
  - ~seen_twice is all 1s. All 1s AND x is just x
seen_once = ~seen_twice & (seen_once ^ x) = x
seen_twice ^ x = x
~seen_once = negation of x
~seen_once & (seen_twice ^ x) = negation of x AND x
  - ~10 AND 10
  - 01 AND 10 = 00
seen_once: 10
seen_twice: 00

2nd
- seen_once ^ x = 10 ^ 10 = 00
- ~seen_twice = ~00 = 11
- ~seen_twice & (seen_once ^ x) = 11 & 00 = 00
- seen_once: 00
- seen_twice ^ x = 00 ^ 10 = 10
- ~seen_once = 11
- ~seen_once & (seen_twice ^ x) = 11 & 10 = 10

Idea
- In 1st round,
  - get seen_once, by 0 ^ x = x, by 1 & x = x
  - get seen_twice, by 0 ^ x = x, by ~x AND x = 0
- In 2nd round,
  - update seen_once, by x ^ x = 0, by 1 AND 0 = 0
  - update seen_twice, by 0 ^ x = x, by 1 & x = x
- In 3rd round,
  - update seen_once, by 0 ^ x = x, by ~x AND x = 0
  - update seen_twice, by x ^ x = 0, by 1 AND 0 = 0
- So the numbers appear three times will be zero, but number appearing once remain
"""

x = 0b10
seen_once = 0b00
seen_twice = 0b00
print(f'x: {x}')
print(f'bin(x): {bin(x)}')
print(f'seen_once: {seen_once}')
print(f'bin(seen_once): {bin(seen_once)}')
print(f'seen_twice: {seen_twice}')
print(f'bin(seen_twice): {bin(seen_twice)}')
print(f'~seen_twice: {~seen_twice}')
print(f'bin(~seen_twice): {bin(~seen_twice)}')
print(f'bin(seen_once ^ x): {bin(seen_once ^ x)}')
print(f'bin(~seen_twice & (seen_once ^ x)): {bin(~seen_twice & (seen_once ^ x))}')
seen_once = ~seen_twice & (seen_once ^ x)
print(f'bin(~seen_once & (seen_twice ^ x)): {bin(~seen_once & (seen_twice ^ x))}')


from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen_once = seen_twice = 0
        for num in nums:
            seen_once = ~seen_twice & (seen_once ^ num)
            seen_twice = ~seen_once & (seen_twice ^ num)
        return seen_once




