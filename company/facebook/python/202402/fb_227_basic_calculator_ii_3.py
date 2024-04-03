"""
Stack
  contains only number
  number could be negative
"""


class Solution:
    def calculate(self, s: str) -> int:

        i = 0
        operator = "+"
        ans = 0
        last_num = 0

        while i < len(s):

            if s[i] == " ":
                i += 1
                continue

            elif s[i].isdigit():
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1

                if operator == "+":
                    ans += last_num
                    num *= 1
                    last_num = num
                elif operator == "-":
                    ans += last_num
                    num *= -1
                    last_num = num
                elif operator == "*":
                    new_num = last_num * num
                    last_num = new_num
                elif operator == "/":
                    new_num = int(last_num / num)
                    last_num = new_num

            elif s[i] in "+-*/":
                operator = s[i]
                i += 1

        ans += last_num

        return ans

    def calculate1(self, s: str) -> int:
        stack = []

        i = 0
        operator = "+"

        while i < len(s):

            if s[i] == " ":
                i += 1
                continue

            elif s[i].isdigit():
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1

                if operator == "+":
                    num *= 1
                    stack.append(num)
                elif operator == "-":
                    num *= -1
                    stack.append(num)
                elif operator == "*":
                    top_num = stack.pop()
                    new_num = top_num * num
                    stack.append(new_num)
                elif operator == "/":
                    top_num = stack.pop()
                    new_num = int(top_num / num)
                    stack.append(new_num)

            elif s[i] in "+-*/":
                operator = s[i]
                i += 1

        return sum(stack)