"""
- Divisors are paired
  - if i is a divisor of n, n/i is also a divisor of n
"""


class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        divisors = []
        sqrt_n = int(n**0.5)

        for x in range(1, sqrt_n + 1):
            if n % x == 0:
                k -= 1
                divisors.append(x)
                if k == 0:
                    return x

        # ?
        if sqrt_n * sqrt_n == n:
            k += 1

        n_div = len(divisors)

        if k <= n_div:
            # why -k?
            divisor = divisors[n_div - k]
            return n // divisor
        else:
            return -1


n = 12
k = 3
n = 7
k = 2
n = 4
k = 4
n = 1
k = 1
n = 1000
k = 3
print(Solution().kthFactor(n, k))



