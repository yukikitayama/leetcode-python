from typing import List


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def can_place(gap):
            num_placed_ball = 0

            prev_position = min(position)
            num_placed_ball += 1

            for i in range(1, len(position)):

                if position[i] - prev_position >= gap:
                    num_placed_ball += 1
                    prev_position = position[i]

            return num_placed_ball >= m

        left = 1
        # e.g. m: 3, 2 partitions are created
        right = max(position) // (m - 1)
        ans = 0

        while left <= right:

            mid = (left + right) // 2

            # print(f"mid: {mid}")

            if can_place(mid):
                ans = max(ans, mid)
                left = mid + 1

            else:
                right = mid - 1

        return ans
