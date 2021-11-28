from typing import List
from collections import Counter


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        # print(f'nums: {nums}')
        left = Counter(nums)
        # end[i] counts the number of consecurive subsequences that ends at number i
        end = Counter()
        # print(f'left: {left}')
        # print(f'end: {end}')

        for i in nums:
            # print(f'i: {i}')

            # When we used up the numbers in left, left[i] gives us the value 0
            if not left[i]:
                # print(f'if not with left[i]: {left[i]}')
                continue

            # Because we are currently using i, so decrement the available numbers in nums
            left[i] -= 1

            # When the previous iteration made 3 consecutive subsequence,
            # current iteration with the below if made it one number longer
            if end[i - 1] > 0:
                # It won't end with i - 1 any more, so decrement it
                end[i - 1] -= 1
                # Instead new subsequence ends with i, so increment it
                end[i] += 1
                # print(f'if with end: {end}, left: {left}')

            # There 2 more consecutive numbers to make all subsequences have a length of 3 or more
            elif left[i + 1] and left[i + 2]:
                # Decrement because we just use those numbers
                left[i + 1] -= 1
                left[i + 2] -= 1

                end[i + 2] += 1
                # print(f'elif left: {left}, end: {end}')

            # The current number is still left to be used, but it cannot find 2 numbers which are bigger than
            # the current number by 1 and 2 to make subsequences a length of 3 or more, so return False
            else:
                # print(f'False with left: {left}, end: {end}')
                return False

        return True


"""
Time complexity
Let n be the length of nums. O(n) for for loop

Space complexity
O(n) for two counters
"""


# nums = [1, 2, 3, 3, 4, 5]
# nums = [1,2,3,3,4,4,5,5]
nums = [1,2,3,4,4,5]
print(Solution().isPossible(nums))
