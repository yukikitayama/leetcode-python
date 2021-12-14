"""
- States
  - Index at houses
  - Color of a house
  - Number of neighborhoods
- Base case
  -
"""


from typing import List


class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        memo = {}

        def dp(index, num_neighbor, prev_color):

            # Key for memoization hashmap
            # Use tuple to be hashable
            key = (index, num_neighbor, prev_color)

            # Base case
            # m - index < num_neighbor?
            # e.g. m: 5, meaning there are 5 houses, num_neighbor: 3, meaning we need to make 3 neighbors
            #      If index is 2, m - index: 3, which is not smaller than num_neighbor: 3
            #      It means [0, 1, "2", 3, 4], we can form 3 neighbors by [[0, 1, 2], [3], [4]]
            #      If index is 3, m - index: 2, which is smaller than num_neighbor: 3
            #      It means [0, 1, 2, "3", 4], we cannot form 3 neighbors because [[0, 1, 2, 3], [4]]
            if index == len(houses) or num_neighbor < 0 or m - index < num_neighbor:
                # If we formed target number of neighbors (num_neighbor == 0) and
                # if no more houses are left (index == len(houses)), we don't have to spend any more cost
                # So it can return 0 as the base case
                # Otherwise, it's not possible, so we need to return -1 eventually, so return negative infinity
                # and later convert it to -1 as the final answer
                return 0 if num_neighbor == 0 and index == len(houses) else float('inf')

            if key not in memo:
                # If the current house is not painted yet, we need to paint it
                if houses[index] == 0:
                    memo[key] = min(
                        [
                            # If current color (color) is different from previous color (prev_color),
                            # it needs to form a new neighborhood, so num_neighbor - 1 if colors are different
                            # -1 in cost[index][color - 1] because index in cost 2d array is 0-based.
                            dp(index + 1, num_neighbor - (color != prev_color), color) + cost[index][color - 1]
                            for color
                            # Starting at 1 because color is 1-based
                            in range(1, n + 1)
                        ]
                    )

                # If houses is already painted, no add cost because it doesn't need to paint
                else:
                    # But the number of neighborhood could be decremented depending on the current color
                    # and the previous color
                    # houses[index] is the current color
                    memo[key] = dp(index + 1, num_neighbor - (houses[index] != prev_color), houses[index])

            return memo[key]

        # Third argument is previous color.
        # When starting from index 0, there's no previous color, so pass -1
        # dp() only checks if the current color index is the same as previous color index,
        # so -1 will work
        result = dp(0, target, -1)

        return result if result != float('inf') else -1


houses = [0,0,0,0,0]
cost = [[1,10],[10,1],[10,1],[1,10],[5,1]]
m = 5
n = 2
target = 3
# 9
houses = [3,1,2,3]
cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]]
m = 4
n = 3
target = 3
# -1
print(Solution().minCost(houses, cost, m, n, target))
