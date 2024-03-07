from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]
        for i in range(len(nums) - 1):
            ans.append(ans[-1] * nums[i])

        r = 1

        for i in range(len(ans) - 1, -1, -1):
            ans[i] *= r
            r *= nums[i]

        return ans

    def productExceptSelf1(self, nums: List[int]) -> List[int]:
        prefix_products = [1]
        for i in range(len(nums) - 1):
            prefix_products.append(prefix_products[-1] * nums[i])

        suffix_products = [1]
        for i in range(len(nums) - 1, 0, -1):
            suffix_products.append(suffix_products[-1] * nums[i])
        suffix_products.reverse()

        # print(prefix_products)
        # print(suffix_products)

        ans = []

        for i in range(len(prefix_products)):
            ans.append(prefix_products[i] * suffix_products[i])

        return ans
