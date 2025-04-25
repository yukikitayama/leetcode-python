"""
base case
  1 is "1"
Scan
  if next character exists and next character is the same
    increment counter
  else
    reset counter to 1
"""


class Solution:
    def countAndSay(self, n: int) -> str:

        def recursion(n):

            if n == 1:
                return "1"

            rle = recursion(n - 1)

            curr_num = rle[0]
            curr_counter = 1

            res = [[curr_counter, curr_num]]
            for i in range(1, len(rle)):

                if rle[i] == res[-1][1]:
                    res[-1][0] += 1
                else:
                    curr_num = rle[i]
                    curr_counter = 1
                    res.append([curr_counter, curr_num])

            res = "".join(str(c) + n for c, n in res)

            return res

        return recursion(n)