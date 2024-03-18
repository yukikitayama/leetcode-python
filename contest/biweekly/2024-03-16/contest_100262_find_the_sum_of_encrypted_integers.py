from typing import List


class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        def encrypt(num):
            max_digit = max([d for d in str(num)])

            return int(len(str(num)) * max_digit)

        ans = 0

        for i in range(len(nums)):
            encrypted_num = encrypt(nums[i])
            ans += encrypted_num

        return ans