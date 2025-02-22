"""
Stack
  contains numbers only
scan from left to right
if current character is not number
  record current operator
if current character is part of number
  create current number
  if prev operator was * or /
    pop number from stack, do * or / and save it to current number
  else if prev operator was -,
    convert current number to negative
  append current number to stack
return sum of stack
"""


class Solution:
    def calculate(self, s: str) -> int:
        operator = "+"
        stack = []
        i = 0

        while i < len(s):

            ch = s[i]

            if ch == " ":
                i += 1

            elif ch.isdigit():
                num = 0
                while i < len(s) and s[i].isdigit():
                    num *= 10
                    num += int(s[i])
                    i += 1
                # Here, i is at non digit

                if operator == "-":
                    num *= -1
                elif operator == "*":
                    prev_num = stack.pop()
                    num = num * prev_num
                elif operator == "/":
                    prev_num = stack.pop()
                    if num == 0:
                        num = 0
                    else:
                        # int() truncates toward zero. int(-3 / 2) = -1
                        # // doesn't truncate toward zero -3 // 2 = -2
                        # -3 / 2 = -1.5
                        num = int(prev_num / num)

                stack.append(num)

            elif ch in "+-*/":
                operator = ch
                i += 1

        return sum(stack)