"""
- https://florian.github.io/xor-trick/
- XOR is coommutative, so we can change the order
  - a ^ b = b ^ a
- Sequence of XOR operations
  - If we find pairs of duplicated values, we can remove the pair without affecting the result
  - a ^ b ^ c ^ a ^ b
  - Use commutativity to change order
  - a ^ a ^ b ^ b ^ c
  - Use XOR on the same argument, i.e. a ^ a = 0
  - 0 ^ 0 ^ c
  - Use XOR on 0, i.e. a ^ 0 = a
  - c

- XOR in-place swapping
  - To swap x and w, x ^= y, y ^= x, x ^= y, then now x is y, and y is x
    - (x, y)
    - x ^= y -> (x ^ y, y)
    - y ^= x -> (x ^ y, y ^ x ^ y) = (x ^ y, x)
    - x ^= y -> (x ^ y ^ x, x) = (y, x)
"""


from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0

        for i in nums:

            # x ^ x = 0,
            # 0 ^ y = y
            # elements appearing twice becomes 0
            # elements appearing once remain by 0 ^ y
            a ^= i

        return a


nums = [4,1,2,1,2]
print(Solution().singleNumber(nums))
