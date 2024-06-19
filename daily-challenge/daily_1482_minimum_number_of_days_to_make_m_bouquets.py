from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        def can_make_bouquet(day):
            res = 0
            curr = 0

            for i in range(len(bloomDay)):

                # Check adjescency
                if bloomDay[i] <= day:
                    curr += 1
                else:
                    # Reset
                    curr = 0

                # Check if can make bouquet
                if curr == k:
                    res += 1
                    # Reset
                    curr = 0

            return res >= m

        # print(can_make_bouquet(2))
        # print(can_make_bouquet(3))
        # print(can_make_bouquet(7))
        # print(can_make_bouquet(12))

        left = 0
        right = max(bloomDay)

        ans = -1

        while left <= right:

            mid = (left + right) // 2

            if can_make_bouquet(mid):
                ans = mid
                right = mid - 1

            else:
                left = mid + 1

        return ans