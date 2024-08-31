"""

"""

from typing import List


class Solution:
    def pathSum(self, nums: List[int]) -> int:

        # Edge case
        if not nums:
            return 0

        coordinate_to_val = {}
        for num in nums:
            coordinate, val = divmod(num, 10)
            coordinate_to_val[coordinate] = val

        def dfs(root_coordinate, pre_sum):
            d, p = divmod(root_coordinate, 10)

            # root d is 1, 2nd level should be 2 = 1 + 1
            # position: 2, left: 3, right: 4 (1-based index)
            left_coordinate = (d + 1) * 10 + p * 2 - 1
            right_coordinate = (d + 1) * 10 + p * 2
            curr_sum = pre_sum + coordinate_to_val[root_coordinate]

            # Leaf
            if left_coordinate not in coordinate_to_val and right_coordinate not in coordinate_to_val:
                return curr_sum

            left_sum = dfs(left_coordinate, curr_sum) if left_coordinate in coordinate_to_val else 0
            right_sum = dfs(right_coordinate, curr_sum) if right_coordinate in coordinate_to_val else 0

            return left_sum + right_sum

        return dfs(nums[0] // 10, 0)