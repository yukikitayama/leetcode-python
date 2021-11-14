"""
- Similar to 1286
- Lexicographic binary sorted subsets
"""


from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []

        # e.g. n: 3, 2**n: 2**3 = 8 = '1000', 2**4: 16 = '10000'
        # 8: 1000, 9: 1001, 10: 1010, ... 15: 1111
        for i in range(2**n, 2**(n + 1)):
            # print(f'  i: {i}, bin(i): {bin(i)}')
            # bin(1)[:3] is '0b1' which we don't need here
            bitmask = bin(i)[3:]

            # j: 0, bitmask[0] means whether there's 1-bit at leftmost in binary number
            # j: 1, bitmask[1] means whether there's 1-bit at second from the left in binary number
            # So starts from empty 000, 001, 010,... and ends at 111 if n: 3
            ans.append([nums[j] for j in range(n) if bitmask[j] == '1'])

        return ans


nums = [1, 2, 3]
print(Solution().subsets(nums))

