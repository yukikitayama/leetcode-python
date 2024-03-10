"""
Binary search
"""


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    pass


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n

        # l: 4, r: 5, m: 4
        # l: 4, r: 3, break
        while left <= right:

            mid = (left + right) // 2
            res = isBadVersion(mid)

            if res:
                right = mid - 1
            else:
                left = mid + 1

        return left
