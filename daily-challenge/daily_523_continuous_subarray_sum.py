"""
- two pointers sliding window
"""


from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_to_index = {0: 0}
        cumsum = 0

        for i in range(len(nums)):

            cumsum += nums[i]

            remainder = cumsum % k

            # print(f'i: {i}, remainder: {remainder}, remainder_to_index: {remainder_to_index}')

            if remainder not in remainder_to_index:
                # +1 because cumsum started with 0, which was index 0
                # so we need to start with index 1
                remainder_to_index[remainder] = i + 1
            elif remainder in remainder_to_index:
                if remainder_to_index[remainder] < i:
                    return True

        return False


if __name__ == '__main__':
    nums = [23, 2, 4, 6, 7]
    k = 6
    print(Solution().checkSubarraySum(nums, k))
