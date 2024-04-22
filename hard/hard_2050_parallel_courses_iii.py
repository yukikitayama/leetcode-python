"""
Indegree array
  if indegree is 0
    you can take this course
BFS

"""

from typing import List
import collections


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = collections.defaultdict(list)
        indegree = [0] * n
        for prev, next_ in relations:
            graph[prev].append(next_)
            indegree[next_ - 1] += 1


        queue = collections.deque()
        total_time = [0] * n
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i + 1)
                total_time[i] = time[i]

        # print(graph)
        # print("indegree", indegree)
        # print("queue", queue)
        # print("total_time", total_time)

        while queue:

            curr_time = 0

            for _ in range(len(queue)):

                node = queue.popleft()

                for neighbor in graph[node]:
                    indegree[neighbor - 1] -= 1

                    # Find the max time of finishing current course and next course
                    total_time[neighbor - 1] = max(
                        total_time[neighbor - 1],
                        total_time[node - 1] + time[neighbor - 1]
                    )

                    if indegree[neighbor - 1] == 0:
                        queue.append(neighbor)

            # print(f"total_time: {total_time}, indegree: {indegree}, queue: {queue}")

        # print(indegree)

        return max(total_time)
