"""
- dynamic programming
"""


from typing import List
from collections import defaultdict


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # Key: stone position, Value jumpsize to come to this stone position
        map = {}
        for i in range(len(stones)):
            map[stones[i]] = set()

        # Base case
        map[0].add(0)

        # For each index of stones,
        for i in range(len(stones)):
            # For each last jump to the current stone
            for last_jump in map[stones[i]]:

                print(f'i: {i}, stones[i]: {stones[i]}, last_jump: {last_jump}')

                # Get the current jump
                for step in [last_jump - 1, last_jump, last_jump + 1]:

                    # Current jump is valid if it's in boundary and the next stone exists
                    if step > 0 and stones[i] + step in map:

                        print(f'  valid step: {step}')

                        # Record the jump to the next stone
                        map[stones[i] + step].add(step)

        print(f'map: {map}')
        print(f'map[stones[len(stones) - 1]]: {map[stones[len(stones) - 1]]}')

        # return len(map[stones[len(stones) - 1]]) > 0

        # If there is last jump to the last index, it means the last index is reachable
        return len(map[stones[-1]]) > 0



stones = [0,1,3,5,6,8,12,17]  # True
# stones = [0,1,2,3,4,8,9,11]  # False
print(Solution().canCross(stones))


