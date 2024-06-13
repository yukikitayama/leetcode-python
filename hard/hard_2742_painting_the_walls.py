from typing import List
import functools


class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:

        @functools.cache
        def dp(i, remain):

            # Base case: no more walls to pain
            if remain <= 0:
                return 0

            # Base case: before painting all walls, run out of walls to assign paid painter
            if i == len(cost):
                return float("inf")

            # -1 is a wall painted by paid painter
            # Free painter can paint time[i] amount of walls
            paint = cost[i] + dp(i + 1, remain - (1 + time[i]))
            # Don't assign paid painter, meaning wishing in the next iterations, paid painter will be occupied and free painter can paint the previous ones
            dont_paint = dp(i + 1, remain)

            return min(paint, dont_paint)

        # All walls from 0 index and all walls are remaining
        return dp(0, len(cost))