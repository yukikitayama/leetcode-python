from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        ans[0] = 1

        # From left to right
        for i in range(1, len(nums)):
            ans[i] = ans[i - 1] * nums[i - 1]

        # print(ans)

        # From right to left
        curr = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= curr
            curr *= nums[i]

        # print(ans)

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

        return [p * s for p, s in zip(prefix_products, suffix_products)]