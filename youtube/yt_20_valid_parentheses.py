"""
([])
Bracket balance for each bracket type
After iteration, if all the balances are 0, return T, otherwise F
  If one balance negative, just return F
"""

class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for i in range(len(s)):

            if s[i] in ["(", "[", "{"]:
                stack.append(s[i])
            elif s[i] == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif s[i] == "}":
                if stack and stack[-1] == "{":
                    stack.pop()
                else:
                    return False
            elif s[i] == "]":
                if stack and stack[-1] == "[":
                    stack.pop()
                else:
                    return False

        if not stack:
            return True
        else:
            return False
