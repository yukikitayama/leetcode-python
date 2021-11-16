"""
- Binary search
"""


class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:

        # enough() is True if there are k or more values in table that are less than or equal to x
        def enough(x):
            count = 0
            for i in range(1, m + 1):
                count += min(x // i, n)

            # print(f'    enough, x: {x}, count: {count}')

            return count >= k

        lo = 1
        hi = m * n
        while lo < hi:
            mi = lo + (hi - lo) // 2

            # print(f'  mi: {mi}, enough(mi): {enough(mi)}, lo: {lo}, hi: {hi}')

            if not enough(mi):
                lo = mi + 1
            else:
                hi = mi

        return lo


"""
- enough() takes O(m)
"""


m = 3
n = 3
k = 5
# m = 2
# n = 3
# k = 6
print(Solution().findKthNumber(m, n, k))

