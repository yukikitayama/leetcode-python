"""
Result
- Start: 3:27
- End: 3:45
- Solved:
- Saw solution: 1
- Optimized: 0
- TLE

Idea
- Iterate each index as start station
"""


from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        n = len(gas)

        for i in range(n):
        # for i in range(3, 4):
        # for i in range(2, 3):

            # print(f'i: {i}')

            tank = 0
            j = i
            while j < n:

                # Fill gas
                tank += gas[j % n]

                # print(f'  j: {j}, tank: {tank}')

                # Travel to the next gas station
                tank -= cost[j % n]

                # If during travel running up the gas, stop current iteration
                # and go to the next index as the start station
                if tank < 0:
                    break

                # Go to the next station in a circular manner
                j = (j + 1) % n

                if j == i and tank >= 0:
                    # print(f'    tank: {tank}')
                    return i

        return -1


gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
# 3
gas = [2,3,4]
cost = [3,4,3]
# -1
print(Solution().canCompleteCircuit(gas, cost))



