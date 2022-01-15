"""
- BFS or DP
"""


from typing import List
import collections


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) <= 1:
            return 0

        # Key: array value, value: array index
        graph = collections.defaultdict(list)

        for i in range(len(arr)):
            graph[arr[i]].append(i)

        # Queue contains arr index
        queue = collections.deque([0])
        # Visited also contains arr index
        visited = {0}
        step = 0

        while queue:

            for _ in range(len(queue)):

                curr_index = queue.popleft()

                if curr_index == (len(arr) - 1):
                    return step

                for same_value_index in graph[arr[curr_index]]:
                    if same_value_index not in visited:
                        visited.add(same_value_index)
                        queue.append(same_value_index)

                # Since the above already will visit all the same value index,
                # we can remove from the list
                graph[arr[curr_index]].clear()

                for neighbor_index in [curr_index - 1, curr_index + 1]:
                    if 0 <= neighbor_index < len(arr):
                        if neighbor_index not in visited:
                            visited.add(neighbor_index)
                            queue.append(neighbor_index)

            step += 1


if __name__ == '__main__':
    arr = [100, -23, -23, 404, 100, 23, 23, 23, 3, 404]
    # 3
    arr = [7]
    # 0
    arr = [7, 6, 9, 6, 9, 6, 9, 7]
    # 1
    print(Solution().minJumps(arr))
