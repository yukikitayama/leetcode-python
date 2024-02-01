"""
sort
iterate
  curr - prev <= k
  if not
    break and return []
"""

from typing import List


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:

        if len(nums) < 3:
            return []

        nums.sort()

        ans = []
        curr_list = []
        min_so_far = float("inf")

        for i in range(len(nums)):

            if not curr_list:
                curr_list.append(nums[i])
                min_so_far = nums[i]

            elif len(curr_list) <= 2:

                if nums[i] - min_so_far <= k:

                    curr_list.append(nums[i])
                    min_so_far = min(min_so_far, nums[i])

                    if len(curr_list) == 3:
                        ans.append(curr_list)
                        curr_list = []

                else:
                    return []

            # print(i, curr_list, ans)

        return ans


if __name__ == "__main__":
    nums = [1, 3, 4, 8, 7, 9, 3, 5, 1]
    k = 2

    nums = [1, 3, 3, 2, 7, 3]
    k = 3

    nums = [15,13,12,13,12,14,12,2,3,13,12,14,14,13,5,12,12,2,13,2,2]
    k = 2
    # []

    print(Solution().divideArray(nums, k))
