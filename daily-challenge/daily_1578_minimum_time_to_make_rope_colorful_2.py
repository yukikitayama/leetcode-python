"""
Find consecutive
Take min
Greedy
"""

from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:

        ans = 0
        left = 0
        right = 0

        while right < len(colors):

            curr_total = 0
            curr_max = 0

            while right < len(colors) and colors[left] == colors[right]:
                curr_total += neededTime[right]
                curr_max = max(curr_max, neededTime[right])
                right += 1

            ans += curr_total - curr_max
            left = right

        return ans


if __name__ == "__main__":
    colors = "aabbbcc"
    neededTime = [1, 2, 3, 4, 5, 6, 7]
    # 14
    print(Solution().minCost(colors, neededTime))
