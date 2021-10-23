from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        # first is the current starting index to make permutation
        def backtrack(first=0):

            # When first is n, it finished all the indices to make permutation
            if first == n:

                print(f'append nums: {nums} to output')

                output.append(nums[:])

            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]

                # Go to the next index
                backtrack(first + 1)

                # Backtrack by recovering the previous array state
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        output = []
        backtrack()
        return output


nums = [1, 20, 300]
print(Solution().permute(nums))

