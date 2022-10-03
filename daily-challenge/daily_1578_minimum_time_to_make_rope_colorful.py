"""
- dp
"""


from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        left = right = 0

        ans = 0

        while left < len(neededTime) and right < len(neededTime):
            curr_total = 0
            curr_max = 0

            while right < len(neededTime) and colors[left] == colors[right]:
                curr_total += neededTime[right]
                curr_max = max(curr_max, neededTime[right])
                right += 1

            # Here different color
            ans += curr_total - curr_max
            left = right

        return ans


if __name__ == '__main__':
    pass
