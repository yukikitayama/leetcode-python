from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        ans = []

        def backtracking(i, curr):

            if len(curr) == k:
                ans.append(curr[:])

            for num in range(i, n + 1):
                curr.append(num)
                backtracking(num + 1, curr)
                curr.pop()

        backtracking(1, [])

        return ans


if __name__ == '__main__':
    print(Solution().combine(4, 2))
