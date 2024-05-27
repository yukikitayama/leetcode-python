from typing import List
import collections


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        indegrees = [0] * numCourses
        graph = collections.defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)
            indegrees[a] += 1

        # print(graph)
        # print(indegrees)

        # Topological sorting
        ans = []
        # this can omit because graph is uni-directional, no cycle
        # taken = [False] * numCourses
        queue = collections.deque()
        for i in range(len(indegrees)):
            if indegrees[i] == 0:
                queue.append(i)
                ans.append(i)
                # taken[i] = True

        while queue:

            for _ in range(len(queue)):

                curr_course = queue.popleft()

                for next_course in graph[curr_course]:
                    indegrees[next_course] -= 1

                    # if indegrees[next_course] == 0 and not taken[next_course]:
                    if indegrees[next_course] == 0:
                        # taken[next_course] = True
                        queue.append(next_course)
                        ans.append(next_course)

        if len(ans) == numCourses:
            return ans
        else:
            return []
