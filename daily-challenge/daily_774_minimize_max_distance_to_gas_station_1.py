from typing import List
import pprint


class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        n = len(stations)
        deltas = [stations[i + 1] - stations[i] for i in range(n - 1)]

        # print(f'deltas: {deltas}')

        # dp[n][k] the answer for adding k gas stations to the first n intervals of stations
        # dp[i][j] is answer for deltas[:i + 1] when adding j gas stations
        # e.g. stations = [23,24,36,39,46,56,57,65,84,98],
        # deltas: [1, 12, 3, 7, 10, 1, 8, 19, 14]
        # i: 0, j: 1, dp[0][1]: answer for adding 1 gas station to 0th interval
        # 0th interval means that it's between stations[1] and stations[0]
        # deltas[:1]: 1,
        # * (k + 1) because we are gonna make dp from 0 to k.
        # e.g. k: 1, k + 1: 2, so we will make 2 answer spaces for k: 0 and k: 1.
        # It doesn't mean we are making something for k: 2.
        dp = [[0.0] * (k + 1) for _ in range(n - 1)]

        # print(f'Initialized dp')
        # pprint.pprint(dp)
        # print()

        # deltas[0] is distance between stations[0] and stations[1]
        # e.g. k: 1,
        # i: 0, dp[0][0]: distance between stations[0] and stations[1] without adding a new gas stations,
        #   deltas[0] / float(1): distance divided by 1
        # i: 1, dp[0][1]: the answer for adding one new gas stations between stations[0] and stations[1]
        #   deltas[0] / float(2): distance will be divided into 2,
        #   because a new gas station sits between stations[0] and stations[1]
        for i in range(k + 1):
            dp[0][i] = deltas[0] / float(i + 1)

        # print(f'dp after 1st for')
        # pprint.pprint(dp)
        # print()

        # n - 1 because of delta
        for p in range(1, n - 1):
            # k + 1 because we wanna have answer for 0 too for k
            for k in range(k + 1):

                # p: first p intervals of stations
                # k: number of a new gas stations added; 0 to k
                # x: this is also the number of a new gas stations added; 0 to k
                # e.g. dp[1][k]: the first 1 intervals of stations
                #   k: 1, n: 3, stations: [23, 24, 36], deltas[1, 12]
                #
                #   Case when we add 0 new station
                #   p: 1, k: 0, x: 0, delta[1]: 12, (x + 1): 1, division: 12, dp[0][0]: 1, max(): 12
                #
                #   Case when we add 1 new station between 0th and 1st stations
                #   p: 1, k: 1, x: 0, delta[1]: 12, (x + 1): 1, division: 12, dp[0][1]: 0.5, max(): 12
                #
                #   Case when we add 1 new station between 1st and 2nd stations
                #   p: 1, k: 1, x: 1, delta[1]: 12, (x + 1): 2, division: 6, dp[0][0]: 1.0, max(): 6
                dp[p][k] = min(max(deltas[p] / float(x + 1), dp[p - 1][k - x]) for x in range(k + 1))

        # print(f'dp after 2nd for')
        # pprint.pprint(dp)

        # [-1][k] because we wanna consider all the intervals and add all the k gas stations
        return dp[-1][k]


stations = [23,24,36,39,46,56,57,65,84,98]
k = 1

# for i in range(1, len(stations)):
#     print(f'i: {i}, stations[i] - stations[i - 1]: {stations[i] - stations[i - 1]}')

# print((84 + 65) / 2)
# stations.insert(8, 74.5)
# print(stations)
# for i in range(1, len(stations)):
#     print(f'i: {i}, stations[i] - stations[i - 1]: {stations[i] - stations[i - 1]}')

print(Solution().minmaxGasDist(stations, k))
