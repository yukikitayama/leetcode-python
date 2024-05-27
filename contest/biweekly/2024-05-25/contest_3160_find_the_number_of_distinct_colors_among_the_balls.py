"""
Input: limit = 4, queries = [[1,4],[2,5],[1,3],[3,4]]

Output: [1,2,2,3]
"""

from typing import List
import collections


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        color_to_balls = collections.defaultdict(set)
        ball_to_color = collections.defaultdict(int)

        ans = []

        for ball, color in queries:

            if ball in ball_to_color:
                prev_color = ball_to_color[ball]
                color_to_balls[prev_color].discard(ball)
                if len(color_to_balls[prev_color]) == 0:
                    del color_to_balls[prev_color]

            ball_to_color[ball] = color

            color_to_balls[color].add(ball)

            ans.append(len(color_to_balls.keys()))

            # print(ball_to_color, color_to_balls)

        return ans
