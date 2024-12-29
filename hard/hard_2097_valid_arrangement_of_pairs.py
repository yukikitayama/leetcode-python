from typing import List
import collections


class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:

        graph = collections.defaultdict(collections.deque)
        in_degree = collections.Counter()
        out_degree = collections.Counter()

        for start, end in pairs:
            graph[start].append(end)
            out_degree[start] += 1
            in_degree[end] += 1

        ans = []

        def dfs(node):
            while graph[node]:
                next_node = graph[node].popleft()
                dfs(next_node)
            # Append root at the end, because of Postorder traversal
            ans.append(node)

        # Find start node
        start_node = -1
        for node in out_degree:
            if out_degree[node] == in_degree[node] + 1:
                start_node = node
                break
        if start_node == -1:
            start_node = pairs[0][0]

        dfs(start_node)

        # This creates [11, 9, 4, 5, 1]
        ans.reverse()

        # print(ans)

        # This creates [[11, 9], [9, 4], [4, 5], [5, 1]]
        ans = [[ans[i - 1], ans[i]] for i in range(1, len(ans))]

        # print(ans)

        return ans
