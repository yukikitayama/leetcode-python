"""
- We get 1 to 7 with 1/7 probability
- If we can get 8 to 10 with 1/7 probability, that's useful
"""


def rand7():
    return 0


class Solution:
    def rand10(self):
        idx = 41
        while idx > 40:
            row = rand7()
            col = rand7()
            # -1 because index start from 0, though row is from 1 to 7
            # *7 for the next row
            idx = col + (row - 1) * 7

        # col is from 1 to 7, so the above idx is from 1 to 40
        # When idx is 1, (1 - 1) % 10 = 0, but we want integer from 1 to 10
        # so +1
        return (idx - 1) % 10 + 1
