from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_tank = 0
        curr_tank = 0

        ans = 0

        for i in range(len(gas)):

            g = gas[i]
            c = cost[i]
            total_tank += g - c
            curr_tank += g - c

            if curr_tank < 0:

                ans = i + 1
                curr_tank = 0

        return ans if total_tank >= 0 else -1



