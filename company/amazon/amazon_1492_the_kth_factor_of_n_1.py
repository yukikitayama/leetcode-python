"""
Complexity
- For time, the worst case is when it returns -1 by O(n)
- Space is O(1)
"""


class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        c = 0
        for i in range(1, n + 1):
            if n % i == 0:
                c += 1
                if c == k:
                    return i
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



