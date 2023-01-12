"""
- Compute parent answer from its child nodes
"""


from typing import List
import collections


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:

        adj = collections.defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(node, parent):

            label = labels[node]
            idx = ord(label) - ord('a')

            node_counts = [0] * 26
            node_counts[idx] = 1

            for child in adj[node]:

                if child == parent:
                    continue

                else:
                    child_counts = dfs(child, node)

                    for i in range(26):
                        node_counts[i] += child_counts[i]

            ans[node] = node_counts[idx]

            return node_counts

        ans = [0] * n

        dfs(0, -1)

        return ans


if __name__ == '__main__':
    n = 5
    edges = [[0,1],[0,2],[1,3],[0,4]]
    labels = "aabab"
    print(Solution().countSubTrees(n, edges, labels))
