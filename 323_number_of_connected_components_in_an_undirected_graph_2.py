class Solution:
    def countComponents(self, n, edges):
        answer = 0
        visit = [0] * n
        adjacency_list = {}

        for i in range(n):
            adjacency_list[i] = []

        for i in range(len(edges)):
            a, b = edges[i]
            adjacency_list[a].append(b)
            adjacency_list[b].append(a)

        print(adjacency_list)

        for i in range(len(visit)):
            if visit[i] == 0:
                self.dfs(visit, adjacency_list, i)
                answer += 1

        return answer

    def dfs(self, visit, adjacency_list, vertex):
        visit[vertex] = 1
        # List
        neighbors = adjacency_list[vertex]

        for neighbor in neighbors:
            if visit[neighbor] == 0:
                self.dfs(visit, adjacency_list, neighbor)


n_test = 5
# edges_test = [[0,1],[1,2],[3,4]]
edges_test = [[0,1],[1,2],[2,3],[3,4]]
sol = Solution()
answer = sol.countComponents(n=n_test, edges=edges_test)
print(f'Answer: {answer}')