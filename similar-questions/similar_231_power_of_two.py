"""
- Numbers of a power of two are having one 1 bit somewhere in
  binary representation
  - 2: 10
  - 4: 100
  - 8: 1000
- But numbers which are not a power of two have more than 1 1-bit
  somewhere in binary representation
  - 3: 11
  - 5: 101
  - 6: 110
- So the goal is to find a number which in binary representation,
  only has one 1 bit somewhere


- subtract 1 from a number means change the rightmost 1 bit to 0 bit,
  and all the lower bits to 1
- So this result applying AND operator to the original number means
  that turning off rightmost 1 bit
- Because number power of two only has one 1-bit so, turning off the
  rightmost 1-bit means making it zero
  - So if the result is zero, it's power of two, otherwise, not power of two
"""
# print(bin(7))
# print(bin(-7))
# print(bin(~7))
# print(bin(~7 + 1))

print(bin(5))
print(bin(5 - 1))
print(bin(6))
print(bin(6 - 1))
print(bin(8))
print(bin(8 - 1))


# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         if n == 0:
#             return False
#         return n & (~n + 1) == n


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n & (n - 1) == 0


print(Solution().isPowerOfTwo(0))
print(Solution().isPowerOfTwo(2))
print(Solution().isPowerOfTwo(3))
print(Solution().isPowerOfTwo(4))
