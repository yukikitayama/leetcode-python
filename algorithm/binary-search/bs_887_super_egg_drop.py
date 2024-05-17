import functools


class Solution:
    def superEggDrop(self, k: int, n: int) -> int:

        @functools.cache
        def dp(k, n):

            if n == 0:
                return 0

            if k == 1:
                return n

            left = 1
            right = n
            while left + 1 < right:

                mid = (left + right) // 2

                # Egg breaks
                t1 = dp(k - 1, mid - 1)

                # Egg doesn't break
                t2 = dp(k, n - mid)

                if t1 < t2:
                    left = mid

                elif t1 > t2:
                    right = mid

                else:
                    left = right = mid

            return 1 + min(
                max(dp(k - 1, x - 1), dp(k, n - x)) for x in (left, right)
            )