"""
- N-ary tree
- Create a graph from edges
- DFS from each node to update answer

- Find the one of the farthest nodes
- From the farthest node, find the farthest node and return the distance
"""


from typing import List
import collections
import pprint


class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:

        if not edges:
            return 0

        graph = collections.defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        # pprint.pprint(graph)

        def bfs(start):
            visited = [False] * len(graph)
            visited[start] = True

            queue = collections.deque([start])
            # -1 because, because we increment distance at the end of for loop
            # there's increment even if queue is empty
            distance = -1
            while queue:

                for _ in range(len(queue)):

                    curr = queue.popleft()

                    for neighbor in graph[curr]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
                            last_node = neighbor

                distance += 1

            return last_node, distance

        farthest_1, distance_1 = bfs(0)

        # print(f'farthest_1: {farthest_1}, distance_1: {distance_1}')

        farthest_2, distance_2 = bfs(farthest_1)

        # print(f'farthest_2: {farthest_2}, distance_2: {distance_2}')

        return distance_2


if __name__ == '__main__':
    edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]
    edges = []
    print(Solution().treeDiameter(edges))
