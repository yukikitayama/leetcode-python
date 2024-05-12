"""
Greedy dp

Input:  energy = [5,2,-10,-5,1], k = 3

[1, 2, 3, 4], k: 1
[
  1 + 2 + 3 + 4
  2 + 3 + 4
  3 + 4
  4
]

[1, 2, 3, 4, 5], k: 2
[
  1 + 3 + 5
  2 + 4
  3 + 5
  4,
  5
]

Output: 3

Explanation: We can gain a total energy of 3 by starting from magician 1 absorbing 2 + 1 = 3.

for each index,
  we start from here, or not
    if start, proceed to the end by skipping k
    if not start
"""

from typing import List


class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        ans = float("-inf")

        for i in range(len(energy) - 1, -1, -1):

            if i + k >= len(energy):
                ans = max(ans, energy[i])

            else:
                energy[i] = energy[i] + energy[i + k]
                ans = max(ans, energy[i])

        return ans

    def maximumEnergy2(self, energy: List[int], k: int) -> int:
        ans = float("-inf")

        for start in range(len(energy)):

            curr_energy_sum = 0
            i = start
            while i < len(energy):
                curr_energy_sum += energy[i]
                i += k

            ans = max(ans, curr_energy_sum)

        return ans

    def maximumEnergy1(self, energy: List[int], k: int) -> int:

        def dp(i):
            if i >= len(energy):
                return 0

            return max(
                dp(i + 1),
                energy[i] + dp(i + k)
            )

        return dp(0)
