"""
cas(1): 1
cas(2): cas(2 - 1) = cas(1) has one 1 digit, "11"
cas(3): cas(3 - 1) = cas(2) has two 1 digits, "21"
cas(4): cas(4 - 1) = cas(3) has one 2 digit and one 1 digit, "1211"
cas(5): cas(5 - 1) = cas(4) = "1211" = "1", "2", "11", has one 1, one 2, two 1, "111221"

Recursive
  cas(n)
    terminal n = 1, return "1"
    Compute counter of cas(n - 1)
      iterater from left to right
        if curr digit is same as the prev digit, count up
        if curr digit is different from the prev digit
          save prev digit and counter
          reset counter to 1, prev digit to be current digit
    Create digit string from the counter
    return digit string
"""


class Solution:
    def countAndSay(self, n: int) -> str:

        def create_digit_string(digits: str):

            ans = []

            prev = "0"
            counter = 1

            for i in range(len(digits)):

                curr = digits[i]

                if curr != prev:

                    if prev != "0":
                        ans.append(str(counter) + prev)

                    prev = curr
                    counter = 1

                else:
                    counter += 1

            ans.append(str(counter) + prev)

            return "".join(ans)

        def recursion(n):

            if n == 1:
                return "1"

            return create_digit_string(recursion(n - 1))

        return recursion(n)

