"""
simulation
"""

class Solution:
    def countArrangement(self, n: int) -> int:

        ans = 0

        nums = [i for i in range(1, n + 1)]

        def permute(nums, curr_idx):
            nonlocal ans

            if curr_idx == len(nums):
                ans += 1

            for i in range(curr_idx, len(nums)):

                nums[i], nums[curr_idx] = nums[curr_idx], nums[i]

                if nums[curr_idx] % (curr_idx + 1) == 0 or (curr_idx + 1) % nums[curr_idx] == 0:
                    permute(nums, curr_idx + 1)

                nums[i], nums[curr_idx] = nums[curr_idx], nums[i]

        permute(nums, 0)

        return ans


if __name__ == "__main__":
    n = 2
    print(Solution().countArrangement(n))
