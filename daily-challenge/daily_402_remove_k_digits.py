"""
Remove digits so that small digits should remain at left
Stack
  if current digit is smaller than top
    pop and append
    decrement k
  else
    keep previous digit
  if k is 0
    append current
Join stack
Clean leading 0

"12345", 2
"""


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i in range(len(num)):
            while stack and k and stack[-1] > num[i]:
                stack.pop()
                k -= 1
            stack.append(num[i])

        # Post process
        while k > 0 and stack:
            stack.pop()
            k -= 1

        # print(stack)

        # Leading 0
        ans = "".join(stack).lstrip("0")

        # Empty
        if not ans:
            return "0"
        else:
            return ans

    def removeKdigits1(self, num: str, k: int) -> str:
        stack = []

        for i in range(len(num)):

            if stack and stack[-1] > num[i] and k > 0:
                stack.pop()
                stack.append(num[i])
                k -= 1

            elif stack and stack[-1] < num[i] and k > 0:
                k -= 1

            elif k == 0:
                stack.append(num[i])

            else:
                stack.append(num[i])

        # print(stack)

        if k > 0:
            while stack and k:
                stack.pop()
                k -= 1

        if len(stack) == 0:
            return "0"

        else:
            ans = str(int("".join(stack)))
            return ans