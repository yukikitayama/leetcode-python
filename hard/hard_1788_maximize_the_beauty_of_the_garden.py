"""
Two pointers move from edges to center

Ans
  Greedy
"""

from typing import List
import collections


class Solution:
    def maximumBeauty(self, flowers: List[int]) -> int:
        positive_cumsum = []
        prefix_sum = 0

        for i in range(len(flowers)):
            if flowers[i] >= 0:
                prefix_sum += flowers[i]
            positive_cumsum.append(prefix_sum)

        # print(positive_cumsum)

        value_to_indices = collections.defaultdict(list)
        for i in range(len(flowers)):
            value_to_indices[flowers[i]].append(i)

        # print(value_to_indices)

        ans = float("-inf")

        for value, indices in value_to_indices.items():

            # Find leftmost and rightmost flowers
            if len(indices) >= 2:
                left = indices[0]
                right = indices[-1]

                # Leftmost and rightmost flower
                beauty_sum = flowers[left] + flowers[right]

                # Flowers in the middle, no need to add negative beauties
                # nums: [1, 2, 3, 4], cumsum: [1, 3, 6, 10], left: 0, right: 3
                # cumsum[2] - cumsum[0] = 6 - 1 = 5
                beauty_sum += positive_cumsum[right - 1] - positive_cumsum[left]

                ans = max(ans, beauty_sum)

        return ans
