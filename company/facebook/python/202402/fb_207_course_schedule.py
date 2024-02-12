"""
compute inorder degree of each course

complete_course boolean array
  True for inorder degree 0 course

DFS from course with inorder degree 0
  When you visit a course, mark complete course array to be True
If not
  return false

Edge case
  [2, 1], [2, 0]

Answer
  If there is a cycle in graph, not be able to finish all courses
"""

from typing import List
import collections


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        graph = collections.defaultdict(list)

        for prerequisite in prerequisites:
            after_ = prerequisite[0]
            before_ = prerequisite[1]
            indegree[after_] += 1
            graph[before_].append(after_)

        queue = collections.deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)

        visited_count = 0

        while queue:

            curr = queue.popleft()
            visited_count += 1

            for neighbor in graph[curr]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # print(indegree)
        # print(visited_count)

        return visited_count == numCourses



