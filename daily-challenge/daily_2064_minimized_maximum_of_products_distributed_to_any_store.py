from typing import List


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:

        def can_distribute(num):
            right = 0
            remaining = quantities[right]
            for left in range(n):
                if remaining <= num:
                    right += 1
                    if right == len(quantities):
                        return True
                    else:
                        remaining = quantities[right]
                else:
                    remaining -= num
            return False

        left = 0
        right = max(quantities)
        ans = right

        while left <= right:

            mid = (left + right) // 2
            if can_distribute(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans