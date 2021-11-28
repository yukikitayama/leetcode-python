from typing import List
from collections import defaultdict
import pprint


class Solution:
    def __init__(self):
        self.WHITE = 1  # No visited
        self.GRAY = 2  # During recursion
        self.BLACK = 3  # Recursion finished

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Key: prerequisite, value: a list of next courses
        adj_list = defaultdict(list)
        for dest, src in prerequisites:
            adj_list[src].append(dest)

        topological_sorted_order = []
        is_possible = True
        # color is a dictionary Key: course integer, Value: color
        color = {k: self.WHITE for k in range(numCourses)}
        # pprint.pprint(color)
        def dfs(node):
            nonlocal is_possible

            # Avoid cycle
            if not is_possible:
                return

            color[node] = self.GRAY

            # node in adj_list dictionary key set
            if node in adj_list:
                for neighbor in adj_list[node]:
                    # If not visited yet, dfs
                    if color[neighbor] == self.WHITE:
                        dfs(neighbor)
                    # If already visited but visited now again, it's cycle
                    elif color[neighbor] == self.GRAY:
                        # Even if it's impossible graph, keep doing dfs
                        # But at return statement, if is_possible is marked as False,
                        # return empty list
                        is_possible = False

            color[node] = self.BLACK
            # Final courses at the beginning of the list,
            # And prerequisite courses at the end of the list
            # So need to reverse at the end
            topological_sorted_order.append(node)

        # Start DFS
        for vertex in range(numCourses):
            if color[vertex] == self.WHITE:
                dfs(vertex)

        return topological_sorted_order[::-1] if is_possible else []


"""
Time complexity
Let E the number of edges and V the number of vertices. 
Making adjacency list takes V(E), and dfs takes V(V), so O(E + V)

Space complexity
Adjacency list takes O(V) to store all nodes
Each node contains edge list, so it takes O(E)
We have stack of nodes in DFS, so O(V)
O(V + E + V) = O(2V + E) = O(V + E)
"""


numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print(Solution().findOrder(numCourses, prerequisites))
