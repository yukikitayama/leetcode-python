"""
- If cycle, -1
- Topological sorting
  - Kahn's algorithm
"""


from typing import List
import collections


class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        in_degrees = [0] * n

        for prev, next_ in relations:
            graph[prev].append(next_)
            in_degrees[next_ - 1] += 1

        # print(f'graph: {graph}')
        # print(f'in_degrees: {in_degrees}')

        queue = collections.deque()
        for i in range(len(in_degrees)):
            if in_degrees[i] == 0:
                queue.append(i + 1)

        ans = 0
        visited = 0

        # print(f'queue: {queue}')

        while queue:

            ans += 1

            for _ in range(len(queue)):

                curr = queue.popleft()

                visited += 1

                for next_ in graph[curr]:
                    in_degrees[next_ - 1] -= 1
                    if in_degrees[next_ - 1] == 0:
                        queue.append(next_)

        return ans if visited == n else -1


if __name__ == '__main__':
    n = 3
    relations = [[1, 3], [2, 3]]
    n = 3
    relations = [[1, 2], [2, 3], [3, 1]]
    print(Solution().minimumSemesters(n, relations))
