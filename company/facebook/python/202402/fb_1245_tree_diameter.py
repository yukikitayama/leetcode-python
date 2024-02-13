"""
Indegee is 0
DFS from all the nodes which have indegree 0

Start from a node which has highest indegree and DFS
"""


class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:

        if not edges:
            return 0

        # Create graph
        graph = collections.defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        # Define BFS
        def bfs(start):

            queue = collections.deque()
            visited = [False] * len(graph)
            queue.append(start)
            visited[start] = True
            distance = -1

            while queue:

                for _ in range(len(queue)):

                    curr_node = queue.popleft()

                    for neighbor in graph[curr_node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)

                distance += 1

            return curr_node, distance

        # First BFS from one random node to find one furthest node and distance
        furthest_node, distance = bfs(0)

        # Second BFS from the last node to find another furthest node and distance
        furthest_node, distance = bfs(furthest_node)

        # Answer is the distance from the second BFS
        return distance
