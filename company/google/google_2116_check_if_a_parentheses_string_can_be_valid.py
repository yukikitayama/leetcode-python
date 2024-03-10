"""
balance
iterate
  if negative,
    if lock 0
      balance 0 by assuming ) -> (
check if balance is 0

case
  "(("
  "00"

  ")("
  "00"
"""


class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        # Edge
        if len(s) % 2 != 0:
            return False

        # Check if ")" without matching "(" exists
        unlock = 0
        balance = 0
        for i in range(len(s)):

            if locked[i] == "0":
                unlock += 1

            else:
                if s[i] == "(":
                    balance += 1
                else:
                    balance -= 1

            if unlock + balance < 0:
                return False

        # Check if "(" without matching ")" exists
        unlock = 0
        balance = 0
        for i in range(len(s) - 1, -1, -1):

            if locked[i] == "0":
                unlock += 1

            else:
                if s[i] == "(":
                    balance -= 1
                else:
                    balance += 1

            if unlock + balance < 0:
                return False

        return True

    def canBeValid2(self, s: str, locked: str) -> bool:

        # Edge
        if len(s) % 2 != 0:
            return False

        def check(s, locked, parenthesis):
            balance = 0
            unlock = 0

            for i in range(len(s)):

                # When lock is 1, do the normal balance calculation
                if locked[i] == "1":
                    if s[i] == parenthesis:
                        balance += 1
                    else:
                        balance -= 1

                # Count unlocked
                else:
                    unlock += 1

                # unlock: 0, balance: -1, cannot find ( to make ()
                # unlock: 1, balance: -1, can find (
                if unlock + balance < 0:
                    return False

            print(f"balance: {balance}, unlock: {unlock}")

            return balance <= unlock

        # Check if ")" without matching "(" exists
        left_to_right = check(s, locked, "(")
        # print(left_to_right)
        # Check if "(" without matching ")" exists
        right_to_left = check(s[::-1], locked[::-1], ")")
        # print(right_to_left)

        return left_to_right and right_to_left

    def canBeValid1(self, s: str, locked: str) -> bool:
        s = list(s)

        balance = 0

        for i in range(len(s)):

            if s[i] == ")":
                balance -= 1
            elif s[i] == "(":
                balance += 1

            if balance < 0:
                if locked[i] == "0":
                    balance = 1
                    s[i] = "("

            elif balance > 0:
                if locked[i] == "0":
                    balance -= 1
                    s[i] = ")"

        print(s)

        if balance == 0:
            return True

        s.reverse()

        balance = 0

        for i in range(len(s)):

            if s[i] == ")":
                balance -= 1
            elif s[i] == "(":
                balance += 1

            if balance < 0:
                if locked[i] == "0":
                    balance = 1
                    s[i] = "("

            elif balance > 0:
                if locked[i] == "0":
                    balance -= 1
                    s[i] = ")"

        return balance == 0
