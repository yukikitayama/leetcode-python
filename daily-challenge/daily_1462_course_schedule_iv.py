"""
As we move from node u to node v, we’ll add all of u's prerequisites to v's prerequisites. This is important because it computes the transitive closure, meaning we’re not just tracking immediate dependencies, but also indirect ones.
"""

from typing import List
import collections


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[
        bool]:
        adj = collections.defaultdict(list)
        indegree = [0] * numCourses
        for a, b in prerequisites:
            adj[a].append(b)
            indegree[b] += 1

        queue = collections.deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)

        node_to_prerequisites = collections.defaultdict(set)
        while queue:

            for _ in range(len(queue)):

                node = queue.popleft()

                for next_node in adj[node]:
                    node_to_prerequisites[next_node].add(node)

                    for pre in node_to_prerequisites[node]:
                        node_to_prerequisites[next_node].add(pre)

                    indegree[next_node] -= 1

                    if indegree[next_node] == 0:
                        queue.append(next_node)

        # print(node_to_prerequisites)

        ans = []
        for u, v in queries:
            if u in node_to_prerequisites[v]:
                ans.append(True)
            else:
                ans.append(False)

        return ans