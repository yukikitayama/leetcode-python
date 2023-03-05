from typing import List
import collections


class Solution:
    def minJumps(self, arr: List[int]) -> int:

        n = len(arr)

        if n <= 1:
            return 0

        graph = collections.defaultdict(list)
        for i in range(n):
            graph[arr[i]].append(i)

        queue = collections.deque([0])
        visited = {0}
        ans = 0

        while queue:

            for _ in range(len(queue)):

                curr = queue.popleft()

                if curr == n - 1:
                    return ans

                for next_ in graph[arr[curr]]:
                    if next_ not in visited:
                        visited.add(next)
                        queue.append(next_)

                # Make the list empty
                graph[arr[curr]].clear()

                for next_ in [curr - 1, curr + 1]:
                    if 0 <= next_ < n and next_ not in visited:
                        visited.add(next_)
                        queue.append(next_)

            ans += 1

        return -1


