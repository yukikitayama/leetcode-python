"""
- Sort citations in descending order
- if citations[i] > i, papers 0 to i have at least i + 1 citations
- Find the largest i
- If the if condition is False, following papers have citations no more than i + 1
"""


from typing import List


class Solution:
    def hIndex(self, citations: List[int]):
        citations.sort(reverse=True)

        i = 0
        while i < len(citations) and citations[i] > i:
            i += 1
        return i


"""
Complexity
- Time is O(nlogn) for sorting
- Space is O(n) for sorting
"""


citations = [3,0,6,1,5]
citations = [1,3,1]
print(Solution().hIndex(citations))




