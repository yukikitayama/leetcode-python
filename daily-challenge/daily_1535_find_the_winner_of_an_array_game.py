from typing import List
import collections


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:

        max_num = max(arr)
        streak = 0
        queue = collections.deque(arr[1:])
        curr = arr[0]

        while True:

            opponent = queue.popleft()

            if curr > opponent:
                queue.append(opponent)
                streak += 1
            else:
                queue.append(curr)
                curr = opponent
                streak = 1

            if streak == k or curr == max_num:
                return curr


class Solution2:
    def getWinner(self, arr: List[int], k: int) -> int:
        max_num = max(arr)
        curr = arr[0]
        streak = 0

        for i in range(1, len(arr)):

            op = arr[i]

            if curr > op:
                streak += 1

            else:
                curr = op
                streak = 1

            if streak == k or curr == max_num:
                return curr

