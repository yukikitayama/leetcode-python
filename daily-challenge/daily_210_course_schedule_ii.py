"""
- Topological sorting
- If there's cycle, return empty array
"""


from typing import List
import collections


class Solution:
    def findOrder(self, numCourses: int, prerequisite: List[List[int]]) -> List[int]:
        adj_list = collections.defaultdict(list)
        in_degree = collections.defaultdict(int)
        for dest, src in prerequisite:
            adj_list[src].append(dest)
            in_degree[dest] += 1

        queue = collections.deque([k for k in range(numCourses) if k not in in_degree])

        ans = []

        while queue:

            curr = queue.popleft()
            ans.append(curr)

            if curr in adj_list:
                for neighbor in adj_list[curr]:
                    in_degree[neighbor] -= 1

                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)

        return ans if len(ans) == numCourses else []


class Solution1:
    WHITE = 1
    GRAY = 2
    BLACK = 3
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = collections.defaultdict(list)

        for dest, src in prerequisites:
            adj_list[src].append(dest)

        topological_sorted_order = []
        is_possible = True

        color = {k: Solution.WHITE for k in range(numCourses)}

        def dfs(node):
            nonlocal is_possible

            if not is_possible:
                return

            color[node] = Solution.GRAY

            if node in adj_list:
                for neighbor in adj_list[node]:
                    if color[neighbor] == Solution.WHITE:
                        dfs(neighbor)
                    # If the currently processed node face a node which is also being processed,
                    # then it means a cycle
                    elif color[neighbor] == Solution.GRAY:
                        is_possible = False

            color[node] = Solution.BLACK
            topological_sorted_order.append(node)

        for vertex in range(numCourses):
            # White means not processed yet
            if color[vertex] == Solution.WHITE:
                dfs(vertex)

        # [::-1] because start of the list contains the courses which require prerequisite courses
        return topological_sorted_order[::-1] if is_possible else []



