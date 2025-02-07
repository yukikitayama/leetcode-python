"""
if indegee is 0
  take course
boolean array to track courses
"""

from typing import List
import collections


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = collections.defaultdict(list)
        indegrees = [0] * numCourses
        for a, b in prerequisites:
            indegrees[a] += 1
            adj[b].append(a)

        print(indegrees)

        queue = collections.deque()
        for i in range(len(indegrees)):
            if indegrees[i] == 0:
                queue.append(i)

        courses_taken = [False] * numCourses
        while queue:

            for _ in range(len(queue)):

                curr = queue.popleft()
                courses_taken[curr] = True

                for next_ in adj[curr]:
                    indegrees[next_] -= 1
                    if indegrees[next_] == 0:
                        queue.append(next_)

        return sum(courses_taken) == numCourses
