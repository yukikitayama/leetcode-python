"""
create graph from prerequisites
Compute indegree
  start from the course whose indegree is 0
  if not exist, false
BFS
  choose next course from graph
  when take it, reduce the indegree
Return True if indegree array cotains only 0,
  else False

[[1, 0], [2, 1]]

"""

from typing import List
import collections


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        indegrees = [0] * numCourses

        for prerequisite in prerequisites:
            graph[prerequisite[1]].append(prerequisite[0])
            indegrees[prerequisite[0]] += 1

        # print(graph)
        # print(indegrees)

        queue = collections.deque()
        for i in range(len(indegrees)):
            if indegrees[i] == 0:
                queue.append(i)

        num_taken_courses = 0
        while queue:

            for _ in range(len(queue)):

                curr_course = queue.popleft()

                num_taken_courses += 1

                for next_course in graph[curr_course]:
                    indegrees[next_course] -= 1
                    # If indegree is 0, we can take this course,
                    # but if not, we still need to take other courses to clear the prerequisite
                    if indegrees[next_course] == 0:
                        queue.append(next_course)

        return num_taken_courses == numCourses
