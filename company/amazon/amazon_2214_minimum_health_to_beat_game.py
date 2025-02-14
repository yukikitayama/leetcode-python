"""
Greedy
Find max number
  decrement max number by armor
sum all the damage
return the sum + 1
"""

from typing import List


class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:

        sum_ = 0
        max_d = 0
        for d in damage:
            sum_ += d
            max_d = max(max_d, d)
        return sum_ - min(armor, max_d) + 1

    def minimumHealth1(self, damage: List[int], armor: int) -> int:
        max_num = max(damage)
        ans = 1
        used = False

        for d in damage:

            if d == max_num and not used:
                d = max(d - armor, 0)
                used = True

            ans += d

        return ans
