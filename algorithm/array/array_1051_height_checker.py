"""
- Make a copy of array and sort
- Iterate two arrays to compare
- Time is O(nlogn) and space is O(N)
- Is there time O(N) solution?
  -
"""


from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = heights[:]
        expected.sort()

        ans = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                ans += 1
        return ans


if __name__ == '__main__':
    heights = [1, 1, 4, 2, 1, 3]
    print(Solution().heightChecker(heights))
