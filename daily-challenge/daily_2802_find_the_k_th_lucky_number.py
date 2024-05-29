"""
Digit length: 1
  2 patterns: 2**1 = 1
Digit length: 2
  4 patterns: 2**2 = 4
Digit length: 3
  2**3 = 8 patterns
Every digit position has 2 choices to fill; 4 or 7
"""


class Solution:
    def kthLuckyNumber(self, k: int) -> str:
        k += 1
        binary = bin(k)
        dropped = binary[3:]
        dropped_list = list(dropped)

        for i in range(len(dropped_list)):
            if dropped_list[i] == "1":
                dropped_list[i] = "7"
            else:
                dropped_list[i] = "4"

        return "".join(dropped_list)
