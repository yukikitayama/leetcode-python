class Solution:
    def calculate(self, s: str) -> int:

        stack = []
        curr_num = 0
        curr_operator = "+"
        s = s.replace(" ", "")

        for i in range(len(s)):

            curr_str = s[i]

            if curr_str.isdigit():
                curr_num = curr_num * 10 + int(curr_str)

            if not curr_str.isdigit() or i == (len(s) - 1):
                if curr_operator == "+":
                    stack.append(curr_num)
                elif curr_operator == "-":
                    stack.append(-curr_num)
                elif curr_operator == "*":
                    prev_num = stack.pop()
                    res = prev_num * curr_num
                    stack.append(res)
                elif curr_operator == "/":
                    prev_num = stack.pop()
                    res = int(prev_num / curr_num)
                    stack.append(res)

                curr_operator = curr_str
                curr_num = 0

        print(stack)
        ans = 0
        while stack:
            ans += stack.pop()
        return ans
