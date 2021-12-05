from typing import List
import collections


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Edge cases
        # If there's no prerequisites, whatever order is fine to complete numCourses courses
        # so just return numerical order
        if not prerequisites:
            return [i for i in range(numCourses)]

        # Calculate in-degree of each vertex
        # It will be decremented when it find the dependent node
        in_degree = [0] * numCourses
        for prerequisite in prerequisites:
            in_degree[prerequisite[0]] += 1

        # Find starting vertices which have in-degree 0
        queue = collections.deque()
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                queue.append(i)

        # If it cannot find a vertex with in-degree 0,
        # the graph has a cycle. In cyclic graph, it's impossible to return a valid answer
        if not queue:
            return []

        # ans contains a valid any-order course numbers
        ans = [0] * numCourses
        # It will increment the index to fill a current course to the answer list
        i = 0
        while queue:
            course = queue.popleft()
            ans[i] = course
            i += 1
            for prerequisite in prerequisites:
                # If it finds the dependent node, decrement in-degree
                # and if it becomes in-degree 0, it can enter the queue
                if prerequisite[1] == course:
                    in_degree[prerequisite[0]] -= 1
                    if in_degree[prerequisite[0]] == 0:
                        queue.append(prerequisite[0])

        # We could have a course which has prerequisites,
        # but the prerequisite courses do not exist in the graph
        if any(i for i in in_degree):
            return []
        else:
            return ans



