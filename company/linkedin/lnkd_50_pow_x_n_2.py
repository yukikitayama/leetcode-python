"""
- 2^4
  - With linear approach, 2 * 2 * 2 * 2, takes O(3)
  - With optimized approach,
    - O(1) to get 2 ^ 2 = 2 * 2 = 4
    - another O(1) to get the 4 * the 4 = 16
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:

        def fast_pow(x, n):

            print(f'fast_pow({x}, {n})')

            if n == 0:

                print(f'  return 1.0')

                return 1.0

            # n // 2 will be 1 when n == 2
            # When n == 1, fast_pow(x, 0): 1, half: 1,
            # n % 2 != 0, 1 * 1 * x = x
            # When n == 2, fast_pow(x, 1): x,
            # n % 2 == 0, return x * x
            half = fast_pow(x, n // 2)
            if n % 2 == 0:

                print(f'  return half * half = {half * half}')

                return half * half
            else:

                print(f'  return half * half * x = {half * half * x}')

                return half * half * x

        if n < 0:
            x = 1 / x
            n = -n

        return fast_pow(x, n)


"""
Test
x = 2, n = 4
fast_pow(2, 4), 
  x: 2, n: 4, if1: F, half: fast_pow(2, 2),
    x: 2, n: 2, if1: F, half: fast_pow(2, 1),
      x: 2, n: 1, if1: F, half: fast_pow(2, 0)
        x: 2, n: 0, if1: T, return 1
      half: 1, n % 2: 1 % 2 = 1, if2: F, half * half * x: 1 * 1 * 2 = 2, return 2
    half: 2, n % 2: 2 % 2 = 0, if2: T, half * half: 4, return 4
  half: 4, n % 2: 4 % 2 = 0, if2: T, half * half: 16, return 16
return 16 

"""
x = 2.00000
n = 10
# x = 2.10000
# n = 3
# x = 2.00000
# n = -2
# x = 10
# n = 0
x = 2
n = 4
print(Solution().myPow(x, n))
