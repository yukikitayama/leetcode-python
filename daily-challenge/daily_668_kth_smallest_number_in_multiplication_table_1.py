"""
- Brute force
"""


class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        nums = []
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                nums.append(i * j)

        nums.sort()

        # print(f'nums: {nums}')

        return nums[k - 1]


"""
- It takes O(n^2) to generate all the number
- O(1) to access kth smallest after sorting
"""


m = 3
n = 3
k = 5
m = 2
n = 3
k = 6
print(Solution().findKthNumber(m, n, k))

