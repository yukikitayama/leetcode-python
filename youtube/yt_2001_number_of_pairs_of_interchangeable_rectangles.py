"""
Brute force
  T: O(N**2)

Sorting and hashmap
  T: O(NlogN)
  Hashmap
    k: ratio
    v: first index
"""

from typing import List
import collections


class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ratios = sorted([r[0] / r[1] for r in rectangles])

        # print(ratios)

        ratio_to_first_idx = collections.defaultdict(int)

        ans = 0

        for i in range(len(ratios)):

            if ratios[i] not in ratio_to_first_idx:
                ratio_to_first_idx[ratios[i]] = i
            else:
                curr_num_pair = i - ratio_to_first_idx[ratios[i]]
                ans += curr_num_pair

        return ans

    def interchangeableRectangles1(self, rectangles: List[List[int]]) -> int:
        ans = 0

        for i in range(len(rectangles)):
            for j in range(i + 1, len(rectangles)):
                # print(rectangles[i][0] / rectangles[i][1])
                # print(rectangles[j][0] / rectangles[j][1])
                if rectangles[i][0] / rectangles[i][1] == rectangles[j][0] / rectangles[j][1]:
                    ans += 1

        return ans
