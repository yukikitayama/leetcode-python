import collections


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:

        counter = collections.Counter(tiles)

        def backtracking():

            res = 0

            for k, v in counter.items():
                if v != 0:
                    res += 1
                    counter[k] -= 1

                    res += backtracking()

                    counter[k] += 1

            return res

        return backtracking()