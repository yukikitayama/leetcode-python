"""
balance
(*))
  T
  minus after *
()(*
  T
  plus before *
(*)(
  F
  plus after *
)()*
  F
  minus before *

Save parenthesis and * into separate stack
  * stack append indices
Iterate
  track balance
  if *,
    append indices to stack
  if balance negative
    pop * stack
If iteration ends with 0 balance
  0

"""


class Solution:
    def checkValidString(self, s: str) -> bool:
        bracket_stack = []
        asterisk_stack = []

        for i in range(len(s)):
            if s[i] == "(":
                bracket_stack.append(i)

            elif s[i] == "*":
                asterisk_stack.append(i)

            elif s[i] == ")":
                if bracket_stack:
                    bracket_stack.pop()
                elif asterisk_stack:
                    asterisk_stack.pop()
                else:
                    return False

        while bracket_stack and asterisk_stack:
            last_open_bracket = bracket_stack.pop()
            last_asterisk = asterisk_stack.pop()

            if last_open_bracket < last_asterisk:
                continue
            # "*(" cannot close
            else:
                return False

        # After closing open by asterisk and if still open brackets are remaining
        if bracket_stack:
            return False
        else:
            return True

    def checkValidString1(self, s: str) -> bool:

        # Left to right
        stack = []
        balance = 0
        for i in range(len(s)):
            if s[i] == "(":
                balance += 1
            elif s[i] == ")":
                balance -= 1
            elif s[i] == "*":
                stack.append(i)

            if balance == -1 and stack:
                stack.pop()
                balance = 0
            elif balance == -1 and not stack:
                return False

        print(stack, balance)

        if balance == 0:
            return True

        # Right to left
        stack = []
        balance = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ")":
                balance += 1
            elif s[i] == "(":
                balance -= 1
            elif s[i] == "*":
                stack.append(i)

            if balance == -1 and stack:
                stack.pop()
                balance = 0
            elif balance == -1 and not stack:
                return False

        print(stack, balance)

        if balance == 0:
            return True

        return False

        # elif balance > 0 and balance <= len(stack):
        #     return True
        # else:
        #     return False


