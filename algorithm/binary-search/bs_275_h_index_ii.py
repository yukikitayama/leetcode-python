"""
Binary search
  num citations = length of array - mid + 1 is the number of paper
  citations num at mid >= num citations
    seach left to explore bigger H
  citations num at mid < num citations
    invalid, so search right
"""

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # Edge
        if len(citations) == 1:
            if citations[0] == 0:
                return 0
            else:
                return 1

        left = 0
        right = len(citations) - 1

        while left <= right:
            mid = (left + right) // 2
            num_citation = len(citations) - mid

            # print(f"left: {left}, mid: {mid}, right: {right}, num_citation: {num_citation}")

            # [1, 2, 3]
            if citations[mid] == num_citation:
                return citations[mid]

            elif citations[mid] > num_citation:
                right = mid - 1

            elif citations[mid] < num_citation:
                left = mid + 1

        # print(left, right)

        return len(citations) - left