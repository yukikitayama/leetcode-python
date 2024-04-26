from typing import List
import collections
import heapq


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        def bfs(mid):
            visited = [[False] * len(heights[0]) for _ in range(len(heights))]
            # [(row, col)]
            queue = collections.deque([(0, 0)])
            while queue:
                curr_r, curr_c = queue.popleft()

                if (curr_r, curr_c) == (len(heights) - 1, len(heights[0]) - 1):
                    return True

                visited[curr_r][curr_c] = True

                for offset_r, offset_c in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    next_r = curr_r + offset_r
                    next_c = curr_c + offset_c

                    if 0 <= next_r < len(heights) and 0 <= next_c < len(heights[0]) and not visited[next_r][next_c]:
                        diff = abs(heights[next_r][next_c] - heights[curr_r][curr_c])

                        # If current diff is smaller than or equal to pre-specified mid effort value, we can proceed
                        if diff <= mid:
                            visited[next_r][next_c] = True
                            queue.append((next_r, next_c))

            return False

        left = 0
        right = 10 ** 6
        while left <= right:
            mid = (left + right) // 2

            res = bfs(mid)

            # print(f"mid: {mid}, res: {res}")

            # If we can go, we wanna try smaller effort to find minimum effort
            if res:
                right = mid - 1

            else:
                left = mid + 1

        return left

    def minimumEffortPath1(self, heights: List[List[int]]) -> int:
        efforts = [[float("inf")] * len(heights[0]) for _ in range(len(heights))]
        efforts[0][0] = 0
        visited = [[False] * len(heights[0]) for _ in range(len(heights))]
        # [(diff so far, row, col)]
        queue = [(0, 0, 0)]

        while queue:

            diff, curr_r, curr_c = heapq.heappop(queue)
            visited[curr_r][curr_c] = True

            for offset_r, offset_c in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                next_r = curr_r + offset_r
                next_c = curr_c + offset_c

                if 0 <= next_r < len(heights) and 0 <= next_c < len(heights[0]) and not visited[next_r][next_c]:
                    next_diff = abs(heights[next_r][next_c] - heights[curr_r][curr_c])

                    # We need to track max difference so far, even if current step is smaller
                    max_diff = max(next_diff, efforts[curr_r][curr_c])

                    # If we find another way to have smaller difference so far
                    if max_diff < efforts[next_r][next_c]:
                        efforts[next_r][next_c] = max_diff
                        heapq.heappush(queue, (max_diff, next_r, next_c))

        return efforts[-1][-1]