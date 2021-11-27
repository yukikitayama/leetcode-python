class Solution:
    def myPow(self, x: float, n: int) -> float:

        # When n: 0, return 1.0, then next recursion will return x because 1 * 1 * x
        # by half being 1.0
        def fast_pow(x, n):
            if n == 0:
                return 1.0
            half = fast_pow(x, n // 2)
            if n % 2 == 0:
                return half * half
            # When n is even, one multiplication is missing so add it
            else:
                return half * half * x

        if n < 0:
            x = 1/x
            n = -n

        return fast_pow(x, n)


"""
- 2^4 = 16
  - 2 * 2 * 2 * 2, O(4)
  - 2 * 2: 4, 4 * 4 = 16, O(2)
  - Reduce Time O(n) to O(logn), because reduce by half
  
x: 2, n: 4, ans: 16
fast_pow(2, 4)
  x: 2, n: 4, fast_pow(x, 2)
    x: 2, n: 2, fast_pow(x, 1)
      x: 2, n: 1, fast_pow(x, 0)
        x: 2, n: 0, return 1
      half: 1, if: F, return half * half * x: 1 * 1 * 2 = 2
    half: 2, if: T, return half * half: 4, 
  half: 4, if: T, return half * half: 16
return 16
"""


x = 2.00000
n = 10
# x = 2.10000
# n = 3
# x = 2.00000
# n = -2
x = 2
n = 4
print(Solution().myPow(x, n))

