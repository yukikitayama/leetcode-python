"""
- Initialize max_so_far to 0
- Initialize empty list ans
- iterate index and heights enumerate from right to left
  - if current height is bigger than max_so_far, current building can see ocean
  - append current index to ans
    - 0: 3, 1: 2
      - n - i - 1
        - n: 4,
          - i: 0, n - i - 1: 3
          - i: 1, n - i - 1: 2,
  - keep max so far
  -

- It became LeetCode solution Approach 3: Monotonic Stack Space Optimization
"""


from typing import List


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        # List to be returned
        ans = []
        # This is updated if it sees the higher building
        max_so_far = 0
        n = len(heights)

        # e.g. heights: [4, 2, 3, 1]
        # (i: 0, height: 1), (i: 1, height: 3), (i: 2, height: 2), (i: 3, height: 4)
        for i, height in enumerate(heights[::-1]):

            # print(f'i: {i}, height: {height}')

            if height > max_so_far:
                # e.g. n: 4, n - i - 1: (3, 2, 1, 0)
                ans.append(n - i - 1)

            max_so_far = max(max_so_far, height)

        # When it appends index to ans, it started from the end, so index is decreasing order
        # but we are required to return in increasing order
        return ans[::-1]


"""
Complexity
- Time is O(n) for the for loop by letting n be the length of heights
- Space is O(1) because it only uses max_so_far variable to keep data, excluding ans list
"""


heights = [4,2,3,1]
# heights = [4,3,2,1]
# heights = [1,3,2,4]
# heights = [2,2,2,2]
print(Solution().findBuildings(heights))
