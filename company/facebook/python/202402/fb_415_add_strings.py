"""

get length of each digits
get max length of digits
Iterate from right to left in digits
  get current digit position (0 to max len - 1)
  while curr position within either digit length
    Sum from curr digits
      summed % 10 appends to ans list
      if summed > 9, carry is 1
    if either digit out of bound, 0 + another
"""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        len1 = len(num1)
        len2 = len(num2)

        ans = []
        carry = 0

        for i in range(max(len1, len2)):
            idx = -(i + 1)

            if i >= len1:
                int1 = 0
            else:
                # int1 = int(num1[idx])
                int1 = ord(num1[idx]) - ord("0")

            if i >= len2:
                int2 = 0
            else:
                # int2 = int(num2[idx])
                int2 = ord(num2[idx]) - ord("0")

            sum_ = int1 + int2 + carry

            ans.append(str(sum_ % 10))

            if sum_ > 9:
                carry = 1
            else:
                carry = 0

        if carry:
            ans.append(str(carry))

        # print(ans)

        ans.reverse()

        return "".join(ans)
