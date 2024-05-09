"""
n: 7
2**0 + 2**1 + 2**2 = 1 + 2 + 4 = 7
binary: 111
"""

from typing import List


class Solution:
    def evenOddBit(self, n: int) -> List[int]:

        even = 0
        odd = 0

        # 0b___
        binary = bin(n)[2:][::-1]

        # print(bin(n))
        # print(binary)

        for i in range(len(binary)):

            if binary[i] == "1":

                if i % 2 == 0:
                    even += 1
                elif i % 2 != 0:
                    odd += 1

        return [even, odd]
