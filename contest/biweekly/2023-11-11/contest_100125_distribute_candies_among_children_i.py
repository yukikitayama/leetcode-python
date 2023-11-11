"""
Backtracking
"""


class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:

        ans = 0

        def backtracking(candies, curr):

            nonlocal ans

            if len(candies) == 3 and curr == 0:
                # print(candies)
                ans += 1
                return

            if len(candies) >= 3 and curr != 0:
                return

            for i in range(limit + 1):

                candies.append(i)
                backtracking(candies, curr - i)
                candies.pop()

        backtracking([], n)

        return ans


if __name__ == "__main__":
    n = 5
    limit = 2

    n = 3
    limit = 3

    print(Solution().distributeCandies(n, limit))
