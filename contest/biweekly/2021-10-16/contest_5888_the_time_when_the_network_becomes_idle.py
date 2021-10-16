"""
- Find the shortest path from each data server to master server 0
- 2 * the length of the shortest path is the time the first message spends
- if patience[i] < 2 * the length, total time for idle is 2 * the length + (2 * length) / patience[i]
"""


from typing import List
import collections
import pprint


class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        graph = collections.defaultdict(list)
        for i in range(len(edges)):
            graph[edges[i][0]].append(edges[i][1])
            graph[edges[i][1]].append(edges[i][0])

        pprint.pprint(graph)

        steps = [0] * len(patience)

        for i in range(1, len(patience)):

            queue = collections.deque([(i, 0)])
            steps[i] = 2 * self.bfs(graph, queue)

        print(f'steps: {steps}')

        extras = [0] * len(patience)

        for i in range(1, len(patience)):

            if patience[i] < steps[i]:
                extras[i] = steps[i] // patience[i]

        print(f'extras: {extras}')

        ans = 0
        for i in range(1, len(patience)):
            if extras[i] == 0:
                ans = max(ans, steps[i] + 1)
            elif extras[i] != 0:
                ans = max(ans, steps[i] + extras[i])

        return ans

    def bfs(self, graph, queue):

        while queue:

            curr_node, steps = queue.popleft()

            if curr_node == 0:
                return steps

            for neighbors in graph[curr_node]:
                queue.append((neighbors, steps + 1))


edges = [[0,1],[1,2]]
patience = [0,2,1]
# edges = [[0,1],[0,2],[1,2]]
# patience = [0,10,10]
edges = [[5,7],[15,18],[12,6],[5,1],[11,17],[3,9],[6,11],[14,7],[19,13],[13,3],[4,12],[9,15],[2,10],[18,4],[5,14],[17,5],[16,2],[7,1],[0,16],[10,19],[1,8]]
patience = [0,2,1,1,1,2,2,2,2,1,1,1,2,1,1,1,1,2,1,1]
# Memory Limit Exceeded
print(Solution().networkBecomesIdle(edges, patience))
