"""
a special binary string is a mountain if it touches the starting horizontal line only at the very beginning and the very end of the drawing.
we only swap mountains.
"""


class Solution:
    def makeLargestSpecial(self, s: str) -> str:

        # print(f"start, s: {s}")

        # Terminate recursion
        if not s:
            return s

        mountains = []

        anchor = 0
        balance = 0

        for i, ch in enumerate(s):

            if ch == "1":
                balance += 1
            else:
                balance -= 1

            if balance == 0:
                # +1 and :i to be inside of current mountain
                res = self.makeLargestSpecial(s[anchor + 1:i])

                mountains.append(f"1{res}0")

                # +1 to be the beginning of another mountain
                anchor = i + 1

        # print(mountains)

        mountains.sort(reverse=True)

        return "".join(mountains)
