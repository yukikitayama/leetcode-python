from typing import List
import collections


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:

        num1_plus_num2_to_count = collections.defaultdict(int)

        for num1 in nums1:
            for num2 in nums2:
                sum_ = num1 + num2
                num1_plus_num2_to_count[sum_] += 1

        # print(num1_plus_num2_to_count)

        ans = 0
        for num3 in nums3:
            for num4 in nums4:
                sum_ = num3 + num4
                ans += num1_plus_num2_to_count[-sum_]

        return ans


if __name__ == '__main__':
    nums1 = [1, 2]
    nums2 = [-2, -1]
    nums3 = [-1, 2]
    nums4 = [0, 2]
    print(Solution().fourSumCount(nums1, nums2, nums3, nums4))
