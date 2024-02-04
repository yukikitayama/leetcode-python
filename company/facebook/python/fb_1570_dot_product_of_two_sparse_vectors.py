from typing import List


class SparseVector:
    def __init__(self, nums: List[int]):
        self.i_to_num = {}
        for i in range(len(nums)):
            if nums[i] != 0:
                self.i_to_num[i] = nums[i]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = 0

        for k, v in self.i_to_num.items():

            if k in vec.i_to_num:

                ans += v * vec.i_to_num[k]

        return ans


