from typing import List
import bisect


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []

        for num in nums:

            i = bisect.bisect_left(sub, num)

            # When current num is bigger than the last element in sub
            if i == len(sub):

                # print(f'  num: {num}, i: {i}, len(sub): {len(sub)}')

                sub.append(num)

            # Otherwise i from bisect_left binary search gives us the index where
            # we can insert the current num to replace the number in sub
            else:

                sub[i] = num

            # print(f'    sub: {sub}')

        return len(sub)

"""
Because we append a new number to sub when we find a bigger number,
sub maintains an increasing sorted order. And we try to search a specific num from an array,
the first number in sub which is greater than current number num.
So to find that number, we can use binary search
"""


# nums = [10,9,2,5,3,7,101,18]
nums = [5, 6, 7, 8, 1, 2, 3]
nums = [5, 6, 7, 8, 1, 2, 3, 4, 5]
# nums = [8, 1, 6, 2, 3, 10]
# nums = [3, 4, 5, 1]
print(Solution().lengthOfLIS(nums))

