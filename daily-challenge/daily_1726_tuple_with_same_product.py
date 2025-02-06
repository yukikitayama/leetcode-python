from typing import List


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        pair_products = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                pair_products.append(nums[i] * nums[j])
        pair_products.sort()

        # ?
        last_product_seen = -1
        same_product_count = 0
        ans = 0

        for i in range(len(pair_products)):
            if pair_products[i] == last_product_seen:
                same_product_count += 1

            else:
                # e.g., same_product_count: 2, should be 1
                # same_product_count: 3, should be 2
                # 4, (4 - 1) * 4 // 2 = 3 * 2 = 6
                pairs_of_equal_product = (same_product_count - 1) * same_product_count // 2
                ans += 8 * pairs_of_equal_product
                last_product_seen = pair_products[i]
                same_product_count = 1

        # Remaining
        pairs_of_equal_product = (same_product_count - 1) * same_product_count // 2
        ans += 8 * pairs_of_equal_product

        return ans

    def tupleSameProduct1(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0

        # From left
        for a in range(len(nums)):

            # From right
            for b in range(len(nums) - 1, a, -1):

                product = nums[a] * nums[b]

                possible_d_values = set()

                # From left, but excluding a and b
                for c in range(a + 1, b):

                    if product % nums[c] == 0:

                        d_value = product // nums[c]

                        if d_value in possible_d_values:
                            ans += 8

                        possible_d_values.add(nums[c])

        return ans