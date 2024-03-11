"""
Create graph
BFS
  can visit if indegree is 0

If queue is empty before ans length becomes numCourses
  return empty array
"""

from typing import List
import collections


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        ans = []
        indegree = [0] * numCourses

        graph = collections.defaultdict(list)
        for prerequisite in prerequisites:
            graph[prerequisite[1]].append(prerequisite[0])
            indegree[prerequisite[0]] += 1

        print(graph)
        print(indegree)

        queue = collections.deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)

        while queue:

            for _ in range(len(queue)):

                curr = queue.popleft()

                ans.append(curr)

                if len(ans) == numCourses:
                    return ans

                for next_course in graph[curr]:
                    indegree[next_course] -= 1
                    if indegree[next_course] == 0:
                        queue.append(next_course)

        return []
