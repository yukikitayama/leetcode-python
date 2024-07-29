"""
The bitwise XOR of one element is that element itself
  If only one element left, result of operation is the number itself.
the bitwise XOR of no elements is 0
  You cannot be the person to erase the last element to win
Also, if any player starts their turn with the bitwise XOR of all the elements of the chalkboard equal to 0, then that player wins.
  if the XOR of the entire array is 0, then Alice wins.
"""

from typing import List


class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        xor = 0
        for num in nums:
            xor ^= num

        # If all numbers are the same, XOR is 0
        if xor == 0:
            return True

        # If all numbers are not the same, there are at least 2 different numbers
        # Alice can always erase a number different from current XOR
        # [1, 1, 2, 2] -> A -> [1, 2, 2] -> B -> [1, 2] -> A -> [2] -> B erase, but empty, so 0
        # [1, 1, 2, 2] -> A -> [1, 2, 2] -> B -> [1, 1] but XOR is 0, so B lose
        else:
            if len(nums) % 2 == 0:
                return True
            else:
                return False