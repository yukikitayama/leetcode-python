"""
- Backtracking
- current list for answer
- current set for at most once check
"""


from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        def backtracking(remain, comb, next_start):
            if remain == 0 and len(comb) == k:
                ans.append(comb[:])

            # remain < 0 means added too much
            # second condition means that remain is not 0 but we already used k numbers
            elif remain < 0 or len(comb) == k:
                return

            # exclusively end ad 9 because it uses i + 1,
            # so it can include 9
            for i in range(next_start, 9):
                comb.append(i + 1)
                backtracking(remain - (i + 1), comb, i + 1)
                comb.pop()

        backtracking(n, [], 0)

        return ans


if __name__ == '__main__':
    k = 3
    n = 7
    k = 3
    n = 9
    print(Solution().combinationSum3(k, n))
