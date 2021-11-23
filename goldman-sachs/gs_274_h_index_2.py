"""
"""


from typing import List


class Solution:
    def hIndex(self, citations: List[int]):
        n = len(citations)
        # + 1 for 0 citation
        papers = [0] * (n + 1)
        for citation in citations:
            # Count
            papers[min(n, citation)] += 1

        # print(f'papers: {papers}')

        k = n
        s = papers[n]
        while s < k:

            # print(f'  k: {k}, papers[k]: {papers[k]}, s: {s}')

            k -= 1
            s += papers[k]

            # print(f'    k: {k}, papers[k]: {papers[k]}, s: {s}')

        return k


"""
Complexity
- Time is O(n)
- Space is O(n)
"""


citations = [3,0,6,1,5]  # 3
# citations = [1,3,1]  # 1
# citations = [1, 3, 2, 3, 100]  # 3
print(Solution().hIndex(citations))




