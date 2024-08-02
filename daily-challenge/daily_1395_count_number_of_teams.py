"""
Backtracking
"""

from typing import List


class Solution:
    def numTeams(self, rating: List[int]) -> int:

        # 4 for 0 person, 1, 2, 3 people in a team
        increasing_cache = [[-1] * 4 for _ in range(len(rating))]
        decreasing_cache = [[-1] * 4 for _ in range(len(rating))]

        def count_increasing_teams(index, team_size):
            # Base case
            if index == len(rating):
                return 0

            # Base case
            if team_size == 3:
                return 1

            if increasing_cache[index][team_size] != -1:
                return increasing_cache[index][team_size]

            res = 0

            for next_ in range(index + 1, len(rating)):
                if rating[next_] > rating[index]:
                    res += count_increasing_teams(next_, team_size + 1)

            increasing_cache[index][team_size] = res
            return increasing_cache[index][team_size]

        def count_decreasing_teams(index, team_size):
            # Base case
            if index == len(rating):
                return 0

            # Base case
            if team_size == 3:
                return 1

            if decreasing_cache[index][team_size] != -1:
                return decreasing_cache[index][team_size]

            res = 0

            for next_ in range(index + 1, len(rating)):
                if rating[next_] < rating[index]:
                    res += count_decreasing_teams(next_, team_size + 1)

            decreasing_cache[index][team_size] = res
            return decreasing_cache[index][team_size]

        ans = 0

        for i in range(len(rating)):
            ans += count_increasing_teams(i, 1)
            ans += count_decreasing_teams(i, 1)

        return ans