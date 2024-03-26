# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n

        while left <= right:

            mid = (left + right) // 2

            if isBadVersion(mid):
                right = mid - 1

            # If bad
            else:
                left = mid + 1

        return left
