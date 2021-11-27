"""
- Since citations is a sorted list, use binary search
"""


from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left = 0
        right = n - 1

        while left <= right:
            mid = left + (right - left) // 2
            if citations[mid] == n - mid:
                return n - mid
            if citations[mid] < n - mid:
                left = mid + 1
            else:
                right = mid - 1

        # ?
        return n - left


citations = [0, 1, 3, 5, 6]
citations = [1,2,100]
print(Solution().hIndex(citations))

