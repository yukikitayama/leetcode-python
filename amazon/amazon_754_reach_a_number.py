"""
- In each step, the distance that a step makes expands
- Because we can use + and - signs, the answer for target is same as abs(target)
  - It's safe to consider only target > 0

- Let S be the sum of steps
- S = 1 + 2 + 3
  - k: 3,
  - 6 >= target
  - if target is S: 6,
  - 3 is the smallest number to be the sum is equal to or greater than target
- If S > target,
  - delta = S - target
    -
- target: 4
  - 1 + 2 + 3 = 6 = S, delta = S - target = 2, delta is even
    - delta / 2 = 1, switch 1 sign to -1
    - -1 + 2 + 3 = 4
- target: 5
  - 1 + 2 + 3 = 6 = S, delta = S - target = 6 - 5 = 1, delta is odd
  - Try k + 1, 1 + 2 + 3 + 4 = 10, delta: 10 - 5 = 5, delta is still odd
  - Try k + 2, 1 + 2 + 3 + 4 + 5, k: 5,
- target: 7
  - 1 + 2 + 3 + 4 = 10, delta = 10 - 7 = 3, delta is odd,
    - try k + 1, 1 + 2 + 3 + 4 + 5 = 15, 15 - 7 = 8, delta is even
    - It reaches target, by delta / 2 = 4, switch -1
    - 1 + 2 + 3 - 4 + 5 = 11 - 4 = 7
"""


class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        k = 0
        while target > 0:
            k += 1
            target -= k

        print(f'k: {k}, target: {target}, k + 1: {k + 1}, k % 2: {k % 2}')

        # Below target is delta = sum - target,
        # If it is even, k is the answer by making negative one of the numbers previously
        # If it is odd, k + 1 or k + 2,
        #
        return k if target % 2 == 0 else k + 1 + k % 2


print(f'4')
print(Solution().reachNumber(4))
print()
print(f'7')
print(Solution().reachNumber(7))
print()
