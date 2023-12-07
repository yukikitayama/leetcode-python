"""
1, 2, 3, ... 7
2, 3, 4, ... 8
3
"""


class Solution:
    def totalMoney(self, n: int) -> int:

        ans = 0
        monday = 1

        while n > 0:
            for day in range(min(n, 7)):
                ans += monday + day

            n -= 7
            monday += 1

        return ans


if __name__ == "__main__":
    n = 4
    print(Solution().totalMoney(n))
