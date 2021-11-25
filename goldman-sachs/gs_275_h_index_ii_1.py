"""
- iterate from the end
"""


from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h = 0
        for i, citation in enumerate(citations[::-1]):
            # print(f'i: {i}, citation: {citation}')
            if citation > i:
                h += 1

        return h


citations = [0, 1, 3, 5, 6]
citations = [1,2,100]
print(Solution().hIndex(citations))

