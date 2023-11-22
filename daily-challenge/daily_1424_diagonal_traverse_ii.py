from typing import List
import collections


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:

        group_id_to_nums = collections.defaultdict(list)

        for r in range(len(nums) - 1, -1, -1):

            row = nums[r]

            for c in range(len(row)):

                group_id = r + c
                group_id_to_nums[group_id].append(nums[r][c])

        ans = []
        curr_id = 0

        while curr_id in group_id_to_nums:
            ans.extend(group_id_to_nums[curr_id])
            curr_id += 1

        return ans


if __name__ == "__main__":
    nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(Solution().findDiagonalOrder(nums))
