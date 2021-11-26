"""
- Impossible to perform the round trip if sum(gas) < sum(cost)
- Impossible for station i to be a start station if gas[i] - cost[i] < 0
"""


from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        total_tank = 0
        curr_tank = 0
        starting_station = 0

        for i in range(n):

            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]

            # Reset a starting station if currently tank is negative
            if curr_tank < 0:
                starting_station = i + 1
                curr_tank = 0

        # Each starting station does not need to actually make a round trip.
        # If at the end of one iteration, total tank is positive, a round trip is possible
        # so we only need to know which station can be the starting station.
        # e.g. len(gas): 5, select index: 3 as starting station,
        # and when i: 4, it's the end of one iteration
        # when i: 4, if total_tank is positive, round trip is possible
        return starting_station if total_tank >= 0 else -1


"""
- Time is O(n)
- Space is O(1)
"""


gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
# 3
# gas = [2,3,4]
# cost = [3,4,3]
# -1
print(Solution().canCompleteCircuit(gas, cost))



