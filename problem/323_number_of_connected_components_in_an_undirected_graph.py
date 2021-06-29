class Solution:
    def countComponents(self, n, edges):
        # Initialize
        answer = 0
        # e.g. n = 3, visited = [0, 0, 0] meaning vertex: 0 not visited, vertex: 1 not visited, and vertex: 2 not
        # visited
        visited = [0] * n
        # adjacency_list[i] contains all the adjacent vertices
        adjacency_list = dict()
        for i in range(n):
            adjacency_list[i] = []

        # Fill adjacency list
        for i in range(len(edges)):
            curr_node = edges[i][0]
            neighbor = edges[i][1]
            adjacency_list[curr_node].append(neighbor)
            # Do opposite because we want to track each node
            adjacency_list[neighbor].append(curr_node)

        # print(adjacency_list)

        # Depth first search
        for i in range(n):
            if visited[i] == 0:
                answer += 1
                self.dfs(adjacency_list, visited, i)

        return answer

    def dfs(self, adjacency_list, visited, node):
        # Check we visited node
        visited[node] = 1
        neighbors = adjacency_list[node]

        for i in range(len(neighbors)):
            neighbor = neighbors[i]
            if visited[neighbor] == 0:
                self.dfs(adjacency_list, visited, neighbor)


n_test = 5
# edges_test = [[0, 1], [1, 2], [3, 4]]
edges_test = [[0, 1], [1, 2], [2, 3], [3, 4]]
sol = Solution()
answer = sol.countComponents(n=n_test, edges=edges_test)
print(f'Answer: {answer}')
