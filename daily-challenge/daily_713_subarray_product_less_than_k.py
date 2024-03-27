"""
[10,5,2,6]
Prefix products
[10, 50, 100, 600]
  current prefix product divided by previous prefix product gives the subarray products
  e.g. To get subarray product [5, 2], current prefix prodcut 100 divided by prefix_products[0]
[1, 10, 50, 100, 600]

For each current index
  compute current prefix product
  for each previous index,
    divide current prefix product by the previous index prefix product
    if smaller than k,
      increment answer

right - left + 1
  The number of subarrays which ends at right and starts >= left
  [0, 1, 2, 3]
"""

from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        product = 1
        left = 0
        ans = 0
        for right in range(len(nums)):
            product *= nums[right]

            while left <= right and product >= k:
                product //= nums[left]
                left += 1

            ans += right - left + 1

        return ans

    def numSubarrayProductLessThanK1(self, nums: List[int], k: int) -> int:
        prefix_products = [1]
        for i in range(len(nums)):
            prefix_products.append(prefix_products[-1] * nums[i])

        # print(prefix_products)

        curr_product = 1
        ans = 0

        for i in range(len(nums)):
            curr_product *= nums[i]

            for j in range(0, i + 1):

                if curr_product // prefix_products[j] < k:
                    ans += 1

        return ans
