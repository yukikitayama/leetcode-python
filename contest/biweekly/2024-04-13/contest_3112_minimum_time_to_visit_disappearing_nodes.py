"""
Create graph
  k: node number
  v: list of list [neighbot node num, length]
BFS with min heap
  min heap initialized with [(0, 0)], (cumulative time, node num)
  answer array initilized with n length [-1]
  while min heap
    for current min heap
      if cumulative time is <= disappear of current node
        update answer array with the cumulative time
        for each neighbor
          append (time + neighbor left, neighbor node num) to min heap
      else
        stop further iteration


Input:  n = 3, edges = [[0,1,2],[1,2,1],[0,2,4]], disappear = [1,1,5]
graph
  0: [[1, 2], [2, 4]]
Output:  [0,-1,4]
"""

from typing import List
import collections
import heapq


class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        graph = collections.defaultdict(list)
        for u, v, length in edges:
            graph[u].append([v, length])
            graph[v].append([u, length])

        # print(graph)

        min_heap = []
        heapq.heappush(min_heap, (0, 0))
        ans = [-1] * n

        while min_heap:

            for _ in range(len(min_heap)):

                cum_time, node = heapq.heappop(min_heap)

                if (
                        (node == 0 and ans[node] == -1)
                        or (ans[node] == -1 and cum_time < disappear[node])
                ):
                    ans[node] = cum_time

                    for neighbor, length in graph[node]:
                        heapq.heappush(min_heap, (cum_time + length, neighbor))

        return ans



