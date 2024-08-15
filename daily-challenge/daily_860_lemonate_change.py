"""
Change choice
  When $10, give $5
    1 $5 bill
  When $20, give $15
    3 $5 bills
    1 $5 bill and 1 $10 bill
Simulation
  Hashmap
  Greedy to always save $5 bill
"""

from typing import List
import collections


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        counter = collections.Counter()
        for bill in bills:

            if bill == 5:
                counter[5] += 1

            elif bill == 10:
                counter[5] -= 1
                counter[10] += 1

            elif bill == 20:
                if counter[10] > 0 and counter[5] > 0:
                    counter[10] -= 1
                    counter[5] -= 1
                else:
                    counter[5] -= 3
                counter[20] += 1

            if counter[5] < 0:
                return False

        return True