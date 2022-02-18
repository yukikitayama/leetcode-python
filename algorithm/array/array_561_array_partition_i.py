from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # Step: 2, from 0 to end
        return sum(sorted(nums)[::2])


if __name__ == '__main__':
    nums = [1, 4, 3, 2]
    print(Solution().arrayPairSum(nums))
