"""
Kahn's algorithm
Adjacency graph
  hashmap
    k: course index
    v: list of next courses
Indegree array
  element: number of prerequite courses for each course
BFS
  queue contains the courses that we can take (because took all prererequites)
  append current courses popped from the queue to the answer array
  we check the next course, and decrement indegree array
    e.g. ex2 course 3 has 2 pre,
  if the current number of pre-courses is 0,
    we can take this course
    append this course to the queue
If the answer array size is equal to the number of courses
  return the answer array
else
  return empty array
T: O(vertex)
S: O(vertex + edge)

graph: [[1, 0], [0, 1]]
indegree: [1, 1]
"""

from typing import List
import collections


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Create graph
        graph = collections.defaultdict(list)
        indegree = [0] * numCourses

        # Traver prerequiste
        for a, b in prerequisites:
            # Add to graph
            graph[b].append(a)
            # Update indegree
            indegree[a] += 1

        # BFS
        queue = collections.deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        ans = []
        while queue:

            curr = queue.popleft()
            ans.append(curr)
            for next_ in graph[curr]:
                indegree[next_] -= 1
                if indegree[next_] == 0:
                    queue.append(next_)

        # Return answer array
        if len(ans) == numCourses:
            return ans
        else:
            return []


