"""
- answer[0] indices which are not in the second element in any match
- answer[1]
"""


from typing import List
import collections


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

        counter = collections.Counter(match[1] for match in matches)

        # print(counter)

        players = set(match[0] for match in matches).union(set(match[1] for match in matches))
        players = sorted(list(players))

        # print(players)

        ans = [[], []]

        for player in players:

            if player not in counter:
                ans[0].append(player)
            elif player in counter and counter[player] == 1:
                ans[1].append(player)

        return ans


if __name__ == '__main__':
    matches = [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]
    print(Solution().findWinners(matches))
