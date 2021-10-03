from typing import List
from collections import deque


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = deque([start])

        while len(queue) != 0:
            curr_index = queue.popleft()

            # print(curr_index)
            if arr[curr_index] == 0:
                return True

            # Skip if we already visited this index
            if arr[curr_index] < 0:
                continue

            # Append go to left index if possible
            if curr_index - arr[curr_index] >= 0:
                next_index = curr_index - arr[curr_index]
                queue.append(next_index)

            # Append go to right index if possible
            if curr_index + arr[curr_index] < len(arr):
                next_index = curr_index + arr[curr_index]
                print(next_index)
                queue.append(next_index)

            # Mark current index as visited
            arr[curr_index] *= -1

        return False


arr = [4, 2, 3, 0, 3, 1, 2]
start = 5
arr = [3,0,2,1,2]
start = 2
print(Solution().canReach(arr, start))

