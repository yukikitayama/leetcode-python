


class Solution:
    def checkPowersOfThree(self, n: int) -> bool:

        def recursion(p, num):

            if num == 0:
                return True

            if 3 ** p > num:
                return False

            # Include
            include = recursion(p + 1, num - 3 ** p)

            # Skip
            skip = recursion(p + 1, num)

            return include or skip

        return recursion(0, n)