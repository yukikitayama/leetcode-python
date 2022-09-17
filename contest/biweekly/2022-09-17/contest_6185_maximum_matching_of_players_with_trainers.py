from typing import List


class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        i = j = 0

        ans = 0

        while i < len(players) and j < len(trainers):

            if players[i] <= trainers[j]:
                ans += 1
                i += 1
                j += 1

            else:
                j += 1

        return ans


if __name__ == '__main__':
    players = [4, 7, 9]
    trainers = [8, 2, 5, 8]

    players = [1, 1, 1]
    trainers = [10]

    print(Solution().matchPlayersAndTrainers(players, trainers))
