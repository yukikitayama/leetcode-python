"""
Recursion function
while loop to count a current character

1
  1
2

"""


class Solution:
    def countAndSay(self, n: int) -> str:

        def recursion(n: int) -> str:

            if n == 1:
                return "1"

            digit_string = recursion(n - 1)

            # Count and say
            ans = []
            i = 0
            while i < len(digit_string):
                count = 1
                while i < len(digit_string) - 1 and digit_string[i] == digit_string[i + 1]:
                    i += 1
                    count += 1

                ans.append(str(count) + digit_string[i])
                i += 1

            # print(n, ans)

            return "".join(ans)

        return recursion(n)
