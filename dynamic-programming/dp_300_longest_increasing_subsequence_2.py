from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # print(f'nums: {nums}')

        # Base case
        sub = [nums[0]]

        for num in nums[1:]:

            # print(f'num: {num}')

            # If current number is bigger than recorded number, safe to create increasing subsequence
            # so just append it
            # sub maitains the list in an increasing order
            if num > sub[-1]:
                sub.append(num)

            else:
                # Sub maintains the increasing order, so once the current number is smaller than
                # a number in sub, it replaces the smallest in sub with current number.
                # Find the first element is sub that is greater than or equal to current num
                i = 0
                # print(f'    num: {num}, i: {i}, sub[i]: {sub[i]}')
                while num > sub[i]:
                    i += 1
                    # print(f'    num: {num}, i: {i}, sub[i]: {sub[i]}')

                # Replace the currently bigger number in sub with the newly found smaller number
                # to possibly make a longer increasing subsequence in the following iteration
                sub[i] = num

            # print(f'  sub: {sub}')

        # sub itself is not subsequence, but the length is correct
        return len(sub)


"""
"""


# nums = [10,9,2,5,3,7,101,18]
nums = [5, 6, 7, 8, 1, 2, 3]
# nums = [8, 1, 6, 2, 3, 10]
# nums = [3, 4, 5, 1]
print(Solution().lengthOfLIS(nums))

