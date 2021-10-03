"""
- Implement BFS because we want the minimum number of steps
- Edges
  - i -> i + 1
  - i -> i - 1
  - i -> j where arr[i] == arr[j]

"""


from typing import List
from collections import defaultdict, deque


class Solution:
    def minJumps(self, arr: List[int]) -> int:

        # Edge case
        if len(arr) == 1:
            return 0

        num_to_index = defaultdict(list)
        for i, num in enumerate(arr):
            num_to_index[num].append(i)

        # Start position
        # Track the indices already visited
        visited = {0}
        # Steps to return representing the minimum steps to the last index
        steps = 0
        # Queue stores (index, steps)
        queue = deque([(0, steps)])

        while len(queue) > 0:

            curr_index, steps = queue.popleft()
            curr_num = arr[curr_index]

            # Return current steps if curr_index is the last index
            if curr_index == len(arr) - 1:
                return steps

            # J jump of arr[i] == arr[j]
            for next_index in num_to_index[curr_num]:
                if next_index not in visited:
                    visited.add(next_index)
                    queue.append((next_index, steps + 1))

            # Reduce time of the above for loop
            num_to_index[curr_num].clear()

            # +1 -1 jumps
            for next_index in [curr_index - 1 , curr_index + 1]:
                # We can go to the next index if that's in the boundary
                # and have not visited
                if 0 <= next_index < len(arr) and next_index not in visited:
                    visited.add(next_index)
                    queue.append((next_index, steps + 1))

        # Otherwise it can't reach
        return -1


arr = [100,-23,-23,404,100,23,23,23,3,404]  # 3
arr = [7]  # 0
arr = [7,6,9,6,9,6,9,7]  # 1
arr = [6,1,9]  # 2
arr = [11,22,7,7,7,7,7,7,7,22,13]  # 3
print(Solution().minJumps(arr))


