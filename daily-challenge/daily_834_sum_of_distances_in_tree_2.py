class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # print(graph)

        # Number of nodes in ith subtree including itself
        count = [1] * n

        ans = [0] * n

        def dfs(node=0, parent=None):
            for child in graph[node]:

                # Leaf won't process below
                if child != parent:
                    dfs(child, node)

                    # This is happening from the parent view
                    # Aggregating the number of child nodes
                    count[node] += count[child]

                    # If this node has leaves, ans[child] is 0, count[child] is 1
                    # so it's just adding edge counts
                    # Example 1, node: 0, child: 2, 3 + 4 = 7
                    # Example 1, node: 0, child: 1, 0 + 1 = 1
                    # ans[child] to add the number of edges that child has
                    # count[child] to add the additional edges to ans[child] that node needs to reach
                    ans[node] += ans[child] + count[child]

        dfs()

        # print(count)
        # print(ans)

        # This won't update count array any more
        def dfs2(node=0, parent=None):
            for child in graph[node]:
                if child != parent:
                    # Example 1, node: 0, child: 1
                    # (n - cound[child]) adding additional edges of the part of parent subtree that child subtree doesn't belong ot
                    # -count[child] reducing the additional edges we counted in the previous dfs for the edges between child and parent
                    ans[child] = ans[node] - count[child] + (n - count[child])
                    dfs2(child, node)

        dfs2()

        # print(ans)

        return ans