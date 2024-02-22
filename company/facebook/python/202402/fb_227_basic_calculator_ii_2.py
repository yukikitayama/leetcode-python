"""
* and / perform first than + and -
string of number could have length more than 1

3 + 2 * 2 + 4
stack
  store numbers only
    save negative number too
  when iterating, keep current operator
    if current operator is * or /, and after getting current number
      do math between stack top number and current number
      after math, append the number to stack
After iteration
  stack only contains positive or negative numbers to sum up

"""


class Solution:
    def calculate(self, s: str) -> int:

        stack = []
        operator = "+"

        i = 0

        while i < len(s):

            if s[i].isdigit():

                num = 0

                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1

                if operator == "+":
                    stack.append(num)
                elif operator == "-":
                    stack.append(-num)
                elif operator == "*":
                    prev = stack.pop()
                    res = prev * num
                    stack.append(res)
                elif operator == "/":
                    prev = stack.pop()
                    res = int(prev / num)
                    stack.append(res)

            elif s[i] in ["+", "-", "*", "/"]:
                operator = s[i]
                i += 1

            else:
                i += 1

        return sum(stack)