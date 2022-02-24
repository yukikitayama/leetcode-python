from typing import List
import collections


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)

        # max_num = float('-inf')
        # for k, v in counter.items():
        #     if v > max_num:
        #         ans = k
        #         max_num = v
        # return ans

        return max(counter.keys(), key=counter.get)


if __name__ == '__main__':
    nums = [2, 2, 1, 1, 1, 2, 2]
    print(Solution().majorityElement(nums))
