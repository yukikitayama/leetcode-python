"""
balance for each bracket type
iterate s
  when negative return False
After iteration
  when positive balance, return False
return True
"""


class Solution:
    def isValid(self, s: str) -> bool:
        # balance_pa = 0
        # balance_cu = 0
        # balance_sq = 0

        # for i in range(len(s)):

        #     curr = s[i]

        #     if curr == "(":
        #         balance_pa += 1
        #     elif curr == ")":
        #         balance_pa -= 1

        #     if curr == "{":
        #         balance_cu += 1
        #     elif curr == "}":
        #         balance_cu -= 1

        #     if curr == "[":
        #         balance_sq += 1
        #     elif curr == "]":
        #         balance_sq -= 1

        #     if balance_pa < 0 or balance_cu < 0 or balance_sq < 0:
        #         return False

        # if balance_pa > 0 or balance_cu > 0 or balance_sq > 0:
        #     return False
        # else:
        #     return True

        stack = []

        for i in range(len(s)):

            curr = s[i]

            if curr in ["(", "{", "["]:
                stack.append(curr)

            else:
                if not stack:
                    return False
                elif stack and curr == ")" and stack[-1] == "(":
                    stack.pop()
                elif stack and curr == "}" and stack[-1] == "{":
                    stack.pop()
                elif stack and curr == "]" and stack[-1] == "[":
                    stack.pop()
                else:
                    return False

        # Unclosed open
        if stack:
            return False
        else:
            return True

