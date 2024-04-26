"""
2
4
16
1 + 36 = 37
3**2 + 7**2 = 9 + 49 = 58
5**2 + 8**2 = 25 + 64 = 89
8**2 + 9**2 = 64 + 81 =
...

..

37
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        nums = set()

        curr_sum = n

        while curr_sum != 1:

            digits = list(str(curr_sum))

            curr_sum = 0

            for d in digits:
                curr_sum += int(d) ** 2

            # Cycle
            if curr_sum in nums:
                return False

            else:
                nums.add(curr_sum)

        return True
