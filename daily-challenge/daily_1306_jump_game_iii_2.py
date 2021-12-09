from typing import List
import collections


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:

        # Contain index
        queue = collections.deque([start])

        while queue:

            curr = queue.popleft()

            if arr[curr] == 0:
                return True

            if arr[curr] < 0:
                continue

            for next in [curr + arr[curr], curr - arr[curr]]:
                if 0 <= next < len(arr):
                    queue.append(next)

            # Mark as visited
            arr[curr] *= -1

        return False


arr = [4,2,3,0,3,1,2]
start = 5
print(Solution().canReach(arr, start))
