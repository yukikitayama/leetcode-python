"""
topological sort
"""

from typing import List
import collections


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans = []

        adj = collections.defaultdict(list)
        indegree = [0] * numCourses
        for a, b in prerequisites:
            adj[b].append(a)
            indegree[a] += 1

        queue = collections.deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)

        while queue:

            for _ in range(len(queue)):

                curr = queue.popleft()
                ans.append(curr)

                for next_ in adj[curr]:
                    indegree[next_] -= 1
                    if indegree[next_] == 0:
                        queue.append(next_)

        return ans if len(ans) == numCourses else []