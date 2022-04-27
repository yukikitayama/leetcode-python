from typing import List


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        year_delta = []
        for birth, death in logs:
            year_delta.append((birth, 1))
            year_delta.append((death, -1))

        # sort because the problem asks us to return the earliest year
        year_delta.sort()

        population = max_population = 0
        for year, delta in year_delta:
            population += delta

            # Because we are required to return earliest year of the maximum population
            # we need to keep updating max population and its year
            if population > max_population:
                max_population = population
                ans = year

        return ans


if __name__ == '__main__':
    logs = [[1993, 1999], [2000, 2010]]
    logs = [[1950, 1961], [1960, 1971], [1970, 1981]]
    print(Solution().maximumPopulation(logs))
