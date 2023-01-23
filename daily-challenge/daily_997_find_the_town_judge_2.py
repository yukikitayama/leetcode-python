"""
- Town judge has 0 outdegree and n - 1 indegree
"""


from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        if len(trust) < n - 1:
            return -1

        # +1 because index in trust starts with 1, not 0
        outdegree = [0] * (n + 1)
        indegree = [0] * (n + 1)

        for out, in_ in trust:

            outdegree[out] += 1
            indegree[in_] += 1

        for i in range(1, n + 1):

            if outdegree[i] == 0 and indegree[i] == n - 1:
                return i

        return -1


