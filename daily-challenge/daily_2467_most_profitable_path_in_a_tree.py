"""
Ans
find Bob’s path to node0and then find the best path Alice can take to maximize her collected amount.

"""

from typing import List
import collections


class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:

        adj = collections.defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        bob_node_to_time = dict()
        bob_visited = set()

        def find_bob_path(node, time):
            bob_node_to_time[node] = time
            bob_visited.add(node)

            # Base
            if node == 0:
                return True

            for nei in adj[node]:
                if nei not in bob_visited:
                    if find_bob_path(nei, time + 1):
                        return True

            # Remove nodes which are not in the direct path to 0
            del bob_node_to_time[node]

            return False

        find_bob_path(bob, 0)

        print(bob_node_to_time)
        print(bob_visited)

        ans = float("-inf")
        # [(node, time, income), ...]
        queue = collections.deque([(0, 0, 0)])
        alice_visited = set()
        while queue:

            for _ in range(len(queue)):

                node, time, income = queue.popleft()
                alice_visited.add(node)

                if node not in bob_node_to_time or time < bob_node_to_time[node]:
                    income += amount[node]

                elif time == bob_node_to_time[node]:
                    income += amount[node] // 2

                # Node in adj has only one neighbor, it means it's a leaf
                if len(adj[node]) == 1 and node != 0:
                    ans = max(ans, income)

                for nei in adj[node]:
                    if nei not in alice_visited:
                        queue.append((nei, time + 1, income))

        return ans
