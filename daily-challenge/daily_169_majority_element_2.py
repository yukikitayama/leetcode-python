"""
naive
  counter
  max value

return num key with the max valu
T: O(N)
"""


class Solution:
    # def majorityElement(self, nums: List[int]) -> int:
    #     counter = collections.Counter(nums)
    #     max_value = max(counter.values())
    #     for k, v in counter.items():
    #         if counter[k] == max_value:
    #             return k

    def majorityElement(self, nums: List[int]) -> int:
        """Boyer-Moore voting algorithm"""
        count = 0
        candidate = None

        for i in range(len(nums)):
            if count == 0:
                candidate = nums[i]

            if nums[i] == candidate:
                count += 1
            else:
                count -= 1

        return candidate

