"""
simulation
iterate given list
create counter hashmap and get hashset of player who lost once
sort
"""

from typing import List
import collections


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

        counter = collections.Counter()
        players = set()

        for winner, loser in matches:

            counter[loser] += 1
            players.add(winner)
            players.add(loser)

        who_not_lost = sorted([p for p in players if p not in counter.keys()])
        who_lost_once = sorted([k for k, v in counter.items() if v == 1])

        return [who_not_lost, who_lost_once]

    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

        counter = collections.Counter()

        for winner, loser in matches:

            counter[winner] += 0
            counter[loser] += 1

        who_not_lost = sorted([k for k, v in counter.items() if v == 0])
        who_lost_once = sorted([k for k, v in counter.items() if v == 1])

        return [who_not_lost, who_lost_once]

    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # Counting sort
        losses = [-1] * (10 ** 5 + 1)
        for winner, loser in matches:
            if losses[winner] == -1:
                losses[winner] = 0

            if losses[loser] == -1:
                losses[loser] = 1
            else:
                losses[loser] += 1

        ans = [[], []]

        for i in range(len(losses)):
            if losses[i] == 0:
                ans[0].append(i)
            elif losses[i] == 1:
                ans[1].append(i)

        return ans



if __name__ == "__main__":
    matches = [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]
    print(Solution().findWinners(matches))