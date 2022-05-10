"""
Time
- We have 9 choices and make it up to K <= 9
- P(9, K) = 9! / (9 - K)!
- To add current path to answer list, coping takes O(K)
- So overall, time takes O(9!/(9 - K)! * K)
"""


from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        ans = []

        def backtracking(prev, curr_sum, path):

            if len(path) == k and curr_sum == n:
                ans.append(path[:])
                return

            if len(path) > k:
                return

            if curr_sum > n:
                return

            for i in range(prev + 1, 10):

                path.append(i)

                backtracking(i, curr_sum + i, path)

                path.pop()

        backtracking(0, 0, [])

        return ans


if __name__ == '__main__':
    k = 3
    n = 7
    k = 3
    n = 9
    print(Solution().combinationSum3(k, n))
