"""
preprocess balance
then shift
"""

from typing import List


class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        balance = 0
        for d, a in shift:
            if d == 0:
                balance -= a
            elif d == 1:
                balance += a

            balance %= len(s)

        # print(balance)

        return s[-balance:] + s[:-balance]