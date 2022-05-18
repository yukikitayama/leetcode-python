"""
- Start with i = k = j
- And expand the size of window by two pointers i and j
"""


from typing import List


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        ans = nums[k]
        mini = nums[k]

        i = k
        j = k
        n = len(nums)

        while i > 0 or j < n - 1:

            # By removing a higher value, min() will be reduced slowly
            if (nums[i - 1] if i else 0) < (nums[j + 1] if j < n - 1 else 0):
                j += 1
            else:
                i -= 1

            mini = min(mini, nums[i], nums[j])

            ans = max(ans, mini * (j - i + 1))

        return ans


if __name__ == '__main__':
    nums = [1,4,3,7,4,5]
    k = 3
    nums = [5, 5, 4, 5, 4, 1, 1, 1]
    k = 0
    print(Solution().maximumScore(nums, k))
