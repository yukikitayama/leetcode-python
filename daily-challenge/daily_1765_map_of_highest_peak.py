from typing import List
import collections


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:

        ans = [[-1] * len(isWater[0]) for _ in range(len(isWater))]

        # [(row, col), ...]
        queue = collections.deque()
        for r in range(len(isWater)):
            for c in range(len(isWater[0])):
                if isWater[r][c] == 1:
                    queue.append((r, c))
                    ans[r][c] = 0

        curr_height = 1
        while queue:

            for _ in range(len(queue)):
                curr_r, curr_c = queue.popleft()

                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    next_r = curr_r + dr
                    next_c = curr_c + dc

                    if 0 <= next_r < len(isWater) and 0 <= next_c < len(isWater[0]):
                        if ans[next_r][next_c] == -1:
                            ans[next_r][next_c] = curr_height
                            queue.append((next_r, next_c))

            curr_height += 1

        return ans
