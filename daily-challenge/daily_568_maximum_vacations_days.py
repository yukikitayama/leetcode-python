"""
- dp
- topological sorting

"""


from typing import List


class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        # Row is city, column is k weeks
        memo = [[float('-inf')] * len(days[0]) for _ in range(len(flights))]
        return self.dfs(flights, days, 0, 0, memo)

    def dfs(self, flights, days, cur_city, weekno, memo):
        # No more weeks for vacation
        if weekno == len(days[0]):
            return 0

        if memo[cur_city][weekno] != float('-inf'):
            return memo[cur_city][weekno]

        maxvac = 0
        for i in range(len(flights)):
            if flights[cur_city][i] == 1 or i == cur_city:
                vac = days[i][weekno] + self.dfs(flights, days, i, weekno + 1, memo)
                maxvac = max(maxvac, vac)

        memo[cur_city][weekno] = maxvac
        return maxvac


if __name__ == '__main__':
    # flights = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
    # days = [[1, 3, 1], [6, 0, 3], [3, 3, 3]]
    flights = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
    days = [[7, 0, 0], [0, 7, 0], [0, 0, 7]]
    print('Flights')
    [print(flight) for flight in flights]
    print('Days')
    [print(day)for day in days]
    print(Solution().maxVacationsDays(flights, days))