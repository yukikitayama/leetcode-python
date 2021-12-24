"""
- Topological sorting
- BFS
"""


from typing import List
import collections
import pprint


class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adj_list = {i: [] for i in range(1, n + 1)}
        in_degrees = {i: 0 for i in range(1, n + 1)}
        for relation in relations:
            adj_list[relation[0]].append(relation[1])
            in_degrees[relation[1]] += 1

        # pprint.pprint(adj_list)
        # print(in_degrees)

        queue = collections.deque()
        for i in adj_list:
            if in_degrees[i] == 0:
                queue.append(i)

        # print(queue)

        semester = 0
        num_class_taken = 0

        while queue:

            semester += 1

            for _ in range(len(queue)):

                curr = queue.popleft()
                num_class_taken += 1

                end_nodes = adj_list[curr]

                for end_node in end_nodes:
                    in_degrees[end_node] -= 1
                    if in_degrees[end_node] == 0:
                        queue.append(end_node)

        return semester if num_class_taken == n else -1


n = 3
relations = [[1,3],[2,3]]
print(Solution().minimumSemesters(n, relations))

